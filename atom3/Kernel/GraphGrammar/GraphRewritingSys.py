# _ File: GraphRewritingSys.py _________________________________________________________________
# Implements : class GraphRewritingSys
# Author     : Juan de Lara
# Description: A class that implements a simple graph rewriting system.
# Modified   :
#   - 20 Oct 2001. Added capability to execute in parallel or sequential modes
#   - 09 Aug 2002. Added capability to animate a gg.
# ________________________________________________________________________________________

from GGrule           import *
from executionControl import *
from Tkinter          import *
#from threading        import * #<-- Removed by Denis
from animationControl import *
import time

# Added by Denis
import tkMessageBox
from random import shuffle
from exceptionHookFriendlyThreading        import *

class GraphRewritingSys:
   # flags that show the execution mode
   SEQ_RANDOM = 0
   SEQ_MANUAL = 1
   PARALLEL   = 2
   STEPBYSTEP = 0
   CONTINUOUS = 1

   numgg = 0         # counter of active graph rewriting systems...

   def __init__(self, parent, GGs = None, graph = None):
      "constructor, takes a list of GraphGrammars and a graph as inputs"
      self.parent           = parent
      self.GraphGrammars    = GGs
      self.graph            = graph
      self.initialized      = 0                    	# No initialization yet
      self.lastExecutedGG   = 0                    	# last executed GG
      self.lastExecutedRule = 0                    	# last executed GG
      self.stepByStep       = 0                    	# must execute SBS??
      self.executed         = 1
      self.lastRule         = 0                    	# show last executed rule
      self.executionMode    = 0			 	# can be one of (SEQ_RANDOM, SEQ_MANUAL, PARALLEL)
      self.graphics         = 1				# if we should update the graphics information
      							# it should be 0 in the case for example of a graph-grammar acting on a non-visible model.
      self.animate          = 0                         # 0 or 1 depending if we want animation or not.
      self.delay_ms         = 0                         # delay in ms we have to wait if animation is ON.
      self.ggThread         = None                      # This contains a pointer to the thread currently executing...
      self.numgg            = self.numgg+1
      self.stop             = 0
      self.pause            = 0
      self.wait_idle = 0
            

   def unSetWaitIdle(self):
      self.wait_idle = 0

   def run_gg( self, mode ):
      """
      This is the function to be called in the thread's execution.
      It executes the doStep function until no matching is found (or forever)
      """
      self.stop = 0
      if( mode == self.CONTINUOUS):
        c = 0
        while (c == 0 and self.stop == 0):
          c = self.doStep()          
          while (self.pause): pass
 
   def getCurrentGG(self):
      "returns the name of the current graph grammar"
      if self.lastExecutedGG < len (self.GraphGrammars):
         return self.GraphGrammars[self.lastExecutedGG].__class__.__name__
      else: return ""

   def getLastRule(self):
      "returns the name of the last executed rule"
      if self.lastExecutedGG < len (self.GraphGrammars):
         gg = self.GraphGrammars[self.lastExecutedGG]
         if self.lastRule < len(gg.GGrules):
            rule = gg.GGrules[self.lastRule]
            return rule.__class__.__name__+" (order: "+str(rule.executionOrder)+")"
      return ""

   def evaluate(self, stepByStep, moveEntities, execute, graphics = 1, animate = 0):
      """
         executes each rule of each Graph Grammar until none of them is applicable
      """

      self.moveEntities     = moveEntities         # if entities should move
      self.stepByStep       = stepByStep
      self.lastExecutedGG   = 0                    # last executed GG
      self.lastExecutedRule = 0                    # last executed Rule
      self.initialized      = 0                    # last executed GG
      self.executionMode    = execute
      self.graphics         = graphics
      self.animate          = animate              # if we have to make some delay (taken from GGrule's). Added 09 Aug 2002 by JL
      self.animationControls= None
      
      #todo: fix animate
      if( self.animate): 
        tkMessageBox.showwarning('Animate Graph Grammar (DISABLED)         ',
                'This feature has been shown to cause near random exceptions'
                + ' AND cancer in small animals.'
                + '\n Therefore it is disabled for your own safety... \n'
                +'\nIf you have a Model & Grammar that uses this feature please'
                +' send it to Denis --> d3n14@yahoo.com so I can fix it.'
                +'\n\nie. I expect someone has a Model & Grammar that worked'
                + ' under the old AToM3 0.2.2 version' )
        # self.animationControls = animationControl(self)
        self.animate = False
        
      # Continuous mode & Animated
      if( not self.stepByStep and self.animate):
         self.ggThread = Thread(None, self.run_gg, "graph-grammar-thread-"
                                   +str(self.numgg), (self.CONTINUOUS, ) )
         self.ggThread.start()
         self.ggThread = None
         
      # Continuous mode
      elif( not self.stepByStep):
         # Modified by Denis, Feb 19, 2005: It is now possible to halt 
         # grammars that never stop executing! 
         #self.run_gg( self.CONTINUOUS )
         self.ec = executionControl(self)
         self.ec.continuous( closeWhenDone = True )
         
      # Step by Step mode
      else: # present a window with a button to step through the GG rules
        self.ec = executionControl(self)
        
   def areDisjoint (self, graph1, graph2):
      "Test whether graph1 and graph2 are disjoints"
      # for each node in the first graph, see if they appear in te other list...
      for node in graph1:				
         if node in graph2: return 0
      return 1

   def executeRule( self, subGraph, rule = None ):
     """ Executes current rule on the subgraph subGraph"""
     # first, determine the rule to be executed
     if( not rule): 
       rule2exec = self.GraphGrammars[self.lastExecutedGG].GGrules[self.lastExecutedRule]
     else: 
       rule2exec = rule
     # Perform substitution on each morphism graph
     rule2exec.replaceSides(self.parent, subGraph, self.graph, 
                                  self.moveEntities, self.graphics)	
     # Execute associated action...
     rule2exec.action(subGraph[0], subGraph[1], self.parent)  
     # restore graph						
     rule2exec.unMatch(self.graph)                                    					
     if self.parent.console: 
      self.parent.console.appendText('Rule '+str(rule2exec.executionOrder)
                          + '('+rule2exec.__class__.__name__+') was executed!')
     self.lastRule = self.lastExecutedRule
     self.lastExecutedRule = 0    # begin again
     return 0

   def doStepInitilization(self, gg):
      self.initialized = 1
      # sets an extra label to each node in the host graph, with a list of links to matched LHS rule nodes
      for tip in self.graph.listNodes.keys():
        for node in self.graph.listNodes[tip]:
          node._matched = []

      self.executed         = 1   # flag that indicates if some rule has been applied
      self.lastExecutedRule = 0   # index to the last executed rule...

      # set a pointer to myself in each graph grammar...
      gg.setGraphRewritingSystem(self)

      # execute the initial action method
      gg.initialAction(self.graph)

      # This code paragraph added by Denis on Feb 19, 2005
      # Build a dictionary of rules with the same execution order      
      self.execOrderToRuleDict = dict() 
      for rule in gg.GGrules:
        if( self.execOrderToRuleDict.has_key( rule.executionOrder ) ):
          self.execOrderToRuleDict[rule.executionOrder].extend( [rule] )          
        else:
          self.execOrderToRuleDict[rule.executionOrder] = [ rule ]
      
      # Build a dictionary of rules to the 'real' order
      self.ruleToRealorderDict = dict() 
      realOrderIndex = 0
      for rule in gg.GGrules:
        self.ruleToRealorderDict[ rule ] = realOrderIndex 
        realOrderIndex += 1
        


   def doStep(self):
      """ 
      Applies grammar rules, if successful, this method is called again after
      each rule application. If not, it will be called again, but on the next
      grammar.
      """
      # No doing steps until this one is done!
      self.ec.setButtonsState( ['Step', 'Continuous'], False )

      #todo: fix animate
      self.animate = False
      
      # No more Grammars to execute, let alone any rules, HALT
      if( self.lastExecutedGG >= len(self.GraphGrammars) ): return 0
         
      # INITILIZATION PHASE
      gg  = self.GraphGrammars[self.lastExecutedGG]
      if( not self.initialized ): self.doStepInitilization( gg )
          
      # EXECUTION PHASE
      executed = 0
      # Loop while we still have some rules to execute...
  
      while( (not executed) and (self.lastExecutedRule < len(gg.GGrules)) ): 
       
        currentOrder = gg.GGrules[self.lastExecutedRule].executionOrder
        ruleList = self.execOrderToRuleDict[ currentOrder ]
        
        # Get a list of random indices to access the ruleList
        if( len( ruleList ) > 1 ):
          randomIndexList = []
          for i in range(0,len(ruleList) ):
            randomIndexList.append( i )
          shuffle( randomIndexList )
        else:
          randomIndexList = [0] # <-- Just take the first rule
        
        ## print 'self.lastExecutedRule', self.lastExecutedRule
        ## print 'len(gg.GGrules)',len(gg.GGrules)
        ## print 'currentOrder =gg.GGrules[self.lastExecutedRule].executionOrder',gg.GGrules[self.lastExecutedRule].executionOrder
        ## print 'ruleList =self.execOrderToRuleDict[ currentOrder ]', self.execOrderToRuleDict[ currentOrder ]
        
        # Try rules of the same order in a random fashion
        for i in randomIndexList:
          rule = ruleList[i]
   
          if( self.parent.console): self.parent.console.appendText(
                                'Trying rule '+str(rule.executionOrder)
                                  + '('+rule.__class__.__name__+')')
          
          # Find matchines in the graph with this rule, then execute it
          # If the execution works, then we are done here...
          matchings = rule.evaluate(self.graph)  
          
          if( matchings and self.doExecution( matchings, rule, executed ) ): 
              self.lastRule = self.ruleToRealorderDict[rule]
              self.ec.setButtonsState( ['Step', 'Continuous'], True )
              return False

        # Okay, no rules of the previous order can be applied
        self.lastExecutedRule += 1
        
      # If we reach this point, no more rules can be applied to the host graph
      # Therefore, execution of the current GraphGrammar effectively ends      

      # Execute the global final action (postaction) method
      gg.finalAction(self.graph)

      # Try a new GG (if we have other GG's available)
      self.lastExecutedGG = self.lastExecutedGG+1
      self.lastExecutedRule = 0
      self.initialized = 0
      self.ec.setButtonsState( ['Step', 'Continuous'], True )
      return 1

   def doExecution(self, matchings, rule, executed ):
    
      # filter the isographs that don't fulfil the condition...
      condMatchings = [] 
      executedGraphs = {}
      
      
      
      # Sequential Manual, so must choose one if there's more than one...
      if( self.executionMode == self.SEQ_MANUAL and len(matchings)>0 ):			
        condTrue = []
        # See how many graphs make the condition true 
        for isograph in matchings:						
          # the condition is hold!               
          if( rule.condition(isograph[0], isograph[1], self.parent) ):		
            # Add graph to list of graphs that make condition true
            condTrue.append(isograph)		
                  
        # if we have several graphs, highlight them and the user must choose one              
        if len (condTrue) > 1:							
          #print "Conditions hold for :", condTrue
          self.parent.highLightGraphs(condTrue)
          self.ec.currGG.config( text = 
            'Waiting for user to manually LEFT-CLICK transformation target' )
          chosenIndex = self.doMatchingChoice( condTrue )
                     
          
          
          # Reset highlighting now that we have our choice
          self.parent.highLightGraphs(condTrue, flag = False)
          if( not self.ec.isDestroyed ):
            self.ec.currGG.config( text ='Executing Graph-Grammar: ')
            self.ec.rootWindow.focus_force()
          
          # Bad choice, return
          if( chosenIndex == None ): return True          
  
          # Perform substitution on each morphism graph
          rule.replaceSides(self.parent, condTrue[chosenIndex], self.graph, 
                                    self.moveEntities, self.graphics)
          # Execute associated action...
          rule.action(condTrue[chosenIndex][0], condTrue[chosenIndex][1], self.parent)  		
          condMatchings.append(condTrue[chosenIndex])
          executed = 1
          
        # only one, so apply the rule rightaway
        elif len (condTrue) == 1:							
          # Perform substitution on each morphism graph
          rule.replaceSides(self.parent, condTrue[0], self.graph, 
                                    self.moveEntities, self.graphics)
          # Execute associated action...
          rule.action(condTrue[0][0], condTrue[0][1], self.parent)  		
          condMatchings.append(condTrue[0])
          executed = 1
      else:
        for isograph in matchings:
          doExecute = 1
          if( self.executionMode == self.PARALLEL):
            # keep a copy of the graph before replacement (make a new list...)
            graphBeforeReplacement = []+isograph[1]       
            # for all the graphs that have been executed                        
            for graphID in executedGraphs.keys():					
              if not self.areDisjoint(isograph[1], executedGraphs[graphID]):
                # do not try this subgraph because it is not disjoint!
                doExecute = 0							
                break
          
          # the condition is hold!
          if( doExecute 
                and rule.condition(isograph[0], isograph[1], self.parent)):	 
                    
            # Perform substitution on each morphism graph
            print '(DEBUG) Executing rule:', rule.__class__.__name__, rule.executionOrder, __file__
            rule.replaceSides(self.parent, isograph, self.graph, 
                                    self.moveEntities, self.graphics) 
            # Execute associated action...
            rule.action(isograph[0], isograph[1], self.parent)  			 
            condMatchings.append(isograph)
            executed = 1
            
            # Execute only once if sequential/random mode is set
            if( self.executionMode == self.SEQ_RANDOM ): break	
            
            # Mark the graph before the replacement subraph as executed, 
            # and store it for subsequent comparisons...		
            executedGraphs[isograph[0]] = graphBeforeReplacement    
                
      # Restore graph
      rule.unMatch(self.graph)   
      # If rule has been executed...                                 			
      if( executed == 1):     
        if( self.parent.console): 
          self.parent.console.appendText('Rule '+str(rule.executionOrder)
                          + '('+rule.__class__.__name__+') was executed!')
        self.lastRule = self.lastExecutedRule
        
        # Begin again
        self.lastExecutedRule = 0  
        
        # ---------------------------------------------------------------
        # WARNING by Denis: testing shows that the animate function does
        # use threads, and generates nearly random exceptions!!!
        # ---------------------------------------------------------------
        
        # Check if we have to do an animation (Added 09 Aug 2002, JL)
        if( self.animate):   
            # Check that the rule has the info about the time delay                                                         
          if( rule.TimeDelay):   
            # this is a hand-crafted update_idletasks, 
            # which does not work with threads (Added 27 July 2002, by JL)
            self.wait_idle = 1                                                     
            self.parent.after_idle(self.unSetWaitIdle)                              
            while (self.wait_idle): pass                                            
            
            # Get the appropriate delay
            self.delay_ms = rule.TimeDelay.getValue()   
            # Go to sleep for delay_ms miliseconds                            
            self.parent.after(self.delay_ms)                                        
        return True
       
      return False

   def doMatchingChoice( self, matchList ):
      """
      This allows the user to interactively
      specify which subgraph will be transformed by capturing the Left-Click
      event and looking for what is under the cursor.
      Uses the behavior statechart
      Created by Denis: Feb 19, 2005
      """
      atom3i = self.parent
      cb = atom3i.cb
            
      no_value_yet = -1
      cb.initMatchChoice( no_value_yet, matchList )
      atom3i.UI_Statechart.event("GG Select",None)  
              
      # Now we wait for the user to click somewhere
      while( cb.getMatchChoice() == no_value_yet ):
        # Update the 2 Tkinter windows, checking that they aren't dead
        try: atom3i.parent.update()
        except: 
          self.ec.rootWindow.destroy()  
          self.ec.isDestroyed = True
          return None
        
        try: self.ec.rootWindow.update()     
        except:           
          self.ec.isDestroyed = True
          return None
                
        # User is taking a long time, lets get some sleep :D
        time.sleep( 0.3 )       

      return cb.getMatchChoice()
    
    
  
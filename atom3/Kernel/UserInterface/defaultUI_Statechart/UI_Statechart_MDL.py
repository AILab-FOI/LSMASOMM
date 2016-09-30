"""
__UI_Statechart_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Mon Jun 19 01:24:59 2006
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from contains import *
from Hyperedge import *
from graph_Basic import *
from graph_contains import *
from graph_Hyperedge import *
from graph_Composite import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def UI_Statechart_MDL(self, rootNode, DChartsRootNode=None):

    # --- Generating attributes code for ASG DCharts ---
    if( DChartsRootNode ): 
        # variables
        DChartsRootNode.variables.setValue('\n')
        DChartsRootNode.variables.setHeight(15)

        # misc
        DChartsRootNode.misc.setValue('\n')
        DChartsRootNode.misc.setHeight(15)

        # event_clauses
        DChartsRootNode.event_clauses.setValue('\n')
        DChartsRootNode.event_clauses.setHeight(15)
    # --- ASG attributes over ---


    self.obj28=Composite(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # auto_adjust
    self.obj28.auto_adjust.setValue((None, 1))
    self.obj28.auto_adjust.config = 0

    # name
    self.obj28.name.setValue('Active Event Loop')

    # is_default
    self.obj28.is_default.setValue((None, 0))
    self.obj28.is_default.config = 0

    # visible
    self.obj28.visible.setValue((None, 1))
    self.obj28.visible.config = 0

    # exit_action
    self.obj28.exit_action.setValue('\n')
    self.obj28.exit_action.setHeight(15)

    # enter_action
    self.obj28.enter_action.setValue('\n')
    self.obj28.enter_action.setHeight(15)

    self.obj28.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(120.0,-40.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,92.0,31.0,717.0,942.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,92.0,24.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Active Event Loop')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [190.0, -13.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=Composite(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # auto_adjust
    self.obj29.auto_adjust.setValue((None, 1))
    self.obj29.auto_adjust.config = 0

    # name
    self.obj29.name.setValue('Arrow Editor')

    # is_default
    self.obj29.is_default.setValue((None, 0))
    self.obj29.is_default.config = 0

    # visible
    self.obj29.visible.setValue((None, 1))
    self.obj29.visible.config = 0

    # exit_action
    self.obj29.exit_action.setValue('\n')
    self.obj29.exit_action.setHeight(15)

    # enter_action
    self.obj29.enter_action.setValue('\n')
    self.obj29.enter_action.setHeight(15)

    self.obj29.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(540.0,600.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,450.0,692.0,709.0,906.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,450.0,685.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Arrow Editor')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [34.0, -4.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=Composite(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # auto_adjust
    self.obj30.auto_adjust.setValue((None, 1))
    self.obj30.auto_adjust.config = 0

    # name
    self.obj30.name.setValue('New Arrow')

    # is_default
    self.obj30.is_default.setValue((None, 0))
    self.obj30.is_default.config = 0

    # visible
    self.obj30.visible.setValue((None, 1))
    self.obj30.visible.config = 0

    # exit_action
    self.obj30.exit_action.setValue('\n')
    self.obj30.exit_action.setHeight(15)

    # enter_action
    self.obj30.enter_action.setValue('\n')
    self.obj30.enter_action.setHeight(15)

    self.obj30.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(260.0,609.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,245.0,692.0,413.0,913.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,245.0,685.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='New Arrow')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [54.0, -6.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=Basic(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # is_default
    self.obj31.is_default.setValue((None, 1))
    self.obj31.is_default.config = 0

    # name
    self.obj31.name.setValue('Initial')

    # exit_action
    self.obj31.exit_action.setValue('\n')
    self.obj31.exit_action.setHeight(15)

    # enter_action
    self.obj31.enter_action.setValue('\n')
    self.obj31.enter_action.setHeight(15)

    self.obj31.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(0.0,40.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,12.0,43.0,30.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,47.0,52.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Initial')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [24.0, -18.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=Basic(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # is_default
    self.obj32.is_default.setValue((None, 1))
    self.obj32.is_default.config = 0

    # name
    self.obj32.name.setValue('Main')

    # exit_action
    self.obj32.exit_action.setValue('\n')
    self.obj32.exit_action.setHeight(15)

    # enter_action
    self.obj32.enter_action.setValue('cb.setLabelDragModeCursor()\n')
    self.obj32.enter_action.setHeight(15)

    self.obj32.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(120.0,240.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,132.0,243.0,150.0,261.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,114.0,251.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Main')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-29.0, -19.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=Basic(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # is_default
    self.obj33.is_default.setValue((None, 0))
    self.obj33.is_default.config = 0

    # name
    self.obj33.name.setValue('Remove From Selection')

    # exit_action
    self.obj33.exit_action.setValue('\n')
    self.obj33.exit_action.setHeight(15)

    # enter_action
    self.obj33.enter_action.setValue('\n')
    self.obj33.enter_action.setHeight(15)

    self.obj33.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,160.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,163.0,610.0,181.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,608.0,199.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Remove From Selection')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [5.0, 9.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=Basic(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # is_default
    self.obj34.is_default.setValue((None, 0))
    self.obj34.is_default.config = 0

    # name
    self.obj34.name.setValue('New Selection')

    # exit_action
    self.obj34.exit_action.setValue('\n')
    self.obj34.exit_action.setHeight(15)

    # enter_action
    self.obj34.enter_action.setValue('\n')
    self.obj34.enter_action.setHeight(15)

    self.obj34.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,100.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,103.0,610.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,600.0,138.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='New Selection')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-3.0, 8.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=Basic(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # is_default
    self.obj35.is_default.setValue((None, 0))
    self.obj35.is_default.config = 0

    # name
    self.obj35.name.setValue('Add To Selection')

    # exit_action
    self.obj35.exit_action.setValue('\n')
    self.obj35.exit_action.setHeight(15)

    # enter_action
    self.obj35.enter_action.setValue('\n')
    self.obj35.enter_action.setHeight(15)

    self.obj35.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,40.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,43.0,610.0,61.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,604.0,79.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Add To Selection')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [1.0, 9.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=Basic(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # is_default
    self.obj36.is_default.setValue((None, 0))
    self.obj36.is_default.config = 0

    # name
    self.obj36.name.setValue('Drag Nodes')

    # exit_action
    self.obj36.exit_action.setValue('\n')
    self.obj36.exit_action.setHeight(15)

    # enter_action
    self.obj36.enter_action.setValue('enteringDragMode( atom3i )\n')
    self.obj36.enter_action.setHeight(15)

    self.obj36.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,280.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,283.0,610.0,301.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,601.0,318.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Drag Nodes')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-2.0, 8.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=Basic(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # is_default
    self.obj37.is_default.setValue((None, 0))
    self.obj37.is_default.config = 0

    # name
    self.obj37.name.setValue('Scale Entity')

    # exit_action
    self.obj37.exit_action.setValue('\n')
    self.obj37.exit_action.setHeight(15)

    # enter_action
    self.obj37.enter_action.setValue('cb.enteringReSizer( atom3i )\n')
    self.obj37.enter_action.setHeight(15)

    self.obj37.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,349.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,352.0,610.0,370.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,598.0,391.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Scale Entity')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-5.0, 12.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=Basic(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # is_default
    self.obj38.is_default.setValue((None, 0))
    self.obj38.is_default.config = 0

    # name
    self.obj38.name.setValue('Exit')

    # exit_action
    self.obj38.exit_action.setValue('\n')
    self.obj38.exit_action.setHeight(15)

    # enter_action
    self.obj38.enter_action.setValue('\n')
    self.obj38.enter_action.setHeight(15)

    self.obj38.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(0.0,880.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,12.0,883.0,30.0,901.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,42.0,893.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Exit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [19.0, -17.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=Basic(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # is_default
    self.obj39.is_default.setValue((None, 1))
    self.obj39.is_default.config = 0

    # name
    self.obj39.name.setValue('Default')

    # exit_action
    self.obj39.exit_action.setValue('\n')
    self.obj39.exit_action.setHeight(15)

    # enter_action
    self.obj39.enter_action.setValue('atom3i.arrowEditor.enteringArrowEditorMode( atom3i , eventhandler.get_event_params() )\n')
    self.obj39.enter_action.setHeight(15)

    self.obj39.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(480.0,720.0,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,492.0,723.0,510.0,741.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,475.0,719.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Default')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-28.0, -31.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=Basic(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # is_default
    self.obj40.is_default.setValue((None, 0))
    self.obj40.is_default.config = 0

    # name
    self.obj40.name.setValue('Active Point')

    # exit_action
    self.obj40.exit_action.setValue('\n')
    self.obj40.exit_action.setHeight(15)

    # enter_action
    self.obj40.enter_action.setValue('atom3i.arrowEditor.enteringActiveControlPointMode( atom3i )\n')
    self.obj40.enter_action.setHeight(15)

    self.obj40.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(620.0,740.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,632.0,743.0,650.0,761.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,672.0,737.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Active Point')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [29.0, -33.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=Basic(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # is_default
    self.obj41.is_default.setValue((None, 1))
    self.obj41.is_default.config = 0

    # name
    self.obj41.name.setValue('Snap Points')

    # exit_action
    self.obj41.exit_action.setValue('\n')
    self.obj41.exit_action.setHeight(15)

    # enter_action
    self.obj41.enter_action.setValue('atom3i.pilotArrow.enteringArrowMode( atom3i )\n')
    self.obj41.enter_action.setHeight(15)

    self.obj41.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(260.0,709.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,272.0,712.0,290.0,730.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,284.0,705.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Snap Points')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [1.0, -34.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=Basic(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # is_default
    self.obj42.is_default.setValue((None, 0))
    self.obj42.is_default.config = 0

    # name
    self.obj42.name.setValue('No Snap')

    # exit_action
    self.obj42.exit_action.setValue('\n')
    self.obj42.exit_action.setHeight(15)

    # enter_action
    self.obj42.enter_action.setValue('atom3i.pilotArrow.enteringArrowMode( atom3i )\n')
    self.obj42.enter_action.setHeight(15)

    self.obj42.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(260.0,869.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,272.0,872.0,290.0,890.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,290.0,900.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='No Snap')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [7.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=Basic(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # is_default
    self.obj43.is_default.setValue((None, 0))
    self.obj43.is_default.config = 0

    # name
    self.obj43.name.setValue('Postscript')

    # exit_action
    self.obj43.exit_action.setValue('\n')
    self.obj43.exit_action.setHeight(15)

    # enter_action
    self.obj43.enter_action.setValue('atom3i.postscriptBox.enteringPostscript()\n')
    self.obj43.enter_action.setHeight(15)

    self.obj43.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,460.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,463.0,610.0,481.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,642.0,476.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Postscript')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [39.0, -14.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=Basic(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # is_default
    self.obj44.is_default.setValue((None, 0))
    self.obj44.is_default.config = 0

    # name
    self.obj44.name.setValue('Bounding Box Edit')

    # exit_action
    self.obj44.exit_action.setValue('\n')
    self.obj44.exit_action.setHeight(15)

    # enter_action
    self.obj44.enter_action.setValue('\n')
    self.obj44.enter_action.setHeight(15)

    self.obj44.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,540.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,543.0,610.0,561.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,607.0,571.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Bounding Box Edit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [4.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Basic(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # is_default
    self.obj45.is_default.setValue((None, 0))
    self.obj45.is_default.config = 0

    # name
    self.obj45.name.setValue('Drag Label')

    # exit_action
    self.obj45.exit_action.setValue('\n')
    self.obj45.exit_action.setHeight(15)

    # enter_action
    self.obj45.enter_action.setValue('enteringDragMode( atom3i )\n')
    self.obj45.enter_action.setHeight(15)

    self.obj45.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,220.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,223.0,610.0,241.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,603.0,260.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Drag Label')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [0.0, 10.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=Basic(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # is_default
    self.obj46.is_default.setValue((None, 0))
    self.obj46.is_default.config = 0

    # name
    self.obj46.name.setValue('Scale Text')

    # exit_action
    self.obj46.exit_action.setValue('\n')
    self.obj46.exit_action.setHeight(15)

    # enter_action
    self.obj46.enter_action.setValue('cb.enteringReSizer( atom3i )\n')
    self.obj46.enter_action.setHeight(15)

    self.obj46.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,400.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,403.0,610.0,421.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,601.0,440.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Scale Text')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-2.0, 10.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Basic(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # is_default
    self.obj47.is_default.setValue((None, 0))
    self.obj47.is_default.config = 0

    # name
    self.obj47.name.setValue('GG Graph Select')

    # exit_action
    self.obj47.exit_action.setValue('cb.setMatchChoice( atom3i, eventhandler.get_event_params() )\n')
    self.obj47.exit_action.setHeight(15)

    # enter_action
    self.obj47.enter_action.setValue('\n')
    self.obj47.enter_action.setHeight(15)

    self.obj47.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(580.0,588.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,592.0,591.0,610.0,609.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,603.125,618.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='GG Graph Select')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font27238352')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Basic(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # is_default
    self.obj48.is_default.setValue((None, 0))
    self.obj48.is_default.config = 0

    # name
    self.obj48.name.setValue('Drop Point')

    # exit_action
    self.obj48.exit_action.setValue('\n')
    self.obj48.exit_action.setHeight(15)

    # enter_action
    self.obj48.enter_action.setValue('dropArrowPoints( atom3i, eventhandler.get_event_params() )\n\neventhandler.event(\'[Done]\')\n')
    self.obj48.enter_action.setHeight(15)

    self.obj48.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(340.0,740.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,352.0,743.0,370.0,761.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,363.125,770.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Drop Point')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font37785768')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Basic(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # is_default
    self.obj49.is_default.setValue((None, 0))
    self.obj49.is_default.config = 0

    # name
    self.obj49.name.setValue('Drop Point2')

    # exit_action
    self.obj49.exit_action.setValue('\n')
    self.obj49.exit_action.setHeight(15)

    # enter_action
    self.obj49.enter_action.setValue('dropArrowPoints( atom3i, eventhandler.get_event_params(), snap=False)\n\n\neventhandler.event(\'[Done]\')\n')
    self.obj49.enter_action.setHeight(15)

    self.obj49.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(340.0,820.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,352.0,823.0,370.0,841.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,365.125,817.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Drop Point2')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font26484288')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [2.0, -33.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=contains(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(633.0,8.125,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=contains(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(644.625,33.75,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=contains(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    self.obj52.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(644.25,67.75,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=contains(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    self.obj53.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(231.125,182.875,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=contains(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    self.obj54.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(166.25,350.375,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=contains(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(232.5,336.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=contains(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(173.0,402.875,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=contains(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(765.375,862.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=contains(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    self.obj58.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(789.875,899.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=contains(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    self.obj59.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(489.5,670.375,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=contains(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    self.obj60.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(8.0,716.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=contains(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(47.875,1004.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=contains(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(387.638290478,781.443472332,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=contains(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    self.obj63.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(390.460104451,814.747395833,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=Hyperedge(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # name
    self.obj64.name.setValue('')
    self.obj64.name.setNone()

    # broadcast
    self.obj64.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj64.broadcast.setHeight(15)

    # guard
    self.obj64.guard.setValue('cb.isNoItemUnderCursor( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj64.trigger.setValue('<Alt-ButtonPress-1>')

    # action
    self.obj64.action.setValue('event=eventhandler.get_event_params()\ncb.clearSelectionTuple()\nstartNewSelectionBox(atom3i, event, "red")\n\nsetCursor( atom3i.parent, \'Selection\' )\nsetDefaultCursor( atom3i.parent )\n')
    self.obj64.action.setHeight(15)

    # broadcast_to
    self.obj64.broadcast_to.setValue('')
    self.obj64.broadcast_to.setNone()

    # display
    self.obj64.display.setValue('Negative Selection')

    self.obj64.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(424.0,160.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=Hyperedge(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # name
    self.obj65.name.setValue('')
    self.obj65.name.setNone()

    # broadcast
    self.obj65.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj65.broadcast.setHeight(15)

    # guard
    self.obj65.guard.setValue('1')

    # trigger
    self.obj65.trigger.setValue('<Any-Motion>')

    # action
    self.obj65.action.setValue('savePosition = cb.getCanvasCoords( eventhandler.get_event_params()  )\n')
    self.obj65.action.setHeight(15)

    # broadcast_to
    self.obj65.broadcast_to.setValue('')
    self.obj65.broadcast_to.setNone()

    # display
    self.obj65.display.setValue('Motion')

    self.obj65.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-34.0, -19.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=Hyperedge(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # name
    self.obj66.name.setValue('')
    self.obj66.name.setNone()

    # broadcast
    self.obj66.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj66.broadcast.setHeight(15)

    # guard
    self.obj66.guard.setValue('1')

    # trigger
    self.obj66.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj66.action.setValue('cb.deleteFromSelectionDict( getFinalSelectionBoxItems( atom3i ) )\n                  \n# Enable highlighting on selected items\ncb.highlighter(1)  \n\nsetDefaultCursor( atom3i.parent )\n')
    self.obj66.action.setHeight(15)

    # broadcast_to
    self.obj66.broadcast_to.setValue('')
    self.obj66.broadcast_to.setNone()

    # display
    self.obj66.display.setValue('Finish Selection')

    self.obj66.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(417.0,200.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=Hyperedge(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # name
    self.obj67.name.setValue('')
    self.obj67.name.setNone()

    # broadcast
    self.obj67.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj67.broadcast.setHeight(15)

    # guard
    self.obj67.guard.setValue('cb.isNoItemUnderCursor( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj67.trigger.setValue('<Shift-ButtonPress-1>')

    # action
    self.obj67.action.setValue('event=eventhandler.get_event_params()\ncb.clearSelectionTuple()\nstartNewSelectionBox(atom3i, event, "green")\nsetCursor( atom3i.parent, \'Selection\' )\n')
    self.obj67.action.setHeight(15)

    # broadcast_to
    self.obj67.broadcast_to.setValue('')
    self.obj67.broadcast_to.setNone()

    # display
    self.obj67.display.setValue('Additive Selection')

    self.obj67.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(420.0,40.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=Hyperedge(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # name
    self.obj68.name.setValue('')
    self.obj68.name.setNone()

    # broadcast
    self.obj68.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj68.broadcast.setHeight(15)

    # guard
    self.obj68.guard.setValue('cb.isNoItemUnderCursor( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj68.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj68.action.setValue('cb.clearSelectionTuple()\nstartNewSelectionBox(atom3i, eventhandler.get_event_params(), "yellow")\n\ncb.highlighter( 0 )      \ncb.clearSelectionDict()\n\nsetCursor( atom3i.parent, \'Selection\' )\n')
    self.obj68.action.setHeight(15)

    # broadcast_to
    self.obj68.broadcast_to.setValue('')
    self.obj68.broadcast_to.setNone()

    # display
    self.obj68.display.setValue('Fresh Selection')

    self.obj68.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(416.0,100.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=Hyperedge(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # name
    self.obj69.name.setValue('')
    self.obj69.name.setNone()

    # broadcast
    self.obj69.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj69.broadcast.setHeight(15)

    # guard
    self.obj69.guard.setValue('1')

    # trigger
    self.obj69.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj69.action.setValue('cb.updateSelectionDict( getFinalSelectionBoxItems( atom3i )  )\n                  \n# Enable highlighting on selected items\ncb.highlighter(1)  \n\nsetDefaultCursor( atom3i.parent )\n')
    self.obj69.action.setHeight(15)

    # broadcast_to
    self.obj69.broadcast_to.setValue('')
    self.obj69.broadcast_to.setNone()

    # display
    self.obj69.display.setValue('Finish Selection')

    self.obj69.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(417.0,80.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Hyperedge(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # name
    self.obj70.name.setValue('')
    self.obj70.name.setNone()

    # broadcast
    self.obj70.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj70.broadcast.setHeight(15)

    # guard
    self.obj70.guard.setValue('1')

    # trigger
    self.obj70.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj70.action.setValue('cb.updateSelectionDict( getFinalSelectionBoxItems( atom3i )  )\n                  \n# Enable highlighting on selected items\ncb.highlighter(1)  \n\nsetDefaultCursor( atom3i.parent )\n')
    self.obj70.action.setHeight(15)

    # broadcast_to
    self.obj70.broadcast_to.setValue('')
    self.obj70.broadcast_to.setNone()

    # display
    self.obj70.display.setValue('Finish Selection')

    self.obj70.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(417.0,140.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=Hyperedge(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # name
    self.obj71.name.setValue('')
    self.obj71.name.setNone()

    # broadcast
    self.obj71.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj71.broadcast.setHeight(15)

    # guard
    self.obj71.guard.setValue('cb.isItemUnderCursorUnselected( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj71.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj71.action.setValue('event = eventhandler.get_event_params()\n\ncb.clearSelectionTuple()\n# Item under cursor, make sure it\'s in the selection\ncb.appendSelectionTuple( cb.getItemUnderCursor( atom3i, event)[0]  )\n\ncb.highlighter(0) \ncb.clearSelectionDict() \nstartNewSelectionBox(atom3i,event , "yellow")\n\nsetCursor( atom3i.parent, \'Selection\' )\n')
    self.obj71.action.setHeight(15)

    # broadcast_to
    self.obj71.broadcast_to.setValue('')
    self.obj71.broadcast_to.setNone()

    # display
    self.obj71.display.setValue('Fresh Selection')

    self.obj71.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(416.0,120.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=Hyperedge(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # name
    self.obj72.name.setValue('')
    self.obj72.name.setNone()

    # broadcast
    self.obj72.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj72.broadcast.setHeight(15)

    # guard
    self.obj72.guard.setValue('1')

    # trigger
    self.obj72.trigger.setValue('<Any-Motion>')

    # action
    self.obj72.action.setValue('dragInMotion(atom3i,eventhandler.get_event_params() )\n\n\nwasDragged = True\n')
    self.obj72.action.setHeight(15)

    # broadcast_to
    self.obj72.broadcast_to.setValue('')
    self.obj72.broadcast_to.setNone()

    # display
    self.obj72.display.setValue('Motion')

    self.obj72.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,300.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-6.0, -7.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Hyperedge(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # name
    self.obj73.name.setValue('')
    self.obj73.name.setNone()

    # broadcast
    self.obj73.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj73.broadcast.setHeight(15)

    # guard
    self.obj73.guard.setValue('cb.isItemUnderCursorSelected( atom3i, eventhandler.get_event_params()) and not cb.isLabelDragMode()')

    # trigger
    self.obj73.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj73.action.setValue('# Create an object set from the selectionDict\ncb.buildSelectionObjectSet()     \n # Start dragging!\ndragStart( atom3i )    \nsetCursor( atom3i.parent, \'Drag\' )\n\n\nwasDragged = False\n')
    self.obj73.action.setHeight(15)

    # broadcast_to
    self.obj73.broadcast_to.setValue('')
    self.obj73.broadcast_to.setNone()

    # display
    self.obj73.display.setValue('Start Drag')

    self.obj73.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(402.0,280.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Hyperedge(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # name
    self.obj74.name.setValue('')
    self.obj74.name.setNone()

    # broadcast
    self.obj74.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj74.broadcast.setHeight(15)

    # guard
    self.obj74.guard.setValue('1')

    # trigger
    self.obj74.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj74.action.setValue('dragFinish( atom3i, eventhandler.get_event_params() )  \nsetDefaultCursor( atom3i.parent )\n\n\nif(not wasDragged): cb.clearSelectionTuple()\nif(not wasDragged): cb.highlighter( 0 )      \nif(not wasDragged): cb.clearSelectionDict()\nif(wasDragged): cb.highlighter( 1 )  \n')
    self.obj74.action.setHeight(15)

    # broadcast_to
    self.obj74.broadcast_to.setValue('')
    self.obj74.broadcast_to.setNone()

    # display
    self.obj74.display.setValue('Finish Drag')

    self.obj74.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(407.0,316.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=Hyperedge(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # name
    self.obj75.name.setValue('')
    self.obj75.name.setNone()

    # broadcast
    self.obj75.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj75.broadcast.setHeight(15)

    # guard
    self.obj75.guard.setValue('cb.isItemUnderCursorUnselected( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj75.trigger.setValue('<Shift-ButtonPress-1>')

    # action
    self.obj75.action.setValue('event=eventhandler.get_event_params()\n\nstartNewSelectionBox(atom3i, event, "green")\n\n\n# Item under cursor, make sure it\'s in the selection\ncb.appendSelectionTuple( cb.getItemUnderCursor( atom3i, event)[0]  )\n\nsetCursor( atom3i.parent, \'Selection\' )\n')
    self.obj75.action.setHeight(15)

    # broadcast_to
    self.obj75.broadcast_to.setValue('')
    self.obj75.broadcast_to.setNone()

    # display
    self.obj75.display.setValue('Additive Selection')

    self.obj75.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(420.0,60.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=Hyperedge(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # name
    self.obj76.name.setValue('')
    self.obj76.name.setNone()

    # broadcast
    self.obj76.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj76.broadcast.setHeight(15)

    # guard
    self.obj76.guard.setValue('cb.isItemUnderCursorSelected( atom3i, eventhandler.get_event_params())')

    # trigger
    self.obj76.trigger.setValue('<Alt-ButtonPress-1>')

    # action
    self.obj76.action.setValue('event=eventhandler.get_event_params()\n\nstartNewSelectionBox(atom3i, event, "red")\n\n\n# Item under cursor, make sure it\'s in the selection\ncb.appendSelectionTuple( cb.getItemUnderCursor( atom3i, event)[0]  )\n\nsetCursor( atom3i.parent, \'Selection\' )\n')
    self.obj76.action.setHeight(15)

    # broadcast_to
    self.obj76.broadcast_to.setValue('')
    self.obj76.broadcast_to.setNone()

    # display
    self.obj76.display.setValue('Negative Selection')

    self.obj76.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(424.0,180.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=Hyperedge(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # name
    self.obj77.name.setValue('')
    self.obj77.name.setNone()

    # broadcast
    self.obj77.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj77.broadcast.setHeight(15)

    # guard
    self.obj77.guard.setValue('1')

    # trigger
    self.obj77.trigger.setValue('Start')

    # action
    self.obj77.action.setValue('from CallbackHandlers import *\nfrom Cursors                 import setCursor, setDefaultCursor\nfrom Utilities                 import modelChange,optimizeConnectionPorts\nimport ZoomFocus \nimport SnapGrid\n\natom3i=eventhandler.get_event_params()\ncb=atom3i.cb\n')
    self.obj77.action.setHeight(15)

    # broadcast_to
    self.obj77.broadcast_to.setValue('')
    self.obj77.broadcast_to.setNone()

    # display
    self.obj77.display.setValue('Start')

    self.obj77.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(20.0,260.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [14.0, 146.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=Hyperedge(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # name
    self.obj78.name.setValue('')
    self.obj78.name.setNone()

    # broadcast
    self.obj78.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj78.broadcast.setHeight(15)

    # guard
    self.obj78.guard.setValue('1')

    # trigger
    self.obj78.trigger.setValue('<Any-Motion>')

    # action
    self.obj78.action.setValue('selectionBoxDragging(atom3i, eventhandler.get_event_params())  \n')
    self.obj78.action.setHeight(15)

    # broadcast_to
    self.obj78.broadcast_to.setValue('')
    self.obj78.broadcast_to.setNone()

    # display
    self.obj78.display.setValue('Motion')

    self.obj78.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,180.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-7.0, -9.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=Hyperedge(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # name
    self.obj79.name.setValue('')
    self.obj79.name.setNone()

    # broadcast
    self.obj79.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj79.broadcast.setHeight(15)

    # guard
    self.obj79.guard.setValue('1')

    # trigger
    self.obj79.trigger.setValue('<Any-Motion>')

    # action
    self.obj79.action.setValue('selectionBoxDragging(atom3i,eventhandler.get_event_params()) \n\n##atom3i.execAction( selectionBoxDragging, \n##            [atom3i, eventhandler.get_event_params()] )\n')
    self.obj79.action.setHeight(15)

    # broadcast_to
    self.obj79.broadcast_to.setValue('')
    self.obj79.broadcast_to.setNone()

    # display
    self.obj79.display.setValue('Motion')

    self.obj79.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,120.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-7.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=Hyperedge(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # name
    self.obj80.name.setValue('')
    self.obj80.name.setNone()

    # broadcast
    self.obj80.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj80.broadcast.setHeight(15)

    # guard
    self.obj80.guard.setValue('1')

    # trigger
    self.obj80.trigger.setValue('<Any-Motion>')

    # action
    self.obj80.action.setValue('selectionBoxDragging(atom3i, eventhandler.get_event_params()) \n')
    self.obj80.action.setHeight(15)

    # broadcast_to
    self.obj80.broadcast_to.setValue('')
    self.obj80.broadcast_to.setNone()

    # display
    self.obj80.display.setValue('Motion')

    self.obj80.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,60.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-7.0, -8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=Hyperedge(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # name
    self.obj81.name.setValue('')
    self.obj81.name.setNone()

    # broadcast
    self.obj81.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj81.broadcast.setHeight(15)

    # guard
    self.obj81.guard.setValue('1')

    # trigger
    self.obj81.trigger.setValue('Reset')

    # action
    self.obj81.action.setValue('setDefaultCursor( atom3i.parent )\n')
    self.obj81.action.setHeight(15)

    # broadcast_to
    self.obj81.broadcast_to.setValue('')
    self.obj81.broadcast_to.setNone()

    # display
    self.obj81.display.setValue('Reset')

    self.obj81.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(20.0,480.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-6.0, -14.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=Hyperedge(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # name
    self.obj82.name.setValue('')
    self.obj82.name.setNone()

    # broadcast
    self.obj82.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj82.broadcast.setHeight(15)

    # guard
    self.obj82.guard.setValue('not cb.isLabelDragMode()')

    # trigger
    self.obj82.trigger.setValue('<KeyPress-r>')

    # action
    self.obj82.action.setValue('cb.initReSizer()\nsetCursor( atom3i.parent, \'Sizing\' )\n')
    self.obj82.action.setHeight(15)

    # broadcast_to
    self.obj82.broadcast_to.setValue('')
    self.obj82.broadcast_to.setNone()

    # display
    self.obj82.display.setValue('Scale Selection')

    self.obj82.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(417.0,357.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=Hyperedge(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # name
    self.obj83.name.setValue('')
    self.obj83.name.setNone()

    # broadcast
    self.obj83.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj83.broadcast.setHeight(15)

    # guard
    self.obj83.guard.setValue('1')

    # trigger
    self.obj83.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj83.action.setValue('setDefaultCursor( atom3i.parent )\n')
    self.obj83.action.setHeight(15)

    # broadcast_to
    self.obj83.broadcast_to.setValue('')
    self.obj83.broadcast_to.setNone()

    # display
    self.obj83.display.setValue('Finish Scale')

    self.obj83.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(392.0,370.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [17.0, 1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=Hyperedge(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # name
    self.obj84.name.setValue('')
    self.obj84.name.setNone()

    # broadcast
    self.obj84.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj84.broadcast.setHeight(15)

    # guard
    self.obj84.guard.setValue('1')

    # trigger
    self.obj84.trigger.setValue('<Any-Motion>')

    # action
    self.obj84.action.setValue('scaleWithMotion( atom3i, eventhandler.get_event_params() )\n')
    self.obj84.action.setHeight(15)

    # broadcast_to
    self.obj84.broadcast_to.setValue('')
    self.obj84.broadcast_to.setNone()

    # display
    self.obj84.display.setValue('Motion')

    self.obj84.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,378.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-6.0, -9.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=Hyperedge(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # name
    self.obj85.name.setValue('')
    self.obj85.name.setNone()

    # broadcast
    self.obj85.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj85.broadcast.setHeight(15)

    # guard
    self.obj85.guard.setValue('1')

    # trigger
    self.obj85.trigger.setValue('<Control-ButtonPress-3>')

    # action
    self.obj85.action.setValue('atom3ActionMap( atom3i, eventhandler.get_event_params()  )\n')
    self.obj85.action.setHeight(15)

    # broadcast_to
    self.obj85.broadcast_to.setValue('')
    self.obj85.broadcast_to.setNone()

    # display
    self.obj85.display.setValue('Model Action')

    self.obj85.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-19.0, -35.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=Hyperedge(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # name
    self.obj86.name.setValue('')
    self.obj86.name.setNone()

    # broadcast
    self.obj86.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj86.broadcast.setHeight(15)

    # guard
    self.obj86.guard.setValue('1')

    # trigger
    self.obj86.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj86.action.setValue('createDynamicMenu( atom3i, eventhandler.get_event_params() )\n')
    self.obj86.action.setHeight(15)

    # broadcast_to
    self.obj86.broadcast_to.setValue('')
    self.obj86.broadcast_to.setNone()

    # display
    self.obj86.display.setValue('Popup Menu')

    self.obj86.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-16.0, -129.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=Hyperedge(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # name
    self.obj87.name.setValue('')
    self.obj87.name.setNone()

    # broadcast
    self.obj87.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj87.broadcast.setHeight(15)

    # guard
    self.obj87.guard.setValue('1')

    # trigger
    self.obj87.trigger.setValue('<Control-KeyPress-a>')

    # action
    self.obj87.action.setValue('selectAllVisibleObjects( atom3i )\n')
    self.obj87.action.setHeight(15)

    # broadcast_to
    self.obj87.broadcast_to.setValue('')
    self.obj87.broadcast_to.setNone()

    # display
    self.obj87.display.setValue('Select All')

    self.obj87.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-21.0, 358.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=Hyperedge(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # name
    self.obj88.name.setValue('')
    self.obj88.name.setNone()

    # broadcast
    self.obj88.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj88.broadcast.setHeight(15)

    # guard
    self.obj88.guard.setValue('1')

    # trigger
    self.obj88.trigger.setValue('<Control-KeyPress-Delete>')

    # action
    self.obj88.action.setValue('cb.clearSelectionDict()\natom3i.clearModel()\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj88.action.setHeight(15)

    # broadcast_to
    self.obj88.broadcast_to.setValue('')
    self.obj88.broadcast_to.setNone()

    # display
    self.obj88.display.setValue('Clear Canvas')

    self.obj88.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-11.0, 211.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=Hyperedge(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # name
    self.obj89.name.setValue('')
    self.obj89.name.setNone()

    # broadcast
    self.obj89.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj89.broadcast.setHeight(15)

    # guard
    self.obj89.guard.setValue('1')

    # trigger
    self.obj89.trigger.setValue('<KeyPress-Delete>')

    # action
    self.obj89.action.setValue('#deleteSelected(atom3i)\ngetSelectedItemsForDelete(atom3i)\n')
    self.obj89.action.setHeight(15)

    # broadcast_to
    self.obj89.broadcast_to.setValue('')
    self.obj89.broadcast_to.setNone()

    # display
    self.obj89.display.setValue('DeleteRequest')

    self.obj89.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-8.0, 559.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=Hyperedge(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # name
    self.obj90.name.setValue('')
    self.obj90.name.setNone()

    # broadcast
    self.obj90.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj90.broadcast.setHeight(15)

    # guard
    self.obj90.guard.setValue('1')

    # trigger
    self.obj90.trigger.setValue('<KeyPress-s>')

    # action
    self.obj90.action.setValue('cb.smoothSelected()\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj90.action.setHeight(15)

    # broadcast_to
    self.obj90.broadcast_to.setValue('')
    self.obj90.broadcast_to.setNone()

    # display
    self.obj90.display.setValue('Smooth')

    self.obj90.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-26.0, 461.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=Hyperedge(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # name
    self.obj91.name.setValue('')
    self.obj91.name.setNone()

    # broadcast
    self.obj91.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj91.broadcast.setHeight(15)

    # guard
    self.obj91.guard.setValue('1')

    # trigger
    self.obj91.trigger.setValue('Edit Properties')

    # action
    self.obj91.action.setValue('event =  eventhandler.get_event_params() \natom3i.editclass( event.x_root, event.y_root )\n')
    self.obj91.action.setHeight(15)

    # broadcast_to
    self.obj91.broadcast_to.setValue('')
    self.obj91.broadcast_to.setNone()

    # display
    self.obj91.display.setValue('Edit Properties')

    self.obj91.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-7.0, 341.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=Hyperedge(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # name
    self.obj92.name.setValue('')
    self.obj92.name.setNone()

    # broadcast
    self.obj92.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj92.broadcast.setHeight(15)

    # guard
    self.obj92.guard.setValue('1')

    # trigger
    self.obj92.trigger.setValue('<KeyPress-Left>')

    # action
    self.obj92.action.setValue('cb.buildSelectionObjectSet()\nselection = cb.getSelectionObjectSet()\ndragStart(atom3i)\ndragMotion(atom3i,[0,0],[-1,0],selection)\ndragDrop(atom3i,selection)\noptimizeConnectionPorts( atom3i )\n')
    self.obj92.action.setHeight(15)

    # broadcast_to
    self.obj92.broadcast_to.setValue('')
    self.obj92.broadcast_to.setNone()

    # display
    self.obj92.display.setValue('Move Left')

    self.obj92.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-21.0, 506.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=Hyperedge(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # name
    self.obj93.name.setValue('')
    self.obj93.name.setNone()

    # broadcast
    self.obj93.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj93.broadcast.setHeight(15)

    # guard
    self.obj93.guard.setValue('1')

    # trigger
    self.obj93.trigger.setValue('<KeyPress-Right>')

    # action
    self.obj93.action.setValue('cb.buildSelectionObjectSet()\nselection = cb.getSelectionObjectSet()\ndragStart(atom3i)\ndragMotion(atom3i,[0,0],[1,0],selection)\ndragDrop(atom3i,selection)\noptimizeConnectionPorts( atom3i )\n')
    self.obj93.action.setHeight(15)

    # broadcast_to
    self.obj93.broadcast_to.setValue('')
    self.obj93.broadcast_to.setNone()

    # display
    self.obj93.display.setValue('Move Right')

    self.obj93.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, 521.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=Hyperedge(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    # name
    self.obj94.name.setValue('')
    self.obj94.name.setNone()

    # broadcast
    self.obj94.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj94.broadcast.setHeight(15)

    # guard
    self.obj94.guard.setValue('1')

    # trigger
    self.obj94.trigger.setValue('<KeyPress-Down>')

    # action
    self.obj94.action.setValue('cb.buildSelectionObjectSet()\nselection = cb.getSelectionObjectSet()\ndragStart(atom3i)\ndragMotion(atom3i,[0,0],[0,1],selection)\ndragDrop(atom3i,selection)\noptimizeConnectionPorts( atom3i )\n')
    self.obj94.action.setHeight(15)

    # broadcast_to
    self.obj94.broadcast_to.setValue('')
    self.obj94.broadcast_to.setNone()

    # display
    self.obj94.display.setValue('Move Down')

    self.obj94.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-16.0, 535.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=Hyperedge(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    # name
    self.obj95.name.setValue('')
    self.obj95.name.setNone()

    # broadcast
    self.obj95.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj95.broadcast.setHeight(15)

    # guard
    self.obj95.guard.setValue('1')

    # trigger
    self.obj95.trigger.setValue('<KeyPress-Up>')

    # action
    self.obj95.action.setValue('cb.buildSelectionObjectSet()\nselection = cb.getSelectionObjectSet()\ndragStart(atom3i)\ndragMotion(atom3i,[0,0],[0,-1],selection)\ndragDrop(atom3i,selection)\noptimizeConnectionPorts( atom3i )\n')
    self.obj95.action.setHeight(15)

    # broadcast_to
    self.obj95.broadcast_to.setValue('')
    self.obj95.broadcast_to.setNone()

    # display
    self.obj95.display.setValue('Move Up')

    self.obj95.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-25.0, 547.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=Hyperedge(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    # name
    self.obj96.name.setValue('')
    self.obj96.name.setNone()

    # broadcast
    self.obj96.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj96.broadcast.setHeight(15)

    # guard
    self.obj96.guard.setValue('1')

    # trigger
    self.obj96.trigger.setValue('<Control-KeyPress-o>')

    # action
    self.obj96.action.setValue('atom3i.open()\n')
    self.obj96.action.setHeight(15)

    # broadcast_to
    self.obj96.broadcast_to.setValue('')
    self.obj96.broadcast_to.setNone()

    # display
    self.obj96.display.setValue('Open')

    self.obj96.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-33.0, 8.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=Hyperedge(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    # name
    self.obj97.name.setValue('')
    self.obj97.name.setNone()

    # broadcast
    self.obj97.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj97.broadcast.setHeight(15)

    # guard
    self.obj97.guard.setValue('1')

    # trigger
    self.obj97.trigger.setValue('<Control-KeyPress-s>')

    # action
    self.obj97.action.setValue('atom3i.save(0, atom3i.statusbar.getState( atom3i.statusbar.MODEL )[1][0] )\n')
    self.obj97.action.setHeight(15)

    # broadcast_to
    self.obj97.broadcast_to.setValue('')
    self.obj97.broadcast_to.setNone()

    # display
    self.obj97.display.setValue('Save')

    self.obj97.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-34.0, 25.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=Hyperedge(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # name
    self.obj98.name.setValue('')
    self.obj98.name.setNone()

    # broadcast
    self.obj98.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj98.broadcast.setHeight(15)

    # guard
    self.obj98.guard.setValue('1')

    # trigger
    self.obj98.trigger.setValue('<Alt-KeyPress-s>')

    # action
    self.obj98.action.setValue('atom3i.save(0)\n')
    self.obj98.action.setHeight(15)

    # broadcast_to
    self.obj98.broadcast_to.setValue('')
    self.obj98.broadcast_to.setNone()

    # display
    self.obj98.display.setValue('Save As')

    self.obj98.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-25.0, 40.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=Hyperedge(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    # name
    self.obj99.name.setValue('')
    self.obj99.name.setNone()

    # broadcast
    self.obj99.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj99.broadcast.setHeight(15)

    # guard
    self.obj99.guard.setValue('atom3i.optionsDatabase.showOptionsDatabase()')

    # trigger
    self.obj99.trigger.setValue('<KeyPress-F1>')

    # action
    self.obj99.action.setValue('atom3i.loadImmediateOptions()\n')
    self.obj99.action.setHeight(15)

    # broadcast_to
    self.obj99.broadcast_to.setValue('')
    self.obj99.broadcast_to.setNone()

    # display
    self.obj99.display.setValue('Options')

    self.obj99.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-29.0, 55.0]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=Hyperedge(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # name
    self.obj100.name.setValue('')
    self.obj100.name.setNone()

    # broadcast
    self.obj100.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj100.broadcast.setHeight(15)

    # guard
    self.obj100.guard.setValue('1')

    # trigger
    self.obj100.trigger.setValue('<KeyPress-F2>')

    # action
    self.obj100.action.setValue('atom3i.showConsole()\n')
    self.obj100.action.setHeight(15)

    # broadcast_to
    self.obj100.broadcast_to.setValue('')
    self.obj100.broadcast_to.setNone()

    # display
    self.obj100.display.setValue('Show Console')

    self.obj100.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-11.0, 73.0]
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=Hyperedge(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # name
    self.obj101.name.setValue('')
    self.obj101.name.setNone()

    # broadcast
    self.obj101.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj101.broadcast.setHeight(15)

    # guard
    self.obj101.guard.setValue('1')

    # trigger
    self.obj101.trigger.setValue('<KeyPress-F3>')

    # action
    self.obj101.action.setValue('atom3i.openMetaModel()\n')
    self.obj101.action.setHeight(15)

    # broadcast_to
    self.obj101.broadcast_to.setValue('')
    self.obj101.broadcast_to.setNone()

    # display
    self.obj101.display.setValue('Open Metamodel')

    self.obj101.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-4.0, 90.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=Hyperedge(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # name
    self.obj102.name.setValue('')
    self.obj102.name.setNone()

    # broadcast
    self.obj102.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj102.broadcast.setHeight(15)

    # guard
    self.obj102.guard.setValue('1')

    # trigger
    self.obj102.trigger.setValue('<KeyPress-F9>')

    # action
    self.obj102.action.setValue('toggleCreateAsSmooth( atom3i )\n')
    self.obj102.action.setHeight(15)

    # broadcast_to
    self.obj102.broadcast_to.setValue('')
    self.obj102.broadcast_to.setNone()

    # display
    self.obj102.display.setValue('Smooth Default')

    self.obj102.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-10.0, 108.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=Hyperedge(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    # name
    self.obj103.name.setValue('')
    self.obj103.name.setNone()

    # broadcast
    self.obj103.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj103.broadcast.setHeight(15)

    # guard
    self.obj103.guard.setValue('1')

    # trigger
    self.obj103.trigger.setValue('<KeyPress-F4>')

    # action
    self.obj103.action.setValue('atom3i.closeMetaModel()\n')
    self.obj103.action.setHeight(15)

    # broadcast_to
    self.obj103.broadcast_to.setValue('')
    self.obj103.broadcast_to.setNone()

    # display
    self.obj103.display.setValue('Close Metamodel')

    self.obj103.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-3.0, 125.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=Hyperedge(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # name
    self.obj104.name.setValue('')
    self.obj104.name.setNone()

    # broadcast
    self.obj104.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj104.broadcast.setHeight(15)

    # guard
    self.obj104.guard.setValue('1')

    # trigger
    self.obj104.trigger.setValue('<KeyPress-F6>')

    # action
    self.obj104.action.setValue('atom3i.popupMenuCreator.LastModelPopup(eventhandler.get_event_params() )\n')
    self.obj104.action.setHeight(15)

    # broadcast_to
    self.obj104.broadcast_to.setValue('')
    self.obj104.broadcast_to.setNone()

    # display
    self.obj104.display.setValue('Recent Model')

    self.obj104.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-12.0, 142.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=Hyperedge(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # name
    self.obj105.name.setValue('')
    self.obj105.name.setNone()

    # broadcast
    self.obj105.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj105.broadcast.setHeight(15)

    # guard
    self.obj105.guard.setValue('1')

    # trigger
    self.obj105.trigger.setValue('<KeyPress-F7>')

    # action
    self.obj105.action.setValue('atom3i.popupMenuCreator.LastMetaModelPopup( eventhandler.get_event_params() )\n')
    self.obj105.action.setHeight(15)

    # broadcast_to
    self.obj105.broadcast_to.setValue('')
    self.obj105.broadcast_to.setNone()

    # display
    self.obj105.display.setValue('Recent Metamodel')

    self.obj105.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [2.0, 160.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Hyperedge(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # name
    self.obj106.name.setValue('')
    self.obj106.name.setNone()

    # broadcast
    self.obj106.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj106.broadcast.setHeight(15)

    # guard
    self.obj106.guard.setValue('1')

    # trigger
    self.obj106.trigger.setValue('<KeyPress-m>')

    # action
    self.obj106.action.setValue('atom3i.popupMenuCreator.ModelPopup( eventhandler.get_event_params()  )\n')
    self.obj106.action.setHeight(15)

    # broadcast_to
    self.obj106.broadcast_to.setValue('')
    self.obj106.broadcast_to.setNone()

    # display
    self.obj106.display.setValue('Model Menu')

    self.obj106.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-19.0, -68.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=Hyperedge(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    # name
    self.obj107.name.setValue('')
    self.obj107.name.setNone()

    # broadcast
    self.obj107.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj107.broadcast.setHeight(15)

    # guard
    self.obj107.guard.setValue('1')

    # trigger
    self.obj107.trigger.setValue('<KeyPress-t>')

    # action
    self.obj107.action.setValue('atom3i.popupMenuCreator.TransformationPopup( eventhandler.get_event_params()  )\n')
    self.obj107.action.setHeight(15)

    # broadcast_to
    self.obj107.broadcast_to.setValue('')
    self.obj107.broadcast_to.setNone()

    # display
    self.obj107.display.setValue('Trans. Menu')

    self.obj107.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, -98.0]
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=Hyperedge(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # name
    self.obj108.name.setValue('')
    self.obj108.name.setNone()

    # broadcast
    self.obj108.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj108.broadcast.setHeight(15)

    # guard
    self.obj108.guard.setValue('1')

    # trigger
    self.obj108.trigger.setValue('<KeyPress-m>')

    # action
    self.obj108.action.setValue('atom3i.popupMenuCreator.ModelPopup( eventhandler.get_event_params() )\n')
    self.obj108.action.setHeight(15)

    # broadcast_to
    self.obj108.broadcast_to.setValue('')
    self.obj108.broadcast_to.setNone()

    # display
    self.obj108.display.setValue('Model Menu')

    self.obj108.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-18.0, -83.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=Hyperedge(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # name
    self.obj109.name.setValue('')
    self.obj109.name.setNone()

    # broadcast
    self.obj109.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj109.broadcast.setHeight(15)

    # guard
    self.obj109.guard.setValue('1')

    # trigger
    self.obj109.trigger.setValue('<KeyPress-f>')

    # action
    self.obj109.action.setValue('atom3i.popupMenuCreator.FilePopup( eventhandler.get_event_params() )\n')
    self.obj109.action.setHeight(15)

    # broadcast_to
    self.obj109.broadcast_to.setValue('')
    self.obj109.broadcast_to.setNone()

    # display
    self.obj109.display.setValue('File Menu')

    self.obj109.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-26.0, -52.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=Hyperedge(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # name
    self.obj110.name.setValue('')
    self.obj110.name.setNone()

    # broadcast
    self.obj110.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj110.broadcast.setHeight(15)

    # guard
    self.obj110.guard.setValue('1')

    # trigger
    self.obj110.trigger.setValue('<KeyPress-l>')

    # action
    self.obj110.action.setValue('atom3i.popupMenuCreator.LayoutPopup( eventhandler.get_event_params() )\n')
    self.obj110.action.setHeight(15)

    # broadcast_to
    self.obj110.broadcast_to.setValue('')
    self.obj110.broadcast_to.setNone()

    # display
    self.obj110.display.setValue('Layout Menu')

    self.obj110.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,180.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, -113.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=Hyperedge(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # name
    self.obj111.name.setValue('')
    self.obj111.name.setNone()

    # broadcast
    self.obj111.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj111.broadcast.setHeight(15)

    # guard
    self.obj111.guard.setValue('atom3i.exitFromATOM3()')

    # trigger
    self.obj111.trigger.setValue('<Alt-x>')

    # action
    self.obj111.action.setValue('\n')
    self.obj111.action.setHeight(15)

    # broadcast_to
    self.obj111.broadcast_to.setValue('')
    self.obj111.broadcast_to.setNone()

    # display
    self.obj111.display.setValue('Exit')

    self.obj111.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(20.0,578.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [14.0, -60.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=Hyperedge(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # name
    self.obj112.name.setValue('')
    self.obj112.name.setNone()

    # broadcast
    self.obj112.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj112.broadcast.setHeight(15)

    # guard
    self.obj112.guard.setValue('1')

    # trigger
    self.obj112.trigger.setValue('<Double-ButtonPress-1>')

    # action
    self.obj112.action.setValue('startArrowEditorMode( atom3i, eventhandler.get_event_params()  ) \n\nsetCursor( atom3i.parent, \'Arrow Editor Idle\' )\n\n# OBFUSCATION WARNING:\n# If start arrow editor mode fails, it is assumed that the \n# user is clicking a non-link and wants to do Edit \n# Properties on it. \n# On entering ArrowEditor mode, \'Reset\' then \n# \'Edit Properties\' events will be generated. \n')
    self.obj112.action.setHeight(15)

    # broadcast_to
    self.obj112.broadcast_to.setValue('')
    self.obj112.broadcast_to.setNone()

    # display
    self.obj112.display.setValue('Edit Arrow')

    self.obj112.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(540.0,660.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [43.0, -8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=Hyperedge(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # name
    self.obj113.name.setValue('')
    self.obj113.name.setNone()

    # broadcast
    self.obj113.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj113.broadcast.setHeight(15)

    # guard
    self.obj113.guard.setValue('1')

    # trigger
    self.obj113.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj113.action.setValue('atom3i.arrowEditor.clearActiveControlPoint()\nsetCursor( atom3i.parent, \'Arrow Editor Idle\' )\n')
    self.obj113.action.setHeight(15)

    # broadcast_to
    self.obj113.broadcast_to.setValue('')
    self.obj113.broadcast_to.setNone()

    # display
    self.obj113.display.setValue('Done')

    self.obj113.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(585.20036934,770.027515936,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-46.0, 15.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=Hyperedge(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # name
    self.obj114.name.setValue('')
    self.obj114.name.setNone()

    # broadcast
    self.obj114.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj114.broadcast.setHeight(15)

    # guard
    self.obj114.guard.setValue('1')

    # trigger
    self.obj114.trigger.setValue('<KeyPress-Delete>')

    # action
    self.obj114.action.setValue('pos = cb.getCanvasCoords( eventhandler.get_event_params()   )\natom3i.arrowEditor.deleteControlPoint(  pos )\nsetCursor( atom3i.parent, \'Arrow Editor Idle\' )\n')
    self.obj114.action.setHeight(15)

    # broadcast_to
    self.obj114.broadcast_to.setValue('')
    self.obj114.broadcast_to.setNone()

    # display
    self.obj114.display.setValue('Delete')

    self.obj114.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(585.20036934,770.027515936,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-43.0, -1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=Hyperedge(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # name
    self.obj115.name.setValue('')
    self.obj115.name.setNone()

    # broadcast
    self.obj115.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj115.broadcast.setHeight(15)

    # guard
    self.obj115.guard.setValue('1')

    # trigger
    self.obj115.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj115.action.setValue('atom3i.popupMenuCreator.ArrowEditorPopup( eventhandler.get_event_params() )\n')
    self.obj115.action.setHeight(15)

    # broadcast_to
    self.obj115.broadcast_to.setValue('')
    self.obj115.broadcast_to.setNone()

    # display
    self.obj115.display.setValue('Popup Menu')

    self.obj115.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(500.0,800.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-35.0, 8.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=Hyperedge(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # name
    self.obj116.name.setValue('')
    self.obj116.name.setNone()

    # broadcast
    self.obj116.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj116.broadcast.setHeight(15)

    # guard
    self.obj116.guard.setValue('1')

    # trigger
    self.obj116.trigger.setValue('<KeyPress-s>')

    # action
    self.obj116.action.setValue('atom3i.arrowEditor.smoothArrow()\n')
    self.obj116.action.setHeight(15)

    # broadcast_to
    self.obj116.broadcast_to.setValue('')
    self.obj116.broadcast_to.setNone()

    # display
    self.obj116.display.setValue('Smooth')

    self.obj116.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(500.0,800.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-48.0, 47.0]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=Hyperedge(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # name
    self.obj117.name.setValue('')
    self.obj117.name.setNone()

    # broadcast
    self.obj117.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj117.broadcast.setHeight(15)

    # guard
    self.obj117.guard.setValue('1')

    # trigger
    self.obj117.trigger.setValue('Edit Properties')

    # action
    self.obj117.action.setValue('itemHandler = atom3i.arrowEditor.getArrowHandler()\n#atom3i.editclass( 0,0,itemHandler )\nevent =  eventhandler.get_event_params() \natom3i.editclass( event.x_root, event.y_root, itemHandler )\n')
    self.obj117.action.setHeight(15)

    # broadcast_to
    self.obj117.broadcast_to.setValue('')
    self.obj117.broadcast_to.setNone()

    # display
    self.obj117.display.setValue('Edit Properties')

    self.obj117.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(500.0,800.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-28.0, 21.0]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=Hyperedge(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # name
    self.obj118.name.setValue('')
    self.obj118.name.setNone()

    # broadcast
    self.obj118.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj118.broadcast.setHeight(15)

    # guard
    self.obj118.guard.setValue('1')

    # trigger
    self.obj118.trigger.setValue('<Any-Motion>')

    # action
    self.obj118.action.setValue('atom3i.arrowEditor.setInMotion(  eventhandler.get_event_params()   )\n')
    self.obj118.action.setHeight(15)

    # broadcast_to
    self.obj118.broadcast_to.setValue('')
    self.obj118.broadcast_to.setNone()

    # display
    self.obj118.display.setValue('Motion')

    self.obj118.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-51.0, 0.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=Hyperedge(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # name
    self.obj119.name.setValue('')
    self.obj119.name.setNone()

    # broadcast
    self.obj119.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj119.broadcast.setHeight(15)

    # guard
    self.obj119.guard.setValue('1')

    # trigger
    self.obj119.trigger.setValue('<KeyPress-Left>')

    # action
    self.obj119.action.setValue('atom3i.arrowEditor.dragOps(0,0,-1,0,mouseMove=False )\n')
    self.obj119.action.setHeight(15)

    # broadcast_to
    self.obj119.broadcast_to.setValue('')
    self.obj119.broadcast_to.setNone()

    # display
    self.obj119.display.setValue('Move Left')

    self.obj119.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-45.0, 66.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=Hyperedge(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # name
    self.obj120.name.setValue('')
    self.obj120.name.setNone()

    # broadcast
    self.obj120.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj120.broadcast.setHeight(15)

    # guard
    self.obj120.guard.setValue('1')

    # trigger
    self.obj120.trigger.setValue('<KeyPress-Right>')

    # action
    self.obj120.action.setValue('atom3i.arrowEditor.dragOps(0,0,1,0,mouseMove=False )\n')
    self.obj120.action.setHeight(15)

    # broadcast_to
    self.obj120.broadcast_to.setValue('')
    self.obj120.broadcast_to.setNone()

    # display
    self.obj120.display.setValue('Move Right')

    self.obj120.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-39.0, 53.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=Hyperedge(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # name
    self.obj121.name.setValue('')
    self.obj121.name.setNone()

    # broadcast
    self.obj121.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj121.broadcast.setHeight(15)

    # guard
    self.obj121.guard.setValue('1')

    # trigger
    self.obj121.trigger.setValue('<KeyPress-Up>')

    # action
    self.obj121.action.setValue('atom3i.arrowEditor.dragOps(0,0,0,1,mouseMove=False )\n')
    self.obj121.action.setHeight(15)

    # broadcast_to
    self.obj121.broadcast_to.setValue('')
    self.obj121.broadcast_to.setNone()

    # display
    self.obj121.display.setValue('Move Up')

    self.obj121.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-46.0, 41.0]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=Hyperedge(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # name
    self.obj122.name.setValue('')
    self.obj122.name.setNone()

    # broadcast
    self.obj122.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj122.broadcast.setHeight(15)

    # guard
    self.obj122.guard.setValue('1')

    # trigger
    self.obj122.trigger.setValue('<KeyPress-Down>')

    # action
    self.obj122.action.setValue('atom3i.arrowEditor.dragOps(0,0,0,-1,mouseMove=False )\n')
    self.obj122.action.setHeight(15)

    # broadcast_to
    self.obj122.broadcast_to.setValue('')
    self.obj122.broadcast_to.setNone()

    # display
    self.obj122.display.setValue('Move Down')

    self.obj122.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-38.0, 28.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=Hyperedge(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # name
    self.obj123.name.setValue('')
    self.obj123.name.setNone()

    # broadcast
    self.obj123.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj123.broadcast.setHeight(15)

    # guard
    self.obj123.guard.setValue('not editPoint(atom3i, eventhandler.get_event_params()) ')

    # trigger
    self.obj123.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj123.action.setValue('atom3i.arrowEditor.removeOldEditorArrow()\nsetDefaultCursor( atom3i.parent )\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj123.action.setHeight(15)

    # broadcast_to
    self.obj123.broadcast_to.setValue('')
    self.obj123.broadcast_to.setNone()

    # display
    self.obj123.display.setValue('Edit Arrow')

    self.obj123.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(499.0,707.5,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [4.0, -11.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=Hyperedge(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # name
    self.obj124.name.setValue('')
    self.obj124.name.setNone()

    # broadcast
    self.obj124.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj124.broadcast.setHeight(15)

    # guard
    self.obj124.guard.setValue('1')

    # trigger
    self.obj124.trigger.setValue('<KeyPress-space>')

    # action
    self.obj124.action.setValue('atom3i.arrowEditor.toggleMoveLabelDrawingMode()\neditPoint( atom3i, eventhandler.get_event_params() )\n')
    self.obj124.action.setHeight(15)

    # broadcast_to
    self.obj124.broadcast_to.setValue('')
    self.obj124.broadcast_to.setNone()

    # display
    self.obj124.display.setValue('Move Label Toggle')

    self.obj124.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(500.0,800.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-18.0, 34.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=Hyperedge(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # name
    self.obj125.name.setValue('')
    self.obj125.name.setNone()

    # broadcast
    self.obj125.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj125.broadcast.setHeight(15)

    # guard
    self.obj125.guard.setValue('1')

    # trigger
    self.obj125.trigger.setValue('<KeyPress-Insert>')

    # action
    self.obj125.action.setValue('pos = cb.getCanvasCoords( eventhandler.get_event_params()   )\natom3i.arrowEditor.insertControlPoint( pos )\nmodelChange( atom3i )\n\nsetCursor( atom3i.parent, \'Arrow Editor Active\' )\n')
    self.obj125.action.setHeight(15)

    # broadcast_to
    self.obj125.broadcast_to.setValue('')
    self.obj125.broadcast_to.setNone()

    # display
    self.obj125.display.setValue('Insert Point')

    self.obj125.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(575.474476916,712.530366835,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-29.0, 7.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=Hyperedge(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # name
    self.obj126.name.setValue('')
    self.obj126.name.setNone()

    # broadcast
    self.obj126.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj126.broadcast.setHeight(15)

    # guard
    self.obj126.guard.setValue('editPoint(atom3i, eventhandler.get_event_params()) ')

    # trigger
    self.obj126.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj126.action.setValue('setCursor(atom3i.parent, \'Arrow Editor Active\')\n')
    self.obj126.action.setHeight(15)

    # broadcast_to
    self.obj126.broadcast_to.setValue('')
    self.obj126.broadcast_to.setNone()

    # display
    self.obj126.display.setValue('Select Point')

    self.obj126.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(575.474476916,712.530366835,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-28.0, 21.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=Hyperedge(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # name
    self.obj127.name.setValue('')
    self.obj127.name.setNone()

    # broadcast
    self.obj127.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj127.broadcast.setHeight(15)

    # guard
    self.obj127.guard.setValue('1')

    # trigger
    self.obj127.trigger.setValue('<KeyPress-space>')

    # action
    self.obj127.action.setValue('atom3i.arrowEditor.toggleMoveLabelDrawingMode()\neditPoint( atom3i, eventhandler.get_event_params() )\n')
    self.obj127.action.setHeight(15)

    # broadcast_to
    self.obj127.broadcast_to.setValue('')
    self.obj127.broadcast_to.setNone()

    # display
    self.obj127.display.setValue('Move Label Toggle')

    self.obj127.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,820.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-17.0, 14.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=Hyperedge(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # name
    self.obj128.name.setValue('')
    self.obj128.name.setNone()

    # broadcast
    self.obj128.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj128.broadcast.setHeight(15)

    # guard
    self.obj128.guard.setValue('1')

    # trigger
    self.obj128.trigger.setValue('<Control-KeyPress-v>')

    # action
    self.obj128.action.setValue('pasteLoader( atom3i, eventhandler.get_event_params()  )\nsetCursor( atom3i.parent, \'Drag\' )\n\nwasDragged = False\n')
    self.obj128.action.setHeight(15)

    # broadcast_to
    self.obj128.broadcast_to.setValue('')
    self.obj128.broadcast_to.setNone()

    # display
    self.obj128.display.setValue('Paste')

    self.obj128.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(390.0,260.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=Hyperedge(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # name
    self.obj129.name.setValue('')
    self.obj129.name.setNone()

    # broadcast
    self.obj129.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj129.broadcast.setHeight(15)

    # guard
    self.obj129.guard.setValue('1')

    # trigger
    self.obj129.trigger.setValue('<Any-Motion>')

    # action
    self.obj129.action.setValue('realtimeArrowMotion( atom3i, eventhandler.get_event_params() )\n')
    self.obj129.action.setHeight(15)

    # broadcast_to
    self.obj129.broadcast_to.setValue('')
    self.obj129.broadcast_to.setNone()

    # display
    self.obj129.display.setValue('Motion')

    self.obj129.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(340.0,729.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-4.0, -26.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=Hyperedge(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # name
    self.obj130.name.setValue('')
    self.obj130.name.setNone()

    # broadcast
    self.obj130.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj130.broadcast.setHeight(15)

    # guard
    self.obj130.guard.setValue('1')

    # trigger
    self.obj130.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj130.action.setValue('arrowRollback( atom3i, eventhandler.get_event_params() ) \n')
    self.obj130.action.setHeight(15)

    # broadcast_to
    self.obj130.broadcast_to.setValue('')
    self.obj130.broadcast_to.setNone()

    # display
    self.obj130.display.setValue('Rollback')

    self.obj130.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(340.0,729.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [2.0, -13.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=Hyperedge(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # name
    self.obj131.name.setValue('')
    self.obj131.name.setNone()

    # broadcast
    self.obj131.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj131.broadcast.setHeight(15)

    # guard
    self.obj131.guard.setValue('1')

    # trigger
    self.obj131.trigger.setValue('<Any-Motion>')

    # action
    self.obj131.action.setValue('realtimeArrowMotion( atom3i, eventhandler.get_event_params(), snap=False )\n')
    self.obj131.action.setHeight(15)

    # broadcast_to
    self.obj131.broadcast_to.setValue('')
    self.obj131.broadcast_to.setNone()

    # display
    self.obj131.display.setValue('Motion')

    self.obj131.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(340.0,869.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-8.0, -3.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=Hyperedge(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # name
    self.obj132.name.setValue('')
    self.obj132.name.setNone()

    # broadcast
    self.obj132.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj132.broadcast.setHeight(15)

    # guard
    self.obj132.guard.setValue('1')

    # trigger
    self.obj132.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj132.action.setValue('arrowRollback( atom3i, eventhandler.get_event_params() ) \n')
    self.obj132.action.setHeight(15)

    # broadcast_to
    self.obj132.broadcast_to.setValue('')
    self.obj132.broadcast_to.setNone()

    # display
    self.obj132.display.setValue('Rollback')

    self.obj132.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(340.0,869.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-8.0, 9.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=Hyperedge(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # name
    self.obj133.name.setValue('')
    self.obj133.name.setNone()

    # broadcast
    self.obj133.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj133.broadcast.setHeight(15)

    # guard
    self.obj133.guard.setValue('1')

    # trigger
    self.obj133.trigger.setValue('<KeyPress-space>')

    # action
    self.obj133.action.setValue('setCursor( atom3i.parent, \'New Arrow No Snap\' )\nrealtimeArrowMotion( atom3i, eventhandler.get_event_params(), snap=False )\n')
    self.obj133.action.setHeight(15)

    # broadcast_to
    self.obj133.broadcast_to.setValue('')
    self.obj133.broadcast_to.setNone()

    # display
    self.obj133.display.setValue('Toggle Snap')

    self.obj133.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(294.0,809.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, -29.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=Hyperedge(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # name
    self.obj134.name.setValue('')
    self.obj134.name.setNone()

    # broadcast
    self.obj134.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj134.broadcast.setHeight(15)

    # guard
    self.obj134.guard.setValue('1')

    # trigger
    self.obj134.trigger.setValue('<KeyPress-space>')

    # action
    self.obj134.action.setValue('setCursor( atom3i.parent, \'New Arrow\' )\nrealtimeArrowMotion( atom3i, eventhandler.get_event_params() )\n')
    self.obj134.action.setHeight(15)

    # broadcast_to
    self.obj134.broadcast_to.setValue('')
    self.obj134.broadcast_to.setNone()

    # display
    self.obj134.display.setValue('Toggle Snap')

    self.obj134.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(274.0,809.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, -14.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=Hyperedge(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # name
    self.obj135.name.setValue('')
    self.obj135.name.setNone()

    # broadcast
    self.obj135.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj135.broadcast.setHeight(15)

    # guard
    self.obj135.guard.setValue('1')

    # trigger
    self.obj135.trigger.setValue('<KeyPress-F8>')

    # action
    self.obj135.action.setValue('atom3i.popupMenuCreator.SourcePathPopup( eventhandler.get_event_params()  )\n')
    self.obj135.action.setHeight(15)

    # broadcast_to
    self.obj135.broadcast_to.setValue('')
    self.obj135.broadcast_to.setNone()

    # display
    self.obj135.display.setValue('Source Paths')

    self.obj135.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-13.0, 177.0]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=Hyperedge(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # name
    self.obj136.name.setValue('')
    self.obj136.name.setNone()

    # broadcast
    self.obj136.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj136.broadcast.setHeight(15)

    # guard
    self.obj136.guard.setValue('1')

    # trigger
    self.obj136.trigger.setValue('<Control-KeyPress-c>')

    # action
    self.obj136.action.setValue('copySave( atom3i )\n')
    self.obj136.action.setHeight(15)

    # broadcast_to
    self.obj136.broadcast_to.setValue('')
    self.obj136.broadcast_to.setNone()

    # display
    self.obj136.display.setValue('Copy')

    self.obj136.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-32.0, 392.0]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=Hyperedge(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # name
    self.obj137.name.setValue('')
    self.obj137.name.setNone()

    # broadcast
    self.obj137.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj137.broadcast.setHeight(15)

    # guard
    self.obj137.guard.setValue('1')

    # trigger
    self.obj137.trigger.setValue('<Control-KeyPress-d>')

    # action
    self.obj137.action.setValue('cb.highlighter(0)\ncb.clearSelectionDict()\n')
    self.obj137.action.setHeight(15)

    # broadcast_to
    self.obj137.broadcast_to.setValue('')
    self.obj137.broadcast_to.setNone()

    # display
    self.obj137.display.setValue('Deselect All')

    self.obj137.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-15.0, 375.0]
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=Hyperedge(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # name
    self.obj138.name.setValue('')
    self.obj138.name.setNone()

    # broadcast
    self.obj138.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj138.broadcast.setHeight(15)

    # guard
    self.obj138.guard.setValue('1')

    # trigger
    self.obj138.trigger.setValue('<Control-KeyPress-x>')

    # action
    self.obj138.action.setValue('cutSave( atom3i )\n')
    self.obj138.action.setHeight(15)

    # broadcast_to
    self.obj138.broadcast_to.setValue('')
    self.obj138.broadcast_to.setNone()

    # display
    self.obj138.display.setValue('Cut')

    self.obj138.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-39.0, 410.0]
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=Hyperedge(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # name
    self.obj139.name.setValue('')
    self.obj139.name.setNone()

    # broadcast
    self.obj139.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj139.broadcast.setHeight(15)

    # guard
    self.obj139.guard.setValue('1')

    # trigger
    self.obj139.trigger.setValue('<Alt-KeyPress-c>')

    # action
    self.obj139.action.setValue('copyObjectAttributes( atom3i, eventhandler.get_event_params() )\n')
    self.obj139.action.setHeight(15)

    # broadcast_to
    self.obj139.broadcast_to.setValue('')
    self.obj139.broadcast_to.setNone()

    # display
    self.obj139.display.setValue('Copy Attributes')

    self.obj139.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-6.0, 426.0]
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=Hyperedge(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # name
    self.obj140.name.setValue('')
    self.obj140.name.setNone()

    # broadcast
    self.obj140.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj140.broadcast.setHeight(15)

    # guard
    self.obj140.guard.setValue('1')

    # trigger
    self.obj140.trigger.setValue('<Alt-KeyPress-v>')

    # action
    self.obj140.action.setValue('pasteObjectAttributes( atom3i, eventhandler.get_event_params() )\n')
    self.obj140.action.setHeight(15)

    # broadcast_to
    self.obj140.broadcast_to.setValue('')
    self.obj140.broadcast_to.setNone()

    # display
    self.obj140.display.setValue('Paste Attributes')

    self.obj140.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-4.0, 444.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=Hyperedge(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    # name
    self.obj141.name.setValue('')
    self.obj141.name.setNone()

    # broadcast
    self.obj141.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj141.broadcast.setHeight(15)

    # guard
    self.obj141.guard.setValue('1')

    # trigger
    self.obj141.trigger.setValue('<Control-ButtonPress-1>')

    # action
    self.obj141.action.setValue('startArrowDrawing( atom3i, eventhandler.get_event_params() )  \nsetCursor( atom3i.parent, \'New Arrow\' )\n')
    self.obj141.action.setHeight(15)

    # broadcast_to
    self.obj141.broadcast_to.setValue('')
    self.obj141.broadcast_to.setNone()

    # display
    self.obj141.display.setValue('Create New Arrow')

    self.obj141.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(340.0,558.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-91.0, 63.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=Hyperedge(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    # name
    self.obj142.name.setValue('')
    self.obj142.name.setNone()

    # broadcast
    self.obj142.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj142.broadcast.setHeight(15)

    # guard
    self.obj142.guard.setValue('1')

    # trigger
    self.obj142.trigger.setValue('<Control-KeyPress-z>')

    # action
    self.obj142.action.setValue('atom3i.undoer.undo()\n')
    self.obj142.action.setHeight(15)

    # broadcast_to
    self.obj142.broadcast_to.setValue('')
    self.obj142.broadcast_to.setNone()

    # display
    self.obj142.display.setValue('Undo')

    self.obj142.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-31.0, 475.0]
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=Hyperedge(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    # name
    self.obj143.name.setValue('')
    self.obj143.name.setNone()

    # broadcast
    self.obj143.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj143.broadcast.setHeight(15)

    # guard
    self.obj143.guard.setValue('1')

    # trigger
    self.obj143.trigger.setValue('<Control-KeyPress-y>')

    # action
    self.obj143.action.setValue('atom3i.undoer.redo()\n')
    self.obj143.action.setHeight(15)

    # broadcast_to
    self.obj143.broadcast_to.setValue('')
    self.obj143.broadcast_to.setNone()

    # display
    self.obj143.display.setValue('Redo')

    self.obj143.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-31.0, 491.0]
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=Hyperedge(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    # name
    self.obj144.name.setValue('')
    self.obj144.name.setNone()

    # broadcast
    self.obj144.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj144.broadcast.setHeight(15)

    # guard
    self.obj144.guard.setValue('1')

    # trigger
    self.obj144.trigger.setValue('<KeyPress-F5>')

    # action
    self.obj144.action.setValue('atom3i.postscriptBox.createMask( eventhandler.get_event_params()   )\nsetCursor( atom3i.parent, \'Postscript\' )\n')
    self.obj144.action.setHeight(15)

    # broadcast_to
    self.obj144.broadcast_to.setValue('')
    self.obj144.broadcast_to.setNone()

    # display
    self.obj144.display.setValue('Postscript')

    self.obj144.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(440.0,460.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-34.0, 2.0]
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    self.obj145=Hyperedge(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    # name
    self.obj145.name.setValue('')
    self.obj145.name.setNone()

    # broadcast
    self.obj145.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj145.broadcast.setHeight(15)

    # guard
    self.obj145.guard.setValue('1')

    # trigger
    self.obj145.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj145.action.setValue('atom3i.postscriptBox.generatePostscript()\natom3i.disableSnapGridForPrinting(False)\nsetDefaultCursor( atom3i.parent )\n')
    self.obj145.action.setHeight(15)

    # broadcast_to
    self.obj145.broadcast_to.setValue('')
    self.obj145.broadcast_to.setNone()

    # display
    self.obj145.display.setValue('Done')

    self.obj145.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(400.0,480.0,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-11.0, 3.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj146=Hyperedge(self)
    self.obj146.isGraphObjectVisual = True

    if(hasattr(self.obj146, '_setHierarchicalLink')):
      self.obj146._setHierarchicalLink(False)

    # name
    self.obj146.name.setValue('')
    self.obj146.name.setNone()

    # broadcast
    self.obj146.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj146.broadcast.setHeight(15)

    # guard
    self.obj146.guard.setValue('atom3i.postscriptBox.setActiveSide( cb.getCanvasCoords( eventhandler.get_event_params() )  )')

    # trigger
    self.obj146.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj146.action.setValue('setCursor( atom3i.parent, \'Sizing\' )\n')
    self.obj146.action.setHeight(15)

    # broadcast_to
    self.obj146.broadcast_to.setValue('')
    self.obj146.broadcast_to.setNone()

    # display
    self.obj146.display.setValue('Select Point')

    self.obj146.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(611.0,506.0,self.obj146)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj146.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj146)
    self.globalAndLocalPostcondition(self.obj146, rootNode)
    self.obj146.postAction( rootNode.CREATE )

    self.obj147=Hyperedge(self)
    self.obj147.isGraphObjectVisual = True

    if(hasattr(self.obj147, '_setHierarchicalLink')):
      self.obj147._setHierarchicalLink(False)

    # name
    self.obj147.name.setValue('')
    self.obj147.name.setNone()

    # broadcast
    self.obj147.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj147.broadcast.setHeight(15)

    # guard
    self.obj147.guard.setValue('1')

    # trigger
    self.obj147.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj147.action.setValue('setCursor( atom3i.parent, \'Postscript\' )\n')
    self.obj147.action.setHeight(15)

    # broadcast_to
    self.obj147.broadcast_to.setValue('')
    self.obj147.broadcast_to.setNone()

    # display
    self.obj147.display.setValue('Done')

    self.obj147.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(591.0,506.0,self.obj147)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-46.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj147.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj147)
    self.globalAndLocalPostcondition(self.obj147, rootNode)
    self.obj147.postAction( rootNode.CREATE )

    self.obj148=Hyperedge(self)
    self.obj148.isGraphObjectVisual = True

    if(hasattr(self.obj148, '_setHierarchicalLink')):
      self.obj148._setHierarchicalLink(False)

    # name
    self.obj148.name.setValue('')
    self.obj148.name.setNone()

    # broadcast
    self.obj148.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj148.broadcast.setHeight(15)

    # guard
    self.obj148.guard.setValue('1')

    # trigger
    self.obj148.trigger.setValue('<Any-Motion>')

    # action
    self.obj148.action.setValue('atom3i.postscriptBox.inMotion( cb.getCanvasCoords( eventhandler.get_event_params() ) )\n')
    self.obj148.action.setHeight(15)

    # broadcast_to
    self.obj148.broadcast_to.setValue('')
    self.obj148.broadcast_to.setNone()

    # display
    self.obj148.display.setValue('Motion')

    self.obj148.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(641.25,546.0,self.obj148)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-5.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj148.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj148)
    self.globalAndLocalPostcondition(self.obj148, rootNode)
    self.obj148.postAction( rootNode.CREATE )

    self.obj149=Hyperedge(self)
    self.obj149.isGraphObjectVisual = True

    if(hasattr(self.obj149, '_setHierarchicalLink')):
      self.obj149._setHierarchicalLink(False)

    # name
    self.obj149.name.setValue('')
    self.obj149.name.setNone()

    # broadcast
    self.obj149.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj149.broadcast.setHeight(15)

    # guard
    self.obj149.guard.setValue('cb.isItemUnderCursorSelected( atom3i, eventhandler.get_event_params()) and cb.isLabelDragMode()')

    # trigger
    self.obj149.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj149.action.setValue('# Create an object set from the selectionDict\ncb.buildSelectionObjectSet()     \ncb.getCanvasCoords( eventhandler.get_event_params() )\nsetCursor( atom3i.parent, \'Drag Label Motion\' )\n')
    self.obj149.action.setHeight(15)

    # broadcast_to
    self.obj149.broadcast_to.setValue('')
    self.obj149.broadcast_to.setNone()

    # display
    self.obj149.display.setValue('Start Drag')

    self.obj149.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(400.0,220.0,self.obj149)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj149.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj149)
    self.globalAndLocalPostcondition(self.obj149, rootNode)
    self.obj149.postAction( rootNode.CREATE )

    self.obj150=Hyperedge(self)
    self.obj150.isGraphObjectVisual = True

    if(hasattr(self.obj150, '_setHierarchicalLink')):
      self.obj150._setHierarchicalLink(False)

    # name
    self.obj150.name.setValue('')
    self.obj150.name.setNone()

    # broadcast
    self.obj150.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj150.broadcast.setHeight(15)

    # guard
    self.obj150.guard.setValue('1')

    # trigger
    self.obj150.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj150.action.setValue('setDefaultCursor( atom3i.parent )\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj150.action.setHeight(15)

    # broadcast_to
    self.obj150.broadcast_to.setValue('')
    self.obj150.broadcast_to.setNone()

    # display
    self.obj150.display.setValue('Finish Drag')

    self.obj150.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(406.0,240.0,self.obj150)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj150.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj150)
    self.globalAndLocalPostcondition(self.obj150, rootNode)
    self.obj150.postAction( rootNode.CREATE )

    self.obj151=Hyperedge(self)
    self.obj151.isGraphObjectVisual = True

    if(hasattr(self.obj151, '_setHierarchicalLink')):
      self.obj151._setHierarchicalLink(False)

    # name
    self.obj151.name.setValue('')
    self.obj151.name.setNone()

    # broadcast
    self.obj151.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj151.broadcast.setHeight(15)

    # guard
    self.obj151.guard.setValue('1')

    # trigger
    self.obj151.trigger.setValue('<Any-Motion>')

    # action
    self.obj151.action.setValue('dragLabelsInMotion(atom3i,eventhandler.get_event_params() )\n')
    self.obj151.action.setHeight(15)

    # broadcast_to
    self.obj151.broadcast_to.setValue('')
    self.obj151.broadcast_to.setNone()

    # display
    self.obj151.display.setValue('Motion')

    self.obj151.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,240.0,self.obj151)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-5.0, -8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj151.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj151)
    self.globalAndLocalPostcondition(self.obj151, rootNode)
    self.obj151.postAction( rootNode.CREATE )

    self.obj152=Hyperedge(self)
    self.obj152.isGraphObjectVisual = True

    if(hasattr(self.obj152, '_setHierarchicalLink')):
      self.obj152._setHierarchicalLink(False)

    # name
    self.obj152.name.setValue('')
    self.obj152.name.setNone()

    # broadcast
    self.obj152.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj152.broadcast.setHeight(15)

    # guard
    self.obj152.guard.setValue('1')

    # trigger
    self.obj152.trigger.setValue('<KeyPress-space>')

    # action
    self.obj152.action.setValue('cb.toggleLabelDragMode()\n')
    self.obj152.action.setHeight(15)

    # broadcast_to
    self.obj152.broadcast_to.setValue('')
    self.obj152.broadcast_to.setNone()

    # display
    self.obj152.display.setValue('Toggle Label Drag')

    self.obj152.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj152)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [1.0, 228.0]
    else: new_obj = None
    self.obj152.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj152)
    self.globalAndLocalPostcondition(self.obj152, rootNode)
    self.obj152.postAction( rootNode.CREATE )

    self.obj153=Hyperedge(self)
    self.obj153.isGraphObjectVisual = True

    if(hasattr(self.obj153, '_setHierarchicalLink')):
      self.obj153._setHierarchicalLink(False)

    # name
    self.obj153.name.setValue('')
    self.obj153.name.setNone()

    # broadcast
    self.obj153.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj153.broadcast.setHeight(15)

    # guard
    self.obj153.guard.setValue('1')

    # trigger
    self.obj153.trigger.setValue('<KeyPress-F10>')

    # action
    self.obj153.action.setValue('atom3i.toggleSnapGrid()\n')
    self.obj153.action.setHeight(15)

    # broadcast_to
    self.obj153.broadcast_to.setValue('')
    self.obj153.broadcast_to.setNone()

    # display
    self.obj153.display.setValue('Snap Grid Toggle')

    self.obj153.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj153)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-1.0, 247.0]
    else: new_obj = None
    self.obj153.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj153)
    self.globalAndLocalPostcondition(self.obj153, rootNode)
    self.obj153.postAction( rootNode.CREATE )

    self.obj154=Hyperedge(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # name
    self.obj154.name.setValue('')
    self.obj154.name.setNone()

    # broadcast
    self.obj154.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj154.broadcast.setHeight(15)

    # guard
    self.obj154.guard.setValue('1')

    # trigger
    self.obj154.trigger.setValue('<KeyPress-F12>')

    # action
    self.obj154.action.setValue('import ArrowOptimizer\nArrowOptimizer.applyLayout( atom3i = atom3i )\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj154.action.setHeight(15)

    # broadcast_to
    self.obj154.broadcast_to.setValue('')
    self.obj154.broadcast_to.setNone()

    # display
    self.obj154.display.setValue('Arrow Optimizer')

    self.obj154.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-6.0, 265.0]
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=Hyperedge(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # name
    self.obj155.name.setValue('')
    self.obj155.name.setNone()

    # broadcast
    self.obj155.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj155.broadcast.setHeight(15)

    # guard
    self.obj155.guard.setValue('1')

    # trigger
    self.obj155.trigger.setValue('<KeyPress-F11>')

    # action
    self.obj155.action.setValue('import SpringLayout\nselection = cb.buildSelectionObjectSet()\nSpringLayout.applyLayout( atom3i = atom3i, selection = selection )\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj155.action.setHeight(15)

    # broadcast_to
    self.obj155.broadcast_to.setValue('')
    self.obj155.broadcast_to.setNone()

    # display
    self.obj155.display.setValue('Spring Layout')

    self.obj155.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-11.0, 282.0]
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=Hyperedge(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # name
    self.obj156.name.setValue('')
    self.obj156.name.setNone()

    # broadcast
    self.obj156.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj156.broadcast.setHeight(15)

    # guard
    self.obj156.guard.setValue('1')

    # trigger
    self.obj156.trigger.setValue('<Control-KeyPress-f>')

    # action
    self.obj156.action.setValue('import ForceTransfer\nForceTransfer.applyLayout( atom3i=atom3i , selection=cb.buildSelectionObjectSet() )\nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj156.action.setHeight(15)

    # broadcast_to
    self.obj156.broadcast_to.setValue('')
    self.obj156.broadcast_to.setNone()

    # display
    self.obj156.display.setValue('Force Layout')

    self.obj156.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-12.0, 299.0]
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=Hyperedge(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # name
    self.obj157.name.setValue('')
    self.obj157.name.setNone()

    # broadcast
    self.obj157.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj157.broadcast.setHeight(15)

    # guard
    self.obj157.guard.setValue('1')

    # trigger
    self.obj157.trigger.setValue('<Any-Motion>')

    # action
    self.obj157.action.setValue('scaleWithMotion( atom3i, eventhandler.get_event_params(), textMode=True )\n')
    self.obj157.action.setHeight(15)

    # broadcast_to
    self.obj157.broadcast_to.setValue('')
    self.obj157.broadcast_to.setNone()

    # display
    self.obj157.display.setValue('Motion')

    self.obj157.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,420.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-5.0, -11.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=Hyperedge(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # name
    self.obj158.name.setValue('')
    self.obj158.name.setNone()

    # broadcast
    self.obj158.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj158.broadcast.setHeight(15)

    # guard
    self.obj158.guard.setValue('cb.isLabelDragMode()')

    # trigger
    self.obj158.trigger.setValue('<KeyPress-r>')

    # action
    self.obj158.action.setValue('cb.initReSizer()\nsetCursor( atom3i.parent, \'Sizing\' )\n')
    self.obj158.action.setHeight(15)

    # broadcast_to
    self.obj158.broadcast_to.setValue('')
    self.obj158.broadcast_to.setNone()

    # display
    self.obj158.display.setValue('Scale Selection')

    self.obj158.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(411.0,400.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [6.0, 1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=Hyperedge(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # name
    self.obj159.name.setValue('')
    self.obj159.name.setNone()

    # broadcast
    self.obj159.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj159.broadcast.setHeight(15)

    # guard
    self.obj159.guard.setValue('1')

    # trigger
    self.obj159.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj159.action.setValue('setDefaultCursor( atom3i.parent )\n')
    self.obj159.action.setHeight(15)

    # broadcast_to
    self.obj159.broadcast_to.setValue('')
    self.obj159.broadcast_to.setNone()

    # display
    self.obj159.display.setValue('Finish Scale')

    self.obj159.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(411.0,420.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-1.0, 3.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=Hyperedge(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # name
    self.obj160.name.setValue('')
    self.obj160.name.setNone()

    # broadcast
    self.obj160.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj160.broadcast.setHeight(15)

    # guard
    self.obj160.guard.setValue('1')

    # trigger
    self.obj160.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj160.action.setValue('scaleReset( atom3i, textMode=True )\n')
    self.obj160.action.setHeight(15)

    # broadcast_to
    self.obj160.broadcast_to.setValue('')
    self.obj160.broadcast_to.setNone()

    # display
    self.obj160.display.setValue('Reset Scale')

    self.obj160.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,420.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [11.0, 1.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=Hyperedge(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # name
    self.obj161.name.setValue('')
    self.obj161.name.setNone()

    # broadcast
    self.obj161.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj161.broadcast.setHeight(15)

    # guard
    self.obj161.guard.setValue('1')

    # trigger
    self.obj161.trigger.setValue('<ButtonPress-3>')

    # action
    self.obj161.action.setValue('scaleReset( atom3i )\n')
    self.obj161.action.setHeight(15)

    # broadcast_to
    self.obj161.broadcast_to.setValue('')
    self.obj161.broadcast_to.setNone()

    # display
    self.obj161.display.setValue('Reset Scale')

    self.obj161.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(640.0,378.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [9.0, 4.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=Hyperedge(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # name
    self.obj162.name.setValue('')
    self.obj162.name.setNone()

    # broadcast
    self.obj162.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj162.broadcast.setHeight(15)

    # guard
    self.obj162.guard.setValue('1')

    # trigger
    self.obj162.trigger.setValue('Reboot')

    # action
    self.obj162.action.setValue('atom3i.reboot_AToM3()\n')
    self.obj162.action.setHeight(15)

    # broadcast_to
    self.obj162.broadcast_to.setValue('')
    self.obj162.broadcast_to.setNone()

    # display
    self.obj162.display.setValue('Reboot')

    self.obj162.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-29.0, 194.0]
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=Hyperedge(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    # name
    self.obj163.name.setValue('')
    self.obj163.name.setNone()

    # broadcast
    self.obj163.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj163.broadcast.setHeight(15)

    # guard
    self.obj163.guard.setValue('1')

    # trigger
    self.obj163.trigger.setValue('<KeyPress-z>')

    # action
    self.obj163.action.setValue('ZoomFocus.applyLayout( atom3i )\nSnapGrid.applyLayout( atom3i )   #<-- Zoom could mess up the snapgrid...\noptimizeConnectionPorts( atom3i, doAllLinks=True ) \nmodelChange( atom3i ) # Model changed, update statusbar & undo\n')
    self.obj163.action.setHeight(15)

    # broadcast_to
    self.obj163.broadcast_to.setValue('')
    self.obj163.broadcast_to.setNone()

    # display
    self.obj163.display.setValue('Zoom Layout')

    self.obj163.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-12.0, 313.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=Hyperedge(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(False)

    # name
    self.obj164.name.setValue('')
    self.obj164.name.setNone()

    # broadcast
    self.obj164.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj164.broadcast.setHeight(15)

    # guard
    self.obj164.guard.setValue('cb.getOverlappedItemUnderCursor( atom3i, eventhandler.get_event_params() )')

    # trigger
    self.obj164.trigger.setValue('<KeyPress-d>')

    # action
    self.obj164.action.setValue('# Create an object set from the selectionDict\ncb.buildSelectionObjectSet()     \n # Start dragging!\ndragStart( atom3i )    \nsetCursor( atom3i.parent, \'Drag\' )\n\nwasDragged = False\n')
    self.obj164.action.setHeight(15)

    # broadcast_to
    self.obj164.broadcast_to.setValue('')
    self.obj164.broadcast_to.setNone()

    # display
    self.obj164.display.setValue('Drag Overlap')

    self.obj164.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(410.5,297.5,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=Hyperedge(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    # name
    self.obj165.name.setValue('')
    self.obj165.name.setNone()

    # broadcast
    self.obj165.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj165.broadcast.setHeight(15)

    # guard
    self.obj165.guard.setValue('cb.getOverlappedItemUnderCursor( atom3i, eventhandler.get_event_params(), \'Select Object to Edit\' )')

    # trigger
    self.obj165.trigger.setValue('<KeyPress-e>')

    # action
    self.obj165.action.setValue('# Edit the item we get from the guard condition\nlistOfLists = cb.getSelectionDict().values()\nitem, obj = listOfLists[0] # There should only be one value actually\n\n#x,y = cb.getLastClickCoord()\n#atom3i.editclass(x,y,item )\nevent =  eventhandler.get_event_params() \natom3i.editclass( event.x_root, event.y_root, item )\n')
    self.obj165.action.setHeight(15)

    # broadcast_to
    self.obj165.broadcast_to.setValue('')
    self.obj165.broadcast_to.setNone()

    # display
    self.obj165.display.setValue('Edit Overlap')

    self.obj165.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-14.0, 327.0]
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=Hyperedge(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    # name
    self.obj166.name.setValue('')
    self.obj166.name.setNone()

    # broadcast
    self.obj166.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj166.broadcast.setHeight(15)

    # guard
    self.obj166.guard.setValue('1')

    # trigger
    self.obj166.trigger.setValue('GG Select')

    # action
    self.obj166.action.setValue('\n')
    self.obj166.action.setHeight(15)

    # broadcast_to
    self.obj166.broadcast_to.setValue('')
    self.obj166.broadcast_to.setNone()

    # display
    self.obj166.display.setValue('GG Select')

    self.obj166.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(440.0,580.0,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [12.0, -16.0]
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=Hyperedge(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    # name
    self.obj167.name.setValue('')
    self.obj167.name.setNone()

    # broadcast
    self.obj167.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj167.broadcast.setHeight(15)

    # guard
    self.obj167.guard.setValue('1')

    # trigger
    self.obj167.trigger.setValue('<Any-ButtonRelease-1>')

    # action
    self.obj167.action.setValue('\n')
    self.obj167.action.setHeight(15)

    # broadcast_to
    self.obj167.broadcast_to.setValue('')
    self.obj167.broadcast_to.setNone()

    # display
    self.obj167.display.setValue('Finish Selection')

    self.obj167.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(480.0,600.0,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-10.0, -15.0]
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=Hyperedge(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    # name
    self.obj168.name.setValue('')
    self.obj168.name.setNone()

    # broadcast
    self.obj168.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj168.broadcast.setHeight(15)

    # guard
    self.obj168.guard.setValue('1')

    # trigger
    self.obj168.trigger.setValue('<Shift-KeyPress-Delete>')

    # action
    self.obj168.action.setValue('getSelectedItemsForDelete(atom3i, entityOnlyFlag=True)\n')
    self.obj168.action.setHeight(15)

    # broadcast_to
    self.obj168.broadcast_to.setValue('')
    self.obj168.broadcast_to.setNone()

    # display
    self.obj168.display.setValue('EntityDeleteRequest')

    self.obj168.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [6.0, 572.0]
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=Hyperedge(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    # name
    self.obj169.name.setValue('')
    self.obj169.name.setNone()

    # broadcast
    self.obj169.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj169.broadcast.setHeight(15)

    # guard
    self.obj169.guard.setValue('1')

    # trigger
    self.obj169.trigger.setValue('<KeyPress-Return>')

    # action
    self.obj169.action.setValue('atom3i.arrowEditor.clearActiveControlPoint()\nsetCursor( atom3i.parent, \'Arrow Editor Idle\' )\n')
    self.obj169.action.setHeight(15)

    # broadcast_to
    self.obj169.broadcast_to.setValue('')
    self.obj169.broadcast_to.setNone()

    # display
    self.obj169.display.setValue('Return')

    self.obj169.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(585.20036934,770.027515936,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-43.0, 28.0]
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=Hyperedge(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(False)

    # name
    self.obj170.name.setValue('')
    self.obj170.name.setNone()

    # broadcast
    self.obj170.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj170.broadcast.setHeight(15)

    # guard
    self.obj170.guard.setValue('1')

    # trigger
    self.obj170.trigger.setValue('<Shift-ButtonPress-3>')

    # action
    self.obj170.action.setValue('startArrowEditorMode( atom3i, eventhandler.get_event_params()  ) \n\nsetCursor( atom3i.parent, \'Arrow Editor Idle\' )\n')
    self.obj170.action.setHeight(15)

    # broadcast_to
    self.obj170.broadcast_to.setValue('')
    self.obj170.broadcast_to.setNone()

    # display
    self.obj170.display.setValue('Edit Arrow 2')

    self.obj170.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(540.0,660.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [49.0, 5.0]
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=Hyperedge(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    # name
    self.obj171.name.setValue('')
    self.obj171.name.setNone()

    # broadcast
    self.obj171.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj171.broadcast.setHeight(15)

    # guard
    self.obj171.guard.setValue('1')

    # trigger
    self.obj171.trigger.setValue('Postscript')

    # action
    self.obj171.action.setValue('atom3i.postscriptBox.createMask( eventhandler.get_event_params()   )\nsetCursor( atom3i.parent, \'Postscript\' )\n')
    self.obj171.action.setHeight(15)

    # broadcast_to
    self.obj171.broadcast_to.setValue('')
    self.obj171.broadcast_to.setNone()

    # display
    self.obj171.display.setValue('Postscript 2')

    self.obj171.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(440.0,460.0,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [35.0, 1.0]
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=Hyperedge(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(False)

    # name
    self.obj172.name.setValue('')
    self.obj172.name.setNone()

    # broadcast
    self.obj172.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj172.broadcast.setHeight(15)

    # guard
    self.obj172.guard.setValue('1')

    # trigger
    self.obj172.trigger.setValue('<serviceNodeDeleteRequest>')

    # action
    self.obj172.action.setValue('# This should only be triggered by CallbackHandlers.getSelectedItemsForDelete() which gives us a DeleteEvent, not a Tkinter event. This DeleteEvent has a destroy method to delete a single ASGNode instance.\nevent = eventhandler.get_event_params()\nevent.destroy() \n')
    self.obj172.action.setHeight(15)

    # broadcast_to
    self.obj172.broadcast_to.setValue('')
    self.obj172.broadcast_to.setNone()

    # display
    self.obj172.display.setValue('<serviceNodeDeleteRequest>')

    self.obj172.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [29.0, 590.0]
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=Hyperedge(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(False)

    # name
    self.obj173.name.setValue('')
    self.obj173.name.setNone()

    # broadcast
    self.obj173.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj173.broadcast.setHeight(15)

    # guard
    self.obj173.guard.setValue('1')

    # trigger
    self.obj173.trigger.setValue('<serviceLinkDeleteRequest>')

    # action
    self.obj173.action.setValue('# This should only be triggered by CallbackHandlers.getSelectedItemsForDelete() which gives us a DeleteEvent, not a Tkinter event. This DeleteEvent has a destroy method to delete a single ASGNode instance.\nevent = eventhandler.get_event_params()\nevent.destroy() \n')
    self.obj173.action.setHeight(15)

    # broadcast_to
    self.obj173.broadcast_to.setValue('')
    self.obj173.broadcast_to.setNone()

    # display
    self.obj173.display.setValue('<serviceLinkDeleteRequest>')

    self.obj173.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(140.0,320.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [27.0, 602.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=Hyperedge(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    # name
    self.obj174.name.setValue('')
    self.obj174.name.setNone()

    # broadcast
    self.obj174.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj174.broadcast.setHeight(15)

    # guard
    self.obj174.guard.setValue('1')

    # trigger
    self.obj174.trigger.setValue('<Arrow Created>')

    # action
    self.obj174.action.setValue('setDefaultCursor( atom3i.parent )\n')
    self.obj174.action.setHeight(15)

    # broadcast_to
    self.obj174.broadcast_to.setValue('')
    self.obj174.broadcast_to.setNone()

    # display
    self.obj174.display.setValue('<Arrow Created>')

    self.obj174.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(371.5,923.5,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [38.0, -6.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=Hyperedge(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    # name
    self.obj175.name.setValue('')
    self.obj175.name.setNone()

    # broadcast
    self.obj175.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj175.broadcast.setHeight(15)

    # guard
    self.obj175.guard.setValue('1')

    # trigger
    self.obj175.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj175.action.setValue('\n')
    self.obj175.action.setHeight(15)

    # broadcast_to
    self.obj175.broadcast_to.setValue('')
    self.obj175.broadcast_to.setNone()

    # display
    self.obj175.display.setValue('Drop Point')

    self.obj175.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(400.0,720.0,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-51.0, 8.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=Hyperedge(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    # name
    self.obj176.name.setValue('')
    self.obj176.name.setNone()

    # broadcast
    self.obj176.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj176.broadcast.setHeight(15)

    # guard
    self.obj176.guard.setValue('1')

    # trigger
    self.obj176.trigger.setValue('[Done]')

    # action
    self.obj176.action.setValue('\n')
    self.obj176.action.setHeight(15)

    # broadcast_to
    self.obj176.broadcast_to.setValue('')
    self.obj176.broadcast_to.setNone()

    # display
    self.obj176.display.setValue('[Done]')

    self.obj176.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(321.100273787,736.452738893,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-21.0, 7.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    self.obj177=Hyperedge(self)
    self.obj177.isGraphObjectVisual = True

    if(hasattr(self.obj177, '_setHierarchicalLink')):
      self.obj177._setHierarchicalLink(False)

    # name
    self.obj177.name.setValue('')
    self.obj177.name.setNone()

    # broadcast
    self.obj177.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj177.broadcast.setHeight(15)

    # guard
    self.obj177.guard.setValue('1')

    # trigger
    self.obj177.trigger.setValue('<ButtonPress-1>')

    # action
    self.obj177.action.setValue('\n')
    self.obj177.action.setHeight(15)

    # broadcast_to
    self.obj177.broadcast_to.setValue('')
    self.obj177.broadcast_to.setNone()

    # display
    self.obj177.display.setValue('Drop Point')

    self.obj177.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(360.0,900.0,self.obj177)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-10.0, -58.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj177.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj177)
    self.globalAndLocalPostcondition(self.obj177, rootNode)
    self.obj177.postAction( rootNode.CREATE )

    self.obj178=Hyperedge(self)
    self.obj178.isGraphObjectVisual = True

    if(hasattr(self.obj178, '_setHierarchicalLink')):
      self.obj178._setHierarchicalLink(False)

    # name
    self.obj178.name.setValue('')
    self.obj178.name.setNone()

    # broadcast
    self.obj178.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj178.broadcast.setHeight(15)

    # guard
    self.obj178.guard.setValue('1')

    # trigger
    self.obj178.trigger.setValue('[Done]')

    # action
    self.obj178.action.setValue('\n')
    self.obj178.action.setHeight(15)

    # broadcast_to
    self.obj178.broadcast_to.setValue('')
    self.obj178.broadcast_to.setNone()

    # display
    self.obj178.display.setValue('[Done]')

    self.obj178.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(320.975273787,856.390238893,self.obj178)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-26.0, -24.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj178.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj178)
    self.globalAndLocalPostcondition(self.obj178, rootNode)
    self.obj178.postAction( rootNode.CREATE )

    self.obj184=Hyperedge(self)
    self.obj184.isGraphObjectVisual = True

    if(hasattr(self.obj184, '_setHierarchicalLink')):
      self.obj184._setHierarchicalLink(False)

    # name
    self.obj184.name.setValue('')
    self.obj184.name.setNone()

    # broadcast
    self.obj184.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj184.broadcast.setHeight(15)

    # guard
    self.obj184.guard.setValue('1')

    # trigger
    self.obj184.trigger.setValue('Done')

    # action
    self.obj184.action.setValue('atom3i.postscriptBox.generatePostscript()\natom3i.disableSnapGridForPrinting(False)\nsetDefaultCursor( atom3i.parent )\n')
    self.obj184.action.setHeight(15)

    # broadcast_to
    self.obj184.broadcast_to.setValue('')
    self.obj184.broadcast_to.setNone()

    # display
    self.obj184.display.setValue('Done 2')

    self.obj184.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(400.0,480.0,self.obj184)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [33.0, 4.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj184.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj184)
    self.globalAndLocalPostcondition(self.obj184, rootNode)
    self.obj184.postAction( rootNode.CREATE )

    # Connections for obj28 (graphObject_: Obj0) named Active Event Loop
    self.drawConnections(
(self.obj28,self.obj50,[416.0, 31.0, 633.0, 8.125], 0, 2),
(self.obj28,self.obj51,[416.0, 31.0, 644.625, 33.75], 0, 2),
(self.obj28,self.obj52,[416.0, 31.0, 644.25, 67.75], 0, 2),
(self.obj28,self.obj53,[416.0, 31.0, 231.125, 182.875], 0, 2),
(self.obj28,self.obj54,[92.0, 486.0, 166.25, 350.375], 0, 2),
(self.obj28,self.obj81,[92.0, 486.0, 20.0, 520.0, 20.0, 480.0],"bezier", 3),
(self.obj28,self.obj55,[92.0, 486.0, 232.5, 336.5], 0, 2),
(self.obj28,self.obj111,[92.0, 486.0, 20.0, 537.99999999999989, 20.0, 578.0],"bezier", 3),
(self.obj28,self.obj56,[92.0, 486.0, 173.0, 402.875],"bezier", 2),
(self.obj28,self.obj59,[404.0, 942.0, 489.5, 670.375],"bezier", 2) )
    # Connections for obj29 (graphObject_: Obj1) named Arrow Editor
    self.drawConnections(
(self.obj29,self.obj57,[709.0, 799.0, 765.375, 862.5],"bezier", 2),
(self.obj29,self.obj58,[709.0, 799.0, 789.875, 899.5],"bezier", 2) )
    # Connections for obj30 (graphObject_: Obj2) named New Arrow
    self.drawConnections(
(self.obj30,self.obj60,[245.0, 802.0, 8.0, 716.0],"bezier", 2),
(self.obj30,self.obj61,[245.0, 802.0, 47.875, 1004.0],"bezier", 2),
(self.obj30,self.obj174,[330.0, 913.0, 371.5, 923.5],"bezier", 2),
(self.obj30,self.obj62,[413.0, 802.0, 387.63829047801295, 781.44347233175608],"bezier", 2),
(self.obj30,self.obj63,[413.0, 802.0, 390.46010445060551, 814.74739583333337],"bezier", 2) )
    # Connections for obj31 (graphObject_: Obj3) named Initial
    self.drawConnections(
(self.obj31,self.obj77,[20.886911429744945, 60.8125, 20.0, 189.0, 20.0, 260.0],"bezier", 3) )
    # Connections for obj32 (graphObject_: Obj4) named Main
    self.drawConnections(
(self.obj32,self.obj64,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 160.0, 424.0, 160.0],"bezier", 4),
(self.obj32,self.obj65,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj67,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 40.0, 420.0, 40.0],"bezier", 4),
(self.obj32,self.obj68,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 360.0, 100.0, 416.0, 100.0],"bezier", 4),
(self.obj32,self.obj71,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 120.0, 416.0, 120.0],"bezier", 4),
(self.obj32,self.obj73,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 360.0, 280.0, 402.0, 280.0],"bezier", 4),
(self.obj32,self.obj75,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 60.0, 420.0, 60.0],"bezier", 4),
(self.obj32,self.obj76,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 180.0, 424.0, 180.0],"bezier", 4),
(self.obj32,self.obj82,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 316.0, 359.0, 417.0, 357.0],"bezier", 4),
(self.obj32,self.obj85,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj86,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj87,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj88,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj89,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj90,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj91,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj92,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj93,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj94,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj95,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj96,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj97,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj98,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj99,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj100,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj101,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj102,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj103,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj104,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj105,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj106,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj107,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj108,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj109,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj110,[136.79896661812458, 244.01853312302836, 100.0, 180.0, 140.0, 180.0],"bezier", 3),
(self.obj32,self.obj112,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 381.0, 540.0, 500.0, 660.0, 540.0, 660.0],"bezier", 5),
(self.obj32,self.obj128,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 340.0, 260.0, 390.0, 260.0],"bezier", 4),
(self.obj32,self.obj135,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj136,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj137,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj138,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj139,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj140,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj141,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 340.0, 438.0, 340.0, 558.0],"bezier", 4),
(self.obj32,self.obj142,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj143,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj144,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 360.0, 460.0, 440.0, 460.0],"bezier", 4),
(self.obj32,self.obj149,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 220.0, 400.0, 220.0],"bezier", 4),
(self.obj32,self.obj152,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj153,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj154,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj155,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj156,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj158,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 400.0, 411.0, 400.0],"bezier", 4),
(self.obj32,self.obj162,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj163,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj164,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 330.0, 298.0, 410.5, 297.5],"bezier", 4),
(self.obj32,self.obj165,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj166,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 340.0, 520.0, 400.0, 580.0, 440.0, 580.0],"bezier", 5),
(self.obj32,self.obj168,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj170,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 380.0, 540.0, 500.0, 660.0, 540.0, 660.0],"bezier", 5),
(self.obj32,self.obj171,[148.97121093312418, 247.34522870662457, 240.0, 160.0, 360.0, 460.0, 440.0, 460.0],"bezier", 4),
(self.obj32,self.obj172,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3),
(self.obj32,self.obj173,[136.61703493148116, 259.73738170346996, 100.0, 320.0, 140.0, 320.0],"bezier", 3) )
    # Connections for obj33 (graphObject_: Obj5) named Remove From Selection
    self.drawConnections(
(self.obj33,self.obj66,[592.0625, 171.92862776025237, 560.0, 180.0, 520.0, 200.0, 417.0, 200.0],"bezier", 4),
(self.obj33,self.obj78,[608.85734755983731, 176.28568611987379, 640.0, 200.0, 640.0, 180.0],"bezier", 3) )
    # Connections for obj34 (graphObject_: Obj6) named New Selection
    self.drawConnections(
(self.obj34,self.obj70,[592.0625, 111.92862776025238, 560.0, 120.0, 520.0, 140.0, 417.0, 140.0],"bezier", 4),
(self.obj34,self.obj79,[608.85734755983731, 116.28568611987379, 640.0, 140.0, 640.0, 120.0],"bezier", 3) )
    # Connections for obj35 (graphObject_: Obj7) named Add To Selection
    self.drawConnections(
(self.obj35,self.obj69,[592.0625, 51.928627760252382, 560.0, 60.0, 500.0, 80.0, 417.0, 80.0],"bezier", 4),
(self.obj35,self.obj80,[608.97121093312421, 47.345228706624603, 640.0, 40.0, 640.0, 60.0],"bezier", 3) )
    # Connections for obj36 (graphObject_: Obj8) named Drag Nodes
    self.drawConnections(
(self.obj36,self.obj72,[608.85734755983731, 296.28568611987379, 640.0, 320.0, 640.0, 300.0],"bezier", 3),
(self.obj36,self.obj74,[593.03033867293959, 296.28568611987379, 500.0, 318.0, 407.0, 316.0],"bezier", 3) )
    # Connections for obj37 (graphObject_: Obj9) named Scale Entity
    self.drawConnections(
(self.obj37,self.obj83,[592.0625, 360.92862776025237, 538.0, 375.0, 392.0, 370.0],"bezier", 3),
(self.obj37,self.obj84,[610.05291297935105, 360.81545741324925, 640.0, 358.0, 640.0, 378.0],"bezier", 3),
(self.obj37,self.obj161,[610.05291297935105, 360.81545741324925, 640.0, 358.0, 640.0, 378.0],"bezier", 3) )
    # Connections for obj38 (graphObject_: Obj10) named Exit
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj11) named Default
    self.drawConnections(
(self.obj39,self.obj115,[496.6170349314811, 739.73738170347008, 460.0, 800.0, 500.0, 800.0],"bezier", 3),
(self.obj39,self.obj116,[496.6170349314811, 739.73738170347008, 460.0, 800.0, 500.0, 800.0],"bezier", 3),
(self.obj39,self.obj117,[496.6170349314811, 739.73738170347008, 460.0, 800.0, 500.0, 800.0],"bezier", 3),
(self.obj39,self.obj123,[501.22850154960616, 722.875, 499.0, 707.5],"bezier", 2),
(self.obj39,self.obj124,[496.6170349314811, 739.73738170347008, 460.0, 800.0, 500.0, 800.0],"bezier", 3),
(self.obj39,self.obj125,[508.97121093312415, 727.34522870662465, 542.16197691599996, 711.03036683499988, 575.47447691599996, 712.530366835],"bezier", 3),
(self.obj39,self.obj126,[508.97121093312415, 727.34522870662465, 542.16197691599996, 711.03036683499988, 575.47447691599996, 712.530366835],"bezier", 3) )
    # Connections for obj40 (graphObject_: Obj12) named Active Point
    self.drawConnections(
(self.obj40,self.obj113,[633.03033867293959, 756.28568611987384, 616.00165744962669, 773.93825134627457, 585.20036933958602, 770.02751593617973],"bezier", 3),
(self.obj40,self.obj114,[633.03033867293959, 756.28568611987384, 616.00165744962669, 773.93825134627457, 585.20036933958602, 770.02751593617973],"bezier", 3),
(self.obj40,self.obj118,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj119,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj120,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj121,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj122,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj127,[636.61703493148116, 759.73738170347008, 600.0, 820.0, 640.0, 820.0],"bezier", 3),
(self.obj40,self.obj169,[633.03033867293959, 756.28568611987384, 616.00165744962669, 773.93825134627457, 585.20036933958602, 770.02751593617973],"bezier", 3) )
    # Connections for obj41 (graphObject_: Obj13) named Snap Points
    self.drawConnections(
(self.obj41,self.obj129,[290.05291297935105, 720.81545741324919, 340.0, 709.0, 340.0, 729.0],"bezier", 3),
(self.obj41,self.obj130,[290.05291297935105, 720.81545741324919, 340.0, 709.0, 340.0, 729.0],"bezier", 3),
(self.obj41,self.obj133,[285.32758298793931, 728.73738170347008, 293.99999999999994, 773.5, 294.0, 809.0],"bezier", 3),
(self.obj41,self.obj175,[288.97121093312421, 716.34522870662465, 360.0, 700.0, 400.0, 700.0, 399.99999999999983, 720.0],"bezier", 4) )
    # Connections for obj42 (graphObject_: Obj14) named No Snap
    self.drawConnections(
(self.obj42,self.obj131,[290.05291297935105, 880.81545741324908, 340.0, 889.0, 340.0, 869.0],"bezier", 3),
(self.obj42,self.obj132,[290.05291297935105, 880.81545741324908, 340.0, 889.0, 340.0, 869.0],"bezier", 3),
(self.obj42,self.obj134,[281.22850154960616, 871.875, 273.99999999999994, 844.49999999999989, 274.0, 809.0],"bezier", 3),
(self.obj42,self.obj177,[288.85734755983731, 885.28568611987384, 340.0, 900.0, 360.0, 900.0],"bezier", 3) )
    # Connections for obj43 (graphObject_: Obj15) named Postscript
    self.drawConnections(
(self.obj43,self.obj145,[592.0625, 471.92862776025237, 560.0, 480.0, 480.0, 480.0, 440.0, 480.0, 400.0, 480.0],"bezier", 5),
(self.obj43,self.obj146,[605.32758298793931, 479.73738170346985, 611.0, 490.49999999999989, 611.0, 506.0],"bezier", 3),
(self.obj43,self.obj184,[592.0625, 471.92862776025237, 560.0, 480.0, 480.0, 480.0, 440.0, 480.0, 400.0, 480.0],"bezier", 5) )
    # Connections for obj44 (graphObject_: Obj16) named Bounding Box Edit
    self.drawConnections(
(self.obj44,self.obj147,[596.79896661812461, 544.01853312302842, 591.0, 521.5, 591.0, 506.0],"bezier", 3),
(self.obj44,self.obj148,[608.97121093312421, 547.34522870662465, 641.25, 526.0, 641.25, 546.0],"bezier", 3) )
    # Connections for obj45 (graphObject_: Obj17) named Drag Label
    self.drawConnections(
(self.obj45,self.obj150,[592.0625, 231.92862776025237, 460.0, 240.0, 406.0, 240.0],"bezier", 3),
(self.obj45,self.obj151,[608.85734755983731, 236.28568611987379, 640.0, 260.0, 640.0, 240.0],"bezier", 3) )
    # Connections for obj46 (graphObject_: Obj18) named Scale Text
    self.drawConnections(
(self.obj46,self.obj157,[608.97121093312421, 407.34522870662454, 640.0, 400.0, 640.0, 420.0],"bezier", 3),
(self.obj46,self.obj159,[592.0625, 411.92862776025237, 540.0, 420.0, 411.0, 420.0],"bezier", 3),
(self.obj46,self.obj160,[608.97121093312421, 407.34522870662454, 640.0, 400.0, 640.0, 420.0],"bezier", 3) )
    # Connections for obj47 (graphObject_: Obj19) named GG Graph Select
    self.drawConnections(
(self.obj47,self.obj167,[592.0114979680867, 600.07819072029429, 540.0, 600.0, 480.0, 600.0],"bezier", 3) )
    # Connections for obj48 (graphObject_: Obj20) named Drop Point
    self.drawConnections(
(self.obj48,self.obj176,[353.34320001431365, 747.61979166666674, 321.10027378699999, 736.45273889299972],"bezier", 2) )
    # Connections for obj49 (graphObject_: Obj21) named Drop Point2
    self.drawConnections(
(self.obj49,self.obj178,[352.97933664102646, 836.43524907991571, 320.97527378699999, 856.39023889299961],"bezier", 2) )
    # Connections for obj50 (graphObject_: Obj22) of type contains
    self.drawConnections(
(self.obj50,self.obj35,[633.0, 8.125, 605.38451467458265, 43.893533123028384], 0, 2) )
    # Connections for obj51 (graphObject_: Obj23) of type contains
    self.drawConnections(
(self.obj51,self.obj34,[644.625, 33.75, 605.38451467458265, 103.89353312302839], 0, 2) )
    # Connections for obj52 (graphObject_: Obj24) of type contains
    self.drawConnections(
(self.obj52,self.obj33,[644.25, 67.75, 605.38451467458265, 163.89353312302839], 0, 2) )
    # Connections for obj53 (graphObject_: Obj25) of type contains
    self.drawConnections(
(self.obj53,self.obj32,[231.125, 182.875, 148.97121093312418, 247.34522870662457], 0, 2) )
    # Connections for obj54 (graphObject_: Obj26) of type contains
    self.drawConnections(
(self.obj54,self.obj36,[166.25, 350.375, 592.0625, 291.92862776025237], 0, 2) )
    # Connections for obj55 (graphObject_: Obj27) of type contains
    self.drawConnections(
(self.obj55,self.obj37,[232.5, 336.5, 592.0625, 360.92862776025237], 0, 2) )
    # Connections for obj56 (graphObject_: Obj28) of type contains
    self.drawConnections(
(self.obj56,self.obj29,[173.0, 402.875, 450.0, 799.0],"bezier", 2) )
    # Connections for obj57 (graphObject_: Obj29) of type contains
    self.drawConnections(
(self.obj57,self.obj39,[765.375, 862.5, 508.85734755983731, 736.28568611987384],"bezier", 2) )
    # Connections for obj58 (graphObject_: Obj30) of type contains
    self.drawConnections(
(self.obj58,self.obj40,[789.875, 899.5, 648.85734755983731, 756.28568611987384],"bezier", 2) )
    # Connections for obj59 (graphObject_: Obj31) of type contains
    self.drawConnections(
(self.obj59,self.obj30,[489.5, 670.375, 413.0, 802.0],"bezier", 2) )
    # Connections for obj60 (graphObject_: Obj32) of type contains
    self.drawConnections(
(self.obj60,self.obj41,[8.0, 716.0, 272.0625, 720.92862776025243],"bezier", 2) )
    # Connections for obj61 (graphObject_: Obj33) of type contains
    self.drawConnections(
(self.obj61,self.obj42,[47.875, 1004.0, 273.03033867293959, 885.28568611987384],"bezier", 2) )
    # Connections for obj62 (graphObject_: Obj34) of type contains
    self.drawConnections(
(self.obj62,self.obj48,[387.63829047801295, 781.44347233175608, 365.27658095602618, 759.88694466351217],"bezier", 2) )
    # Connections for obj63 (graphObject_: Obj35) of type contains
    self.drawConnections(
(self.obj63,self.obj49,[390.46010445060551, 814.74739583333337, 368.92020890121108, 827.49479166666674],"bezier", 2) )
    # Connections for obj64 (graphObject_: Obj36) named 
    self.drawConnections(
(self.obj64,self.obj33,[424.0, 160.0, 500.0, 160.0, 580.0, 160.0, 593.39420204622684, 167.4702287066246],"bezier", 4) )
    # Connections for obj65 (graphObject_: Obj38) named 
    self.drawConnections(
(self.obj65,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj66 (graphObject_: Obj40) named 
    self.drawConnections(
(self.obj66,self.obj32,[417.0, 200.0, 360.0, 200.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj67 (graphObject_: Obj42) named 
    self.drawConnections(
(self.obj67,self.obj35,[420.0, 40.0, 580.0, 40.0, 593.39420204622684, 47.470228706624603],"bezier", 3) )
    # Connections for obj68 (graphObject_: Obj44) named 
    self.drawConnections(
(self.obj68,self.obj34,[416.0, 100.0, 580.0, 100.0, 593.39420204622684, 107.47022870662458],"bezier", 3) )
    # Connections for obj69 (graphObject_: Obj46) named 
    self.drawConnections(
(self.obj69,self.obj32,[417.0, 80.0, 360.0, 80.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj70 (graphObject_: Obj48) named 
    self.drawConnections(
(self.obj70,self.obj32,[417.0, 140.0, 340.0, 140.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj71 (graphObject_: Obj50) named 
    self.drawConnections(
(self.obj71,self.obj34,[416.0, 120.0, 500.0, 120.0, 580.0, 100.0, 593.39420204622684, 107.47022870662458],"bezier", 4) )
    # Connections for obj72 (graphObject_: Obj52) named 
    self.drawConnections(
(self.obj72,self.obj36,[640.0, 300.0, 640.0, 280.0, 608.97121093312421, 287.3452287066246],"bezier", 3) )
    # Connections for obj73 (graphObject_: Obj54) named 
    self.drawConnections(
(self.obj73,self.obj36,[402.0, 280.0, 440.0, 280.0, 580.0, 280.0, 593.39420204622684, 287.4702287066246],"bezier", 4) )
    # Connections for obj74 (graphObject_: Obj56) named 
    self.drawConnections(
(self.obj74,self.obj32,[407.0, 316.0, 346.0, 316.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj75 (graphObject_: Obj58) named 
    self.drawConnections(
(self.obj75,self.obj35,[420.0, 60.0, 500.0, 60.0, 580.0, 40.0, 593.39420204622684, 47.470228706624603],"bezier", 4) )
    # Connections for obj76 (graphObject_: Obj60) named 
    self.drawConnections(
(self.obj76,self.obj33,[424.0, 180.0, 520.0, 180.0, 580.0, 160.0, 593.39420204622684, 167.4702287066246],"bezier", 4) )
    # Connections for obj77 (graphObject_: Obj62) named 
    self.drawConnections(
(self.obj77,self.obj28,[20.0, 260.0, 20.0, 420.0, 92.0, 486.0],"bezier", 3) )
    # Connections for obj78 (graphObject_: Obj64) named 
    self.drawConnections(
(self.obj78,self.obj33,[640.0, 180.0, 640.0, 160.0, 608.97121093312421, 167.3452287066246],"bezier", 3) )
    # Connections for obj79 (graphObject_: Obj66) named 
    self.drawConnections(
(self.obj79,self.obj34,[640.0, 120.0, 640.0, 100.0, 608.97121093312421, 107.3452287066246],"bezier", 3) )
    # Connections for obj80 (graphObject_: Obj68) named 
    self.drawConnections(
(self.obj80,self.obj35,[640.0, 60.0, 640.0, 80.0, 608.85734755983731, 56.285686119873795],"bezier", 3) )
    # Connections for obj81 (graphObject_: Obj70) named 
    self.drawConnections(
(self.obj81,self.obj28,[20.0, 480.0, 20.0, 420.0, 92.0, 486.0],"bezier", 3) )
    # Connections for obj82 (graphObject_: Obj72) named 
    self.drawConnections(
(self.obj82,self.obj37,[417.0, 357.0, 449.0, 359.0, 564.0, 360.0, 592.0625, 360.92862776025237],"bezier", 4) )
    # Connections for obj83 (graphObject_: Obj74) named 
    self.drawConnections(
(self.obj83,self.obj32,[392.0, 370.0, 328.0, 370.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj84 (graphObject_: Obj76) named 
    self.drawConnections(
(self.obj84,self.obj37,[640.0, 378.0, 640.0, 398.0, 608.85734755983731, 365.28568611987379],"bezier", 3) )
    # Connections for obj85 (graphObject_: Obj78) named 
    self.drawConnections(
(self.obj85,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj86 (graphObject_: Obj80) named 
    self.drawConnections(
(self.obj86,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj87 (graphObject_: Obj82) named 
    self.drawConnections(
(self.obj87,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj88 (graphObject_: Obj84) named 
    self.drawConnections(
(self.obj88,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj89 (graphObject_: Obj86) named 
    self.drawConnections(
(self.obj89,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj90 (graphObject_: Obj88) named 
    self.drawConnections(
(self.obj90,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj91 (graphObject_: Obj90) named 
    self.drawConnections(
(self.obj91,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj92 (graphObject_: Obj92) named 
    self.drawConnections(
(self.obj92,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj93 (graphObject_: Obj94) named 
    self.drawConnections(
(self.obj93,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj94 (graphObject_: Obj96) named 
    self.drawConnections(
(self.obj94,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj95 (graphObject_: Obj98) named 
    self.drawConnections(
(self.obj95,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj96 (graphObject_: Obj100) named 
    self.drawConnections(
(self.obj96,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj97 (graphObject_: Obj102) named 
    self.drawConnections(
(self.obj97,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj98 (graphObject_: Obj104) named 
    self.drawConnections(
(self.obj98,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj99 (graphObject_: Obj106) named 
    self.drawConnections(
(self.obj99,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj100 (graphObject_: Obj108) named 
    self.drawConnections(
(self.obj100,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj101 (graphObject_: Obj110) named 
    self.drawConnections(
(self.obj101,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj102 (graphObject_: Obj112) named 
    self.drawConnections(
(self.obj102,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj103 (graphObject_: Obj114) named 
    self.drawConnections(
(self.obj103,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj104 (graphObject_: Obj116) named 
    self.drawConnections(
(self.obj104,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj105 (graphObject_: Obj118) named 
    self.drawConnections(
(self.obj105,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj106 (graphObject_: Obj120) named 
    self.drawConnections(
(self.obj106,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj107 (graphObject_: Obj122) named 
    self.drawConnections(
(self.obj107,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj108 (graphObject_: Obj124) named 
    self.drawConnections(
(self.obj108,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj109 (graphObject_: Obj126) named 
    self.drawConnections(
(self.obj109,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj110 (graphObject_: Obj128) named 
    self.drawConnections(
(self.obj110,self.obj32,[140.0, 180.0, 200.0, 180.0, 145.38451467458265, 243.89353312302836],"bezier", 3) )
    # Connections for obj111 (graphObject_: Obj130) named 
    self.drawConnections(
(self.obj111,self.obj38,[20.0, 578.0, 20.0, 617.99999999999989, 21.228501549606143, 882.875],"bezier", 3) )
    # Connections for obj112 (graphObject_: Obj132) named 
    self.drawConnections(
(self.obj112,self.obj29,[540.0, 660.0, 580.0, 660.0, 579.0, 692.0],"bezier", 3) )
    # Connections for obj113 (graphObject_: Obj134) named 
    self.drawConnections(
(self.obj113,self.obj39,[585.20036933958602, 770.02751593617973, 554.39908122954535, 766.11678052608545, 508.85734755983731, 736.28568611987384],"bezier", 3) )
    # Connections for obj114 (graphObject_: Obj136) named 
    self.drawConnections(
(self.obj114,self.obj39,[585.20036933958602, 770.02751593617973, 554.39908122954535, 766.11678052608545, 508.85734755983731, 736.28568611987384],"bezier", 3) )
    # Connections for obj115 (graphObject_: Obj138) named 
    self.drawConnections(
(self.obj115,self.obj39,[500.0, 800.0, 540.0, 800.0, 505.32758298793931, 739.73738170347008],"bezier", 3) )
    # Connections for obj116 (graphObject_: Obj140) named 
    self.drawConnections(
(self.obj116,self.obj39,[500.0, 800.0, 540.0, 800.0, 505.32758298793931, 739.73738170347008],"bezier", 3) )
    # Connections for obj117 (graphObject_: Obj142) named 
    self.drawConnections(
(self.obj117,self.obj39,[500.0, 800.0, 540.0, 800.0, 505.32758298793931, 739.73738170347008],"bezier", 3) )
    # Connections for obj118 (graphObject_: Obj144) named 
    self.drawConnections(
(self.obj118,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj119 (graphObject_: Obj146) named 
    self.drawConnections(
(self.obj119,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj120 (graphObject_: Obj148) named 
    self.drawConnections(
(self.obj120,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj121 (graphObject_: Obj150) named 
    self.drawConnections(
(self.obj121,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj122 (graphObject_: Obj152) named 
    self.drawConnections(
(self.obj122,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj123 (graphObject_: Obj154) named 
    self.drawConnections(
(self.obj123,self.obj32,[499.0, 707.5, 498.99999999999989, 669.75, 420.0, 660.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 5) )
    # Connections for obj124 (graphObject_: Obj156) named 
    self.drawConnections(
(self.obj124,self.obj39,[500.0, 800.0, 540.0, 800.0, 505.32758298793931, 739.73738170347008],"bezier", 3) )
    # Connections for obj125 (graphObject_: Obj158) named 
    self.drawConnections(
(self.obj125,self.obj40,[575.47447691599996, 712.530366835, 608.78697691599996, 714.030366835, 636.79896661812461, 744.01853312302842],"bezier", 3) )
    # Connections for obj126 (graphObject_: Obj160) named 
    self.drawConnections(
(self.obj126,self.obj40,[575.47447691599996, 712.530366835, 608.78697691599996, 714.030366835, 636.79896661812461, 744.01853312302842],"bezier", 3) )
    # Connections for obj127 (graphObject_: Obj162) named 
    self.drawConnections(
(self.obj127,self.obj40,[640.0, 820.0, 680.0, 820.0, 645.32758298793931, 759.73738170347008],"bezier", 3) )
    # Connections for obj128 (graphObject_: Obj164) named 
    self.drawConnections(
(self.obj128,self.obj36,[390.0, 260.0, 420.0, 260.0, 460.0, 260.0, 580.0, 280.0, 593.39420204622684, 287.4702287066246],"bezier", 5) )
    # Connections for obj129 (graphObject_: Obj166) named 
    self.drawConnections(
(self.obj129,self.obj41,[340.0, 729.0, 340.0, 749.0, 288.85734755983731, 725.28568611987384],"bezier", 3) )
    # Connections for obj130 (graphObject_: Obj168) named 
    self.drawConnections(
(self.obj130,self.obj41,[340.0, 729.0, 340.0, 749.0, 288.85734755983731, 725.28568611987384],"bezier", 3) )
    # Connections for obj131 (graphObject_: Obj170) named 
    self.drawConnections(
(self.obj131,self.obj42,[340.0, 869.0, 340.0, 849.0, 288.97121093312421, 876.34522870662465],"bezier", 3) )
    # Connections for obj132 (graphObject_: Obj172) named 
    self.drawConnections(
(self.obj132,self.obj42,[340.0, 869.0, 340.0, 849.0, 288.97121093312421, 876.34522870662465],"bezier", 3) )
    # Connections for obj133 (graphObject_: Obj174) named 
    self.drawConnections(
(self.obj133,self.obj42,[294.0, 809.0, 293.99999999999994, 844.49999999999989, 285.38451467458248, 872.89353312302842],"bezier", 3) )
    # Connections for obj134 (graphObject_: Obj176) named 
    self.drawConnections(
(self.obj134,self.obj41,[274.0, 809.0, 273.99999999999994, 773.5, 280.88691142974494, 729.8125],"bezier", 3) )
    # Connections for obj135 (graphObject_: Obj178) named 
    self.drawConnections(
(self.obj135,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj136 (graphObject_: Obj180) named 
    self.drawConnections(
(self.obj136,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj137 (graphObject_: Obj182) named 
    self.drawConnections(
(self.obj137,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj138 (graphObject_: Obj184) named 
    self.drawConnections(
(self.obj138,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj139 (graphObject_: Obj186) named 
    self.drawConnections(
(self.obj139,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj140 (graphObject_: Obj188) named 
    self.drawConnections(
(self.obj140,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj141 (graphObject_: Obj190) named 
    self.drawConnections(
(self.obj141,self.obj30,[340.0, 558.0, 329.0, 692.0],"bezier", 2) )
    # Connections for obj142 (graphObject_: Obj192) named 
    self.drawConnections(
(self.obj142,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj143 (graphObject_: Obj194) named 
    self.drawConnections(
(self.obj143,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj144 (graphObject_: Obj196) named 
    self.drawConnections(
(self.obj144,self.obj43,[440.0, 460.0, 560.0, 460.0, 592.0625, 471.92862776025237],"bezier", 3) )
    # Connections for obj145 (graphObject_: Obj198) named 
    self.drawConnections(
(self.obj145,self.obj32,[400.0, 480.0, 340.0, 480.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj146 (graphObject_: Obj200) named 
    self.drawConnections(
(self.obj146,self.obj44,[611.0, 506.0, 611.0, 521.5, 605.38451467458265, 543.89353312302842],"bezier", 3) )
    # Connections for obj147 (graphObject_: Obj202) named 
    self.drawConnections(
(self.obj147,self.obj43,[591.0, 506.0, 591.0, 490.49999999999989, 596.61703493148116, 479.73738170346985],"bezier", 3) )
    # Connections for obj148 (graphObject_: Obj204) named 
    self.drawConnections(
(self.obj148,self.obj44,[641.25, 546.0, 641.25, 566.0, 608.85734755983731, 556.28568611987384],"bezier", 3) )
    # Connections for obj149 (graphObject_: Obj206) named 
    self.drawConnections(
(self.obj149,self.obj45,[400.0, 220.0, 420.0, 220.0, 580.0, 220.0, 593.39420204622684, 227.4702287066246],"bezier", 4) )
    # Connections for obj150 (graphObject_: Obj208) named 
    self.drawConnections(
(self.obj150,self.obj32,[406.0, 240.0, 360.0, 240.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj151 (graphObject_: Obj210) named 
    self.drawConnections(
(self.obj151,self.obj45,[640.0, 240.0, 640.0, 220.0, 608.97121093312421, 227.3452287066246],"bezier", 3) )
    # Connections for obj152 (graphObject_: Obj212) named 
    self.drawConnections(
(self.obj152,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj153 (graphObject_: Obj214) named 
    self.drawConnections(
(self.obj153,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj154 (graphObject_: Obj216) named 
    self.drawConnections(
(self.obj154,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj155 (graphObject_: Obj218) named 
    self.drawConnections(
(self.obj155,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj156 (graphObject_: Obj220) named 
    self.drawConnections(
(self.obj156,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj157 (graphObject_: Obj222) named 
    self.drawConnections(
(self.obj157,self.obj46,[640.0, 420.0, 640.0, 440.0, 608.85734755983731, 416.28568611987379],"bezier", 3) )
    # Connections for obj158 (graphObject_: Obj224) named 
    self.drawConnections(
(self.obj158,self.obj46,[411.0, 400.0, 480.0, 400.0, 580.0, 400.0, 593.39420204622684, 407.47022870662454],"bezier", 4) )
    # Connections for obj159 (graphObject_: Obj226) named 
    self.drawConnections(
(self.obj159,self.obj32,[411.0, 420.0, 380.0, 420.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )
    # Connections for obj160 (graphObject_: Obj228) named 
    self.drawConnections(
(self.obj160,self.obj46,[640.0, 420.0, 640.0, 440.0, 608.85734755983731, 416.28568611987379],"bezier", 3) )
    # Connections for obj161 (graphObject_: Obj230) named 
    self.drawConnections(
(self.obj161,self.obj37,[640.0, 378.0, 640.0, 398.0, 608.85734755983731, 365.28568611987379],"bezier", 3) )
    # Connections for obj162 (graphObject_: Obj232) named 
    self.drawConnections(
(self.obj162,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj163 (graphObject_: Obj234) named 
    self.drawConnections(
(self.obj163,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj164 (graphObject_: Obj236) named 
    self.drawConnections(
(self.obj164,self.obj36,[410.5, 297.5, 511.0, 299.0, 592.0625, 291.92862776025237],"bezier", 3) )
    # Connections for obj165 (graphObject_: Obj238) named 
    self.drawConnections(
(self.obj165,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj166 (graphObject_: Obj240) named 
    self.drawConnections(
(self.obj166,self.obj47,[440.0, 580.0, 500.0, 580.0, 560.0, 580.0, 593.34320001431377, 595.61979166666652],"bezier", 4) )
    # Connections for obj167 (graphObject_: Obj242) named 
    self.drawConnections(
(self.obj167,self.obj32,[480.0, 600.0, 360.0, 600.0, 300.0, 540.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 5) )
    # Connections for obj168 (graphObject_: Obj244) named 
    self.drawConnections(
(self.obj168,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj169 (graphObject_: Obj246) named 
    self.drawConnections(
(self.obj169,self.obj39,[585.20036933958602, 770.02751593617973, 554.39908122954535, 766.11678052608545, 508.85734755983731, 736.28568611987384],"bezier", 3) )
    # Connections for obj170 (graphObject_: Obj248) named 
    self.drawConnections(
(self.obj170,self.obj29,[540.0, 660.0, 580.0, 660.0, 579.0, 692.0],"bezier", 3) )
    # Connections for obj171 (graphObject_: Obj250) named 
    self.drawConnections(
(self.obj171,self.obj43,[440.0, 460.0, 560.0, 460.0, 592.0625, 471.92862776025237],"bezier", 3) )
    # Connections for obj172 (graphObject_: Obj252) named 
    self.drawConnections(
(self.obj172,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj173 (graphObject_: Obj254) named 
    self.drawConnections(
(self.obj173,self.obj32,[140.0, 320.0, 200.0, 320.0, 145.32758298793934, 259.73738170346996],"bezier", 3) )
    # Connections for obj174 (graphObject_: Obj256) named 
    self.drawConnections(
(self.obj174,self.obj28,[371.5, 923.5, 404.0, 942.0],"bezier", 2) )
    # Connections for obj175 (graphObject_: Obj258) named 
    self.drawConnections(
(self.obj175,self.obj48,[399.99999999999989, 720.0, 400.0, 740.0, 368.92020890121108, 747.49479166666674],"bezier", 3) )
    # Connections for obj176 (graphObject_: Obj260) named 
    self.drawConnections(
(self.obj176,self.obj41,[321.10027378707537, 736.45273889327029, 288.85734755983731, 725.28568611987384],"bezier", 2) )
    # Connections for obj177 (graphObject_: Obj262) named 
    self.drawConnections(
(self.obj177,self.obj49,[360.0, 900.0, 380.0, 900.0, 400.0, 880.0, 400.0, 840.0, 370.00191094743792, 831.96502037329117],"bezier", 5) )
    # Connections for obj178 (graphObject_: Obj264) named 
    self.drawConnections(
(self.obj178,self.obj42,[320.97527378707537, 856.39023889327018, 288.97121093312421, 876.34522870662465],"bezier", 2) )
    # Connections for obj184 (graphObject_: Obj266) named 
    self.drawConnections(
(self.obj184,self.obj32,[400.0, 480.0, 340.0, 480.0, 240.0, 300.0, 148.85734755983731, 256.28568611987379],"bezier", 4) )

newfunction = UI_Statechart_MDL

loadedMMName = 'DCharts'

atom3version = '0.3'

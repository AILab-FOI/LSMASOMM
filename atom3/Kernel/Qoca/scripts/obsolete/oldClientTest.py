"""
QOCA Client tests

Denis Dube, Summer 2005
"""

from constraints.QocaConstants import *
from client.PipeQocaClient import PipeQocaClient
from client.TcpQocaClient import TcpQocaClient

def nonInteractiveTest(self):
  """ Quick test mode """
  print 'Testing QcCassSolver'
      
  stayWeight = str(pow(2, 20))
  editWeight = str(pow(2, 60))
  fixedWeight = str(pow(2, 80))
  
  # Initilize variables: w, x, y, z
  s = SOLVER_CASS +';'
  s += FLOAT_FIXED_ADD + " w 10.0 " + fixedWeight + ';'
  s += FLOAT_ADD + " x 10.0 "+stayWeight+" "+editWeight + ';'
  s += FLOAT_ADD + " y 29.0 "+stayWeight+" "+editWeight + ';'
  s += FLOAT_ADD + " z 30.0 "+stayWeight+" "+editWeight + ';'
  
  # Add constraints: w == x; y - x >= 5; y <= z
  s += CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
  s += CONSTRAINT_ADD + " c2 1.0,x,-1.0,y " + LE + " -5.0" + ';'
  s += CONSTRAINT_ADD + " c3 1.0,z,-1.0,y " + GE + " 0.0" + ';'
  
  # Ask the server to solve and return the solution
  s += SOLVER_SOLVE + ';'
  s += GET_RESULT_ALL + '\n'
  self.write( s )    
  print 'Recieved response:\n', self.read()
  
  def manipulationOne():
    print "First manipulation"
    print "Edit y := 25, SOLVER_RESOLVE."
    
    s = EDIT_ADDVAR + " y;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " y 25.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "Edit y := 15, resolve."
    s = EDIT_SUGGEST + " y 15.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "Edit y := 5, resolve."
    s = EDIT_SUGGEST + " y 5.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "End edit."
    s = EDIT_END + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s );
    print 'Recieved response:\n', self.read()
  
  
  def manipulationTwo():
    print "Second manipulation"
    print "Remove `w == x' constraint, edit x := 15, resolve."
    
    s = CONSTRAINT_REMOVE + " c1;"
    s += EDIT_ADDVAR + " x;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " x 15.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "x := 25, resolve."
    s = EDIT_SUGGEST + " x 25.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "x := 35, resolve."
    s = EDIT_SUGGEST + " x 35.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "End edit."
    s = EDIT_END + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s );
    print 'Recieved response:\n', self.read()
    
    
  def manipulationThree():
    print "Third manipulation"
    print "Re-add constraint `w == x', solve."
    
    s = CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
    s += SOLVER_SOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
  
    print "Third manipulation: edit z := 25, resolve."
    s = EDIT_ADDVAR + " z;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " z 25.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "x := 15, resolve."
    s = EDIT_SUGGEST + " z 15.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "z := 5, resolve."
    s = EDIT_SUGGEST + " z 5.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "End edit."
    s = EDIT_END + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s );
    print 'Recieved response:\n', self.read()
    
  
  def manipulationFour():
    print "Fourth manipulation:"
    print "Change `y - x >= 5' to `>= 10'.  edit y := 25, resolve."
    
    s = CONSTRAINT_CHANGE + ' c2 -10.0;'
    s += EDIT_ADDVAR + " y;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " y 25.0;"
    s += SOLVER_SOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
  
    print "y := 15, resolve."
    s = EDIT_ADDVAR + " y;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " y 15.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
    
    print "y := 5, resolve."
    s = EDIT_SUGGEST + " y 5.0;"
    s += SOLVER_RESOLVE + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s )    
    print 'Recieved response:\n', self.read()
          
    print "End edit."
    s = EDIT_END + ';'
    s += GET_RESULT_ALL + '\n'
    self.write( s );
    print 'Recieved response:\n', self.read()
    
  
  manipulationOne()
  manipulationTwo()
  manipulationThree()
  manipulationFour()
  
  # Remove constraints and variables
  s = CONSTRAINT_REMOVE + ' c1;' 
  s += CONSTRAINT_REMOVE + ' c2;'
  s += CONSTRAINT_REMOVE + ' c3;'
  s += FLOAT_REMOVE + ' w;'
  s += FLOAT_REMOVE + ' x;'
  s += FLOAT_REMOVE + ' y;'
  s += FLOAT_REMOVE + ' z\n'
  self.write( s )   
  print "Test complete!"




if(__name__ == '__main__'):
    
#--------------------------------- TCP/IP Test ---------------------------------
    
  ## print '\nQOCA TCP/IP communication test\n'
  
  ## # Setup a TCP/IP client and establish a connection to a host
  ## client = TcpQocaClient('127.0.0.1', 14059, True)
  ## if(client.connect()): 

    ## # Send messages to the host, and recieve a response after each message
    ## nonInteractiveTest(client)
    
    ## print 'QOCA TCP/IP communication test... DONE'
    ## client.disconnect()
  
#---------------------------------- Pipe Test ----------------------------------
  
  print '\nQOCA PIPE communication test\n'

  command = 'java -jar D:\QocaServerB1.jar' # Start the Java Qoca Toolkit
  
  # Setup a TCP/IP client and establish a connection to a host
  client = PipeQocaClient(command)
  if(client.connect()):

    # Send messages to the host, and recieve a response after each message
    nonInteractiveTest(client)
    
    print 'QOCA Pipe communication test... DONE'
    client.disconnect()
  

  
  
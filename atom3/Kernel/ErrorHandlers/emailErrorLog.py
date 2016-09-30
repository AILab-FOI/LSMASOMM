"""
Need a SMTP host anyone can use, otherwise requires config by each user :(
"""

try:
  import smtplib
except:
  print "Skipping, can't import 'smtplib'..."       

class emailErrorLog:
  
  def __init__(self):
    
    #self.smtpServer = 'mailhost.mcgill.ca'
    self.smtpServer = 'relais.videotron.ca'
    self.subjectLine = 'AToM3 Incident Report'
        
  def sendMessage(self, fromAddr, toAddrs,messagePrologue, incident ):
    
    # Prepare the message...
    messageHeader = "From: %s\r\n"\
                    "To: %s\r\n"\
                    "Subject: %s\r\n"\
                    "AToM3-Error-Id: %s\r\n\r\n" % \
                    (fromAddr,
                    ", ".join(toAddrs),self.subjectLine,
                    incident)


    message = messageHeader + messagePrologue 

    # Deliver the message...
    server = None

    try:
        server = smtplib.SMTP(self.smtpServer)
        # server.set_debuglevel(1)
        server.sendmail(fromAddr, toAddrs, message)
    except:
        print 'Failed to e-mail error log'

    if server:
        # If the connection is open we want to close it...
        # (Using .quit() on a closed connection causes an error.)
        if getattr(server, "sock", False): # The 'sock' attribute is
                                          # undocumented...
            server.quit()
            


if __name__ == '__main__':
  print 'Testing e-mail'

  TO_ADDRESSES = ['d3n14@yahoo.com',]  
  FROM_ADDRESS = "mongoose@example.com"

  MESSAGE_PROLOGUE = "An error occured while using the AToM3 tool!\n"
  
  emailLog = emailErrorLog()
  emailLog.sendMessage( FROM_ADDRESS, TO_ADDRESSES, MESSAGE_PROLOGUE,str(555))

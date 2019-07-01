
import socket                

s = socket.socket()          
print ("Socket successfully created")
  
port = 12345                
  

s.bind(('', port))         
print ("socket binded to %s" %(port) )
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print (('Got connection from'), addr )
   print(str(c.recv(1024))[1:])
   #print(s.recv(1024)) 
 
  
   # Close the connection with the client 
   c.close() 
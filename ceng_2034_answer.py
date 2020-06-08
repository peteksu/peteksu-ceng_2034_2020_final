# Peteksu Karpuz 170709063
import os
import requests #Requests library for sending HTTP requests with Python allows header, form or similar parameters to be set “in a human readable form” and the responses from the server can be displayed.
import uuid
import hashlib #This hashlib library provides functionalities of different hashing functions like MD5, SHA-1, etc.

#1question
child = os.fork()
if child == 0:
  print("child PID", os.getpid())


#2question
url= ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024pxHawai%27i.jpg", "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c/Hawai%27i.jpg/1024pxHawai%27i.jpg"]

def download_file(url,file_name=None):
  r = requests.get(url,allow_redirects=True)
  file = file_name if file_name else str(uuid.uuid4())
  open(file,'wb').write(r.content)


for i in url:
  download_file(i,file_name=None)


#3question
print("parent id", os.getpid()) #create parent process and show its pid
child = os.fork() #os.fork() command creates child process
if child == 0:
  print("child id",os.getpid())
  os._exit(0)

print("here is parent proc")
os.wait()  
#If the parent process task ends before the child process, then the child process becomes an orphan process.If we use the os.wait() function, even if the parent process finishes the task before the child process, the parent process waits for the child process to finish and the orphan status is prevented.

#4question
array1 = []
unique = dict()
for file_name in os.listdir('.'):
    if os.path.isfile(file_name):
        filehash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()

        if filehash not in unique: 
            unique[filehash] = file_name
        else:
            print (file_name + ' is a duplicate of ' + unique[filehash])
            array1.append(unique[filehash])
            
            
array_duplicates=[]
def compare_array(array):
  i = -1
  value = array[i]
  try:
      while 1:
          i = array1.index(value, i+1)
          print ("there is coupling in", i, "index")
          array_duplicates.append(array1[i])
  except ValueError:
      pass
      print("duplicates are", array_duplicates)

compare_array(array1)
# I gathered the unique[filehash] values in an array1. I then compared the indexes in this array with each other. I created a new array (array_duplicates) and added the matching file codes to this array.
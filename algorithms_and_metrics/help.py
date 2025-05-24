import os 
from dotenv import load_dotenv

load_dotenv()



# file_name = "tip.csv"



def list_files():
    for (root,dirs,files) in os.walk(os.environ['DATA_PATH'] or "C:\\codes\\data"):
        
        if root == os.environ['DATA_PATH']:
            print("root : ",end='')
            print(files)
        
        else:
            print(f'{root.split(chr(92))[::-1][0]} : ', end='')
            print(files)
    
     
        
def find_file(file_name):
    for (root,dirs,files) in os.walk(os.environ['DATA_PATH'] or "C:\\codes\\data"):
        if file_name in files:
            return f"{root}\\{file_name}"
    
    

        

#list_files()
from curses import keyname
import sys
import textract
from  time import time
import re

class FindKeyWd:
    
    def __init__(self, path: str, keywd: str) -> None: # init function 
        self.path = path
        self.keywd = keywd
        
    def lookup(self) -> dict: # lookup funtion 
        start = time() # counter start time 
        try:
            para = (textract.process(self.path, method='pdfminer')).decode('utf-8')
        except textract.exceptions.MissingFileError: # no file path or wrong
            print("Wrong file's path, please try again!")
            sys.exit()
        return {"duration":round(time() - start,1), "found": True} if re.search(self.keywd, para) else {"duration":round(time() - start,1), "found": False}
        
            
        
from json.tool import main
import sys
import textract
from  time import time
import re
import distro 
from shutil import which
import os

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
    
    
class ExtracPDF:
    
    def __init__(self) -> None:
        pass
    
    def is_tool():
    # """Check whether `name` is on PATH and marked as executable."""
        check_distro = True if distro.id() == "ubuntu" else False
        if which("tshark") and check_distro:
            # logging.info('[Checked]Tshark already installed in Ubuntu distro!') 
            print('[Checked]Tshark already installed in Ubuntu distro!') 
        else:
            # logging.info('Please install tshark before using this tool!')
            # logging.info('run : sudo apt install tshark -y')
            print('Please install tshark before using this tool!')
            print('run : sudo apt install tshark -y')
            sys.exit()
            
    def extract(pcap_path:str, dir:str, protocol: str):
        extracted_dir = f'{dir}/{int(time())}'
        os.system(f'mkdir {extracted_dir}')
        command = f'tshark -r {pcap_path} --export-objects "{protocol},{extracted_dir}"'
        return os.system(command)
        
if __name__ == "__main__":
    ExtracPDF.is_tool()
    ExtracPDF.extract("/home/erik/Videos/ExtractPcap/Raw.pcap", "Data", "http")
    
        
        
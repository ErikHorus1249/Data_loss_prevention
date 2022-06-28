import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
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
    
    def lookup_bord(self):
        # read the Document
        pdf_file: typing.Optional[Document] = None
        texts: SimpleTextExtraction = SimpleTextExtraction()
        with open(self.path, "rb") as in_file_handle:
            pdf_file = PDF.loads(in_file_handle, [texts])

        # check whether we have read a PDF file
        assert pdf_file is not None

        f = open(f'{os.path.dirname(self.path)}/alert1.txt', "w")

        if self.keywd in texts.get_text_for_page(0):
            print(f"Phat hien keyword trong tai lieu: {self.keywd}")
            f.write(f"Phat hien keyword trong tai lieu: {self.keywd}")
            f.close()
        else:
            print(f"Khong phat hien keyword trong tai lieu!")
            f.write(f"Khong phat hien keyword trong tai lieu!")
            f.close()


    
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
        dir_name = str(int(time()))
        command = f'tshark -Q -r {pcap_path} --export-objects "{protocol},{extracted_dir}"'
        os.system(command)
        Non_PDF = f'{dir}/{dir_name}/files'
        PDF = f'{dir}/{dir_name}/files.pdf'
        if os.path.exists(Non_PDF):
            os.rename(Non_PDF, PDF)
            return PDF
        return None

        
if __name__ == "__main__":
    # ExtracPDF.is_tool()
    PDF = ExtracPDF.extract("/home/ubuntu/Desktop/Data_loss_prevention/Pcap/Raw.pcap", "/home/ubuntu/Desktop/Data_loss_prevention/Data", "http")
    # print(PDF)
    # FindKeyWd(PDF, "snalysis").lookup_bord()
    # ExtracPDF.is_tool()
    
        
        
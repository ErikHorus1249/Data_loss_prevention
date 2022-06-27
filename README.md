
  
  

## Searching text in a PDF using Python
## :warning: This tool only works in Linux system :warning:
  

**:one:** Create python env:

  

```c

  

$ python3 -m venv venv
$ source source venv/bin/activate
$ pip install wheel

  

```

  

**:two:** Install pip package in requirement file:

  

```c

  

$ pip install -r requirements.txt

  

```

  

**:three:** How to use:

```c

$ python DLP.py -h

usage: DLP.py [-t TOOL] [-p PCAP] [-pro PROTOCOL] [-d FILE_DIR] [-k KEYWORD]

  

optional arguments:

-h, --help show this help message and exit

-t TOOL, --tool TOOL Tool name: extract pcap - ep ; find text - ft

-p PCAP, --pcap PCAP Pcap file path

-pro PROTOCOL, --protocol PROTOCOL Protocol: http, ftp, ...

-d FILE_DIR, --file_dir FILE_DIR Save extracted file to folder

-k KEYWORD, --keyword KEYWORD Keyword!

```

  

```c

  

# DLP.py

  

Etract files from Pcap:

  

$ python DLP.py -t ep -p <pcap-file-path>  -pro <protocol>  -d <saved-directory>

  

EX: $ python DLP.py -t ep -p /home/ExtractPcap/Raw.pcap -pro http -d Data/

  

Search keyword in a PDF:

  

$ python DLP.py -t ft -d <PDF-file-path>  -k <keyword>

  

EX: $ python DLP.py -t ft -d doc/Test_en.pdf -k "Khan Pathan"

  

```

  
  

**:notebook:** The tool is compatible with English and utf-8 documents

  

:weary:[by ErikHorus1249](https://github.com/ErikHorus1249)
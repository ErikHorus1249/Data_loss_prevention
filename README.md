

## Searching text in a PDF using Python

**Step 1:** Create python env:

```c

$ python3 -m venv venv

```

**Step 2:** Install pip package in requirement file:

```c

$ pip install -r requirements.txt

```

**Step 3:** How to use:
```c
$ python DLP.py -h                                        
usage: DLP.py [-h] [-t TOOL] [-p PCAP] [-pro PROTOCOL] [-d FILE_DIR] [-k KEYWORD]

optional arguments:
  -h,            --help            show this help message and exit
  -t TOOL,       --tool TOOL  Tool name: extract pcap - ep ; find text - ft
  -p PCAP,       --pcap PCAP  Pcap file path
  -pro PROTOCOL, --protocol PROTOCOL Protocol: http, ftp, ...
  -d FILE_DIR,   --file_dir FILE_DIR Save extracted file to folder
  -k KEYWORD,   --keyword KEYWORD Keyword!
```

```c

# DLP.py

Etract files from Pcap:

$ python DLP.py -t ep -p <pcap-file-path> -pro <protocol> -d <saved-directory>

EX: $ python main.py -t ep -p /home/ExtractPcap/Raw.pcap -pro http -d Data/

Search keyword in a PDF:

$ python main.py -t ft -d <PDF-file-path> -k <keyword>

EX: $ python main.py -t ft -d doc/Test_en.pdf -k "Khan Pathan"

```


**Note:** The tool is compatible with English and utf-8 documents

[by ErikHorus1249](https://github.com/ErikHorus1249)

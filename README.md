## Searching text in a PDF using Python
## :warning: This tool only works in Linux system :warning:
  

**:one:** Create python env:

  

```c

  

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install wheel

  

```

  

**:two:** Install pip package in requirement file:

  

```c

  

$ pip install -r requirements.txt

  

```

  

**:three:** How to use:

```c

$ python main.py -h

usage: main.py [-h] [-p PCAP] [-d FILE_DIR] [-k KEYWORD]

optional arguments:
  -h, --help            show this help message and exit
  -p PCAP, --pcap PCAP  path to file pcap
  -d FILE_DIR, --file_dir FILE_DIR
                        Save extracted file to folder
  -k KEYWORD, --keyword KEYWORD
                        Keyword!

```
```c
EX: python main.py -p $HOME/Data_loss_prevention/Pcap/Raw.pcap -d $HOME/Data_loss_prevention/Data -k "Mapping"
```

  
  

**:notebook:** The tool is compatible with English and utf-8 documents

  

:weary:[by ErikHorus1249](https://github.com/ErikHorus1249)

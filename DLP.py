from utils.utils import *
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tool", help="Tool name: extract pcap - ep ; find text - ft")
    parser.add_argument("-p", "--pcap", help="Pcap file path")
    parser.add_argument("-pro", "--protocol", help="Protocol: http, ftp, ...")
    parser.add_argument("-d", "--file_dir", help="Save extracted file to folder")
    parser.add_argument("-k", "--keyword", help="Keyword!")
    
    args = parser.parse_args()

    if args.tool == "ep":
        ExtracPDF.is_tool()
        ExtracPDF.extract(pcap_path=args.pcap, dir=args.file_dir, protocol=args.protocol)
    elif args.tool == "ft":
        print(FindKeyWd(args.file_dir, args.keyword).lookup())
    else:
        pass 
    
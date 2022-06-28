from utils.utils import *
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    # parser.add_argument("-t", "--tool", help="Tool name: extract pcap - ep ; find text - ft")
    parser.add_argument("-p", "--pcap", help="path to file pcap")
    # parser.add_argument("--protocol", help="Protocol: http, ftp, ...")
    parser.add_argument("-d", "--file_dir", help="Save extracted file to folder")
    parser.add_argument("-k", "--keyword", help="Keyword!")
    
    args = parser.parse_args()

    # if args.tool == "dlp":
    ExtracPDF.is_tool()
    if pdf_path := ExtracPDF.extract(pcap_path=args.pcap, dir=args.file_dir, protocol="http"):
        FindKeyWd(pdf_path, args.keyword).lookup_bord()
    
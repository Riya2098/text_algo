import os
import re
import sys
import argparse

class Text_search:
    
    def __init__(self, string2, path1, i=None):
        self.path1=path1
        self.string1=string2
        self.i=i
        if self.i:
            string2=string2.lower()
            self.string2=re.compile(string2)
            
    # Will return the file's name in which string is found!   
    def text_search(self):
        file_number=0;
        files=[f for f in os.listdir(self.path1) if os.path.isfile(self.path1+"/Users/riyaverma/Desktop/intDataset"+f)]
        for file in files:
            file_t=open(self.path1+"/Users/riyaverma/Desktop/intDataset"+file)
            file_text=file_t.read()
            if self.i:
                file_text=file_text.lower()
                file_t.close()
            if re.search(self.string2,file_text):
                print("the text "+self.string1+" found in ",file)
                file_number+=1
            print("Total files are: ",file_number)
                
    
    # It will eventually return the file name and line number in which given string is matched
    def text_search_line(self):
        files=[f for f in os.listdir(self.path1)if os.path.isfile(self.path1+"/Users/riyaverma/Desktop/intDataset"+f)]
        file_number=0
        for file in files:
            file_t=open(self.path1+"/Users/riyaverma/Desktop/intDataset"+file)
        line_number=1
        flag_file=0
        for line_1 in file_t:
            if self.i:
                line_1=line_1.lower()
            if re.search(self.string2, line_1):
                flag_file=1
                print("The text "+ self.string1+" found in ",file,"at line number",line_number)
                line_number+=1
            if flag_file==1:
                file_number+=1
                flag_file=0
                file_t.close()
            print("Total Files are: ",file_number)
                

def main():
    parser=argparse.ArgumentParser(version='1.0')
    parser.add_argument('-m' )     #works for the text_search_Line
    parser.add_argument('-s' )     #works for text_search

    args=parser.parse_args()
    
    if args.m:                  
        dir = args.m[1]
        obj1 = Text_search(args.m[0],dir)
        obj1.text_search_line()
        
    elif args.s:                 
        dir = args.s[1]
        obj1 = Text_search(args.s[0],dir)
        obj1.text_search()
        
        
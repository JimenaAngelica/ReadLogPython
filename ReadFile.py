# coding=utf-8
#!/usr/bin/python
import re

def GetSeekCodes():
    print "Getting seekcodes"
    p = re.compile(ur'\[EP]\[\d+-\d+]\[\d]\[(\w+)]')
    line = ReadLineFile()
    return re.findall(p, line)

def ReadLineFile():
    print "Reading the file"
    with open('31122015.log') as f:
        lines = f.read()
        return lines

def main():
    print "HolaMundo!"
    print "Exito!"
    #lista = GetSeekCodes()
    #print len(lista)
    #Test()

if __name__ == "__main__": main()

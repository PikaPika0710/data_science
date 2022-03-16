#!/usr/bin/env python
"""
This a an example module.
"""
import sys, os

__PUNCTUATION__ = ".,?!"

def introduce(family = "Pham", first = "Minh Tuan"): 
    """
    This a an example function.
    """
    print("Ho va ten: " + family + " "+ first)

def main():
    """
    Main function
    """
        
    #===== process command-line arguments =====#
    strUsage = 'Usage: module1.py     path_to_text_file'
    if len(sys.argv) != 2:
        sys.exit(strUsage)   
    filePath = sys.argv[1]        
    try:
        with open(filePath) as f:
            lines = f.readlines()
    except IOError:
        sys.exit('ERROR: Failed to load input file ' + filePath)
    
    freqDict = {}
    for line in lines:
        words = line.split()
        for word in words:
            if word[-1] in __PUNCTUATION__:
                word = word[:-1]
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
    print("File co tat ca %d tu" % len(freqDict))
    print("Bang tan suat xuat hien cac tu:")
    print(freqDict)
    print('Done!')

 
#===== This module is to be run as the top-level script =====
if __name__ == "__main__":
    main()
    

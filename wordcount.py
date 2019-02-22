# -*- coding: utf-8 -*-

import re
from collections import Counter

def word_count(filename):

    
    with open(filename, 'r') as f:
        word = Counter(f.read().split())
        tup=word.items()
    
   
    for k,v in tup:
        print k,v
        
        
        
    

   
   
    


if __name__ == "__main__":
    filename = "sample.txt"
    print word_count(filename)

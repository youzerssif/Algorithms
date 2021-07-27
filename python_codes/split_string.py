

def solution(word):
    
    liste = []
    if len(word) % 2 != 0:
        word += "_"
    for i in range(0, len(word), 2):
        liste.append(word[i : i+2])
        
    
    return liste

"""
import re

def solution(s):
    return re.findall(".{2}", s + "_")
"""


print(solution("bonjour"))
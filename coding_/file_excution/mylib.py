from collections import Counter
import re


def Count_the_number_of_words_in_a_sentence(path):
    with open(path,encoding='utf8') as f:
        data = f.read()
    return re.findall(r'\w[^.?!:][.?!:]',data).__len__()
    
def Count_the_number_of_words_in_the_file(path):
    with open(path,encoding='utf8') as f:
        data = f.read()
    return re.findall(r'[a-zA-Z]+',data).__len__()

def occurrence_frequency_from_file(path):
    with open(path,encoding='utf8') as f:
        data = f.read()
    return Counter(re.findall(r'[a-zA-Z]+',data))

def one_occurence_from_file(path):
    with open(path,encoding='utf8') as f:
        data = f.read()
    return [x[0] for x in Counter(re.findall(r'[a-zA-Z]+',data)).items() if x[1]==1]



import sys

from mylib import Count_the_number_of_words_in_a_sentence,Count_the_number_of_words_in_the_file,occurrence_frequency_from_file,one_occurence_from_file

def main():
    strUsage = 'Usage: tool.py   path_to_text_file'
    if len(sys.argv) != 2:
        sys.exit(strUsage)   
    path = sys.argv[1] 
    try:
        print(f"Number of centences: {Count_the_number_of_words_in_a_sentence(path)}")
        print("========================================================")
        print(f"Number of words: {Count_the_number_of_words_in_the_file(path)}")
        print("========================================================")
        print(f"Word count: {occurrence_frequency_from_file(path)}")
        print("========================================================")
        print(f"One occerence: {one_occurence_from_file(path)} ")
    except:
        pass

if __name__ == '__main__':
    main()
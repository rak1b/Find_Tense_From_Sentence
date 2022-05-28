import nltk
from downloader import download

'''*********************************************************
* Important:                                               *
* run the  below download() function once then comment it  *           
*********************************************************'''
# download()

helping_verbs = {
    'Present': ['do', 'does', 'is', 'are', 'am'],
    'Past': ['did', 'was', 'were'],
    'Future': ['shall', 'will']
}
main_verb_pos = {
    'Past': ['VBD', 'VBN', 'VB'],
    'Present': ['VBG', 'VBP', 'VBZ']
}


def Find_Tense_Helping_Verb(text):
    result = {'Not Found': 0, 'Future': 0, 'Present': 0, 'Past': 0}
    for word in text:
        for key, val in helping_verbs.items():
            if word in val:
                result[key] += 1
    return max(result, key=result.get)


def Find_Tense_Main_Verb(text):
    result = {'Not Found': 0, 'Future': 0, 'Present': 0, 'Past': 0}

    res = nltk.pos_tag(text)
    res = dict(res)
    for key, val in res.items():
        for tense in main_verb_pos:
            if val in main_verb_pos[tense]:
                result[tense] += 1
    return max(result, key=result.get)


text = input("Enter Sentence:\n")
text = nltk.word_tokenize(text)


result = Find_Tense_Helping_Verb(text)
if(result == "Not Found"):
    result = Find_Tense_Main_Verb(text)

if(result == "Not Found"):
    print("Error!There might be some problem with this sentence,Try again..")
else:
    print(f"This sentence is written in {result} tense")


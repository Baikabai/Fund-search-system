import os
from tqdm import tqdm

class MasterwordAndTestword():
    def MAT_single(masterword,wordlist):
        path = 'D:/text mining/code_name/'
        name_list = os.listdir(path)
        masterlist = []
        testdict = {}
        masterword = ''.join(masterword)
        for name in tqdm(name_list):
            f = open(path+name,'r',encoding='utf-8')
            text = f.read()
            text1 = text.split(" ")
            f.close()
            if masterword in text1:  
                masterlist.append(name)
            for testword in wordlist:
                if testword in text1:
                    if testword in testdict:
                        testdict[testword].append(name)
                    else:
                        testdict[testword] = [name]
        return masterlist,testdict
    
    def MAT_or(masterword,wordlist):
        path = 'D:/text mining/code_name/'
        name_list = os.listdir(path)
        masterlist = []
        testdict = {}
        for name in tqdm(name_list):
            f = open(path+name,'r',encoding='utf-8')
            text = f.read()
            text1 = text.split(" ")
            f.close()
            for single_word in masterword:
                if single_word in text1:
                    masterlist.append(name)
            for testword in wordlist:
                if testword in text1:
                    if testword in testdict:
                        testdict[testword].append(name)
                    else:
                        testdict[testword] = [name]
        return masterlist,testdict
    
    def MAT_and(masterword,wordlist):
        path = 'D:/text mining/code_name/'
        name_list = os.listdir(path)
        masterlist = []
        testdict = {}
        for name in tqdm(name_list):
            f = open(path+name,'r',encoding='utf-8')
            text = f.read()
            text1 = text.split(" ")
            f.close()
            count = 0
            for single_word in masterword:
                if single_word in text1:
                    count +=1
            if count==len(masterword):
                masterlist.append(name)
            for testword in wordlist:
                if testword in text1:
                    if testword in testdict:
                        testdict[testword].append(name)
                    else:
                        testdict[testword] = [name]
        return masterlist,testdict
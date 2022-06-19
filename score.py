import math
import collections
import os
from tqdm import tqdm
import re
class Score():
    def Idf():
        allwords = []
        idf = {}
        path = 'D:/text mining/code_name/'
        file_list = os.listdir(path)
        for i in file_list:
            f = open(path+i,'r',encoding='utf-8')
            text = f.read()
            text1 = text.split(' ')
            for j in text1:
                j = j.replace('\n','')
                allwords.append(j)
        di = dict(collections.Counter(allwords))
        sum1 = sum(di.values())
        for word in di:
            idf[word] = math.log(sum1/di[word])
        return idf
    def tf_idf(final_similarity_dict):
        idf = Score.Idf()
        path = 'D:/text mining/code_name/'
        final_score = {}
        name_list = os.listdir(path)
        word_list = final_similarity_dict.keys()
        for company in tqdm(name_list):
            sum1 = 0
            f = open(path+company,'r',encoding='utf-8').read()
            sum2 = 0
            words = f.split(' ')
            words_process = []
            for i in words:
                if '\n' in i:
                    i= i.replace('\n','')
                    words_process.append(i)
                else:
                    words_process.append(i)
            di = {}
            di = dict(collections.Counter(words_process))
            sum1 = sum(di.values())
            for word in word_list:
                if word in di.keys():
                    sum2 += di[word]/sum1*float(final_similarity_dict[word])*idf[word]*1000
                if sum2 != 0:
                    company1 = re.sub('.txt','',company)
                    final_score[company1]=sum2
        return final_score
    def cs(final_similarity_dict):
        path = 'D:/text mining/code_name/'
        final_score = {}
        name_list = os.listdir(path)
        word_list = final_similarity_dict.keys()
        for company in tqdm(name_list):
            f = open(path+company,'r',encoding='utf-8').read()
            sum = 0
            words = f.split(' ')
            words_process = []
            for i in words:
                if '\n' in i:
                    i= i.replace('\n','')
                    words_process.append(i)
                else:
                    words_process.append(i)
            dict = collections.Counter(words_process)
            for word in word_list:
                if word in dict.keys():
                    sum += float(dict[word])*float(final_similarity_dict[word])
                if sum != 0:
                    company1 = re.sub('.txt','',company)
                    final_score[company1]=sum
        return final_score
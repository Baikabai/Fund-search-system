import itertools
from tqdm import tqdm
import tools as t
import re
import theme_and_test as tt
import SimilarityB
import finalsimilarity
import score
import pandas as pd
if __name__ == '__main__':
    voctor_sizes = [100,200,300,400,500]
    windows = [10,15,20]
    parameters = list(itertools.product(voctor_sizes, windows))
    for i,(vector_size, window) in tqdm(enumerate(parameters)):
        exec("modelword2vec{} = gensim.models.Word2Vec.load('D:/text mining/model/wiki/word2vec_'+str({})+'_'+str({})+'_model')".format(i+1,window,vector_size))
        exec("modelfasttext{} = gensim.models.FastText.load('D:/text mining/model/wiki/fasttext_'+str({})+'_'+str({})+'.model')".format(i+1,window,vector_size))
        exec("modelglove{} = KeyedVectors.load_word2vec_format('D:/text mining/model/wiki/glove_'+str({})+'_'+str({})+'.txt')".format(i+1,window,vector_size))
    masterword = input('検索したいワードを入力してください\n')
    masterword = re.sub('　',' ',masterword)
    masterword = masterword.split(' ')

    #similarityA
    model_sum = 15
    topn =3000
    dictA = {}
    similarityA = {}
    for number in range(1,16):
        exec("textword2vec = modelword2vec{}.wv.most_similar(positive=masterword, topn=topn)".format(number))
        for word,sim in textword2vec:
            if word in dictA:
                dictA[word].append(sim)
            else:
                dictA[word] = [sim]
        exec("textfast = modelfasttext{}.wv.most_similar(positive=masterword, topn=topn)".format(number))
        for word,sim in textfast:
            if word in dictA:
                dictA[word].append(sim)
            else:
                dictA[word] = [sim]
        exec("textglove = modelglove{}.most_similar(positive=masterword, topn=topn)".format(number))
        for word,sim in textglove:
            if word in dictA:
                dictA[word].append(sim)
            else:
                dictA[word] = [sim]
    sub_dic = dictA.copy()
    for d in sub_dic:
        if len(dictA[d]) < model_sum:
            del dictA[d]
    for word in dictA:
        similarityA[word] = sum(dictA[word])/model_sum
    similarityA1 = t.Tools.top_n_scores(500,similarityA)
    similarityA = t.Tools.listtodict(similarityA1)
    
    masterlist,testdict = tt.MasterwordAndTestword.MAT_single(masterword,similarityA)
    similarityB,numbers = SimilarityB.B_calculate(masterlist,testdict)
    final_similarity_list,similarity_dict = finalsimilarity.FS(similarityA,similarityB,numbers)
    new_dict = t.Tools.listtodict(final_similarity_list)
    final_score_idf = score.Score.tf_idf(new_dict)
    final_score_cs = score(new_dict)
    df = pd.read_excel('111.xlsx')
    all_code =df["証券コード"]
    all_code=list(set(all_code))
    code_list=[]
    for i in range(len(df)):
        a =(df.iloc[i])
        if a["テーマ番号"]==1:
            code_list.append(a["証券コード"])
    code_list = list(set(code_list))
    results_idf = sorted(final_score_idf.items(), key=lambda x: x[1])
    results_idf.reverse()
    results_cs = sorted(final_score_cs.items(), key=lambda x: x[1])
    results_cs.reverse()
    
    companyidf = []
    for i in range(len(results_idf)):
        companyidf.append(int(results_idf[i][0]))
        if len(companyidf)>=len(code_list):
            break
    
    #true
    truelist = set(code_list)&set(companyidf)
    print(len(truelist))
    
    #false
    len(code_list)-len(truelist)
    code_list = list(set(code_list))
    asum  = []
    for i in range(len(results_idf)):
        asum.append(results_idf[i][1])
    avg = sum(asum)/len(asum)
    if len(asum) % 2 == 0:

        first_median = asum[len(asum) // 2]

        second_median = asum[len(asum) // 2 - 1]

        median = (first_median + second_median) / 2

    else:

        median = asum[len(asum) // 2]
    company_find_list = []
    eeee = []
    # a = []
    # b = []
    for i in range(len(results_idf)):
        n1 = int(results_idf[i][0])
        if n1 in all_code:
            eeee.append(n1)
    for i in range(len(results_idf)):
            n1 = int(results_idf[i][0])
            if n1 in all_code:
                company_find_list.append(n1)
    #             a.append(n1)
    #             b.append(results[i][1])
    print(len(company_find_list))
    # df1 = pd.DataFrame()
    # df1['companyname'] = a
    # df1['score'] = b
    # df1.to_csv('cs.csv',encoding='utf-8-sig')
    e = code_list+company_find_list
    e = list(set(e))
    print(len(company_find_list))
    TP = []
    FP = []
    FN = []
    TN = []

    for i in range(len(company_find_list)):
        if company_find_list[i] in code_list:
            TP.append(company_find_list[i])
        else :
            FP.append(company_find_list[i])
    for i in range(len(code_list)):
        if code_list[i] not in company_find_list:
            FN.append(code_list[i])
    for i in range(len(all_code)):
        if all_code[i] not in e:
            TN.append(all_code[i])
    precision = len(TP)/(len(TP)+len(FP))
    recall = len(TP)/(len(TP)+len(FN))
    f2_score = (5*precision*recall)/(4*precision+recall)
    f1_score = 2/(1/precision+1/recall)
    # accuracy = (len(TP)+len(TN))/len(all_code)
    print(precision,recall,f1_score,f2_score)
    print(len(TP),len(FP),len(FN),len(TN))
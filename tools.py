import pandas as pd

class Tools():
    def top_n_scores(n, score_dict):
        lot = [(k,v) for k, v in score_dict.items()] #make list of tuple from scores dict
        nl = []
        while len(lot)> 0:
            nl.append(max(lot, key=lambda x: x[1]))
            lot.remove(nl[-1])
        return nl[0:n]
    
    def listtodict(finallist):
        dict = {}
        for word in finallist:
            dict[word[0]] = word[1]
        return dict
    

    def df_tocsv(dict,filename):
        df = pd.DataFrame()
        df['words'] = dict.keys()
        df[filename]= dict.values()
        df.to_csv(filename+'.csv',encoding='utf-8-sig')
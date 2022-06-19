

def B_calculate(masterwordlist,testworddict):
    testdict = {}
    combine_dict = {}
    numbers = 0
    for testwordlist in testworddict.keys():
        combine = set(masterwordlist) & set(testworddict[testwordlist])
        cobine_list = list(combine)
        if testwordlist in combine_dict:
            combine_dict[testwordlist].append(cobine_list)
        else:
            combine_dict[testwordlist] = cobine_list
        similarityB = float(len(combine))/float(len(testworddict[testwordlist]))
        if similarityB != 0.0:
            if testwordlist in testdict:
                testdict[testwordlist].append(similarityB)
            else:
                testdict[testwordlist] = similarityB
        sub_dict = combine_dict.copy()
        for combine_name in sub_dict.keys():
            if combine_name not in testdict.keys():
                del combine_dict[combine_name]
    for i in testdict:
        if testdict[i]!=0:
            numbers+=1
    return testdict,numbers
import tools as t
def FS(similarityA_dict,similarityB_dict,numbers):
    sub_dict = similarityA_dict.copy()
    similarity_dict = {}
    for cz in sub_dict.keys():
        if cz not in similarityB_dict.keys():
            del similarityA_dict[cz]
    for name in similarityA_dict.keys():
        if name in similarityB_dict.keys():
            similarity = (similarityA_dict[name]+similarityB_dict[name])/2
            similarity_dict[name] = similarity
        else:
            pass
    final_list = t.Tools.top_n_scores(int(numbers/2),similarity_dict)
    return final_list,similarity_dict
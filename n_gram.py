def __n_grams(word):
    N = 3   #setting N to 3
    return [word[i:i+N] for i in range(0, len(word)-N+1)]

def get_n_grams(text):
    res = {}
    for word in text.split():
        for n_gram in __n_grams(word):
            res[n_gram] = text.count(n_gram)
    
    return res

def get_n_grams_in_file(file, n_grams_dict):
    res = {}
    with open(file) as f:
        for line in f:
            for n_gram in __n_grams(line):
                res[n_gram] = res.get(n_gram, 0) + 1
    
    return res
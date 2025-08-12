def naive_search(text,pattern): 
    position = []
    for i in range(len(text) - len(pattern) + 1):
        position.append(i)
        return position
    
def compute_lps(pattren):
    lps = [0]*len(pattren)
    length  = 0 
    i = 1

    while i < len(pattren):
        if pattren[i] == pattren[length]:
            length += 1
            i  += 1

    return lps                  

def kpm_search(text,pattren):
    lps = compute_lps(pattren)
    position = []

    i = j = 0
    while i < len(text):
        if pattren[j] == text[i]:
            i += 1
            j += 1

    if j == len(pattren):
        position.append(i-j)
        j = lps[j-1]
    elif i < len(text) and pattren[j] != text[i]:

        if j != 0:
            j = lps[j -1]
        else:
            i += 1    
    return position        

text = "abababababababa"
pattren ="ababad"

print("Navi match at positions:", naive_search(text,pattren))
print("KPM Match at positions:", kpm_search(text,pattren))


minsup = 0.3
minconf = 0.8 
def count_first(transactions):
    adict = {}
    for t in transactions:
        for item in t:
            if item in adict:
                adict[item] += 1
            else:
                adict[item] = 1
    return adict 
def find_frequent(Candidate, minsup, no_of_lines):
    adict={}
    for key in Candidate:
        if ((float)(Candidate[key]/no_of_lines)) >= minsup:
            adict[key] = Candidate[key]   
    return adict 
def candidate_gen(keys):
    adict={}
    for i in keys:
        for j in keys:
            if i != j and (j,i) not in adict:
                adict[tuple([min(i,j),max(i,j)])] = 0
    return adict 
def add_frequency(Candidate, transactions):
    for key in Candidate:
        for t in transactions:
            if key[0] in t and key[1] in t:
                Candidate[key] += 1
    return Candidate 
f = open("facebook_combined.txt","r")
transactions = []
no_of_lines=0 
for line in f:
    split_line = line.split()
    transactions.append(split_line)
    no_of_lines = no_of_lines + 1 
print(no_of_lines) 
with open("words_alpha.txt") as f:
    words = f.read().splitlines()

from collections import Counter, defaultdict

cc = Counter()

for word in words:
    for c in word:
        cc[c] += 1

print(cc)

#print(words[0])
print(len(words), "words")

numchars = len(cc)
print(numchars, "chars")

ccc = defaultdict(list)

for word in words:
    ccc[tuple(sorted(list(set(word))))].append(word)

# Word with most distinct characters
#cccs = sorted(ccc.items(), key=lambda item:len(item[0]), reverse=True)
#print(cccs[0])

from itertools import combinations

#print("".join(possible))

from random import choice


#for letter in sorted(cc.keys()):

#print("FINDING", letter)

possible = set(cc.keys())

while len(possible) > 1:
    for a in ccc.keys():
        intersection = set(possible).intersection(set(a))
        if len(intersection) == 0:
            continue
        ywlen = len(set(possible))
        if (ywlen % 2 == 0 and len(intersection) == ywlen//2) or (ywlen % 2 == 1 and len(intersection) in [ywlen//2-1, ywlen//2+1]):
            #print("newq", a, len(a), ccc[a])
            question = choice(ccc[a])
            break

    print(possible, question, "?")
    #if letter in question:
    if input().lower() in "y yes".split():
        possible = possible.intersection(set(question))
    else:
        possible = possible.difference(question)

    print(possible)

import fileinput

lines = [line.strip() for line in fileinput.input()]

m = []

for line in lines:
    for i,c in  enumerate(line):
        if (i >= len(m)):
            m.append([])
        m[i].append(c)

new_word = []
new_word2 = []

for word in m:
    letters = set(word)
    max_c = 0
    min_c = 99999
    w = ''
    w2 = ''
    for l in letters:
        c = word.count(l)
        if c > max_c:
            max_c = c
            w = l
        if c < min_c:
            min_c = c
            w2 = l
    new_word.append(w)
    new_word2.append(w2)


print("".join(new_word), "".join(new_word2))

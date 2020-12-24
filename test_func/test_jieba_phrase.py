import jieba.posseg as psg
import test_func.cut_sentences as cut


file_path = "../test_data/resource.txt"


with open(file_path, "r", encoding='utf-8') as f:
    texts = f.read()
    texts = cut._cut(sentence=texts)

word_bounds = ['M' for item in texts for x in item]
word_flags = []
start = 0
end = 0

for text in texts:
    for word, flag in psg.cut(text):
        if len(word) == 1:
            start = len(word_flags)
            word_bounds[start] = 'S'
            word_flags.append(flag)
        else:
            start = len(word_flags)
            word_bounds[start] = 'B'
            word_flags+=[flag]*len(word)
            end = len(word_flags) - 1
            word_bounds[end] = 'E'

bounds = []
flags = []
start = 0
end = 0
for s in texts:
    l = len(s)
    end += l
    bounds.append(word_bounds[start:end])
    flags.append(word_flags[start:end])
    start += l
data = {}
data['bounds'] = bounds
data['flags'] = flags
print(len(data.values()))
for i in range(len(data.values())):
    records = list(zip(*[v[i] for v in data.values()]))
    print(records)

for v in data.values():
    print(v[0])


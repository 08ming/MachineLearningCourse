from collections import Counter

words = ['a','a','a','b','c','c']
count = Counter(words)
words = sorted(count.items(), key=lambda x:x[1], reverse=False)
words = [x[0] for x in words if x[1] > 1]
print(words)
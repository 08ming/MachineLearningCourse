def _cut(sentence):
    """
    将一段文本切分成多个句子
    :param sentence:
    :return:
    """
    new_sentence = []
    sen = []
    stop_words = set('.。；;?？》《')
    index = 0
    for i in sentence:
        if i in ['。', '！', '？', '?'] and len(sen) != 0:
            sen.append(i)
            new_sentence.append("".join(sen))
            sen = []
            continue
        sen.append(i)
        index += 1

    if len(new_sentence) <= 1: # 一句话超过max_seq_length且没有句号的，用","分割，再长的不考虑了。
        new_sentence = []
        sen = []
        for i in sentence:
            if i.split(' ')[0] in ['，', ','] and len(sen) != 0:
                sen.append(i)
                new_sentence.append("".join(sen))
                sen = []
                continue
            sen.append(i)
    if len(sen) > 0:  # 若最后一句话无结尾标点，则加入这句话
        new_sentence.append("".join(sen))
    return new_sentence
if __name__ == '__main__':
    with open("../data/train/data/14.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            res = _cut(sentence=line)
            print(res)
    # stop_words = set('.。；;?？》《')
    # print('?' in stop_words)
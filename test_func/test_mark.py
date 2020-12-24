import pandas as pd


lable_file = "../data/train/label/0.csv"
df = pd.read_csv(lable_file, sep=",",encoding="utf-8")
q_dic = dict()
for index, row in df.iterrows():
    print(row)
    cls = row[1]
    start_index = row[2]
    end_index = row[3]
    length = end_index - start_index+1
    for r in range(length):
        if r == 0:
            q_dic[start_index] = ("B-%s" % cls)
        else:
            q_dic[start_index + r] = ("I-%s" % cls)
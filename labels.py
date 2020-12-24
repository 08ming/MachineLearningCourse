import glob
label_file_list = glob.glob('label/*.csv') 
import pandas as pd
labels = dict()
for label_file in label_file_list:
    df = pd.read_csv(label_file, sep=",",encoding="utf-8")
    count_df = df['Category'].value_counts()
    for label in list(count_df.index):
        if labels.get(label) is None:
            labels[label] = count_df[label]
        else:
            labels[label] += count_df[label]
labels

labels
print(1)

q_dic=dict()
for index, row in df.iterrows():
    cls = row[1]
    start_index = row[2]
    end_index = row[3]
    length = end_index - start_index+1
    for r in range(length):
        if r == 0:
            q_dic[start_index] = ("B-%s" % cls)
        else:
            q_dic[start_index + r] = ("I-%s" % cls)
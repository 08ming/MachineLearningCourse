import codecs
from bert4keras.backend import keras, K
from tqdm import tqdm

from Main import cut_test_set, NamedEntityRecognizer, CRF

maxlen = 512
def test_predict(data, NER_):
    test_ner =[]
    for text in tqdm(data):
        cut_text_list, cut_index_list = cut_test_set([text],maxlen)
        posit = 0
        item_ner = []
        index =1
        for str_ in cut_text_list:
            ner_res  = NER_.recognize(str_)
            for tn in ner_res:
                ans = {}
                ans["label_type"] = tn[1]
                ans['overlap'] = "T" + str(index)
                ans["start_pos"] = text.find(tn[0],posit)
                ans["end_pos"] = ans["start_pos"] + len(tn[0])-1
                posit = ans["end_pos"]
                ans["res"] = tn[0]
                item_ner.append(ans)
                index +=1
        test_ner.append(item_ner)
    return test_ner
test_files = os.listdir("./data/test")
ids = []
starts = []
ends = []
labels=[]
ress = []
NER = NamedEntityRecognizer(trans=K.eval(CRF.trans), starts=[0], ends=[0])
for file in test_files:
    if not file.endswith(".txt"):
        continue
    id_ = file.split('.')[0]
    with codecs.open("./data/test/"+file, "r", encoding="utf-8") as f:
        line = f.readlines()
        aa = test_predict(line, NER)
        for line in aa[0]:
            ids.append(id_)
            labels.append(line['label_type'])
            starts.append(line['start_pos'])
            ends.append(line['end_pos'])
            ress.append(line['res'])

df=pd.DataFrame({"ID":ids, "Category":labels,"Pos_b":starts,"Pos_e":ends,"Privacy":ress})
df.to_csv("predict.csv", encoding="utf-8-sig", sep=',',index=False)
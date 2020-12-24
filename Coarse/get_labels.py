import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


test_dir='data/train/label'


def get_entities(dir):
    entities = {}
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        with open(path, encoding='utf-8', mode='r') as f:
            for line in f.readlines()[1:]:
                name = line.split(',')[1]
                if name in entities:
                    entities[name] += 1
                else:
                    entities[name] = 1
    return entities


if __name__ == '__main__':
    entities = get_entities(test_dir)
    index = [k for k in entities.keys()]
    values = [v for v in entities.values()]
    plt.barh(index, values)
    plt.show()
    # res = pd.read_csv('data/train/label/1.csv')
    # print(res['ID'])
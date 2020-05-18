
import keras
import pandas as pd

# 开始加载情感词典
from sklearn.metrics import accuracy_score

negdict = []  # 消极情感词典
posdict = []  # 积极情感词典
nodict = []  # 否定词词典
plusdict = []  # 程度副词词典
sl = open('../0_dataset/dictionary1/负面情绪词.txt', encoding='utf-8')
for i in sl:
    negdict.append(i.strip())
sl = open('../0_dataset/dictionary1/正面情绪词.txt', encoding='utf-8')
for i in sl:
    posdict.append(i.strip())
sl = open('../0_dataset/dictionary1/否定词.txt', encoding='utf-8')
for i in sl:
    posdict.append(i.strip())
sl = open('../0_dataset/dictionary1/程度副词.txt', encoding='utf-8')
for i in sl:
    posdict.append(i.strip())


# 加载情感词典结束

# 预测函数
def predict(s, negdict, posdict, nodict, plusdict):
    p = 0
    sd = keras.preprocessing.text.text_to_word_sequence(s)
    for i in range(len(sd)):
        if sd[i] in negdict:
            if i > 0 and sd[i - 1] in nodict:
                p = p + 1
            elif i > 0 and sd[i - 1] in plusdict:
                p = p - 2
            else:
                p = p - 1
        elif sd[i] in posdict:
            if i > 0 and sd[i - 1] in nodict:
                p = p - 1
            elif i > 0 and sd[i - 1] in plusdict:
                p = p + 2
            elif i > 0 and sd[i - 1] in negdict:
                p = p - 1
            elif i < len(sd) - 1 and sd[i + 1] in negdict:
                p = p - 1
            else:
                p = p + 1
        elif sd[i] in nodict:
            p = p - 0.5
    return p


# 预测函数结束
res1 = predict("It is boring ", negdict, posdict, nodict, plusdict)
res2 = predict("I am sad", negdict, posdict, nodict, plusdict)
res3 = predict("It is really boring", negdict, posdict, nodict, plusdict)
print(res1, res2, res3)

df_test = pd.read_csv('../0_dataset/orign/test_imdb.tsv',
                      usecols=['tag', 'sen'], sep='\t')

test_tag_list = []
predict_tag_list = []
for i in df_test["tag"]:
    test_tag_list.append(int(i))
for i in df_test["sen"]:
    # res = sentAnal.analyse(i)
    res = predict(i, negdict, posdict, nodict, plusdict)
    if res > 0:
        predict_tag_list.append(1)
    else:
        predict_tag_list.append(0)
print('Testing accuracy %s' % accuracy_score(test_tag_list, predict_tag_list))

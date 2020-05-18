# -*- coding: utf-8 -*-
# @File  : get_cache_demo.py
# @Author: redtree
# @Date  : 18-6-27
# @Desc  : 这是一个将特定文本数据预加载到缓存列表的demo,AllList 将作为全局缓存对象供工程内部的任意模块调用
import pandas as pd
from sklearn.metrics import accuracy_score


class AllList():  # 存储所有列表信息的对象
    # 中文情感词库
    positive_words_eng = []  # 正螚量词
    negative_words_eng = []  # 负能量词
    level1_words_eng = []  # 程度1
    level2_words_eng = []  # 程度2
    level3_words_eng = []  # 程度3
    level4_words_eng = []  # 程度4
    level5_words_eng = []  # 程度5
    level6_words_eng = []  # 程度6
    fouding_words_eng = []  # 否定词
    # 英文
    positive_words_cn = []  # 正螚量词
    negative_words_cn = []  # 负能量词
    level1_words_cn = []  # 程度1
    level2_words_cn = []  # 程度2
    level3_words_cn = []  # 程度3
    level4_words_cn = []  # 程度4
    level5_words_cn = []  # 程度5
    level6_words_cn = []  # 程度6
    fouding_words_cn = []  # 否定词


def getAllList():  # 提取所有规则列表（后期要改为多线程提取）

    allList = AllList()

    # 情感分析(英文)
    file = open("../imdb_difficult/emotion_dict/eng/pos.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.positive_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/neg.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.negative_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level1.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level1_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level2.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level2_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level3.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level3_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level4.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level4_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level5.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level5_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/level6.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level6_words_eng.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/eng/fouding.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.fouding_words_eng.append(checkTr)

        # 情感分析(中文)
    file = open("../imdb_difficult/emotion_dict/cn/pos.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.positive_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/neg.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.negative_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level1.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level1_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level2.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level2_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level3.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level3_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level4.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level4_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level5.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level5_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/level6.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level6_words_cn.append(checkTr)

    file = open("../imdb_difficult/emotion_dict/cn/fouding.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.fouding_words_cn.append(checkTr)

    return allList


import nltk
import random

all_list= getAllList()
# 文本情感分析算法
def cutSentence(input):  # 结巴分词
    res = nltk.word_tokenize(input)  # 默认是精确模式
    return res


def reduceFunc(reduceTimes):  # 适用于累加条件下的衰减法 （pos and neg）
    addY = (10 / reduceTimes) / 10
    return addY  # 衰减后当此追加的情感值


def levelReduceFunc(levelReduceTimes, level, type):  # 适用于区间叠乘条件下的衰减法 （level）
    if level == 6:
        levela = 2  # 区间下限
        levelb = 2.5  # 区间上限
        levelER = 0.67  # 衰减系数

    if level == 5:
        levela = 1.6  # 区间下限
        levelb = 1.9  # 区间上限
        levelER = 0.67  # 衰减系数

    if level == 4:
        levela = 1.2  # 区间下限
        levelb = 1.6  # 区间上限
        levelER = 0.67  # 衰减系数

    if level == 3:
        levela = 0.6  # 区间下限
        levelb = 0.9  # 区间上限
        levelER = 1.23  # 衰减系数

    if level == 2:
        levela = 0.4  # 区间下限
        levelb = 0.7  # 区间上限
        levelER = 1.23  # 衰减系数

    if level == 1:
        levela = 0.2  # 区间下限
        levelb = 0.5  # 区间上限
        levelER = 1.23  # 衰减系数

    if level >= 4:

        if type == 'topLimit':  # 上限衰减
            levelbCheck = levelb * (levelER ** (levelReduceTimes - 1))
            if levelbCheck <= 1.001:
                levelbCheck = 1.001
            return levelbCheck
        if type == 'lowerLimit':  # 下限衰减
            levelaCheck = levela * (levelER ** (levelReduceTimes - 1))
            if levelaCheck <= 1.000:
                levelaCheck = 1.000
            return levelaCheck

    if level <= 3:

        if type == 'topLimit':  # 上限衰减
            levelbCheck = levelb * (levelER ** (levelReduceTimes - 1))
            if levelbCheck >= 1.000:
                levelbCheck = 1.000
            return levelbCheck
        if type == 'lowerLimit':  # 下限衰减
            levelaCheck = levela * (levelER ** (levelReduceTimes - 1))
            if levelaCheck >= 0.998:
                levelaCheck = 0.998
            return levelaCheck


def checkMoodValue(segWord):  # 获取句子的情感能量值 mv =(posV*(functionE)+negV*(functionE))*isFouDing*chekLevel
    MoodValue = 0  # functionE 为待加算法，用于处理重复数据的量级衰减
    isFouDing = 1
    checkLevel = 1
    posreduceTimes = 1
    negreduceTimes = 1
    level6ReduceTimes = 1
    level5ReduceTimes = 1
    level4ReduceTimes = 1
    level3ReduceTimes = 1
    level2ReduceTimes = 1
    level1ReduceTimes = 1
    # 正能量词Check
    cutSentence_list = cutSentence(str(segWord))
    for onePos in all_list.positive_words_eng:
        if str(onePos).__contains__(' '):
            if str(onePos) in str(segWord):
                MoodValue = MoodValue + reduceFunc(posreduceTimes)
                posreduceTimes = posreduceTimes + 1
                break
        else:
            if str(onePos) in cutSentence_list:
                MoodValue = MoodValue + reduceFunc(posreduceTimes)
                posreduceTimes = posreduceTimes + 1
                break

    # 负能量词Check
    for oneNeg in all_list.negative_words_eng:
        if str(oneNeg).__contains__(' '):
            if str(oneNeg) in str(segWord):
                MoodValue = MoodValue - reduceFunc(negreduceTimes)
                negreduceTimes = negreduceTimes + 1
                break
        else:
            if str(oneNeg) in cutSentence_list:
                MoodValue = MoodValue - reduceFunc(negreduceTimes)
                negreduceTimes = negreduceTimes + 1
                break
    # 否定词Check
    for fdword in all_list.fouding_words_eng:
        if str(fdword).__contains__(' '):
            if str(fdword) in str(segWord):
                isFouDing = isFouDing * (-1)
                break
        else:
            if str(fdword) in cutSentence_list:
                isFouDing = isFouDing * (-1)
                break
    # 程度级Check 矫正系数 er
    # level1 矫正系数(0.2~0.5)
    # level2 矫正系数(0.4~0.7)
    # level3 矫正系数(0.6~0.9)
    # level4 矫正系数(1.2~1.6)
    # level5 矫正系数(1.6~1.9)
    # level6 矫正系数(2.0~2.5)

    for oneLevel in all_list.level1_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level1ReduceTimes, 1, 'lowerLimit'),
                                    levelReduceFunc(level1ReduceTimes, 1, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level1ReduceTimes, 1, 'lowerLimit'),
                                    levelReduceFunc(level1ReduceTimes, 1, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level2_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level2ReduceTimes, 2, 'lowerLimit'),
                                    levelReduceFunc(level2ReduceTimes, 2, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level2ReduceTimes, 2, 'lowerLimit'),
                                    levelReduceFunc(level2ReduceTimes, 2, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level3_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level3ReduceTimes, 3, 'lowerLimit'),
                                    levelReduceFunc(level3ReduceTimes, 3, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level3ReduceTimes, 3, 'lowerLimit'),
                                    levelReduceFunc(level3ReduceTimes, 3, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level4_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level4ReduceTimes, 4, 'lowerLimit'),
                                    levelReduceFunc(level4ReduceTimes, 4, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level4ReduceTimes, 4, 'lowerLimit'),
                                    levelReduceFunc(level4ReduceTimes, 4, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level5_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level5ReduceTimes, 5, 'lowerLimit'),
                                    levelReduceFunc(level5ReduceTimes, 5, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level5ReduceTimes, 5, 'lowerLimit'),
                                    levelReduceFunc(level5ReduceTimes, 5, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level6_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level6ReduceTimes, 6, 'lowerLimit'),
                                    levelReduceFunc(level6ReduceTimes, 6, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence_list:
                er = random.uniform(levelReduceFunc(level6ReduceTimes, 6, 'lowerLimit'),
                                    levelReduceFunc(level6ReduceTimes, 6, 'topLimit'))
                checkLevel = checkLevel * er
                break

    MoodValue = MoodValue * isFouDing * checkLevel
    return MoodValue


def getMoodValue(text):
    try:
        text = str(text).replace('，', '，|')
        text = str(text).replace('。', '。|')
        text = str(text).replace(',', '，|')
        text = str(text).replace('.', '。|')
        text = str(text).replace('!', '!|')
        text = str(text).replace('！', '！|')
        text = str(text).replace('？', '？|')
        text = str(text).replace('?', '?|')
        tsp_list = text.split('|')
        all_mv = 0
        re_obj = []

        for tl in tsp_list:
            if not (tl == '' or tl == ' '):
                tmp_MoodValue = checkMoodValue(tl)
                all_mv = all_mv + tmp_MoodValue
                cobj = {'text': tl, 'value': round(tmp_MoodValue, 6)}
                re_obj.append(cobj)

        res = {'all_value': round(all_mv, 6), 'split': re_obj}
        return res
    except Exception as err:
        print('文本情感分析失败' + str(err))
        return 'error'


out_put = getMoodValue("it is boring")
print(out_put)

df_test = pd.read_csv('../../0_dataset/orign/test_imdb.tsv',
                      usecols=['tag', 'sen'], sep='\t')

test_tag_list = []
predict_tag_list = []
for i in df_test["tag"]:
    test_tag_list.append(int(i))
for i in df_test["sen"]:
    res = getMoodValue(i).get("all_value")
    print(res)
    if res > 0:
        predict_tag_list.append(1)
    else:
        predict_tag_list.append(0)
print('Testing accuracy %s' % accuracy_score(test_tag_list, predict_tag_list))
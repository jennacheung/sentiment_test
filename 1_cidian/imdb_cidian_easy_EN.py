import keras
import pandas as pd
from sklearn.metrics import accuracy_score


class DictBasedSentAnal:

    def __init__(self):
        self.__vocab_dir = "../0_dataset/aclImdb/imdb.vocab"
        self.__imdb_er_dir = "../0_dataset/aclImdb/imdbEr.txt"
        self.__sent_dict__ = self.__read_dict(self.__vocab_dir, self.__imdb_er_dir)

    def analyse(self, sentence):
        score = 0.00
        for words in keras.preprocessing.text.text_to_word_sequence(sentence):
            score += self.__sent_dict__.get(words, 0)
        return score

    @staticmethod
    def __read_dict(vocab_path, er_path):
        encoding = "utf-8"
        sent_dict = {}

        vocab_list = []
        er_list = []
        with open(vocab_path, encoding=encoding) as vocab_file:
            for line in vocab_file:
                vocab_list.append(line.strip())
        with open(er_path, encoding=encoding) as er_file:
            for line in er_file:
                er_list.append(line.strip())
        for index, i in enumerate(vocab_list):
            sent_dict[i] = float(er_list[index])
        return sent_dict


if __name__ == '__main__':
    sentAnal = DictBasedSentAnal()
    # test1 = sentAnal.analyse("this is a fine day!")
    # print(test1)
    # df_train = pd.read_csv('/Users/yuchk/PycharmProjects/IMDB/0_dataset/orign/train_imdb.tsv',
    #              usecols=['tag', 'sen'], sep='\t')
    df_test = pd.read_csv('../0_dataset/orign/test_imdb.tsv',
                          usecols=['tag', 'sen'], sep='\t')

    test_tag_list = []
    predict_tag_list = []
    for i in df_test["tag"]:
        test_tag_list.append(int(i))
    for i in df_test["sen"]:
        res = sentAnal.analyse(i)
        if res > 0:
            predict_tag_list.append(1)
        else:
            predict_tag_list.append(0)
    print('Testing accuracy %s' % accuracy_score(test_tag_list, predict_tag_list))

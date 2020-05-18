import nltk
import pandas as pd
from sklearn.metrics import accuracy_score

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
df_test = pd.read_csv('../0_dataset/orign/test_imdb.tsv',
                      usecols=['tag', 'sen'], sep='\t')

test_tag_list = []
predict_tag_list = []
for i in df_test["tag"]:
    test_tag_list.append(int(i))
for i in df_test["sen"]:
    res = sia.polarity_scores(i)
    score =float(res.get("compound"))
    if score > 0:
        predict_tag_list.append(1)
    else:
        predict_tag_list.append(0)
print('Testing accuracy %s' % accuracy_score(test_tag_list, predict_tag_list))

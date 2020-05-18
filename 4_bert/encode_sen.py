from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
import pandas as pd

from bert_serving.client import BertClient

file_path = '/Users/yuchk/PycharmProjects/IMDB/0_dataset/orign/train_imdb.tsv'
model_path = '/Users/yuchk/PycharmProjects/IMDB/0_dataset/bert_model'
res_file_path = '/Users/yuchk/PycharmProjects/IMDB/0_dataset/orign/encode_train_imdb.tsv'

args = get_args_parser().parse_args(
    ['-model_dir', model_path,
     '-port', '5558',
     '-port_out', '5559',
     '-max_seq_len', 'NONE',
     '-mask_cls_sep',
     '-cpu'])
server = BertServer(args)
server.start()
bc = BertClient(port=5558, port_out=5559)

df = pd.read_csv(file_path, usecols=['sen', 'tag'], sep='\t')
df['encode'] = df['sen'].apply(lambda x: bc.encode([x])[0])
df.to_csv(res_file_path, sep="\t", encoding="utf-8", columns=['sen', "tag", "encode"], header=True,
          index=False)

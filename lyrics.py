import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch

def inference(query, embedder, corpus_embeddings, df):
    query_embeddings = embedder.encode(query, convert_to_tensor=True)

    cos_scores = util.pytorch_cos_sim(query_embeddings, corpus_embeddings)[0]
    cos_scores = cos_scores.cpu()
    top_results = np.argpartition(-cos_scores, 1)[:1]
    print(df.iloc[top_results]['lyrics'])
    return df.iloc[top_results]['artist_names'].to_string(index=False), df.iloc[top_results]['track_name'].to_string(index=False)

def main(args):
    df = pd.read_csv('./merged.csv')

    embedder = SentenceTransformer('jhgan/ko-sroberta-multitask')
    corpus = df['lyrics'].tolist()
    corpus_embeddings = torch.load("sbert_embeddings.pt")
    result = inference(args, embedder, corpus_embeddings, df)
    print(result)

main("모락모락 김이 올라오는 밥을 먹었다.")
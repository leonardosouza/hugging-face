from datasets import load_dataset

ds = load_dataset("stanfordnlp/imdb", streaming=False)
print(ds)

ds_treino = ds['train']
# print(dataset_treino[9])

df = ds_treino.to_pandas()
print(df.head(10))

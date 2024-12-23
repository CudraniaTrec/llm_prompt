import pandas as pd
results = pd.read_csv('results.csv', index_col='name')
new_res = pd.DataFrame(columns=['model', 'mbpp', 'humaneval', 'mathqa']).set_index('model')
for model in results.index:
    row = results.loc[model]
    dataset = model.split('__')[0]
    model_name = model.split('__')[1]
    tot = int(row['total'])
    acc = int(row['acc'])
    rate = row['acc_rate']
    new_res.loc[model_name, dataset] = f"{acc}/{tot} ({rate})"
new_res.to_csv('results.csv', index=True)


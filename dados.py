import pandas as pd
import json

df = pd.read_csv('dados_brutos.csv')


df_peru = df[df['pais'] == 'Peru']
df_brasil = df[df['pais'] == 'Brazil']
df_colombia = df[df['pais'] == 'Colombia']

json_data_brasil = df_brasil.to_json(orient='records')
json_data_colombia = df_colombia.to_json(orient='records')
json_data_peru = df_peru.to_json(orient='records')

with open(r'fabio_vue\assets\brasil.json', 'w') as outfile:
    json.dump(json_data_brasil, outfile)

with open(r'fabio_vue\assets\colombia.json', 'w') as outfile:
    json.dump(json_data_colombia, outfile)

with open(r'fabio_vue\assets\peru.json', 'w') as outfile:
    json.dump(json_data_peru, outfile)


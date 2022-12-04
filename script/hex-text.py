import json
import pandas

Lang = 'ru'
Table = pandas.read_csv('numerics.tsv', sep='\t').set_index('index').rename_axis(None, axis=0)
Table.columns = pandas.MultiIndex.from_tuples(Table.columns.to_series().apply(lambda x: tuple(json.loads(x))))
Index = Table.transpose().to_dict()
Number = '7FA2'
Text = []

if Number[0] != '0': Text.append(Index[Number[0]][(3, Lang)])
if Number[1] != '0': Text.append(Index[Number[1]][(2, Lang)])
if (Number[2] == '1') and (Number[3] != '0'): Text.append(Index[Number[3]][(10, Lang)])
else:
	if Number[2] != '0': Text.append(Index[Number[2]][(1, Lang)])
	if Number[3] != '0': Text.append(Index[Number[3]][(0, Lang)])
print(' '.join(Text))

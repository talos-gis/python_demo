import pandas as pd

file_path = r'..\demo_core\demo.csv'
source = pd.read_csv(file_path, sep=',\s*', index_col='name',
                     engine='python')

print(source[source.index == 'C'])

print(source[source['year'] == 1995])

average_index_base = source['index_base'].mean()
print(f'the average language starts at index {average_index_base}')

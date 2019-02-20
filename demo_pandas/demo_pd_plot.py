import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import pandas as pd

file_path = r'..\demo_core\demo.csv'
source = pd.read_csv(file_path, sep=',\s*', index_col='name',
                     engine='python')

language_kinds = source['kind'].value_counts()
language_kinds.plot('pie', autopct='%.0f%%')
plt.show()

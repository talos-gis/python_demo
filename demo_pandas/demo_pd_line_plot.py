import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import pandas as pd

file_path0 = r'plt_demo_ice_deaths.csv'
file_path1 = r'plt_demo_lawyers.csv'
source0 = pd.read_csv(file_path0, sep=',', index_col='year')
source1 = pd.read_csv(file_path1, sep=',', index_col='year')
joined = pd.concat([source0, source1], axis=1)

print(joined)

joined.plot('lawyers in florida', 'deaths from slipping on ice', style='o--')
plt.show()

import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt

dataframe_all = pd.read_csv("/root/Downloads/FL_insurance_sample.csv")
num_rows = dataframe_all.shape[0]

counter_nan = dataframe_all.isnull().sum()
counter_without_nan = counter_nan[counter_nan==0]

dataframe_all = dataframe_all[counter_without_nan.keys()]
dataframe_all = dataframe_all.ix[:,7:]

x = dataframe_all.ix[:,:-1].values
standard_scalar = StandardScaler()
x_std = standard_scalar.fit_transform(x)

tsne = TSNE(n_components=2, random_state = 0)
x_test_2d = tsne.fit_transform(x_std)

markers=('s', 'd', 'o', '^', 'v')
color_map = {0:'red', 1:'blue', 2:'lightgreen', 3:'purple', 4:'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(x_test_2d)):
    plt.scatter(x=x_test_2d[cl, 0],y = x_test2d[cl,1], c=color_map[idx], marker = marker[idx], label = cl)
plt.show()

import numpy as np
import pandas as pd

dataset = pd.read_csv("https://raw.githubusercontent.com/sudesh-p/Sem-8-SPPU/main/ML/A2%20DecisionTree/DataTable.csv")
print(dataset)

x = dataset.iloc[ : , 1:-1]
y = dataset.iloc[ : ,-1].values  #our output label should be in array (np.array) .values converts it into array

from sklearn.preprocessing import LabelEncoder
x = x.apply(LabelEncoder().fit_transform) # we need to apply Label Encoder in Dataframe. to normalise the data

print(x)

from sklearn.tree import DecisionTreeClassifier
dtclassifier = DecisionTreeClassifier()
dtclassifier.fit(x,y)


x_in = np.array([1,1,0,1])
y_pred = dtclassifier.predict([x_in])
print(y_pred)

##from sklearn.external.six import StringIO
from six import StringIO
from IPython.display import Image # pip install ipython
from sklearn.tree import export_graphviz 
import pydotplus # pip install pydotplus

dot_data = StringIO()
export_graphviz(dtclassifier, out_file = dot_data, filled = True, rounded = True, special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
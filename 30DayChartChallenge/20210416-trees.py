


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

# https://www.kaggle.com/uciml/mushroom-classification
df=pd.read_csv('Data/mushrooms.csv')

# Encoding a categorical variable
# Option - convert a column to a category, then use those category values for your label encoding
feature_names1=['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']
for f in feature_names1:
    df[f] = df[f].astype('category')
    df[f] = df[f].cat.codes

# Define independent and dependent variable
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

# Fit the classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)

# Print Text Representation
text_representation = tree.export_text(clf)
print(text_representation)

# Plot Tree with plot_tree
fig = plt.figure(figsize=(25,20), facecolor='white')
_ = tree.plot_tree(clf, 
                   feature_names=feature_names1,  
                   class_names=df['class'].unique(),
                   filled=True)
fig.savefig("decistion_tree.png")

############## NOW LETS SEE HOW WE CAN SPLIT DATASET INTO TRAIN AND TEST ######################
############## AND THEN PREDICT 'class' for TEST SET AND MAKE A CONFUSION MATRIX ##############

df=pd.read_csv('Data/mushrooms.csv')

# Encoding a categorical variable
# Option - convert a column to a category, then use those category values for your label encoding
feature_names1=['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat']
for f in feature_names1:
    df[f] = df[f].astype('category')
    df[f] = df[f].cat.codes

# Define independent and dependent variable
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Training the Decision Tree Classification model on the Training set
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=1234) #(criterion = 'entropy', random_state = 0)
clf.fit(X_train, y_train)

# Predicting a new result
# print(clf.predict([[30,87000]]))

# Predicting the Test set results
y_pred = clf.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)




###################
#### Attempt 1 ####
###################

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

df=pd.read_csv('Data/500_Person_Gender_Height_Weight_Index.csv')

# Encoding a categorical variable
# Option - convert a column to a category, then use those category values for your label encoding
df["Gender"] = df["Gender"].astype('category')
df["Gender"] = df["Gender"].cat.codes
# Option
map = {0:'Extremely Weak', 1:'Weak', 2:'Normal', 3:'Overweight', 4:'Obesity', 5:'Extreme Obesity'}
map2 = {0:'Weak', 1:'Weak', 2:'Normal', 3:'Normal', 4:'Obesity', 5:'Obesity'}
df.Index = df.Index.replace(map2)


# Define independent and dependent variable
X = df.iloc[:, :3].values
y = df.iloc[:, 3].values

# Fit the classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)

# Print Text Representation
text_representation = tree.export_text(clf)
print(text_representation)

# Plot Tree with plot_tree
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names=df.iloc[:, :3].columns.to_list(),  
                   class_names=df.Index.unique(),
                   filled=True)

###################### UNUSED CODE ###########################

# https://mljar.com/blog/visualize-decision-tree/
# https://github.com/mljar/mljar-supervised

################## CLASSIFICATION TASK #######################

from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

# Prepare the data data
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Fit the classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)

# Print Text Representation
text_representation = tree.export_text(clf)
print(text_representation)

# Plot Tree with plot_tree
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names=iris.feature_names,  
                   class_names=iris.target_names,
                   filled=True)

# Visualize Decision Tree with graphviz
import graphviz
# DOT data
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names,
                                filled=True)

# Draw graph
graph = graphviz.Source(dot_data, format="png") 
graph
#graph.render("decision_tree_graphivz")

# Plot Decision Tree with dtreeviz Package
from dtreeviz.trees import dtreeviz # remember to load the package

viz = dtreeviz(clf, X, y,
                target_name="target",
                feature_names=iris.feature_names,
                class_names=list(iris.target_names))

viz


################## REGRESSION TASK #######################

# Visualizing the Decision Tree in Regression Task
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

# Prepare the data data
boston = datasets.load_boston()
X = boston.data
y = boston.target

# To keep the size of the tree small, I set max_depth = 3.
# Fit the regressor, set max_depth = 3
regr = DecisionTreeRegressor(max_depth=3, random_state=1234)
model = regr.fit(X, y)

# Print Text Representation
text_representation = tree.export_text(regr)
print(text_representation)

# Plot Tree with plot_tree
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(regr, feature_names=boston.feature_names, filled=True)


# Visualize Decision Tree with graphviz
dot_data = tree.export_graphviz(regr, out_file=None, 
                                feature_names=boston.feature_names,  
                                filled=True)
graphviz.Source(dot_data, format="png") 

# Plot Decision Tree with dtreeviz Package
from dtreeviz.trees import dtreeviz # remember to load the package

viz = dtreeviz(regr, X, y,
                target_name="target",
                feature_names=boston.feature_names)
viz



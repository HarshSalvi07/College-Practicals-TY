import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = load_iris()
X = data.data
y = data.target

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=44)

model = DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(X_train,y_train)

predictions = model.predict(X_test)
print("Accuracy: ",accuracy_score(y_test,predictions))

plot_tree(
    model,
    feature_names=data.feature_names,
    class_names=data.target_names,
    filled=True
)

plt.show()
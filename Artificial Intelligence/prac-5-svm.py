from sklearn import datasets
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_test, X_train , y_test, y_train = train_test_split(X, y , test_size=0.3, random_state=44)

scaler = StandardScaler()
X_train,X_test = scaler.fit_transform(X_train), scaler.transform(X_test)

model = SVC(kernel='linear',C=1)
model.fit(X_train,y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test,pred)*100
report = classification_report(y_test,pred,target_names=iris.target_names)
matrix = confusion_matrix(y_test,pred)

print(f"Accuracy:{accuracy}%")
print("ClassificationReport\n",report)
print("ConfusionMatrix\n",matrix)
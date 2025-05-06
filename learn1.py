import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

np.random.seed(10)
raw_data = datasets.load_iris()
data = raw_data["data"]  # użycie klucza zamiast atrybutu
target = raw_data["target"]

data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.3)

model = LogisticRegression(max_iter=200)  # więcej iteracji dla stabilnej konwergencji
model.fit(data_train, target_train)

print(model.predict(data_test))

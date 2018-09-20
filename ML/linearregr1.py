import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score

training_set = pd.read_csv('train.csv')
testing_set = pd.read_csv('test.csv')

X_train = training_set.iloc[:20, :-1].values  
y_train = training_set.iloc[:20, 1].values

X_test = testing_set.iloc[:20, :-1].values  
y_test = testing_set.iloc[:20, 1].values

regr = linear_model.LinearRegression()

regr.fit(X_train,y_train)

y_pred = regr.predict(X_test)

print(r2_score(y_test,y_pred))

plt.scatter(X_test, y_test, color = 'black')
plt.plot(X_test, y_pred, color = 'red', linewidth = 3)

plt.xticks(())
plt.yticks(())
plt.show()
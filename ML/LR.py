import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("hours.csv")
x= dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x,y)
Accurracy = regressor.score(x,y)*100
print("Accurracy")
print(Accurracy)

y_pred = regressor.predict([[10]])
print(y_pred)

hours=int(input("Enter number of hours"))
eq = regressor.coef_*hours+regressor.intercept_
print("Risk score",eq[0])

plt.plot(x,y,'o')
plt.plot(x,regressor.predict(x))
plt.show()
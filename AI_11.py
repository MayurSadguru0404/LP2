pip install yfinance --user


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.linear_model import LinearRegression

google = yf.Ticker("GOOG")

df = google.history(period='1d', interval="1m")
print(df.head())


df = google.history(period='1d', interval="1m")
df = df[['Low']]
df.head()

df['seconds_since_midnight'] = (df.index.hour * 3600 +
                                df.index.minute * 60 +
                                df.index.second)

X = df[['seconds_since_midnight']].values
y = df['Low'].values

offset = int(0.10*len(df))
X_train = X[:-offset]
y_train = y[:-offset]
X_test  = X[-offset:]
y_test  = y[-offset:]

plt.plot(range(0,len(y_train)),y_train, label='Train')
plt.plot(range(len(y_train),len(y)),y_test,label='Test')
plt.legend()
plt.show()

# Create a linear regression model
model = LinearRegression()

# Fit the model

model.fit(X, y)


# Evaluate the model
score = model.score(X, y)
print("Model score:", score)

forecast = model.predict(X_test[0:1])
print(f'Real data for time 0: {y_train[-1]}')
print(f'Real data for time 1: {y_test[0]}')
print(f'Pred data for time 1: {forecast[0]}')

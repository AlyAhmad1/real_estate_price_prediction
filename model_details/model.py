import pickle
from data_cleaning import data_cleaning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = data_cleaning()
X = data.drop('price', axis='columns')
y = data['price']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

le_model = LinearRegression()
le_model.fit(x_train, y_train)
le_model.score(x_test, y_test)


with open('../server/artifacts/banglore_home_prices_model.pickle', 'wb') as f:
    pickle.dump(le_model, f)


import json
columns = {
    'data_columns' : [col.lower() for col in X.columns]
}
with open("../server/artifacts/columns.json", "w") as f:
    f.write(json.dumps(columns))


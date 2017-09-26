from sklearn.linear_model import LinearRegression

def linear_regression(X, y):
    linear_regressor = LinearRegression(normalize=False)
    linear_regressor.fit(X, y)
    return linear_regressor

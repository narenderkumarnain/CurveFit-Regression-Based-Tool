# ===================================This file contains the code for Regression Algorithms
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
import sklearn.utils._cython_blas
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class PreProcessing:
    def __init__(self, X_l, y_l):
        self.X = np.array(X_l).reshape((len(X_l), 1))
        self.y = np.array(y_l).reshape((len(y_l), 1))

    def scale(self , X , y):
        # standard scaling the features and outputs
        self.sc_X = StandardScaler()
        self.X_s = self.sc_X.fit_transform(X)
        self.sc_y = StandardScaler()
        self.y_s = self.sc_y.fit_transform(y.reshape(-1, 1))
        self.X = X
        self.y = y
        return self.X_s,self.y_s

    def ret_X_y(self):
        return self.X, self.y

    def ret_X_y_s(self):
        return self.X_s

    def ret_scaler(self):
        return self.sc_X, self.sc_y


class Regressors:
    def __init__(self):
        return
    def lin_reg(self , X ,y):
        #-------------------scaling here
        preprocess = PreProcessing(X , y)
        X_l,y_l = preprocess.ret_X_y()
        X_s , y_s = preprocess.scale(X_l , y_l)

        regressor = LinearRegression()
        regressor.fit(X_s, y_s)
        sc_x, sc_y = preprocess.ret_scaler()
        X_s = preprocess.ret_X_y_s()
        return regressor, sc_x, sc_y, X_l , y_l

    def poly_reg(self, n , X , y):
        preprocess = PreProcessing(X, y)
        X_l, y_l = preprocess.ret_X_y()

        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(X_l)
        X_s , y_s = preprocess.scale(X_poly , y_l)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        poly_reg.fit(X_s, y_s)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_s, y_s)
        sc_x, sc_y = preprocess.ret_scaler()
        #X_s = preprocess.ret_X_y_s()
        return lin_reg_2, sc_x, sc_y, X_l,y_l

    def ridge(self, a, n , X , y):
        preprocess = PreProcessing(X, y)
        X_l, y_l = preprocess.ret_X_y()

        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(X_l)
        X_s, y_s = preprocess.scale(X_poly, y_l)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        poly_reg.fit(X_s, y_s)
        regressor = Ridge(alpha=a, solver='cholesky')
        regressor.fit(X_s, y_s)
        sc_x, sc_y = preprocess.ret_scaler()
        #X_s = preprocess.ret_X_y_s()
        return regressor, sc_x, sc_y, X_l,y_l

    def lasso(self, a, n , X , y):
        preprocess = PreProcessing(X, y)
        X_l, y_l = preprocess.ret_X_y()

        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(X_l)
        X_s, y_s = preprocess.scale(X_poly, y_l)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        poly_reg.fit(X_s, y_s)

        regressor = Lasso(alpha=a)
        regressor.fit(X_s, y_s)
        sc_x, sc_y = preprocess.ret_scaler()
        #X_s = preprocess.ret_X_y_s()
        return regressor, sc_x, sc_y, X_l,y_l

    def elastic(self, a, r, n , X , y):
        preprocess = PreProcessing(X, y)
        X_l, y_l = preprocess.ret_X_y()

        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(X_l)
        X_s, y_s = preprocess.scale(X_poly, y_l)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        poly_reg.fit(X_s, y_s)
        regressor = ElasticNet(alpha=a, l1_ratio=r)
        regressor.fit(X_s, y_s)
        sc_x , sc_y = preprocess.ret_scaler()
        #X_s = preprocess.ret_X_y_s()
        return regressor , sc_x , sc_y , X_l,y_l

    def get_xpoly(self):
        return self.X_poly

    def getsc_poly(self):
        return self.sc_poly
# ==============================class for matplotlib



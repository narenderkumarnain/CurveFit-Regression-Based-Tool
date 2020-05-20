#===================================This file contains the code for Regression Algorithms
import  numpy as np
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
    def __init__(self , X_l , y_l):
        self.X = np.array(X_l).reshape((len(X_l) , 1))
        self.y = np.array(y_l).reshape((len(y_l), 1))

        #standard scaling the features and outputs
        self.sc_X = StandardScaler()
        self.X_s = self.sc_X.fit_transform(self.X)
        self.sc_y = StandardScaler()
        self.y_s = self.sc_y.fit_transform(self.y.reshape(-1, 1))

    def ret_X_y(self):
        return self.X , self.y

    def ret_X_y_s(self):
        return self.X_s , self.y_s

    def ret_scaler(self):
        return self.sc_X , self.sc_y


class Regressors:
    def __init__(self , X_s ,  y_s):
        self.X = X_s
        self.y = y_s
        self.X_poly = X_s
        self.sc_poly =  X_s

    def lin_reg(self):
        regressor = LinearRegression()
        regressor.fit(self.X , self.y)
        return regressor

    def poly_reg(self , n):
        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(self.X)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        poly_reg.fit(X_poly, self.y)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_poly, self.y)
        return lin_reg_2

    def ridge(self , a , n):
        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(self.X)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        regressor = Ridge(alpha = a  , solver = 'cholesky')
        regressor.fit(self.X_poly, self.y)
        return regressor

    def lasso(self , a , n):
        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(self.X)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        regressor = Lasso(alpha = a)
        regressor.fit(self.X_poly , self.y)
        return regressor

    def elastic(self , a , r , n):
        poly_reg = PolynomialFeatures(degree=n)
        X_poly = poly_reg.fit_transform(self.X)
        self.X_poly = X_poly
        self.sc_poly = poly_reg
        regressor = ElasticNet(alpha = a , l1_ratio = r)
        regressor.fit(self.X_poly , self.y)
        return regressor
    def get_xpoly(self):
        return self.X_poly

    def getsc_poly(self):
        return self.sc_poly
#==============================class for matplotlib

        

# CurveFit-Regression-Based-Tool
CurveFit is a GUI tool created using Tkinter Module of Python. It uses Linear Regression , Polynomial Features and other Machine Learning Algorithms. It uses scikit-learn's linear_model library for the implementations of Linear Regression , SGD Ridge Lasso and ElasticNet Algorithms. CurveFit Tool outputs the live Matplotlib Plot for the diffrent values of Hyperparameters set by user through GUI interface. Matplolib with Tkinter as a backend , is used to Embedd Plots directly in the Tkinter Frame. User can input the induvidual data items Manually through the GUI interface or a .csv file can also be provided which is automatically preprocessed into numpy arrays using pandas and numpy , and scaled properly by StandardScalar class by scikit-learn for Regression Classes.

## Design Style
The Complete Design of GUI consist of Five Windows and code for each of these is stored in root<window code>.py named Files.
These Five Windows are Interconnected through inter root link and the Initil point for code is provided in main.py file.
The Function of These Five Windows is as follow:

#---------------------------------------------Importing Files
import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from root2 import root2_fun
from root2b import root2b_fun
from tkinter import Menu
import webbrowser
from tkinter import scrolledtext
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
import sklearn.utils._cython_blas


#-----------------------------------------Regression Classes

# ===================================This file contains the code for Regression Algorithms
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


#-----------------------------------------Regression Classes Ends
#---------------------------------------------Root Functions

#---------------------------------------------Root1 Function
def root1_fun():
    # ==================================================Required Functions
    def _top1():
        root.destroy()
        root2_fun()
    def _top2():
        root.destroy()
        root2b_fun()
    # ======================================================Main Window
    root = tk.Tk()
    root.config(background="#b3e6ff")
    root.title("CurveFit")
    root.geometry("500x400+450+150")

    # =====================================================Menu functions
    main_menu = Menu(root)

    def _view_about():
        win3 = tk.Toplevel(root, background="#b3e6ff")
        win3.geometry('350x250+600+200')
        tk.Label(win3, background="#b3e6ff",
                 text='Curve Fit \n Regression Based Tool \n Created By:'
                      ' \n Narender Nain \n For any suggestion, contact:'
                      '\n narenderkumarnain@gmail.com \n'
                      'For any queries about Tool,Refer to', font='1').pack()

        def callback(url):
            webbrowser.open_new(url)

        link1 = tk.Label(win3, background="#b3e6ff",
                         text="https://github.com/narenderkumarnain",
                         font='1', fg="blue",cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/narenderkumarnain"))

    # -------------------------------------------------------------- ABOUT MENU
    about_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="View About", command=_view_about)

    root.config(menu=main_menu)
    # ===============================================Menu Ends
    #-------------------------------------------------Frames Declaration
    br1 = tk.LabelFrame(root, text="CurveFit", font="courier 12 bold", background="#b3e6ff")
    br1.grid(column=0, row=0, padx=8, pady=4, sticky=tk.W + tk.E)

    br2 = tk.LabelFrame(root, text="", bd=10, background="#b3e6ff")
    br2.grid(column=0, row=1, padx=8, pady=4, sticky=tk.W + tk.E)

    br3 = tk.LabelFrame(root, text="", bd=10, background="#b3e6ff")
    br3.grid(column=0, row=2, padx=8, pady=4)

    # --------------------------------------------------Adding The Logo Image
    render = ImageTk.PhotoImage(Image.open(r'C:\Users\Narender Nain\PycharmProjects\CurveFit\lg.jpg'))
    img = tk.Label(br1, image=render, padx=20, relief=tk.RIDGE, bd=8, height=75, width=100)
    img.image = render
    img.grid(column=0, row=0)

    #----------------------------------------------------Label Declaration
    label1 = tk.Label(br1, text="Welcome to CurveFit  :)", font="courier 12 bold", bd=10, fg="Blue",
                      background="#b3e6ff")
    label1.grid(column=1, row=0, padx=8, pady=4, sticky=tk.W)

    label2 = tk.Label(br2, text="We would use Linear Regression to fit your \n data to a Beautiful Curve ",
                      font="courier 12", bd=10, background="#b3e6ff", fg="Blue")
    label2.grid(column=0, row=0, padx=8, pady=4)

    label3 = tk.Label(br2, text="Input the Data Point in the X and Y columns",
                      font="courier 12", width=40, bd=10,
                      fg="Blue", background="#b3e6ff")
    label3.grid(column=0, row=1, padx=8, pady=4)

    #-------------------------------------------------------Button Declaration
    button1 = tk.Button(br3, relief=tk.GROOVE, font="courier 12 bold",
                        bg="#b3e6ff", activebackground="#00FA9A",
                        text='Enter X and y', command=_top1, bd=6)
    button1.grid(column=0, row=1)

    button1 = tk.Button(br3, text='Choose a CSV File', relief=tk.RIDGE,
                        font="courier 12 bold", command=_top2, bd=6,
                        background="#b3e6ff")
    button1.grid(column=0, row=2)

    root.mainloop()

#======================================================Root2 Function Starts
def root2_fun():
        # ===============================================Entry Window Starts

        root2 = tk.Tk()
        root2.title("CurveFit")
        root2.config(background="#b3e6ff")
        root2.geometry('325x500+600+150')
        root2.resizable(False , False)

        # =====================================================Menu functions
        main_menu = Menu(root2)

        def _view_about():
                win3 = tk.Toplevel(root2, background="#b3e6ff")
                win3.geometry('350x250+600+200')
                tk.Label(win3, background="#b3e6ff",
                         text='Curve Fit \n Regression Based Tool \n Created By:'
                              ' \n Narender Nain \n For any suggestion, contact:'
                              '\n narenderkumarnain@gmail.com \n'
                              'For any queries about Tool,Refer to', font='1').pack()

                def callback(url):
                        webbrowser.open_new(url)

                link1 = tk.Label(win3, background="#b3e6ff",
                                 text="https://github.com/narenderkumarnain",
                                 font='1', fg="blue", cursor="hand2")
                link1.pack()
                link1.bind("<Button-1>", lambda e: callback("https://github.com/narenderkumarnain"))

        # -------------------------------------------------------------- ABOUT MENU
        about_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="View About", command=_view_about)

        root2.config(menu=main_menu)
        # ===============================================Menu Ends

        #--------------------------------------------Frame1 Declaration

        frame1 = tk.LabelFrame(root2, text='',background="#b3e6ff", bd=10)
        frame1.grid(column=0, row=0, padx=8, pady=4)

        tk.Label(frame1, text='Enter the DataPoints X and y: ',background="#b3e6ff",
                 font='1', fg='Blue').grid(column=0, row=0, padx=8, pady=4)

        X = []
        y = []
        # --------------------------------------------Frame1 Declaration Ends
        # --------------------------------------------Frame2 Declaration
        frame2 = tk.LabelFrame(root2, text='',background="#b3e6ff", bd=10)
        frame2.grid(column=0, row=1, padx=8, pady=4)

        x_var = tk.StringVar()
        y_var = tk.StringVar()

        tk.Label(frame2, text='Enter X:',font = '1' ,background="#b3e6ff",
                 fg = 'Blue', bd=8).grid(column=0, row=0, padx=8, pady=4)

        entryx = tk.Entry(frame2, width=8, textvariable=x_var)
        entryx.grid(column=1, row=0, padx=8, pady=4)

        #--------------------------------------------Frame2 Declaration Ends
        # -------------------------------------------Frame3 Declaration
        frame3 = tk.LabelFrame(root2,background="#b3e6ff", text='', bd=10)
        frame3.grid(column=0, row=2, padx=8, pady=4)

        labely = tk.Label(frame3, text='Enter y:',background="#b3e6ff",font = '1',fg = 'Blue', bd=8)
        labely.grid(column=0, row=0, padx=8, pady=4)

        entryy = tk.Entry(frame3, width=8, textvariable=y_var)
        entryy.grid(column=1, row=0, padx=8, pady=4)

        # --------------------------------------------Frame3 Declaration Ends
        # --------------------------------------------Frame4 Declaration
        frame4 = tk.LabelFrame(root2, text="", bd=10,background="#b3e6ff")
        frame4.grid(column=0, row=3, padx=8, pady=4)

        stx = ''
        sty = ''

        def _apply():
            global stx
            global sty
            X.append(float(x_var.get()))
            y.append(float(y_var.get()))
            scrol.insert(tk.INSERT, 'X:' + x_var.get() + ' ')
            scrol.insert(tk.INSERT, 'y:' + y_var.get() + ' ')
            scrol.insert(tk.INSERT, '\n')

        savebutton = tk.Button(frame4, text='Save',background="#b3e6ff",font='0.5', command=_apply)
        savebutton.grid(column=0, row=0, padx=8, pady=4)

        # --------------------------------------------Frame4 Declaration Ends
        # --------------------------------------------Frame6 Declaration
        frame6 = tk.LabelFrame(root2, text='Values Entered:',background="#b3e6ff", bd=10)
        frame6.grid(column=0, row=4, padx=8, pady=4)

        scrol_w = 30
        scrol_h = 3
        scrol = scrolledtext.ScrolledText(frame6, width=scrol_w,background="#b3e6ff",
                                          height=scrol_h, wrap=tk.WORD)
        scrol.grid(column=0, row=0, columnspan=3)
        # --------------------------------------------Frame6 Declaration Ends

        # --------------------------------------------Frame6 Declaration
        frame7 = tk.LabelFrame(root2 , text = '' , background="#b3e6ff",bd = 10)
        frame7.grid(column = 0 , row = 5 , padx = 8 , pady = 4)

        def _root2com():
            root2.destroy()
            root3_fun(X , y)
        button1 = tk.Button(frame7 , text = 'Next Step' ,background="#b3e6ff",
                            font = '1', bd = 10 , fg = 'Blue' , command = _root2com)
        button1.grid(column = 0 , row = 0 , padx = 8 , pady = 4)

        entryx.focus()
        root2.mainloop()



#=============================================root2b function starts
def root2b_fun():
    root2b = tk.Tk()
    root2b.config(background="#b3e6ff")
    root2b.title('CurveFit')
    root2b.geometry('550x375+450+200')
    root2b.resizable(False,False)
    # =====================================================Menu functions
    main_menu = Menu(root2b)

    def _view_about():
        win3 = tk.Toplevel(root2b, background="#b3e6ff")
        win3.geometry('350x250+600+200')
        tk.Label(win3, background="#b3e6ff",
                 text='Curve Fit \n Regression Based Tool \n Created By:'
                      ' \n Narender Nain \n For any suggestion, contact:'
                      '\n narenderkumarnain@gmail.com \n'
                      'For any queries about Tool,Refer to', font='1').pack()

        def callback(url):
            webbrowser.open_new(url)

        link1 = tk.Label(win3, background="#b3e6ff",
                         text="https://github.com/narenderkumarnain",
                         font='1', fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/narenderkumarnain"))

    #-------------------------------------------------------------- ABOUT MENU
    about_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="View About", command=_view_about)

    root2b.config(menu=main_menu)
    #=====================================================Menu Ends

    #------------------------------------------------------Frame 1 Declaration
    frame1 = tk.Frame(root2b,background="#b3e6ff")
    frame1.grid(column=0, row=0, padx=8, pady=4)

    label1 = tk.Label(frame1,background="#b3e6ff",font='1',
                      text='Input the .csv file in the Dialog Below', fg='Blue')
    label1.grid(column=0, row=0, padx=8, pady=4)

    label2 = tk.Label(frame1,background="#b3e6ff",font='0.1',
                      text='.csv File must contain 2 Columns , X and y , in Same order', fg='Red')
    label2.grid(column=0, row=1, padx=8, pady=4)
    # ------------------------------------------------------Frame 1 Declaration Ends

    # ------------------------------------------------------Frame 2 Declaration

    frame2 = tk.LabelFrame(root2b ,background="#b3e6ff",font = '0.5', text = 'Input :' , bd = 10)
    frame2.grid(column = 0 , row = 1 , padx = 8 ,pady = 4)

    def _inputfile():
        global X
        global y
        global df
        file_path = askopenfilename(filetypes = [('CSV File' , '*.csv')])
        df = pd.read_csv(file_path)
        df.dropna()
        X = list(df.iloc[:, 0])
        y = list(df.iloc[:, 1])
        scrol1.insert(tk.INSERT, str(X) + '\n')
        scrol2.insert(tk.INSERT, str(y) + '\n')

    button1 = tk.Button(frame2 , text = 'Select File' ,
                        background="#b3e6ff",font='1', command = _inputfile  ,width = 25)
    button1.grid(column = 1 , row = 0 , padx = 8 , pady = 4)

    # ------------------------------------------------------Frame 2 Declaration Ends
    # ------------------------------------------------------Frame 3 Declaration
    frame3 = tk.Frame(root2b,background="#b3e6ff")
    frame3.grid(column = 0 , row = 2)

    label3 = tk.Label(frame3 ,background="#b3e6ff",font='1',
                      text = 'X : ').grid(column = 0 , row = 0 , padx = 8 , pady = 4)

    scrol1 = scrolledtext.ScrolledText(frame3 , wrap = tk.WORD ,
                                       background="#b3e6ff", width = 30 , height = 1)
    scrol1.grid(column = 1 , row = 0 , padx = 8 , pady = 4)

    label4 = tk.Label(frame3,background="#b3e6ff",
                      font='1', text='y : ').grid(column=0, row=1, padx=8, pady=4)

    scrol2 = scrolledtext.ScrolledText(frame3, wrap=tk.WORD,background="#b3e6ff", width=30, height=1)
    scrol2.grid(column=1, row=1, padx=8, pady=4)

    # ------------------------------------------------------Frame 3 Declaration Ends

    # ------------------------------------------------------Frame 4 Declaration
    frame4 = tk.Frame(root2b,background="#b3e6ff")
    frame4.grid(column = 0 , row = 4)

    def _root2bcom():
        try:
            root2b.destroy()
            root3_fun(X, y)
        except:
            messagebox.showerror('CurveFit', message='Input a csv file!')
            root2b_fun()

    button2 = tk.Button(frame4 ,background="#b3e6ff",font = '1', text = '   Save   ' , bd = 10 , fg = 'Blue' , command = _root2bcom)
    button2.grid(column = 0 , row = 0 , padx = 8 , pady = 4)

    root2b.mainloop()


#=====================================root3 function starts
def root3_fun(X , y):
    #---------------------------------------Main Window
    root3 = tk.Tk()
    root3.config(background="#b3e6ff")
    root3.geometry('375x400+550+150')
    root3.resizable(False , False)
    root3.title("CurveFit")

    # =====================================================Menu functins
    main_menu = Menu(root3)

    def _view_about():
        win3 = tk.Toplevel(root3, background="#b3e6ff")
        win3.geometry('350x250+600+200')
        tk.Label(win3, background="#b3e6ff",
                 text='Curve Fit \n Regression Based Tool \n Created By:'
                      ' \n Narender Nain \n For any suggestion, contact:'
                      '\n narenderkumarnain@gmail.com \n'
                      'For any queries about Tool,Refer to', font='1').pack()

        def callback(url):
            webbrowser.open_new(url)

        link1 = tk.Label(win3, background="#b3e6ff",
                         text="https://github.com/narenderkumarnain",
                         font='1', fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/narenderkumarnain"))

    # -------------------------------------------------------------- ABOUT MENU
    about_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="View About", command=_view_about)

    root3.config(menu=main_menu)
    # ===============================================Menu Ends

    #---------------------------------------------Frame1 Declaration Starts
    frame1 = tk.LabelFrame(root3 , text = 'Plot Features' ,
                           background="#b3e6ff", bd = 10 , font = '6')
    frame1.grid(column = 0 , row = 0 , padx = 8  ,pady = 4)

    label1 = tk.Label(frame1 ,font = '2',background="#b3e6ff",
                      text = 'Provide some features for the plot\n Just to make it more Detailed' ,
                      bd = 10 , fg = 'Blue')
    label1.grid(column = 0 , row = 0 , padx = 8 ,pady = 4)

    plot_title = tk.StringVar()
    plot_x = tk.StringVar()
    plot_y = tk.StringVar()

    # ---------------------------------------------Frame1 Declaration Ends

    # ---------------------------------------------Frame2 Declaration Starts
    frame2 = tk.LabelFrame(root3 ,background="#b3e6ff", text = '' , bd = 10)
    frame2.grid(column = 0 , row = 1 , padx = 8 , pady = 4)

    label2 = tk.Label(frame2 ,font = '4',background="#b3e6ff",
                      text = 'X-Label: ' , bd = 8 , fg = 'Blue')
    label2.grid(column = 0 , row = 0 , padx = 8 , pady = 4)

    entry1 = tk.Entry(frame2 , width = 20,relief = tk.RIDGE , bd = 6 , textvariable = plot_x)
    entry1.grid(column = 1 , row = 0 , padx = 8 , pady = 4)

    label3 = tk.Label(frame2,font = '4' ,background="#b3e6ff", text='Y-Label: ', bd=8, fg='Blue')
    label3.grid(column=0, row=1, padx=8, pady=4)

    entry2 = tk.Entry(frame2, width = 20,relief = tk.RIDGE , bd = 6, textvariable=plot_y)
    entry2.grid(column=1, row=1, padx=8, pady=4)

    label4 = tk.Label(frame2, font = '4',background="#b3e6ff",text='Plot-Label: ', bd=8, fg='Blue')
    label4.grid(column=0, row=2, padx=8, pady=4)

    entry3 = tk.Entry(frame2,width = 20,relief = tk.RIDGE , bd = 6, textvariable=plot_title)
    entry3.grid(column=1, row=2, padx=8, pady=4)

    # ---------------------------------------------Frame2 Declaration Ends

    # ---------------------------------------------Frame3 Declaration Starts
    frame3 = tk.LabelFrame(root3 ,background="#b3e6ff", text = '' , bd = 8)
    frame3.grid(column =  0, row = 2 , padx = 8 , pady = 4)

    def _root3com():
        root3.destroy()
        root4_fun(X,y , plot_title.get() , plot_x.get() , plot_y.get())

    button1 = tk.Button(frame3 ,background="#b3e6ff", text = 'Save' ,
                        width = 20, font = '4',bd = 8 , command = _root3com)
    button1.grid(column = 0 , row = 0 , padx = 8 , pady =4 )
    # ---------------------------------------------Frame1 Declaration Ends

    entry1.focus()
    root3.mainloop()


# ==============================================root4 function starts
# ==============================================root4 function starts
def root4_fun(X, y , title , xlabel , ylabel):
    #------------------------------------Main Window
    root4 = tk.Tk()
    root4.config(background="#b3e6ff")
    root4.title('CurveFit')
    root4.geometry('1150x600+200+50')
    root4.resizable(False,False)

    # =====================================================Menu functins
    main_menu = Menu(root4)

    def _view_about():
        win3 = tk.Toplevel(root4, background="#b3e6ff")
        win3.geometry('350x250+600+200')
        tk.Label(win3, background="#b3e6ff",
                 text='Curve Fit \n Regression Based Tool \n Created By:'
                      ' \n Narender Nain \n For any suggestion, contact:'
                      '\n narenderkumarnain@gmail.com \n'
                      'For any queries about Tool,Refer to', font='1').pack()

        def callback(url):
            webbrowser.open_new(url)

        link1 = tk.Label(win3, background="#b3e6ff",
                         text="https://github.com/narenderkumarnain",
                         font='1', fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://github.com/narenderkumarnain"))

    # -------------------------------------------------------------- ABOUT MENU
    about_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="View About", command=_view_about)

    root4.config(menu=main_menu)
    # ===============================================Menu Ends
    #------------------------------------------Main Frames Declaration

    bigframe1 = tk.Frame(root4, bd=8 , background="#b3e6ff")
    bigframe1.grid(column=0, row=0)

    bigframe2 = tk.Frame(root4, bd=8 , background="#b3e6ff")
    bigframe2.grid(column=1, row=0)

    #---------------------------------------------Frame1 Declaration
    frame1 = tk.LabelFrame(bigframe1, text='Plot Wizard',font = '1', bd=10 , background="#b3e6ff")
    frame1.grid(column=0, row=0, padx=8, pady=4)

    label1 = tk.Label(frame1, text='Select The features for your Regression Model: ',
                      font = '1', fg='Blue' , background="#b3e6ff")
    label1.grid(column=0, row=0, padx=8, pady=4, sticky=tk.N)

    # ---------------------------------------------Frame2 Declaration
    frame2 = tk.LabelFrame(bigframe1,width = 80, text='', bd=10 , background="#b3e6ff")
    frame2.grid(column=0, row=1, padx=8, pady=4, sticky=tk.N)

    label2 = tk.Label(frame2, text='Regression Type:          ',
                      bd=10 ,font = '1', background="#b3e6ff")
    label2.grid(column=0, row=0, padx=8, pady=4, sticky=tk.N)

    reg_type = tk.StringVar()

    reg_chossen = ttk.Combobox(frame2, width=25,height = 40,
                               textvariable=reg_type , background="#b3e6ff")
    reg_chossen['values'] = ('LinearRegression', 'PolynomialRegression')
    reg_chossen.current(0)
    reg_chossen.grid(column=1, row=0, padx=8, pady=4, sticky=tk.N)

    # ---------------------------------------------Frame3 Declaration
    frame3 = tk.LabelFrame(bigframe1, text='Polynomial Regression Features',
                           font = '2', bd=10 , background="#b3e6ff")
    frame3.grid(column=0, row=2, padx=8, pady=4, sticky=tk.N)

    label3 = tk.Label(frame3, text='PolyFeatures N: ',font = '2', bd=10 , background="#b3e6ff")
    label3.grid(column=0, row=0, padx=8, pady=4, sticky=tk.N)

    features = tk.Spinbox(frame3, from_=1, to=15, width=20, bd=4 , background="#b3e6ff")
    features.grid(column=1, row=0, padx=8, pady=4, sticky=tk.N)

    label4 = tk.Label(frame3, text='Regularization: ',font = '2', bd=10 , background="#b3e6ff")
    label4.grid(column=0, row=1, padx=8, pady=4, sticky=tk.N)

    regulari_type = tk.StringVar()
    regularization_choosen = ttk.Combobox(frame3, width=20,
                                          textvariable=regulari_type , background="#b3e6ff")
    regularization_choosen['values'] = ['None', 'Ridge', 'Lasso', 'ElasticNet']
    regularization_choosen.current(0)
    regularization_choosen.grid(column=1, row=1, padx=8, pady=4, sticky=tk.N)

    label5 = tk.Label(frame3, text='Alpha: ', bd=10 ,font = '2', background="#b3e6ff")
    label5.grid(column=0, row=2, padx=8, pady=4, sticky=tk.N)

    alpha = tk.IntVar()
    alpha.set('0.1')
    alpha1 = tk.Entry(frame3,width=20, bd=4 ,textvariable = alpha, background="#b3e6ff")
    alpha1.grid(column=1, row=2, padx=8, pady=4, sticky=tk.N)

    # ---------------------------------------------Frame4 Declaration
    frame4 = tk.LabelFrame(bigframe1, text='ElasticNet r ratio:',
                           font = '2', bd=10 ,background="#b3e6ff" )
    frame4.grid(column=0, row=3, padx=8, pady=4, sticky=tk.N)

    label6 = tk.Label(frame4, text='l1_ratio:             ',
                      bd=10 ,font = '2', background="#b3e6ff")
    label6.grid(column=0, row=0, padx=8, pady=4, sticky=tk.N)
    l1_ratio = tk.StringVar()
    l1_ratio.set('0.5')
    l1_ratio1 = tk.Entry(frame4, width=20, bd=4 ,textvariable = l1_ratio, background="#b3e6ff")
    l1_ratio1.grid(column=1, row=0, padx=8, pady=4)

    # ---------------------------------------------Frame5 Declaration
    frame5 = tk.LabelFrame(bigframe1, text='', bd=10 , background="#b3e6ff")
    frame5.grid(column=0, row=4, padx=8, pady=4)

    # ---------------------------------------------Frame6 Declaration
    frame6 = tk.LabelFrame(bigframe2, text='Plot: ',font = '2', bd=10 , background="#b3e6ff")
    frame6.grid(column=0, row=0, padx=8, pady=4, sticky=tk.N)

    # Instances of regression classes
    # Returning scaled features
    # Regression models class
    reg_obj = Regressors()

    def _apply():
        flag = 1
        # -----------------------------------MLCode is here
        if reg_type.get() == 'LinearRegression':
            regressor , sc_x , sc_y, X_l,y_l = reg_obj.lin_reg(X , y)
        elif reg_type.get() == 'PolynomialRegression':
            flag = 0
            n = int(features.get())
            if regulari_type.get() == 'None':
                regressor , sc_x , sc_y,X_l , y_l = reg_obj.poly_reg(n , X , y)
            elif regulari_type.get() == 'Ridge':
                alp = float(alpha.get())
                regressor , sc_x , sc_y,X_l,y_l = reg_obj.ridge(alp, n , X , y)
            elif regulari_type.get() == 'Lasso':
                apl = float(alpha.get())
                regressor , sc_x , sc_y ,X_l,y_l = reg_obj.lasso(apl, n , X , y)
            elif regulari_type.get() == 'ElasticNet':
                ratio = float(l1_ratio.get())
                apl = float(alpha.get())
                regressor ,sc_x,sc_y  ,X_l,y_l = reg_obj.elastic(apl, ratio, n , X ,y)
            poly_reg = reg_obj.getsc_poly()

        X_grid = np.arange(min(X_l), max(X_l), 0.1)
        X_grid = X_grid.reshape((len(X_grid), 1))

        if flag == 0:
            X_fit = poly_reg.fit_transform(X_grid)
        else:
            X_fit = X_grid

        # ----------------------------------MLCode Ends here
        #-----------------------------------Updating Matplotlib Chart
        fig.clear()
        fig.add_subplot(111).scatter(X_l, y_l, color='Red')
        fig.add_subplot(111).plot( X_grid,
                                  sc_y.inverse_transform(regressor.predict(sc_x.transform(X_fit))))

        canvas.draw()

        toolbar.update()
        return

    button1 = tk.Button(frame5, text='Apply',background="#b3e6ff",font = '2', command=_apply, fg='Blue' )
    button1.grid(column=0, row=0, padx=8, pady=4)

    #-----------Initialising Matplotlib Chart
    fig = Figure(figsize=(6, 5), dpi=100)
    fig.add_subplot(111).scatter(X, y, color='Red')
    fig.axes[0].set_title(title)
    fig.axes[0].set_xlabel(xlabel)
    fig.axes[0].set_ylabel(ylabel)
    canvas = FigureCanvasTkAgg(fig, master=frame6)  # A tk.DrawingArea.
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, frame6)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    reg_chossen.focus()
    root4.mainloop()



if __name__ == '__main__':
    root1_fun()




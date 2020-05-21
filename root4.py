# =================================================Importing Libraries
import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from regression import *
import webbrowser
from tkinter import Menu

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


#root4_fun([1, 2, 3, 4, 5], [2, 4, 6, 6, 18] , '' , '' , '')
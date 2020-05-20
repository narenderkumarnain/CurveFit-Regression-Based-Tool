#------------------------------------------Importing Libraries
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
import pandas as pd
from root3 import root3_fun
from tkinter import messagebox
import webbrowser
from tkinter import Menu


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
#================================================root2b functions ends
#root2b_fun()

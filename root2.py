#====================================================Importing Libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from root3 import root3_fun
from tkinter import Menu
from tkinter import  Menu
import webbrowser
from tkinter import scrolledtext

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
#=========================================================Root2 Function Ends

#root2_fun()
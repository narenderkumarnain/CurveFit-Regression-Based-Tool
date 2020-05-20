#====================================================Importing Libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from root2 import root2_fun
from root2b import root2b_fun
from tkinter import Menu
import webbrowser

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

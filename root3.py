#======================================Importing Libraries
import tkinter as tk
from tkinter import ttk
from root4 import root4_fun
from tkinter import Menu
import webbrowser
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
#==================================================root3 function ends
#root3_fun([1] , [1])
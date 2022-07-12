# Python program to create a table

from tkinter import *
headings=("TIME & PERIODS","SUBJECTS & STREAMS","FACULTY NAME","ROOM NO")

def result(lst,shNo):
    lst.insert(0,headings)
    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    if(i==0):
                        self.e = Entry(root, width=60, fg='Blue',
                                       font=('Arial', 10, 'bold'))
                    else:
                        self.e = Entry(root, width=60, fg='Black',
                                   font=('Arial', 10, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])




    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    root.iconbitmap("uem.ico")
    root.title(shNo+", "+"Number of classes : "+str(len(lst)-1))
    t = Table(root)
    root.mainloop()

from tkinter import *
from source import *
root=Tk()
root.title('KNIGHT\'S TOUR ')
root.iconbitmap('Iconsmind-Outline-Knight.ico')
root.geometry("240x480")
root.configure(bg='black')
#colours in either name or #+hex values
#bg= background fg= foreground
my_label=Label(root, text='KNIGHT\'S TOUR',fg='white',bg='black').grid(row=0,column=0)
my_label2=Label(root, text='Do you want to find the solution?...',fg='white',bg='black').grid(row=1,column=0)
#to create spaces
idk=Label(root,text='',bg='black').grid(row=2,column=0)
class Table: 
         
    def __init__(self,root,matrix): 

        # code for printing the solution matrix
        for i in range(len(matrix)): 
            for j in range(len(matrix)): 
                 
                self.e = Entry(root, width=16, fg='blue', 
                            font=('Arial',10,'bold')) 
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, matrix[i][j]+1)    

def click():
    newWindow = Toplevel(root)
    newWindow.title("SOLUTION")
    t1=int(bdim.get())
    t2=int(brow.get())
    t3=int(bcol.get())
    matrix=solve(t1,t2,t3)
    if matrix==2:
        tree=Label(newWindow,text='Solution does not exist :( !').grid(row=0,column=0)
    else:
        t = Table(newWindow,matrix) 

temp1=Label(root,text="Enter the dimensions of the chess-board!",fg='red',bg='white').grid(row=3,column=0)
bdim=Scale(root,from_= 0, to=15,orient=HORIZONTAL,bd=3)
bdim.grid(row=4,column=0)
idk=Label(root,text='',bg='black').grid(row=5,column=0)
temp2=Label(root,text="Starting Row",fg='red',bg='white').grid(row=6,column=0)
brow=Scale(root,from_= 0, to=15,orient=HORIZONTAL,bd=3 )
brow.grid(row=7,column=0)
idk=Label(root,text='',bg='black').grid(row=8,column=0)
temp3=Label(root,text="Starting column",fg='red',bg='white').grid(row=9,column=0)
bcol=Scale(root,from_= 0, to=15,orient=HORIZONTAL,bd=3)
bcol.grid(row=10,column=0)
idk=Label(root,text='',bg='black').grid(row=11,column=0)
Button(root,text="SOLUTION",command=click,fg='Black',bg='green',padx=30,pady=5).grid(row=12,column=0)
idk=Label(root,text='',bg='black').grid(row=13,column=0)
idk=Label(root,text='',bg='black').grid(row=14,column=0)
idk=Label(root,text='',bg='black').grid(row=15,column=0)
Button(root,text="EXIT",bg='blue',fg='black',command=root.quit).grid(row=16,column=0)
#padx determines size in x and pady size in y
root.mainloop()
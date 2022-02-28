import tkinter as tkr
#from tkinter import ttk
app=tkr.Tk(__name__)
app.title('Calculator')
app.geometry('300x400')

def calc():
    print('msg is :',msg.get())
    print('Entry box :',entry.get())
    print('Entry box :',entry1.get())
    print('Radio Button :',option.get())
    print('Result :',entry2.get())     

    calculation()

def calculation():
##    res=eval(entry+option.get()+entry1)
##    print("Calculation :",res)

    c=str(entry.get())
    d=str(entry1.get())
    exp=eval(c+option.get()+d)
    print('Calculation: ',exp)
    tkr.Label(app,text=exp,font=(80)).pack()

#message
msg=tkr.Variable(app)
msg.set('Your calculator is ready')
tkr.Message(app,textvariable=msg,width=100).pack()

#entry box
tkr.Label(app,text = 'Number 1').pack()


entry=tkr.Variable(app)
tkr.Entry(app,textvariable=entry,font=(30),width=15).pack()
tkr.Label(app,text='Number 2').pack()

entry1=tkr.Variable(app)
tkr.Entry(app,textvariable=entry1,font=(30),width=15).pack()

#radio button
option=tkr.Variable(app,'0')
rb_values={'+':'+','-':'-','*':'*','/':'/','%':'%'}
for k,v in rb_values.items():
    tkr.Radiobutton(app,text=k,variable=option,value = v).pack()

# button
tkr.Button(app,text='Calculate',command=calc).pack()

#result
tkr.Label(app,text='Result').pack()
entry2=tkr.Variable(app)

app.mainloop()

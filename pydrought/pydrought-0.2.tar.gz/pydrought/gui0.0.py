# -*- coding: cp1256 -*-
import os
try:
    import Tkinter as tk
    import  tkFileDialog as filedialog
    import ttk
except:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import ttk

#################   
root = tk.Tk()
##root.title(u'محاسبه شاخص خشکسالي')
root.title(u'محاسبه شاخص خشکسالي')
nb=ttk.Notebook(root)

page1=tk.Frame(nb, width=450, height=300)
page1.pack_propagate(False)
page2 = tk.Frame(nb, width=450, height=300)
page2.pack_propagate(False)
##page3 = tk.Frame(nb, width=450, height=300)
##page3.pack_propagate(True)
nb.add(page1,text="SPI")
nb.add(page2,text="SPEI")
##nb.add(page3,text="Explanation")
nb.pack(expand=1, fill="both")

##input##############
label0= tk.Label(nb, text=u"فايل ورودي"  ,
                fg="white",bg="blue",
                anchor = "w")
inFile = tk.StringVar()
inFile.set(u"فايل ورودي" )
entry0=tk.Entry(nb,textvariable=inFile)
################
logo = tk.BitmapImage("data/gorganuni.gif", foreground='red')
logol=tk.Label (page3,compound = tk.CENTER, image=logo )
logol.grid(row=0,column=0)
########Open file###############
def Open():
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),
                                          title = "Select file",
                                          filetypes = (("CSV files","*.csv"),
                                                       ("all files","*.*")))
    inFile.set(filename)
    data=util.readcsv(inFile.get())
    choise=list(data)
    print(choise)
    choise.append("")
    
    menu1 = rainPop["menu"]
    menu1.delete(0, "end")
    menu2 = datePop["menu"]
    menu2.delete(0, "end")    
    if tab=='.!notebook.!frame2':
        menu10 = tempPop["menu"]
        menu10.delete(0, "end")
        menu11 = tempMinPop["menu"]
        menu11.delete(0, "end")
        menu12 = tempMaxPop["menu"]
        menu12.delete(0, "end")
        
    for string in choise:
        menu1.add_command(label=string,
                          command=lambda value=string: field1.set(value))
        menu2.add_command(label=string,
                          command=lambda value=string: field2.set(value))
        if tab=='.!notebook.!frame2':
            menu10.add_command(label=string,
                          command=lambda value=string: field1mean.set(value))
            menu11.add_command(label=string,
                          command=lambda value=string: field1min.set(value))
            menu12.add_command(label=string,
                          command=lambda value=string: field1max.set(value))
    field1.set(choise[0])
    field1mean.set(choise[1])
    field1min.set(choise[2])
    field1max.set(choise[3])
    field2.set(choise[-2])
    text.insert(tk.END,"You selected "+ inFile.get()+ " as input file\n")
    
btn1 = ttk.Button(nb,text="Open", style="C.TButton",command=Open)
##########Select  Field##########
labelrain = tk.Label(nb, text="Rain")
choices = {"Select a Field"}
field1 = tk.StringVar()
rainPop= tk.OptionMenu(nb, field1, *choices)
labelT = tk.Label(nb, text="Tmean")
field1mean = tk.StringVar()
tempPop = tk.OptionMenu(page2, field1mean, *choices)
field1min = tk.StringVar()
labelTmin = tk.Label(nb, text="Tmin ")
tempMinPop = tk.OptionMenu(page2, field1min, *choices)
labelTmax = tk.Label(nb, text="Tmax ")
field1max = tk.StringVar()
tempMaxPop = tk.OptionMenu(page2, field1max, *choices)
field2 = tk.StringVar()
labeld=tk.Label(nb, text="Date")

Freq=tk.StringVar()
def showFreq(event):
    try:
        #print(field2.get())
        data=util.readcsv(inFile.get())
        date=data[field2.get()]
        dif=date[1]-date[0]
        days=dif.days
        if days>=28:
            Freq.set("monthly")
            freq=Freq.get()
            
        else:
            Freq.set(str(days))
            freq=Freq.get()+" Daily"
        labelfreq.config(text=" Frequency: {} ".format(freq))
        labelfreq.grid(row=0,column=3,sticky='W',in_=tab)
    except:
        labelfreq.grid_remove()

    
    
datePop = tk.OptionMenu(nb, field2, *choices,)    
datePop.bind("<Configure>", showFreq)
datePop.bind("<1>",showFreq)
datePop.bind("<<OptionMenuSelect>>", showFreq)

##datePop.bind('<<OptionMenuChanged>>',showFreq)

datePop.bind('<ButtonRelease>',showFreq)

labelfreq=tk.Label(nb,bg="red")
##################################
time=["monthly", "16 daily" , "8 daily"]
times=["monthly", 16 , 8]
v =tk.StringVar()
v.set(times[0])
rb1 = ttk.Radiobutton(nb, text=time[0], variable=v,value=times[0])
rb2 = ttk.Radiobutton(nb, text=time[1], variable=v,value=times[1])
rb3 = ttk.Radiobutton(nb, text=time[2],variable=v, value=times[2])
#############distribution############

labeldist=tk.Label(nb, text="توزيع آماري")
distvar = tk.StringVar()
distsCom = ttk.Combobox(nb, textvariable=distvar)
distvar.set("Select  a distribution")
def disturibution(event):
    global fit
    if distvar.get()=="Log Logistics":
        fit=util.LLfit
    elif distvar.get()=="Pearson Type 3":
        fit=util.pe3fit
    elif distvar.get()=="Gamma 2 Parametrs":
        fit=util.gammafit
        
          
distsCom.bind('<<ComboboxSelected>>', disturibution)

##########Scales############################
label2= tk.Label(nb,text=u"گام زماني",fg="white",bg="blue")
inScale = tk.StringVar()
entry2=tk.Entry(nb,textvariable=inScale)
def evaluate(event):
    print(inScale.get())
entry2.bind("<Leave>", evaluate)

labelLat= tk.Label(nb,text=u"عرض جغرافيايي",fg="white",bg="blue")
inLat= tk.DoubleVar()
inLat.set( 37.6475)
entry20=tk.Entry(nb,textvariable=inLat)

###########Select scales#############
def onClick():
    scales1=[]
    inScale.set("")
    for key in chk:
        if   "var" in key :
            key=chk[key].get()
            scales1.append(key)
    scales1=sorted([int(i) for i in scales1 if str(i)])
    inScale.set(",".join([str(i) for i in scales1 ]))
    
scales=[1,3,6,9,12,24]
chk={}
k=0
for scale in scales:
    chk["var{}".format(scale)] = tk.StringVar()
    chk[str(scale)]= tk.Checkbutton(nb, text=str(scale),
                                    variable=chk["var{}".format(scale)],
                                    command=onClick,
                                    onvalue=str(scale), offvalue="")

########Output File###########
label3= tk.Label(nb,text=u"فايل خروجي",fg="white",bg="blue")


def Save():
    outfilename = filedialog.asksaveasfilename(initialdir = os.getcwd(),
                                               title = "Select Output file",
                                                filetypes = (("CSV files","*.csv"),("all files","*.*")))
    if not outFile.get() .endswith(".csv"):
        outFile.set(outfilename+".csv")
    #text.delete(1.0,2.0)
    text.insert(tk.END,"You selected "+ inFile.get()+ " as input file\n"+outFile.get() +" as output\n"+ inScale.get() +" as scales"  )
outFile = tk.StringVar()
outFile.set(u"فايل خروجي" )
entry3=tk.Entry(nb,textvariable=outFile)

btn3= ttk.Button(nb,text="Save", style="C.TButton",
                 command=Save)
text = tk.Text(nb, height=4, width=50)
##S.config(command=T.yview)
##T.config(yscrollcommand=S.set)



########Run program##########
import spi,spei
import util
def Calculate():
    data=util.readcsv(inFile.get())
##    global dates
##    global rain
    rain=data[field1.get()]
    dates=data[field2.get()]
    dates2=data[field2.get()]
    if Freq.get() ==v.get()=="monthly":
        print("Calculation monthly Values")
    elif Freq.get() !=v.get():
        print("Convertig rain file from {} into {}  scales".format(Freq.get() ,v.get()))
        rain,dates=util.resample(rain,dates , by=v.get())
    scales=list(map(int,inScale.get().split(",")))
    lat=inLat.get()
##    global values
    if  tab=='.!notebook.!frame2':
        
        print("Calculating SPEI")
        if field1mean.get()=="":
            temp=[(t1+t2)/2 for t1,t2 in zip(data[field1min.get()],data[field1max.get()])]
        else:
            temp=data[field1mean.get()]
        if Freq.get() !=v.get():
            print("Convertig  from {} into {}  scales".format(Freq.get() ,v.get()))
            temp,dates=util.resample(temp,dates2 , by=v.get())
        values, cols=spei.SPEI(rain, temp,dates,lat ,scales).calculate( fit=fit)
        util.write(values,outFile.get(),cols)
    else:
        print("Calculating SPI")
        values, cols=spi.SPI(rain, dates ,scales).calculate(fit=fit)
        util.write(values,outFile.get(),cols)
    print ('SPI is calcualted and saved in {}'.format(outFile.get()))
    
btn4= ttk.Button(nb,text="Calculate", style="C.TButton",
                 command=Calculate)
btn4.bind("<1>", showFreq)


btn5= ttk.Button ( nb,text="Close", command=root.destroy)
T = tk.Text(nb, height=4, width=50)



############Menus###############
menubar = tk.Menu(nb )
file = tk.Menu(menubar, tearoff = 2) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Open...', command = Open) 
file.add_command(label ='Save', command = Save) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy)
root.config(menu=menubar)

#########Pack/Grid #########
def display(event):
    global tab
    tab = nb.tabs()[nb.index('current')]
    label0.grid(row=0,column=0,sticky='W',in_=tab)
    entry0.grid(row=0,column=1,sticky='W',in_=tab)
    btn1.grid(row=0,column=2,sticky='W',in_=tab)
    
    labelrain.grid(row = 1, column = 0,in_=tab)
    rainPop.grid(row = 2, column =0,in_=tab)
    labeld.grid(row = 1, column =1,in_=tab)
    datePop.grid(row = 2, column =1,in_=tab)
    if tab=='.!notebook.!frame2':
        labelT.grid(row = 1, column =2,in_=tab)
        tempPop.grid(row = 2, column =2,in_=tab)
        labelTmin.grid(row = 1, column =3,in_=tab)
        tempMinPop.grid(row = 2, column =3,in_=tab)
        labelTmax.grid(row = 1, column =4,in_=tab)
        tempMaxPop.grid(row = 2, column =4,in_=tab)
        labelLat.grid(row = 4, column =3,in_=tab)
        entry20.grid(row=4,column=4,sticky='W',in_=tab)
    rb1.grid(row=3,column=0,sticky='W',in_=tab)
    rb2.grid(row=3,column=1,sticky='W',in_=tab)
    rb3.grid(row=3,column=2,sticky='W',in_=tab)
    
    labeldist.grid(row = 4, column =0,in_=tab)
    distsCom.grid(row = 4, column =1,in_=tab)
    if tab=='.!notebook.!frame2':
        distsCom["values"]=["Log Logistics", "Pearson Type 3"]
    else:
          distsCom["values"]=["Gamma 2 Parametrs"]
        
    label2.grid(row=5,column=0,sticky='W',in_=tab)
    entry2.grid(row=5,column=1,sticky='W',in_=tab)
    
    
    
    k=0
    for scale in scales:
        chk[str(scale)].grid(row=6,column=k,in_=tab)
        chk[str(scale)].deselect()
        k+=1


    label3.grid(row=7,column=0,sticky='W',in_=tab)
    entry3.grid(row=7,column=1,sticky='W', in_=tab)
    btn3.grid(row=7,column=2,sticky='W',in_=tab)
    btn4.grid(row=8,column=1,sticky='W',in_=tab)
    btn5.grid(row=8,column=2,sticky='W',in_=tab)

    text.grid(row=9,column=0,columnspan=10,sticky='W',in_=tab)#rowspan=10
    text.grid_propagate(True)
    #ttk.Sizegrip(nb).grid(column=33, row=33, sticky=(tk.S,tk.E))
    
##    text.grid_bbox(row=9, column=0,  col2=None, row2=None)
    
    
   

nb.bind('<<NotebookTabChanged>>', display)


root.mainloop()
##    

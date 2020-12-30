from pylab import *
from scipy.integrate import quad 
import numpy as np 
from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt



class Milieu(object): 
    def __init__(self, a, b, n, f,c):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.c = c

    def integrate(self,f):
        x=self.x
        h = float(x[1] - x[0])
        s=0
        for i in range(self.n):
            s=s+f((x[i]+x[i+1])*0.5)
        return h*s
       
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl=f(xl);
        xlist_fine=np.linspace(self.a, self.b, resolution)
        
        for i in range(self.n):
            
            m=(xl[i]+xl[i+1])/2
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] 
            y_rect = [0   , f(m), f(m)  , 0     , 0   ] 
            self.c.plot(x_rect, y_rect,"b")
            yflist_fine = f(xlist_fine)
            self.c.plot(xlist_fine, yflist_fine)
            self.c.plot(m,f(m),"y*")
            
            self.c.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )
            



class Rectangle(object): 
    def __init__(self, a, b, n, f,c):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.c = c

    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h * s
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] 
            y_rect = [0   , yl[i], yl[i]  , 0     , 0   ] 
            self.c.plot(x_rect, y_rect,"g")
        yflist_fine = f(xlist_fine)
        self.c.plot(xlist_fine, yflist_fine)
        self.c.plot(xl, yl,"rd")
  
     
        self.c.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )


class Trapezoidal(object):
    def __init__(self, a, b, n, f,c):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
        self.c = c
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] 
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] 
            self.c.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        self.c.plot(xlist_fine, yflist_fine)
        self.c.plot(xl, yl,"cs")
        
        self.c.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )

        
        


class Simpson(object):
    def __init__(self, a, b, n, f, c): 
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n 
        self.c = c

    def integrate(self,f):
        x=self.x 
        y=f(x)
        h = float(x[1] - x[0])
        n = len(x) - 1
        if n % 2 == 1:
            n =n-1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
       
        return h * s / 3.0
    def Graph(self,f,resolution=1001):
        xl = self.x 
        yl = f(xl) 
        xlist_fine=np.linspace(self.a, self.b, resolution)
       
        for i in range(self.n):
            x1=np.linspace(xl[i], xl[i+1], resolution)
            m=(xl[i]+xl[i+1])/2
            bg=xl[i]
            bd=xl[i+1]
            l0 = (x1-m)/(bg-m)*(x1-bd)/(bg-bd)
            l1 = (x1-bg)/(m-bg)*(x1-bd)/(m-bd)
            l2 = (x1-bg)/(bd-bg)*(x1-m)/(bd-m)
            P = f(bg)*l0 + f(m)*l1 + f(bd)*l2
            self.c.plot(x1,P,'b')
            self.c.plot(m,f(m),"g*")
        yflist_fine = f(xlist_fine)
        self.c.plot(xlist_fine, yflist_fine,'b')
        self.c.plot(xl, yl,'r')
        
      
        self.c.text( 0.5*( self.a+ self.b ) , f(self.b ) , 'I_{} ={:0.8f}'.format(self.n,self.integrate( f ) ) , fontsize =15 )





import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,highlightbackground="gray", highlightthickness=2, width=100, height=100, bd= 5)
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=100, height=100, bd= 5)
        self.func_txt=StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4)
        self.label_func.grid(row=1,column=0)
        
        self.a_txt=StringVar()
        self.a_txt.set("la valeur de a :")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4)
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxa.grid(sticky = W,row=2,column=1)
       
    
        self.b_txt=StringVar()
        self.b_txt.set("la valeur de b:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4)
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxb.grid(sticky = W,row=3,column=1)
        
        self.n_txt=StringVar()
        self.n_txt.set("Nombre des points:")
        self.label_n=Label(self.fr1, textvariable=self.n_txt,justify=RIGHT, anchor="w", height=4)
        self.label_n.grid(sticky = E,row=4,column=0)
        self.boxn = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxn.grid(sticky = W,row=4,column=1)
        
        
        
        self.box = Entry(self.fr1,borderwidth=3,bg="powder blue")
        self.box.grid(row=1,column=1)
        self.button = Button (self.fr1, width =35,text="Afficher",bg="powder blue", command=self.plot)
        self.button.grid(row=5,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fig = Figure(figsize=(10,10))
        
        
        self.a = self.fig.add_subplot(221)
        self.b = self.fig.add_subplot(222)
        self.c = self.fig.add_subplot(223)
        self.d = self.fig.add_subplot(224)
        self.a.set_title ("Méthode Rectangle Gauche", fontsize=14)
        self.b.set_title ("Méthode Trapèze", fontsize=14)
        self.c.set_title ("Méthode Simpson", fontsize=14)
        self.d.set_title ("Méthode Points Milieux", fontsize=14)
        
   
        self.a.set_ylabel("y=f(x)", fontsize=16)
        self.a.set_xlabel("x", fontsize=16)
        self.a.set_facecolor("pink")
        
        self.b.set_ylabel("y=f(x)", fontsize=14)
        self.b.set_xlabel("x", fontsize=14)
        self.b.set_facecolor("pink")
        
        self.c.set_ylabel("y=f(x)", fontsize=14)
        self.c.set_xlabel("x", fontsize=14)
        self.c.set_facecolor("pink")
        
        self.d.set_ylabel("y=f(x)", fontsize=14)
        self.d.set_xlabel("x", fontsize=14)
        self.d.set_facecolor("pink")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot (self):
        f= lambda x: eval(self.box.get())
        x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        pp=f(x)
        self.a.cla()
        self.b.cla()
        self.c.cla()
        self.d.cla()

        aa = float(self.boxa.get())
        bb = float(self.boxb.get())
        nn = int(self.boxn.get())
        
        R=Rectangle(aa,bb,nn,f,self.a)
        M=Milieu(aa,bb,nn,f,self.b)
        T=Trapezoidal(aa,bb,nn,f,self.c)
        S=Simpson(aa,bb,nn,f,self.d)
       
        
        
        R.Graph(f)
        S.Graph(f)
        M.Graph(f)
        T.Graph(f)
   
       
        
        self.a.set_title ("Méthode Rectangle Gauche", fontsize=16)
        self.b.set_title ("Méthode mileu", fontsize=16)
        self.c.set_title ("Méthode Trapeze", fontsize=16)
        self.d.set_title ("Méthode Simpson", fontsize=16)
        
        self.a.grid(True)
        self.b.grid(True)
        self.c.grid(True)
        self.d.grid(True)
        

        self.fig.canvas.draw()
        


        
        

        
   
        
        
        
        

window= Tk()

start= mclass(window)

window.mainloop()
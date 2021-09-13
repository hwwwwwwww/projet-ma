# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt

    

def ex1_1(n,pr):
    u=0
    print("U 0 =",u)
    for i in range(n-1):
        u=u+numpy.random.choice(a=[-1,1], p=[1-pr,pr])
        print("U",i+1,"=",u)
        
def ex1_2(n,pr):
    u=0
    max=u
    min=u
    print("U 0 =",u)
    for i in range(n-1):
        u=u+numpy.random.choice(a=[-1,1], p=[1-pr,pr])
        print("U",i+1,"=",u)
        if u>max:
            max=u
        if u<min:
            min=u
    print("min=",min)
    print("max=",max)
    
def ex2_2(N,n,pr):
    for i1 in range(N):
        print("Marche aléatoire n°",i1+1)
        u=0
        max=0
        min=0
        #print("U 0 =",u)
        for i in range(n-1):
            u=u+numpy.random.choice(a=[-1,1], p=[1-pr,pr])
            #print("U",i,"=",u)
            if u>max:
                max=u
            if u<min:
                min=u
        print("min=",min)
        print("max=",max)
        
def ex2_3(N,n,pr):
    for i1 in range(N):
        print("Marche aléatoire n°",i1+1)
        x=range(n)
        y=[0]
        u=0
        max=0
        min=0
        #print("U 0 =",u)
        for i in range(n-1):
            u=u+numpy.random.choice(a=[-1,1], p=[1-pr,pr])
            #print("U",i,"=",u)
            y.append(u)
            if u>max:
                max=u
            if u<min:
                min=u
        print("min=",min)
        print("max=",max)
        plt.plot(x,y)
    plt.show()
    
def ex3_1(n,pr):
    t=[0]
    l0=0
    u=0
    print("U 0 =",u)
    for i in range(n-1):
        u=u+numpy.random.choice(a=[-1,1], p=[1-pr,pr])
        print("U",i+1,"=",u)
        if u==0:  
            t.append(i+1-l0)
            l0=i+1
     for i in range (0,t.__sizeof__()):
         print("temps de retour :",t[i]) 
           
        

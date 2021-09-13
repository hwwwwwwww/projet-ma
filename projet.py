# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
def marche_aléatoire_z1(N,n,pr):
    for i1 in range(N):
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
    plt.plot(x,y,'g-.')
    plt.show()
    

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
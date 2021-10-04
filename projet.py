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
    for i in range (0,len(t)):
        print("temps de retour :",t[i]) 
         
def ex3_2(N,n,pr):
    t=[0]
    for i1 in range(N):
        
        l0=0
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
            if u==0:  
                t.append(i+1-l0)
                l0=i+1
        print("min=",min)
        print("max=",max)
        for i in range (0,len(t)):
            print("temps de retour :",t[i])
        t.clear()
        
def ex4_1(n):
    r=0
    x=0
    y=0
    for i in range(n-1):
        r=numpy.random.choice(a=[0,1,2,3], p=[0.25,0.25,0.25,0.25])
        if r==0:
            x+=1
        elif r==1:
            x-=1
        elif r==2:
            y+=1
        elif r==3:
            y-=1
        print("x =",x," / y =",y)
        
def ex4_2(N,n):
    for i1 in range(N):
        print()
        print("Marche aléatoire n°",i1+1)
        r=0
        x=0
        y=0
        t=[0]
        l0=0
        for i in range(n-1):
            r=numpy.random.choice(a=[0,1,2,3], p=[0.25,0.25,0.25,0.25])
            if r==0:
                for i in range(10):
                    x+=0.1
                    plt.plot(x,y,'b-')
            elif r==1:
                for i in range(10):
                    x-=0.1
                    plt.plot(x,y,'b-')
            elif r==2:
                for i in range(10):
                    y+=0.1
                    plt.plot(x,y,'b-')
            elif r==3:
                for i in range(10):
                    y-=0.1
                    plt.plot(x,y,'b-')
            if int(x)==0 and int(y)==0:  
                t.append(l0)
                l0=0
            l0+=1
            #print("x =",x," / y =",y)
            plt.plot(x,y,'ko')
        for i in range (1,len(t)):
            print("temps de retour :",t[i])
        s=0
        for i in range (1,len(t)):
            s+=t[i]
        s/=len(t)
        print("moyenne de temps de retour en 0 = ", s)
        print("nombre de retour en 0 = ",len(t))
        
            
    plt.plot(0,0,'go')
    plt.show()
        
        
def ex5(n):
    r=0
    x=0
    X=[0]
    y=0
    Y=[0]
    z=0
    Z=[0]
    t=[0]
    l0=0
    tX=[0]
    tY=[0]
    tZ=[0]
    
    for i in range(n):
        r=numpy.random.choice(a=[0,1,2,3,4,5], p=[1/6,1/6,1/6,1/6,1/6,1/6])
        tx=x
        ty=y
        tz=z
        if r==0:
            for i in range(10):
                tx+=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            x+=1
            
        elif r==1:
            for i in range(10):
                tx-=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            x-=1
                
        elif r==2:
            for i in range(10):
                ty+=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            y+=1
            
        elif r==3:
            for i in range(10):
                ty-=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            y-=1
            
        elif r==4:
            for i in range(10):
                tz+=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            z+=1
            
        elif r==5:
            for i in range(10):
                tz-=0.1
                tX.append(tx)
                tY.append(ty)
                tZ.append(tz)
            z-=1
            
        if x==0 and y==0 and z==0:  
            t.append(l0)
            l0=0
        l0+=1
        print("x =",x," / y =",y," / z =",z)
        X.append(x)
        Y.append(y)
        Z.append(z)
    for i in range (0,len(t)):
            print("temps de retour :",t[i])
    ax = plt.axes(projection='3d') 
    ax.plot(tX,tY,tZ,'b-') 
    #ax.plot(X,Y,Z,'ko')
    ax.plot3D(0,0,0,'go')
    ax.plot3D(x,y,z,'ro')
    plt.show()
           
        

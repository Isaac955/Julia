# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:10:04 2021

@author: Isaac
"""
from PIL.Image import *
from math import*
L,H=800,800
x_min,x_max=-2,2
y_min,y_max=-2,2
couleur1=(255, 158, 0) 
couleur2=(255, 0, 0)
MAX_ITERATION=40

def colorpixel(image,x,y,couleur):
    image.putpixel((x,y),couleur)
    
def distanceOMN(Cx,Cy,n,x0,y0):
    x,y=Calculcoord(Cx,Cy,n,x0,y0)
    return sqrt(x**2+y**2)

def conversion(x,y):
    u=x_min+x*(x_max-x_min)/L
    v=y_max-y*(y_max-y_min)/H
    return u,v

def Calculcoord(Cx,Cy,n,x0,y0):
    x,y=x0,y0
    for i in range(n):
        temp=x
        x=x**2-y**2+Cx
        y=2*temp*y+Cy
    return (x,y)

def Julia(MAX_ITERATION):
    image=new('RGB',(L,H))
    for x in range (L):
        for y in range(H):
            u,v=conversion(x,y)
            n=0
            d=distanceOMN (Cx,Cy,n,u,v)
            while d<2 and n<MAX_ITERATION:
                d=distanceOMN(Cx,Cy,n,u,v)
                n=n+1
            if n==MAX_ITERATION:
                colorpixel(image,x,y,couleur1)
                
            else:
                colorpixel(image,x,y,couleur2)
    image.show()
Cx,Cy=0.3,0.5

Julia(10)
            
            
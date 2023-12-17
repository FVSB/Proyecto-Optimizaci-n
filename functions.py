import numpy as np


class BoxBettsFun:
    def __init__(self,n) -> None:
        self.n=n
        self.x0 = np.ones(3)*0.5 # initial point
        self.bl = np.array([0.9, 9, 0.9]) # lower bounds
        self.bu = np.array([1.2, 11.2, 1.2]) # upper bounds
        self.bounds = list(zip(self.bl, self.bu)) # box constraints
    def f(self,x):
        s= 0
        for i in range(1,self.n):
            s += self.__g(x,i)
        return s
    
    def __gi(self,i,xi):
        return np.exp(-0.1*(i+1)*xi)

    def __g(self,x,i): # objective function
    
        g1=self.__gi(i,x[0])
        g2=self.__gi(i,x[1])
        g31=-0.1*(i+1)
        g32=np.exp(-(i+1))
        g3=np.exp((g31-g32)*x[2])
        g =  g1- g2-g3
        return g**2
    
   
        
        
    
    
class ChungReynolds:
    
    def __init__(self,n) -> None:
        self.n=n
        # Generate a random initial guess
        self. x0 = np.random.uniform(-10, 10,self. n)
        #Bounds
        self.bounds = [(-100, 100) for _ in range(self.n)]

    def f(self,x):
        value=0
        for i in range(1,self.n+1):
            value+=self.__chung_reynolds(x)
        return value
        
    def __chung_reynolds(self,x):
        x=np.array(x)
        x2=np.square(x)
        return np.sum(x2)**2


    def __chung_reynolds_grad(self,x):
        return 4 * np.sum(x**2) * x
    
    


class BrentFunction:
    
    def __init__(self,n) -> None:
         self.n=n
         self.x0 = [0.01, 0.01]
         self.bounds=[(-10,10) for _ in range(2)]
    
    def f(self,x):
        return self.__brent_function(x)
    # Definir la función Brent
    def __brent_function(self,x):
     return ((x[0] + 10)**2) + ((x[1] + 10)**2) + (np.exp(-(x[0]**2) - (x[1]**2)))
 
 
 
class BrownFunction:
     
     
     def __init__(self,n) -> None:
         self.n=n
         self. x0 = np.random.uniform(-0.9,3.9,self. n)
         # Definiendo las restricciones de límites para cada variable
         self.bounds = [(-1, 4) for _ in range(self.n)]  # Suponiendo 10 dimensiones, puedes ajustarlo a tus necesidades

         
     def f(self,x):
         return self.__brown_function(x)
     
     def __brown_function(self,x):
   
        result = 0
        for i in range(1,self.n-1):
            result += (x[i]**2)**(x[i+1]**2 + 1) + (x[i+1]**2)**(x[i]**2 + 1)
        return result

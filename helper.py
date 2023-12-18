import pandas as pd
from openpyxl import load_workbook
import time
from scipy.optimize import minimize
import os





def get_data(res,execution_time_ms):
     return pd.DataFrame({
              "Resultado de cada variable": res.x,
              "Óptimo": res.fun,
              'Tiempo de Ejecución': execution_time_ms,
              'Número de Iteraciones':res.nit
              })


def optimizeFun(f,x0,bounds,method_name,n,exercise):
        start_time = time.perf_counter()
        res =  minimize(fun=f, x0=x0, bounds=bounds, method=method_name) 
        end_time = time.perf_counter()
        execution_time_ms = int((end_time - start_time) * 1000)
        data =get_data(res, execution_time_ms)
        #toLatex(data,method_name,n,exercise)
        toExcel(data,method_name,n,exercise)
        return data,method_name
        #options={'gtol': 1e-8}
        
        
        
def toLatex(dataframe,method_name,n,exercise):
       
       # Construye la ruta completa del archivo
        ruta = os.path.join('Ejercicio' + exercise, 'conMetodo' + method_name, 'con_n' + str(n) + 'output.tex')

        # Verifica si la ruta existe
        if not os.path.exists(os.path.dirname(ruta)):
         # Si la ruta no existe, la crea
          os.makedirs(os.path.dirname(ruta), exist_ok=True)

        # Abre el archivo en la ruta
        with open(ruta, 'w') as f:
        # Itera sobre cada DataFrame
        # Escribe el Numero de D
         value='{Con D = '+f'{n}'+'}'
         f.write(f'\section{value}')
         # Exporta el DataFrame a LaTeX
         latex = dataframe.to_latex()
         # Escribe el LaTeX en el archivo .tex
         f.write(latex)

def toExcel(dataframe,method_name,n,exercise):
        
        # Construye la ruta completa del archivo
        ruta = os.path.join('Ejercicio' + exercise, 'conMetodo' + method_name, 'con_n' + str(n) + 'output.xlsx')

        # Verifica si la ruta existe
        if not os.path.exists(os.path.dirname(ruta)):
         # Si la ruta no existe, la crea
         os.makedirs(os.path.dirname(ruta), exist_ok=True)

        # Guarda el DataFrame en el archivo
        dataframe.to_excel(ruta, index=False)
        
        
        

Nelder_Mead=lambda f,x0,bounds,n,e:optimizeFun(f=f,x0=x0,bounds=bounds,method_name='Nelder-Mead',n=n,exercise=e)
SLSQP=lambda f,x0,bounds,n,e: optimizeFun(f=f,x0=x0,bounds=bounds,n=n,method_name='SLSQP',exercise=e) 
L_BFGS_B=lambda f,x0,bounds,n,e:optimizeFun(f=f,x0=x0,bounds=bounds,n=n,method_name='L-BFGS-B',exercise=e)

def Test(fun,min_value,excercise,methods=[SLSQP,L_BFGS_B,Nelder_Mead],method_names=['SLSQP','L_BFGS_B','Nelder_Mead'],have_bounds=[True,True,False], d=[10,100,500,1000]):
       data=[]
       method=[]
       for n in d:
              print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
              print("Valor de N=",n)
              print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
              for i, met in enumerate(methods):
                     f=fun(n)
                     fx=f.f
                     x0=f.x0
                     bounds=f.bounds
                     if(not have_bounds[i]):
                             bounds=None
                     data,method=met(f=fx,x0=x0,bounds=bounds,n=n,e=excercise)
              
                     print(method,'\n')
                     print(data,'\n')
                     print("*****************************************************************************************")
                     print('\n')
       f=fun(len(min_value))
       fx=f.f

       print('Fx in the global minimun',fx( min_value ))

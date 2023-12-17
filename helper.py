import pandas as pd
from openpyxl import load_workbook
import time
from scipy.optimize import minimize






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
        toLatex(data,method_name,n,exercise)
        toExcel(data,method_name,n,exercise)
        return data,method_name
        #options={'gtol': 1e-8}
        
        
        
def toLatex(dataframe,method_name,n,exercise):
       
        # Abre el archivo .tex en modo escritura
        with open(F'Ejercicio{exercise}conMetodo{method_name}con_n{n}output.tex', 'w') as f:
                # Itera sobre cada DataFrame
                        #Escribe el Numero de D
                        value='{Con D = '+f'{n}'+'}'
                        f.write(f'\section{value}')
                        # Exporta el DataFrame a LaTeX
                        latex = dataframe.to_latex()
                        # Escribe el LaTeX en el archivo .tex
                        f.write(latex)

def toExcel(dataframe,method_name,n,exercise):
        
        dataframe.to_excel(F'Ejercicio{exercise}conMetodo{method_name}con_n{n}output.xlsx', index=False)
        
        
        

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

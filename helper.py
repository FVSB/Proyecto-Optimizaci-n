import pandas as pd
import time
from scipy.optimize import minimize






def get_data(res,execution_time_ms):
     return pd.DataFrame({
              'Variables Result': res.x,
              "Optimo": res.fun,
              'Execution Time': execution_time_ms
              })


def optimizeFun(f,x0,bounds,method_name):
        start_time = time.perf_counter()
        res =  minimize(fun=f, x0=x0, bounds=bounds, method=method_name) 
        end_time = time.perf_counter()
        execution_time_ms = int((end_time - start_time) * 1000)
        return get_data(res, execution_time_ms),method_name
        #options={'gtol': 1e-8}
        
        
        
def toLatex(dataframes,n):
       
        # Abre el archivo .tex en modo escritura
        with open('output.tex', 'w') as f:
                # Itera sobre cada DataFrame
                for i, df in enumerate(dataframes):
                        #Escribe el Numero de D
                        value='{Con D = '+f'{n}'+'}'
                        f.write(f'\section{value}')
                        # Exporta el DataFrame a LaTeX
                        latex = df.to_latex()
                        # Escribe el LaTeX en el archivo .tex
                        f.write(latex)
                        # Añade un espacio en blanco entre los DataFrames
                        if i < len(dataframes) - 1:
                                f.write('\n\n')

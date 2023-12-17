import pandas as pd
import time
from scipy.optimize import minimize

def _optimize_by_mame(f,x0,bounds,method_name):
        start_time = time.perf_counter()
        res =  minimize(fun=f, x0=x0, bounds=bounds, method=method_name) # call SLSQP 
        end_time = time.perf_counter()
        execution_time_ms = int((end_time - start_time) * 1000)
        return get_data(res, execution_time_ms, method_name)
        




def get_data(res,execution_time_ms,method_name):
     return pd.DataFrame({
              'Variables Result': res.x,
              "Optimo": res.fun,
              'Execution Time': execution_time_ms
              })
     

TrustRegion=lambda f,x0,bounds: _optimize_by_mame(f,x0,bounds,'trust-constr')
SLSQP=lambda f,x0,bounds: _optimize_by_mame(f,x0,bounds,'SLSQP')
COBYLA=lambda f,x0,bounds: _optimize_by_mame(f,x0,bounds,'COBYLA')  
    
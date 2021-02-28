"""Read the params file and gets the ffield parameters as input"""

from pyDOE import *
from collections import defaultdict

def parameter_generator(parameters, cycle):
    try:
        length = len(parameters)
        parameters_a = defaultdict(list)


        hc = lhs(length, cycle, criterion='centermaximin')

        
        for j in range(0,cycle):
            for i in range(0,length):
           
                parameters_a[j].append((float(parameters[i][6])-float(parameters[i][5]))*hc[j][i]+float(parameters[i][5]))
        
            
    except IOError:
        pass
        
    return parameters_a
    
    
def parameter_generator_sevenfold(parameters, cycle):
    try:
        length = len(parameters)
        parameters_a = defaultdict(list)


        hc = lhs(length, cycle, criterion='centermaximin')

        for k in range(0, 7):
            for j in range(0,cycle):
                for i in range(0,length):
               
                    parameters_a[j].append((float(parameters[i][6])-float(parameters[i][5]))*hc[j][i]+float(parameters[i][5]))
        
            
    except IOError:
        pass
        
    return parameters_a
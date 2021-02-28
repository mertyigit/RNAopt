#### LAST MODIFICATION: 22 Feb 2021

import sys
import pandas as pd
import numpy as np
## path to the python script for data generation
#Path2script = "/Users/mertyigitsengul/Documents/DRUDE/"
Path2script="/home/mert/python_codes"
sys.path.append(Path2script)

import warnings
warnings.filterwarnings("ignore")

import RNAFFopt
from RNAFFopt.pes import pes
from RNAFFopt.plot_pes import plot_PES
from RNAFFopt.params_input_train import params_input_train
from RNAFFopt.parameter_generator import parameter_generator
from RNAFFopt.error_output import error_output
from RNAFFopt.diagonal_term import diagonalterm2
from RNAFFopt.dihedral import dihedral
from RNAFFopt.input_reference_data import input_reference_data
from RNAFFopt.zipping import zipping
from RNAFFopt.clean_fold import clean_fold
from RNAFFopt.error_calc import error_calc
from RNAFFopt.params_output import params_output



import shutil

from pyDOE import *
from collections import defaultdict
import os
import random
import time

#Parallel part
#from joblib import Parallel, delayed
#import multiprocessing
#from multiprocessing.dummy import Pool
from scoop import futures




## number of samples to be taken in the parameter space
nos = 500


cycle = range(nos)
#parameters = params_input_train('params')
#values = parameter_generator(parameters, len(cycle))
#num_of_params = len(parameters)

FF_file_name = 'toppar_drude_nucleic_acid_2021a.str'
dihedral_types=('alpha', 'beta', 'epsilon', 'gamma', 'zeta')
directory='surfaces'
phases=(0, 180) ## Phase values for dihedral fitting
folds=(1, 2, 3) ## Fold values that will be used for dihedral.


sim_num=0

### func is the subroutine for whole cycle of calculation of one sample produced by initial design. This func will be cycled thorugh all sample in the data set ###
def func(values, parameters, i):
    
    num_of_params = len(parameters)
    sim_num=i
    try:
        for p in range(0, len(phases)):
            for f in range(0, len(folds)):
                
                folder_name = 'simulation-'+str(sim_num)
                
                print(folder_name)
                
                                
                sim_num=sim_num+nos
                
                
                if not os.path.exists(folder_name):
                    shutil.copytree('folder', folder_name)
                ### Enter to the folder ###
                os.chdir(folder_name)
                ### Assign new parameter values ###
                for j in range(0, num_of_params):
                    diagonalterm2(parameters[j][0], parameters[j][1], parameters[j][2], parameters[j][3], parameters[j][4], str(values[i][j]), str(folds[f]), str(phases[p]), FF_file_name)
                    
                    params_output('DIHEDRAL', str(j), 'Force',  values[i][j])
                    params_output('DIHEDRAL', str(j), 'Fold',  folds[f])
                    params_output('DIHEDRAL', str(j), 'Phase',  phases[p])
                    
                    
                os.system('./run_rna.sh')
                
                data=input_reference_data()
                data['MM Data']=pd.concat([pd.read_csv(directory+'/r3ps_2oh_'+dihedral_types[i]+'_zero.surf', sep='\t', header=None) for i in range(0, len(dihedral_types))],ignore_index=True)[2]
                
                ## Calculates the dihedral-2'-OH plots for given dihedral types ##
                ## Calculates the difference between QM and MM and records to error.log file ###
                #for k in range(0, len(dihedral_types)):
                #    error_dihedral=dihedral('surfaces', '../qm_surfaces', dihedral_types[k])
                #    error_output('DIHEDRAL', str(dihedral_types[k]), "", str('%.3f' % float(error_dihedral)))
                total_error=error_calc(data) 
                error_output(total_error)
                
                zipping('crd_drude')
                clean_fold('crd_drude')
            
                zipping('init_crd')
                clean_fold('init_crd')
            
                zipping('pdb_drude')
                clean_fold('pdb_drude')
                
                os.chdir('..')
    except:
        pass
        


### These two subroutines are required for running the optimization on multiple cores ###
def doneElement(inFuture):
    print("Done: {}".format(inFuture.result()))

def run(values, parameters):
    # Create launches
    
    launches = [futures.submit(func ,values, parameters, i) for i in cycle]
    # Add a callback on every launches
    for launch in launches:
        launch.add_done_callback(doneElement)
 
 
    # Wait for the launches to complete.
    [completed for completed in futures.as_completed(launches)]
 


if __name__ == '__main__':
    t0 = time.time()
    sim_num=0
    
    parameters = params_input_train('params')
    values = parameter_generator(parameters, len(cycle))
    
    
    run(values, parameters)
    
    t1 = time.time()
    total = t1-t0
    print('Total Time (hours): ' + str(total/3600))

import pandas as pd
import numpy as np
import os
from RNAFFopt.pes import * 
from RNAFFopt.plot_pes import * 




def dihedral(surfaces_directory, directory_qm, dihedral_type):
    
    qm_matrix = pd.DataFrame()
    mm_matrix = pd.DataFrame()
    
    surf_file_name=surfaces_directory+'/r3ps_2oh_'+dihedral_type+'_zero.surf'
    if os.path.isfile(surf_file_name):
        mm=pd.read_csv(surf_file_name, sep='\t', header=None)
        mm_matrix=pes(mm)
        plot_PES(mm_matrix, dihedral_type, "2'-OH", 10, 'Potential Energy Surface (Drude)')
    qm_file_name=directory_qm+'/'+dihedral_type+'_2oh_2d_qm.dat'
    
    if os.path.isfile(surf_file_name):    
        qm=pd.read_csv(qm_file_name, sep='\t', header=None)
        qm_matrix=pes(qm)
        plot_PES(qm_matrix, dihedral_type, "2'-OH", 10, 'Potential Energy Surface (QM)')
        
        plot_PES(qm_matrix-mm_matrix, dihedral_type, "2'-OH", 10, 'Potential Energy Difference (QM-Drude)')
        
        
    return((qm_matrix-mm_matrix).sum().sum())
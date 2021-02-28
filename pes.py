import os
import shutil
from collections import defaultdict
import os
import pandas as pd
import numpy as np

def pes(dihedral):
    ## Create the PES matrix
    ## Columns are dihedral
    column_names=[str(i) for i in range(0, 361, 15)]
    ## Rows are 2'-OH
    row_names=[str(i) for i in range(0, 361, 15)]
    matrix=np.zeros((len(row_names), len(row_names)))
    PES_matrix=pd.DataFrame(matrix, columns=column_names, index=row_names)
    # Subroutine for assigning values from files to dataframe
    for i in range(len(row_names)):
        PES_matrix[PES_matrix.columns[i]]=dihedral[2][len(row_names)*i:len(row_names)*(i+1)].values
    return PES_matrix
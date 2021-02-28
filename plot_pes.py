import os
import shutil
from collections import defaultdict
import os
import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import seaborn as sns


def plot_PES(matrix, CV_1_name, CV_2_name, contour_level_num, name):    
    
    
    plt.figure(figsize=(10,8))
    #plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12)
    contour_filled = plt.contourf(matrix.columns, matrix.index, matrix, 
                                 #cmap = 'CMRmap',
                                  cmap = 'rainbow',
                                  levels=50,
                                )
    #pcolormesh
    contours = plt.contour(matrix.columns, matrix.index, matrix, contour_level_num, colors='black')
    plt.clabel(contours, inline=True, fontsize=8)
    cb=plt.colorbar(contour_filled)
    cb.set_label(label='kcal/mole',weight='bold', size=18)
    
    plt.title(name, fontsize=24)
    plt.xlabel(CV_1_name, fontsize=24)
    plt.ylabel(CV_2_name, fontsize=24)
    #plt.xlim(left=x.min(), right=x.max())
    #plt.ylim(bottom=y.min(), top=y.max())
    #plt.xlim(left=x.min(), right=x.max()-20)
    #plt.ylim(bottom=y.min(), top=y.max()-20)
    plt.savefig(name+CV_1_name+'-'+CV_2_name+'.png', dpi=100)
    plt.show()
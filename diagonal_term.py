import datetime

def diagonalterm(first, second, third, forth, fold, value, ff_file):
    """Assigns values to the diagonal terms part of the force field file."""
    c=1
    n=0
    position=0
    try:
        file = open(ff_file,"r+")
        while c==1 and n<5:
            position = file.read().find(first.ljust(9)+second.ljust(9)+third.ljust(9)+forth.ljust(9))
            file.seek(position+50)
            if file.read(1) == fold:
                c=0
            if file.read(1) != fold:
                n=n+1
                
        if c==0:
            file.seek(position)
            try:            
                position = position + 40
                file.seek(position)
                file.write(('%.3f' % float(value)).rjust(6))
        
            finally:
                file.close()
            
            try:
                log_file = open('log.dat',"a")
                log_file.write(first+'   '+second+'   '+third+'   '+forth+' value has been changed to '+value
                               +"  ("+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+")\n")
            finally:
                log_file.close()
        if c==1:
            print("Error: Dihedral not found!!")
            file.close()
            
    except IOError:
        pass
        
        
def diagonalterm2(first, second, third, forth, fold, value, n_value, phase_value, ff_file):
    """Assigns values to the diagonal terms part of the force field file."""
    c=1
    n=0
    position=0
    try:
        file = open(ff_file,"r+")
        while c==1 and n<5:
            
            dihedral_name = first.ljust(9)+second.ljust(9)+third.ljust(9)+forth.ljust(9)
            position = position+file.read().find(dihedral_name)
            
            position=position+50
            file.seek(position)
            
            if file.read(1) == fold:
                c=0
            if file.read(1) != fold:
                n=n+1
                
        
        if c==0:
            ## Assigns the force constant value to the specified dihedral term
            position=position-50
            file.seek(position)
            
            try:            
                position = position + 40
                file.seek(position)
                file.write(('%.3f' % float(value)).rjust(6))
                  

                log_file = open('log.dat',"a")
                log_file.write(first+'   '+second+'   '+third+'   '+forth+' force constant value has been changed to '+value
                               +"  ("+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+")\n")
            finally:
                log_file.close()
                
            ## Assigns the fold value to the specified dihedral term
            
            position=position-40
            file.seek(position)
            try:            
                position = position + 50
                file.seek(position)
                file.write(str(int(n_value)))
            

                log_file = open('log.dat',"a")
                log_file.write(first+'   '+second+'   '+third+'   '+forth+' fold value has been changed to '+n_value
                               +"  ("+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+")\n")
            finally:
                log_file.close()            
            
            
            ## Assigns the fold value to the specified dihedral term
            
            position=position-50
            file.seek(position)
            try:            
                position = position + 54
                file.seek(position)
                file.write(('%.2f' % float(phase_value)).rjust(6))
        
            finally:
                file.close()
            
            try:
                log_file = open('log.dat',"a")
                log_file.write(first+'   '+second+'   '+third+'   '+forth+' phase value has been changed to '+phase_value
                               +"  ("+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+")\n")
            finally:
                log_file.close()            
                        
            
        if c==1:
            print("Error: Dihedral - "+dihedral_name+"- not found!!")
            file.close()
            
        
            
    except IOError:
        pass
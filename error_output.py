###################################
### Subroutine for error output ###
###################################

def error_output(error_value):
    
    """Write the assigned parameter values into the params file near the corresponding parameter identicator"""
    
    try:
        file = open("parameters","a+")        
        
        
        try:
            file.write('TOTAL ERROR'.ljust(20)+('%.2f' % total_error).ljust(20))
        
        finally:
            file.close()
    except IOError:
        pass
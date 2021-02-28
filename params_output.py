def params_output(section, parameter_number, type, value):
    
    """Write the assigned parameter values into the params file near the corresponding parameter identicator"""
    
    try:
        file = open("parameters","a+")        
        file.seek(0)
        try:
            file.write(section.rjust(10) + "  " + parameter_number.rjust(2) + "  " + type.rjust(10) + "  " + str(value).rjust(8) + "                    \n")
        
        finally:
            file.close()
    except IOError:
        pass

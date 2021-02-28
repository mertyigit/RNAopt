"""Read the params file and gets the ffield parameters as input"""

def params_input_train(parameters_file_name):
    try:
        file = open(parameters_file_name,"r")
        file_length = len(file.readlines())
        print("Number of parameters to be optimized: "+str(file_length-1))
        file.seek(0)
        file.readline()
        position = file.tell()
        file.seek(position)
        
        
        parameters = []

        try:
            for i in range(0,file_length-1):
                parameters.append(file.readline().split())
        
        finally:
            file.close()
    except IOError:
        pass
        
    return parameters
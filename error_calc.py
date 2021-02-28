###################################
### Subroutine for error calc #####
###################################

def error_calc(data):
    total_error=0
    try:
        file = open("error.out", "w+")
        file.seek(0)
        file.write('Reference Name'.ljust(50)+'Weight'.ljust(20)+'Reference Data'.ljust(20)+'MM Data'.ljust(20)+'Error'.ljust(20)+'\n')
        for i in range(0, len(data)):
            
            mm_value=float(data['MM Data'][i])
            qm_value=float(data['Reference Data'][i])
            weight=float(data['Weight'][i])
            individual_error=((mm_value-qm_value)/weight)**2
            total_error=total_error+individual_error
            
            file.write(data['Reference Name'][i].ljust(50)
                       +('%.2f' % weight).ljust(20)
                       +('%.2f' % qm_value).ljust(20)
                       +('%.2f' % mm_value).ljust(20)
                       +('%.2f' % individual_error).ljust(20)
                       +'   \n')
        file.write('TOTAL ERROR'.ljust(110)+('%.2f' % total_error).ljust(20))
    
        file.close()
    
    except IOError:
        pass
        
    return total_error
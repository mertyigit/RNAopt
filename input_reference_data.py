import datetime

def input_reference_data():
    reference_data = pd.DataFrame(columns=['Reference Name', 'Weight', 'Reference Data'])
    try:
        n=0
        file=open('reference_set.in', 'r+')
        position_start = file.read().find('DIHEDRALSTART')
        file.seek(0)
        position_end = file.read().find('DIHEDRALEND')   
        
        file.seek(position_start)
        file.readline()
        position=file.tell()
        # count qm inputs
        while position<position_end:
            reference_data.loc[n]=file.readline().split()
            #print(file.readline().split())
            position=file.tell()
            n=n+1
        finally:
            file.close()
    return reference_data
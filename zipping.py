import os



def zipping(folder_name):
    print("zipping in progress")
    os.system('tar -cvzf '+str(folder_name)+'.tar folder_name')
    print("zipping is finished")
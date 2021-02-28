import os


def clean_fold(folder_name):
    print("clearing in progress")
    os.system('rm -r '+str(folder_name))
    print("clearing is finished")
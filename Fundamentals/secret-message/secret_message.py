import os
#Remove numbers chars from a list of files names
def rename_files():
    cwd_path = os.getcwd()
    file_list = os.listdir(r"C:\\Users\\vinicius.lagedo\\Desktop\\testes\\Fundamentals\\secret-message\\secret-images")
    os.chdir(r"C:\\Users\\vinicius.lagedo\\Desktop\\testes\\Fundamentals\\secret-message\\secret-images")
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        print("From " + file_name + " to " + new_name)
        os.rename(file_name, new_name)
    os.chdir(cwd_path)

rename_files()
import shutil, os


username = os.getlogin()
settings_folder_path = "C:\\Users\\" + username + "\\AppData\\Local"

master_config_folder_path = "C:\\BZ-X"
master_config_exists_flag = os.path.exists(master_config_folder_path)

if master_config_exists_flag == True:
    if (os.path.exists(settings_folder_path + "\\Keyence\\")):
        error_file = open("ERROR-LOG.txt", "w")
        user_documents_path = "C:\\Users\\" + username + "\\Documents\\Keyence\\"
        
        if (os.path.exists(user_documents_path)):
            shutil.rmtree(user_documents_path, ignore_errors=True)
            
        shutil.copytree(settings_folder_path + "\\Keyence\\", user_documents_path)
        shutil.rmtree(settings_folder_path + "\\Keyence\\", ignore_errors=True)
        text = "Old Keyence folder saved at " + user_documents_path
        error_file.write(text)
        error_file.close()               
    shutil.copytree(master_config_folder_path, settings_folder_path + "\\Keyence\\BZ-X\\")
        

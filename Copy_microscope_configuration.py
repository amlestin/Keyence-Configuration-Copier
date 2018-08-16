import shutil, os


username = os.getlogin()
settings_folder_path = "C:\\Users\\" + username + "\\AppData\\Local"

master_config_folder_path = "C:\\BZ-X"
master_config_exists_flag = os.path.exists(master_config_folder_path)

if master_config_exists_flag == True:
    shutil.copytree(master_config_folder_path, settings_folder_path + "\\Keyence\\")
        

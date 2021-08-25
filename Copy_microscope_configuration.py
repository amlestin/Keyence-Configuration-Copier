import shutil, os, platform

def supported_platform():
    # only supports Windows
    if platform.system() != "Windows":
        print("Error: Not a Windows system.")
        return False

    return True
 
def main():
    if not supported_platform():
       quit()

    username = os.getlogin() # gets the folder name of the logged in user in C:\Users\ folder
    settings_folder_path = "C:\\Users\\" + username + "\\AppData\\Local"

    master_config_folder_path = "C:\\BZ-X"
    master_config_exists = os.path.exists(master_config_folder_path) # checks that there is a folder to write from 

    if master_config_exists:
        if os.path.exists(settings_folder_path + "\\Keyence\\"): # makes backup if the user has previous config files
            error_file = open("ERROR-LOG.txt", "w")
            user_documents_path = "C:\\Users\\" + username + "\\Documents\\Keyence\\"
            
            if os.path.exists(user_documents_path): # deletes the previous backup if it exists
                shutil.rmtree(user_documents_path, ignore_errors=True) # delete
                
            shutil.copytree(settings_folder_path + "\\Keyence\\", user_documents_path) # makes backup of user's current config files
            shutil.rmtree(settings_folder_path + "\\Keyence\\", ignore_errors=True) # deletes the user's current config files
            text = "Old Keyence folder saved at " + user_documents_path
            error_file.write(text) # writes a file so the user knows their old configuration files were backed up and where
            error_file.close()
        shutil.copytree(master_config_folder_path, settings_folder_path + "\\Keyence\\BZ-X\\") # copies the master configuration to this user's account
            
if __name__ == '__main__':
    main()
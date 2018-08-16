import shutil, os

activated_users = os.listdir('C:\\Users\\')

print("Users on this computer:")
count = 0
for user in activated_users:
    print(user)
print("\n")

username_valid_flag = False
while (username_valid_flag == False):
    print("Type in the username you used to login: ")
    username = input()
    username_valid_flag = username in activated_users

user_config_directory = "C:\\Users\\" + username + "\\AppData\\Local\\"
config_directory_contents = os.listdir(user_config_directory)

keyence_folder_exists_flag = "Keyence" in config_directory_contents

keyence_config_directory = user_config_directory + "\\Keyence\\"
keyence_config_directory = os.path.normpath(keyence_config_directory)

# DELETE ME
keyence_folder_exists_flag = True
# DELETE ME

if(keyence_folder_exists_flag == False):
    print("\n")
    print("The folder " + keyence_config_directory + " does not yet exist.")
    print("Please open and close the BZ-X Viewer software on the desktop of your computer in order to continue.")
    quit()
    
master_config_exists_flag = "BZ-X" in os.listdir("C:\\")

if master_config_exists_flag == True:
    shutil.copytree("C:\\BZ-X\\", "C:\\Specialdir\\")
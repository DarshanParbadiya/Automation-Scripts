import zipfile
import os
 
current_directory = os.getcwd()
print(f"The current directory is: {current_directory}")
# Specify the path to the ZIP file
zip_file_path = 'C:\\Users\\dparbadiya\\OneDrive - AIC Global Holdings\\Desktop\\unzip test'

# Specify the destination directory where you want to extract the files
destination_path = "C:\\Users\\dparbadiya\\OneDrive - AIC Global Holdings\\Desktop\\unzip test\\"

file_name = "XYZ.zip"
password = "password"

zip_file_path += file_name
# Create the destination directory if it doesn't exist
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Extract the ZIP file to the specified location
with zipfile.ZipFile('XYZ.ZIP', 'r') as zip_ref:
    zip_ref.extractall(destination_path, pwd=password.encode("utf-8"))


# with ZipFile(file_name, "r") as zip:
#     zip.extractall(path="uncompressed", pwd="password".encode("utf-8"))


print(f"ZIP file extracted to: {destination_path}")
import os
import time
import zipfile

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


source = [r'G:\test']

target_dir = r'G:\backup_test'

# os.sep variable - this gives the directory separator according to your operating system
target_fullpath = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zipfile_handle = zipfile.ZipFile(target_fullpath, 'w')

for item in source:
    for root, dirs, files in os.walk(item):
        for file in files:
            fullpath = os.path.join(root, file)
            zipfile_handle.write(fullpath)

zipfile_handle.close()

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
output = os.system('ping 8.8.8.8')

print(output)



# Regular development plan:
# What (Analysis)
# How (Design)
# Do It (Implementation)
# Test (Testing and Debugging)
# Use (Operation or Deployment)
# Maintain (Refinement)
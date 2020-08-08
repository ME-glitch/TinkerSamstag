import os
import sys

branch_name = sys.argv[1]

os.system("echo Hello from the other side!")

os.system("echo " + branch_name)

os.system("git checkout -b " + branch_name)
os.system("git push -u origin " + branch_name)
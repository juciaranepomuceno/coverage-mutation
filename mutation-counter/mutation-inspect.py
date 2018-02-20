import os

import findMutationReport

path = input("Project path:")
dir = findMutationReport.ReadDirectory()
if os.path.exists(path):
    dir.findMutationReport('mutations.csv', path)
else:
    print("Please verify the path...")

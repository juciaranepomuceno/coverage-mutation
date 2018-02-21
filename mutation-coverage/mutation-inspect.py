import os
import findMutationReport

print ("**************** COVERAGE ANALYSIS SUPPORTE **************************** \n"
       "*Please, be sure that your module is in C:/dev/repository/[your module]* \n"
       "************************************************************************ \n")

path = input("Project path:")

dir = findMutationReport.ReadDirectory()
if os.path.exists(path):
    dir.findMutationReport('mutations.csv', path)
else:
    print("Please verify the path...")

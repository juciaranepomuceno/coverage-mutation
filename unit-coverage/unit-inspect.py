import os
import countUnit

print ("**************** COVERAGE ANALYSIS SUPPORTE **************************** \n"
       "*Please, be sure that your module is in C:/dev/repository/[your module]* \n"
       "************************************************************************ \n")

module = input("Module: ")
path = "C:/dev/repository/"+module+"/layers"

dirUnit= countUnit.CountUnit()

if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html',path)

else:
    print("Please verify the path...")
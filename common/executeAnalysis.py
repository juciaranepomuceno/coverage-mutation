import os
import countUnit
import findMutationReport
import sheetMap


print ("**************** COVERAGE ANALYSIS SUPPORTE **************************** \n"
       "*Please, be sure that your module is in C:/dev/repository/[your module]* \n"
       "************************************************************************ \n")

module = input("Module: ")
path = "C:/dev/repository/"+module+"/layers"

dirUnit= countUnit.CountUnit()
dirMutation = findMutationReport.FindReport()
print(sheetMap.sheetId(module))


if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html',path)
    dirMutation.findMutationReport('mutations.csv',path)

else:
    print("Please verify the path of your module...")









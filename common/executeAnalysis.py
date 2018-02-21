import os
import countUnit
import findMutationReport
import dataMap


print("****************COVERAGE ANALYSIS SUPPORTE **************************** \n"
      "*Please, be sure that your module is in C:/dev/repository/[your module]* \n"
      "************************************************************************ \n")

module = input("Module: ")
month = input("Month: ")

path = "C:/dev/repository/"+module+"/layers"

dirUnit = countUnit.CountUnit()
dirMutation = findMutationReport.FindReport()

if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html', path)
    dirMutation.findMutationReport('mutations.csv', path)

else:
    print("Please verify the path of your module...")

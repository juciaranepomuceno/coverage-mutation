import os
import countUnit
import findMutationReport



module = input("Module: ")
path = "C:/dev/repository/"+module+"/layers"

print (path)
dirUnit= countUnit.CountUnit()
dirMutation = findMutationReport.FindReport()

if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html',path)
    dirMutation.findMutationReport('mutations.csv',path)

    
else:
    print("Please verify the path...")









import os

import countUnit
import findMutationReport
import messageStart

messageStart.printMessage()

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

import os

import dataMap
import findMutationReport
import messageStart

messageStart.printMessage()

module = input("Insert the module: ")
month = dataMap.getMonth(input("Insert the month <example: '01' for  for January>: "))
path = "C:/dev/repository/" + module

dirMutation = findMutationReport.FindReport()

if os.path.exists(path):

    dirMutation.findMutationReport('mutations.csv', path, month, module)

else:
    print("Please verify the path of your module...")

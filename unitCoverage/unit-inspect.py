import os

import countUnit
import dataMap
import messageStart

messageStart.printMessage()

module = input("Insert the module: ")
month = dataMap.getMonth(input("Insert the month <example: '01' for  for January>: "))
path = "C:/dev/repository/" + module

dirUnit = countUnit.CountUnit()


if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html', path, month, module)


else:
    print("Please verify the path of your module...")

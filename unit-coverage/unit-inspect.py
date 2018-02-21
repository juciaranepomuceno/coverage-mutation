import os

import countUnit
import messageStart

messageStart.printMessage()
module = input("Module: ")

path = "C:/dev/repository/" + module + "/layers"

dirUnit = countUnit.CountUnit()

if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html', path)

else:
    print("Please verify the path...")

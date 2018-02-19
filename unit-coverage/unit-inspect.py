import os
import countUnit

path = input("Project path:")
dir= countUnit.CountUnit()
if os.path.exists(path):
    dir.findUnitReport('frame-summary.html',path)
else:
    print("Please verify the path...")









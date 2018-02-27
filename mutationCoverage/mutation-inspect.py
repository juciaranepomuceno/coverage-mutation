import os

import findMutationReport
import messageStart

messageStart.printMessage()

path = input("Project path:")

dir = findMutationReport.FindReport()
if os.path.exists(path):
    dir.findMutationReport('mutations.csv', path)
else:
    print("Please verify the path...")

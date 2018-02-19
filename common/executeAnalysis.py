import os
import countUnit



module = input("Module: ")
path = "C:/dev/repository/"+module+"/layers"



print (path)
dirUnit= countUnit.CountUnit()

if os.path.exists(path):
    dirUnit.findUnitReport('frame-summary.html',path)
    #dirMutation.find('mutations.csv', path)
    
else:
    print("Please verify the path...")









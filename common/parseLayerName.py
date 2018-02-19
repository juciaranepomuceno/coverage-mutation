import updateSheet

def parsePath(root,layerNumber):
    parsedPath = root.split('/')
    parsedLayer = (parsedPath[4]).split('\\')
    layer = parsedLayer[1]

    print(layer)
    #updateSheet.updateSheetMutation(layer)
    updateSheet.updateLayersName(layer,layerNumber)

    

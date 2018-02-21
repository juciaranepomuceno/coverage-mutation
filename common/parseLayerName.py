import updateSheet


def parsePath(root, layerNumber, month):
    parsedPath = root.split('/')
    parsedLayer = (parsedPath[4]).split('\\')
    layer = parsedLayer[1]

    print(layer)
    updateSheet.updateLayersName(month, layer, layerNumber)

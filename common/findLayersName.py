class FindLayersName:

    def parsePath(root):
        parsedPath = root.split('/')
        parsedLayer = (parsedPath[3]).split('\\')

        for pos, item in enumerate(parsedLayer):
            if item == 'target':
                layer = parsedLayer[pos - 1]

        # updateSheet.updateLayersName(month, layer, layerNumber)

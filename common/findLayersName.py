import updateSheet


class FindLayersName:

    def parsePath(root, layerNumber, month, module):
        parsedPath = root.split('/')
        parsedLayer = (parsedPath[3]).split('\\')

        for pos, item in enumerate(parsedLayer):
            if item == 'target':
                layer = parsedLayer[pos - 1]

        updateSheet.updateLayersName(month, layer, layerNumber, module)

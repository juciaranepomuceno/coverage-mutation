import fnmatch
import os

import countMutators


class FindReport():
    def findMutationReport(self, pattern, path, month):
        layer = 1
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    countMutators.CountMutators(). \
                        countMutatorsByType(root + "\mutations.csv", layer, month)
                    layer += 1

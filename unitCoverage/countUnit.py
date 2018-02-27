import fnmatch
import os

import findLayersName
import parseUnitReport
import updateSheet


class CountUnit():

    def findUnitReport(self, pattern, path, month):

        total_lines_covered = 0
        total_lines_total = 0
        total_branch_covered = 0
        total_branch_total = 0
        layerNumber = 1

        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):

                    lines_covered, lines_total, \
                    branch_covered, branch_total \
                        = parseUnitReport.read_htlm(root)

                    total_lines_covered += int(lines_covered)
                    total_lines_total += int(lines_total)
                    total_branch_covered += int(branch_covered)
                    total_branch_total += int(branch_total)

                    findLayersName.FindLayersName.parsePath(root, layerNumber, month)
                    updateSheet.updateSheetUnit(month, layerNumber,
                                                lines_covered, lines_total,
                                                branch_covered, branch_total)
                    layerNumber += 1

        print("\n\nlines covered [module]: %s | lines total[module]: %s "
              "\nbranches covered[module]: %s | branches total[module]: %s"
              % (total_lines_covered, total_lines_total,
                 total_branch_covered, total_branch_total))

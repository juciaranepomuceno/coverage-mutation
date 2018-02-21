from __future__ import print_function

import connectSpreadSheet
import dataMap


def updateSheetMutation(layer, totalMutants, \
                        totalMutantsKilled, \
                        mutantReturnValsMutator, \
                        mutantReturnValsMutatorKilled, \
                        mutantNegateConditionalsMutator, \
                        mutantNegateConditionalsMutatorKilled, \
                        mutantVoidMethodCallMutator, \
                        mutantVoidMethodCallMutatorKilled, \
                        mutantConditionalsBoundaryMutator, \
                        mutantConditionalsBoundaryMutatorKilled, \
                        mutantIncrementsMutator, \
                        mutantIncrementsMutatorKilled, \
                        mutantMathMutator, \
                        mutantMathMutatorKilled):

    valuesMutation = [[totalMutants, totalMutantsKilled],
                      [mutantReturnValsMutator, mutantReturnValsMutatorKilled],
                      [mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled],
                      [mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled],
                      [mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKilled],
                      [mutantIncrementsMutator, mutantIncrementsMutatorKilled],
                      [mutantMathMutator, mutantMathMutatorKilled],
                      ]

    bodyMutation = {
        'values': valuesMutation
    }

    rangeMutation = dataMap.getRangeMutation(layer, 'Feb')
    connectSpreadSheet.requestUpdate(rangeMutation, bodyMutation)


def updateSheetUnit(layer,
                    total_lines_covered,total_lines_total,
                    total_branch_covered, total_branch_total):

    valuesUnit = [[total_lines_covered, total_lines_total],[total_branch_covered, total_branch_total]]
    bodyUnit = {
        'values': valuesUnit
    }

    rangeUnit = dataMap.getRangeUnit(layer, 'Feb')
    connectSpreadSheet.requestUpdate(rangeUnit, bodyUnit)


def updateLayersName(layerName, layerID):

    valuesName = [[layerName]]
    bodyName = {
    'values': valuesName
    }
    rangeName = dataMap.getRangeName(layerID, 'Mar')
    connectSpreadSheet.requestUpdate(rangeName, bodyName)


if __name__ == '__main__':
    updateLayersName("teste", 1)

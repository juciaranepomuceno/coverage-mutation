import fnmatch
import os
import countMutators
import updateSheet


class ReadDirectory():
    def findMutationReport(self, pattern, path):

        all_totalMutants = 0
        all_totalMutantsKilled = 0
        all_mutantReturnValsMutator = 0
        all_mutantReturnValsMutatorKilled = 0
        all_mutantNegateConditionalsMutator = 0
        all_mutantNegateConditionalsMutatorKilled = 0
        all_mutantVoidMethodCallMutator = 0
        all_mutantVoidMethodCallMutatorKilled = 0
        all_mutantConditionalsBoundaryMutator = 0
        all_mutantConditionalsBoundaryMutatorKilled = 0
        all_mutantIncrementsMutator = 0
        all_mutantIncrementsMutatorKilled = 0
        all_mutantMathMutator = 0
        all_mutantMathMutatorKilled = 0
        layer = 1

        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    totalMutants, \
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
                    mutantMathMutatorKilled = countMutators.CountMutators().parse_file(root+"\mutations.csv")

                    updateSheet.updateSheetMutation(layer, totalMutants, \
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
                                                    mutantMathMutatorKilled)



                    all_totalMutants += int(totalMutants)
                    all_totalMutantsKilled += int(totalMutantsKilled)
                    all_mutantReturnValsMutator += int(mutantReturnValsMutator)
                    all_mutantReturnValsMutatorKilled += int(mutantReturnValsMutatorKilled)
                    all_mutantNegateConditionalsMutator += int(mutantNegateConditionalsMutator)
                    all_mutantNegateConditionalsMutatorKilled += int(mutantNegateConditionalsMutatorKilled)
                    all_mutantVoidMethodCallMutator += int(mutantVoidMethodCallMutator)
                    all_mutantVoidMethodCallMutatorKilled += int(mutantVoidMethodCallMutatorKilled)
                    all_mutantConditionalsBoundaryMutator += int(mutantConditionalsBoundaryMutator)
                    all_mutantConditionalsBoundaryMutatorKilled += int(mutantConditionalsBoundaryMutatorKilled)
                    all_mutantIncrementsMutator += int(mutantIncrementsMutator)
                    all_mutantIncrementsMutatorKilled += int(mutantIncrementsMutatorKilled)
                    all_mutantMathMutator += int(mutantMathMutator)
                    all_mutantMathMutatorKilled += int(mutantMathMutatorKilled)

                    layer+=1

        print("\n\nmutations killed [module]: %s | mutations total [module]: %s "
              % (all_totalMutantsKilled, all_totalMutants))

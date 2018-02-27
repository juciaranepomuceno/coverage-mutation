import glob

import updateSheet


class CountMutators():

    def countMutatorsByType(self, path, layer, month, module):
        totalMutants = 0
        totalMutantsKilled = 0
        mutantReturnValsMutator = 0
        mutantReturnValsMutatorKilled = 0
        mutantNegateConditionalsMutator = 0
        mutantNegateConditionalsMutatorKilled = 0
        mutantVoidMethodCallMutator = 0
        mutantVoidMethodCallMutatorKilled = 0
        mutantConditionalsBoundaryMutator = 0
        mutantConditionalsBoundaryMutatorKilled = 0
        mutantIncrementsMutator = 0
        mutantIncrementsMutatorKilled = 0
        mutantMathMutator = 0
        mutantMathMutatorKilled = 0

        files = glob.glob(path)

        mutatorType = CountMutators()

        for i, file in enumerate(files):
            with open(files[i]) as fd:
                print(files[i])
                for line in fd:
                    mutantReturnValsMutator, mutantReturnValsMutatorKilled \
                        = mutatorType.isReturnValsMutator \
                        (line, mutantReturnValsMutator, mutantReturnValsMutatorKilled)

                    mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled \
                        = mutatorType.isNegateConditionalsMutator \
                        (line, mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled)

                    mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled \
                        = mutatorType.isVoidMethodCallMutator \
                        (line, mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled)

                    mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKilled \
                        = mutatorType.isConditionalsBoundaryMutator \
                        (line, mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKilled)

                    mutantIncrementsMutator, mutantIncrementsMutatorKilled \
                        = mutatorType.isIncrementsMutator \
                        (line, mutantIncrementsMutator, mutantIncrementsMutatorKilled)

                    mutantMathMutator, mutantMathMutatorKilled = \
                        mutatorType.isMathMutator \
                            (line, mutantMathMutator, mutantMathMutatorKilled)

                    totalMutants += 1
                    totalMutantsKilled += line.count('KILLED')
            print("total: %d" % totalMutants)
            print("total killed: %d" % totalMutantsKilled)

            fd.close()

        updateSheet.updateSheetMutation(month, layer, module, totalMutants, totalMutantsKilled,
                                        mutantReturnValsMutator, mutantReturnValsMutatorKilled,
                                        mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled,
                                        mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled,
                                        mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKilled,
                                        mutantIncrementsMutator, mutantIncrementsMutatorKilled,
                                        mutantMathMutator, mutantMathMutatorKilled)

    def isReturnValsMutator(self, line, mutator, mutantKilled):
        if 'ReturnValsMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isNegateConditionalsMutator(self, line, mutator, mutantKilled):
        if 'NegateConditionalsMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isVoidMethodCallMutator(self, line, mutator, mutantKilled):
        if 'VoidMethodCallMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isConditionalsBoundaryMutator(self, line, mutator, mutantKilled):
        if 'ConditionalsBoundaryMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isIncrementsMutator(self, line, mutator, mutantKilled):
        if 'IncrementsMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isMathMutator(self, line, mutator, mutantKilled):
        if 'MathMutator' in line:
            mutator += 1
            mutantKilled = CountMutators.isKilled(line, mutantKilled)
        return mutator, mutantKilled

    def isKilled(line, mutator):
        if 'KILLED' in line:
            mutator += 1
        return mutator

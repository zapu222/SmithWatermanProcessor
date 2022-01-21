import sys

class results:

    def __init__(self, inputs, scoring, mtrxs, traces):
        self.displayResults(inputs, scoring, mtrxs, traces)

    def displayResults(self, inputs, scoring, mtrxs, traces):
        print('')
        print('----------------------------------------------------------------------------------------------------')
        
        print('\n','Highest score for Matrix 1: ', mtrxs.M1.max())
        print(mtrxs.M1, '\n')

        print(traces.trc1M1)
        for i in range(0, len(traces.trc1M1)):
                if traces.trc1M1[i] == traces.trc2M1[i]:
                    sys.stdout.write('*')
                elif traces.trc1M1[i] == '_' or traces.trc2M1[i] == '_':
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('X')
        print('')
        print(traces.trc2M1)
        print('')
        print('----------------------------------------------------------------------------------------------------')



        print('\n','Highest score for Matrix 2: ', mtrxs.M2.max())
        print(mtrxs.M2, '\n')

        print(traces.trc1M2)
        for i in range(0, len(traces.trc1M2)):
                if traces.trc1M2[i] == traces.trc2M2[i]:
                    sys.stdout.write('*')
                elif traces.trc1M2[i] == '_' or traces.trc2M2[i] == '_':
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('X')
        print('')
        print(traces.trc2M2)
        print('')
        print('----------------------------------------------------------------------------------------------------')


        print('\n','Highest score for Matrix 3: ', mtrxs.M3.max())
        print(mtrxs.M3, '\n')

        print(traces.trc1M3)
        for i in range(0, len(traces.trc1M3)):
                if traces.trc1M3[i] == traces.trc2M3[i]:
                    sys.stdout.write('*')
                elif traces.trc1M3[i] == '_' or traces.trc2M3[i] == '_':
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('X')
        print('')
        print(traces.trc2M3)
        print('')
        print('----------------------------------------------------------------------------------------------------')
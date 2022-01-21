import matplotlib.pyplot as plt
import numpy as np

class traceback:
    
    # Calls function to find tracebacks for each scoring matrix -------------------------------------------------------------------
    def __init__(self, sc, seq1, seq2, M1, M2, M3):
        self.trc1M1, self.trc2M1 = self.createTracebacks(sc, seq1, seq2, M1)
        self.trc1M2, self.trc2M2 = self.createTracebacks(sc, seq1, seq2, M2)
        self.trc1M3, self.trc2M3 = self.createTracebacks(sc, seq1, seq2, M3)
        
    
    # Finds the tracebacks for sequence 1 and 2 -----------------------------------------------------------------------------------
    def createTracebacks(self, sc, seq1, seq2, M):
        trc1, trc2, maxi = '', '', M.max()
        
        if maxi > 0:
            x, y = 0, 0

            # Finds the last max in the case of multiple maxes
            for i in range(1, len(seq1) + 1):
                for j in range(1, len(seq2) + 1):
                    if M[i,j] == maxi:
                        x = i
                        y = j

            while True:

                if (M[x,y] == M[x-1,y-1] + sc.match or M[x,y] == M[x-1,y-1] + sc.miss) and M[x-1,y-1] == max(M[x-1,y-1], M[x-1,y], M[x, y-1]): 
                    trc1 = seq1[x-1] + trc1
                    trc2 = seq2[y-1] + trc2
                    if M[x-1,y-1] == 0:
                        break
                    x = x-1
                    y = y-1
                elif M[x,y] == M[x-1,y] + sc.gap or M[x,y] == M[x-1,y] + sc.gapExt:
                    trc1 = seq1[x-1] + trc1
                    trc2 = '_' + trc2
                    x = x-1
                elif M[x,y] == M[x, y-1] + sc.gap or M[x,y] == M[x,y-1] + sc.gapExt:
                    trc1 = '_' + trc1
                    trc2 = seq2[y-1] + trc2
                    y = y-1
                else:
                    trc1 = seq1[x-1] + trc1
                    trc2 = seq2[y-1] + trc2
                    if M[x-1,y-1] == 0:
                        break
                    x = x-1
                    y = y-1

            return trc1, trc2

        else:
            return trc1, trc2

    # Prints tracebacks for each scoring matrix ----------------------------------------------------------------------------------
    def printTraces(self):
        print(self.trc1M1, '   ', self.trc1M2, '   ', self.trc1M3)
        print(self.trc2M1, '   ', self.trc2M2, '   ', self.trc2M3)
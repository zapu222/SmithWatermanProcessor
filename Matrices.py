import numpy as np

class scoringMatrices:

    # Calls matrix creation functions to create scoring matrices ---------------------------------------------------------------------
    def __init__(self, sc, seq1, seq2):
        self.M1 = self.createM1(sc, seq1, seq2)
        self.M2 = self.createM2(sc, seq1, seq2)
        self.M3 = self.createM3(sc, seq1, seq2)

    # Creating M1 - no extensions ----------------------------------------------------------------------------------------------------
    def createM1(self, sc, seq1, seq2):

        M = np.zeros((len(seq1) + 1, len(seq2) + 1))

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):

                if seq1[i-1] == seq2[j-1]:
                    alignment = M[i-1,j-1] + sc.match
                else:
                    alignment = M[i-1,j-1] + sc.miss

                insert = M[i,j-1] + sc.gap
                delete = M[i-1,j] + sc.gap

                M[i,j] = max(alignment, delete, insert, 0)

        return M


    # Creating M2 - gap extsentions ------------------------------------------------------------------------------------------------
    def createM2(self, sc, seq1, seq2):

        M = np.zeros((len(seq1) + 1, len(seq2) + 1))

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                alignment = 0

                if seq1[i-1] == seq2[j-1]:
                    alignment = M[i-1,j-1] + sc.match
                else:
                    alignment = M[i-1,j-1] + sc.miss

                if j > 1 and M[i,j-1] == M[i,j-2] + sc.gap or M[i,j-1] == M[i,j-2] + sc.gapExt:
                    insert = M[i,j-1] + sc.gapExt
                else:
                    insert = M[i,j-1] + sc.gap

                if i > 1 and M[i-1,j] == M[i-2,j] + sc.gap or M[i-1,j] == M[i-2,j] + sc.gapExt:
                    delete = M[i-1,j] + sc.gapExt
                else:
                    delete = M[i-1,j] + sc.gap      

                M[i,j] = max(alignment, delete, insert, 0)

        return M



    # Creating M3 - gap and match extensions--------------------------------------------------------------------------------------
    def createM3(self, sc, seq1, seq2):

        M = np.zeros((len(seq1) + 1, len(seq2) + 1))

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):

                if seq1[i-1] == seq2[j-1]:
                    k, x, y = 0, i, j
                    while x > 1 and y > 1:
                        if seq1[x-2] == seq2[y-2]:
                            k = k+1
                        else:
                            break
                        x = x-1
                        y = y-1
                    alignment = M[i-1,j-1] + sc.match + k * sc.matchExt
                else:
                    alignment = M[i-1,j-1] + sc.miss

                if j > 2 and M[i,j-1] == M[i,j-2] + sc.gap or M[i,j-1] == M[i,j-2] + sc.gapExt:
                    insert = M[i,j-1] + sc.gapExt
                else:
                    insert = M[i,j-1] + sc.gap

                if i > 2 and M[i-1,j] == M[i-2,j] + sc.gap or M[i-1,j] == M[i-2,j] + sc.gapExt:
                    delete = M[i-1,j] + sc.gapExt
                else:
                    delete = M[i-1,j] + sc.gap      

                M[i,j] = max(alignment, delete, insert, 0)

        return M


    # Prints all scores --------------------------------------------------------------------------------------------------------------
    def printScores(self):
        print('\n','Highest score for Matrix 1: ', self.M1.max())
        print(self.M1)

        print('\n','Highest score for Matrix 2: ', self.M2.max())
        print(self.M2)

        print('\n','Highest score for Matrix 3: ', self.M3.max())
        print(self.M3)

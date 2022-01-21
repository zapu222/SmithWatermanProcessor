# Name: Smith-Waterman Scoring Matrix Comparison
# Creator: Zachary Pulliam

# This program applies three seperate scoring algorithm to 2 sequence string.
#   Matrix 1: a traditional scoring algorithm with match, mismatch, and gap scores
#   Matrix 2: an advanced scoring algorithm with match, mismatch, gap, and gap exstension scores
#   Matrix 3: a new scoring algorithm with match, mismatch, gap, gap exstension scores, AND match exstention multipliers
# This encourages tracebacks with more sequential matches

# Importing modules
import Introduction
import Sequences
import Scores
import Matrices
import Traceback
import Results

def run():

    # Prints the intro information
    intro = Introduction.introduction()

    while True:

        # Stores both sequences
        inputs = Sequences.sequences()

        # Initializing scores to be used to create matrices
        scoring = Scores.scores(2, -2, -3, -1, 1)

        # Creating scoring matrices
        mtrxs = Matrices.scoringMatrices(scoring, inputs.seq1, inputs.seq2)

        # Creating tracebacks for each scoring matrix
        traces = Traceback.traceback(scoring, inputs.seq1, inputs.seq2, mtrxs.M1, mtrxs.M2, mtrxs.M3)

        # Displays results 
        rez = Results.results(inputs, scoring, mtrxs, traces)

        u = input('Would you like to try again? Y/N: ')
        if u == 'N':
            break

if __name__ == "__main__":
    run()
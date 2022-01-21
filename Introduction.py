class introduction:

    def __init__(self):
        print('-------------------------------------------  SMITH WATERMAN PROCESSOR  ------------------------------------------------')
        print('                                                by Zachary Pulliam                                                     ')
        print('')
        print('This program applies three seperate scoring algorithm to 2 sequence string.')
        print('   Matrix 1: a traditional scoring algorithm with match, mismatch, and gap scores')
        print('   Matrix 2: an advanced scoring algorithm with match, mismatch, gap, and gap exstension scores')
        print('   Matrix 3: a new scoring algorithm with match, mismatch, gap, gap exstension scores, AND match exstention multipliers')
        print('By having match extensions, this encourages tracebacks with more sequential matches')
        print('')
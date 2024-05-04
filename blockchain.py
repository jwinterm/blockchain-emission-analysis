import numpy as np

class Blockchain:
    '''Contains time and reward information for a blockchain'''
    def __init__(self, number_of_blocks=7e6, block_skip=10):
        self.number_of_blocks = int(number_of_blocks) # Number of blocks to calculate
        self.block_skip = int(block_skip) # Number of blocks to skip to save time

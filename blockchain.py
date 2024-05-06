import numpy as np

class Blockchain:
    '''Contains time and reward information for a blockchain'''
    def __init__(self, number_of_blocks=0, block_skip=0, block_time=0, launch_time=0):
        self.number_of_blocks = int(number_of_blocks) # Number of blocks to calculate
        self.block_skip = int(block_skip) # Number of blocks to skip to save time
        self.block_time = int(block_time) # Time between blocks in seconds
        self.blocks = np.arange(0, self.number_of_blocks, self.block_skip)
        self.launch_time = int(launch_time) # Launch time of the blockchain in seconds since epoch
        self.time = self.blocks * self.block_time
        self.date = np.array(self.time + self.launch_time, dtype='datetime64[s]')
        self.reward = np.zeros(len(self.blocks))
        self.cum_reward = np.zeros(len(self.blocks))

    def get_inflation_rate(self):
        '''Returns the inflation rate at a given block'''
        inflation_rate = np.zeros(len(self.blocks))
        for i in range(len(self.blocks)):
            year_time_cntr = 0
            year_emission_cntr = self.reward[i]
            j = 1
            while year_time_cntr < 86240*365.25:
                if i+j >= len(self.blocks):
                    year_time_cntr = 1e12
                    continue
                year_emission_cntr += self.reward[i+j]
                year_time_cntr += self.time[i+j] - self.time[i+j-1]
                j += 1
            inflation_rate[i] = (year_emission_cntr / self.cum_reward[i]) * 100
        return inflation_rate
            
    def get_per_block_reward(self):
        '''Returns the reward per block at a given block'''
        return self.reward / self.block_skip






import blockchain
import numpy as np

class Grin(blockchain.Blockchain):
    def __init__(self, number_of_blocks=3e7, block_skip=100, block_time=60, launch_time=1547576904):
        super().__init__(number_of_blocks, block_skip, block_time, launch_time)
        # Calculate Grin emission
        self.block_reward = 60 # Grin block reward forever
        self.already_generated_coins = 0
        for i in range(len(self.blocks)):
            self.already_generated_coins += self.block_reward * self.block_skip
            self.reward[i] = self.block_reward * self.block_skip
            self.cum_reward[i] = self.already_generated_coins 
        
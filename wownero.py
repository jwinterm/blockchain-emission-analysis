import blockchain
import numpy as np

class Wownero(blockchain.Blockchain):
    def __init__(self, number_of_blocks=15e6, block_skip=100, block_time=300, launch_time=1524223213):
        super().__init__(number_of_blocks, block_skip, block_time, launch_time)
        # First generate fully calculated date and reward data
        self.WOW_DIFFICULTY_TARGET = 300
        self.MONEY_SUPPLY = 2**64 - 1
        self.WOW_EMISSION_SPEED_FACTOR_PER_MINUTE = 24
        self.WOW_FINAL_SUBSIDY_PER_MINUTE = 0
        # Calculate Wownero emission
        self.already_generated_coins = 0
        for i in range(len(self.blocks)):
            target = self.WOW_DIFFICULTY_TARGET
            target_minutes = target / 60
            emission_speed_factor = self.WOW_EMISSION_SPEED_FACTOR_PER_MINUTE - (target_minutes - 1)
            reward = (self.MONEY_SUPPLY - int(self.already_generated_coins)) >> int(emission_speed_factor)
            if reward <= self.WOW_FINAL_SUBSIDY_PER_MINUTE * target_minutes:
                reward = self.WOW_FINAL_SUBSIDY_PER_MINUTE * target_minutes
            self.already_generated_coins += reward * self.block_skip
            self.reward[i] = reward*1e-11 * self.block_skip
            self.cum_reward[i] = self.already_generated_coins*1e-11 
        self.date = np.array(self.time, dtype='datetime64[s]')


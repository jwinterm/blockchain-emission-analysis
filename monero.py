import blockchain
import numpy as np

class Monero(blockchain.Blockchain):
    def __init__(self, number_of_blocks=3e7, block_skip=100):
        super().__init__(number_of_blocks, block_skip)
        # First generate fully calculated date and reward data
        self.already_generated_coins = 0
        self.blocks = np.arange(0, self.number_of_blocks, self.block_skip)
        self.launch_time = 1397793600
        self.time = np.zeros(len(self.blocks))
        self.time[0] = self.launch_time
        self.reward = np.zeros(len(self.blocks))
        self.cum_reward = np.zeros(len(self.blocks))
        self.XMR_DIFFICULTY_TARGET_V2 = 120
        self.XMR_DIFFICULTY_TARGET_V1 = 60
        self.MONEY_SUPPLY = 2**64 - 1
        self.XMR_EMISSION_SPEED_FACTOR_PER_MINUTE = 20
        self.XMR_FINAL_SUBSIDY_PER_MINUTE = 0.3e12
        self.v2_START = 1009827
        for i in range(len(self.blocks)):
            if self.blocks[i] < self.v2_START:
                target = self.XMR_DIFFICULTY_TARGET_V1
                target_minutes = target / 60
                emission_speed_factor = self.XMR_EMISSION_SPEED_FACTOR_PER_MINUTE - (target_minutes - 1)
            else:
                target = self.XMR_DIFFICULTY_TARGET_V2
                target_minutes = target / 60
                emission_speed_factor = self.XMR_EMISSION_SPEED_FACTOR_PER_MINUTE - (target_minutes - 1)
            reward = (self.MONEY_SUPPLY - int(self.already_generated_coins)) >> int(emission_speed_factor)
            if reward < self.XMR_FINAL_SUBSIDY_PER_MINUTE * target_minutes:
                reward = self.XMR_FINAL_SUBSIDY_PER_MINUTE * target_minutes
            self.already_generated_coins += reward * self.block_skip
            self.reward[i] = reward*1e-12 * self.block_skip
            self.cum_reward[i] = self.already_generated_coins*1e-12 
            if i > 0:
                self.time[i] = self.time[i-1] + target_minutes*60 * self.block_skip
        self.date = np.array(self.time, dtype='datetime64[s]')
        
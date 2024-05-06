import blockchain
import numpy as np

class Monero(blockchain.Blockchain):
    def __init__(self, number_of_blocks=2e7, block_skip=100, block_time=120, launch_time=1397793600):
        super().__init__(number_of_blocks, block_skip, block_time, launch_time)
        # First generate fully calculated date and reward data
        self.XMR_DIFFICULTY_TARGET_V2 = 120
        self.XMR_DIFFICULTY_TARGET_V1 = 60
        self.MONEY_SUPPLY = 2**64 - 1
        self.XMR_EMISSION_SPEED_FACTOR_PER_MINUTE = 20
        self.XMR_FINAL_SUBSIDY_PER_MINUTE = 0.3e12
        self.v2_START = 1009827
        # We have to fix the Monero time and date array because the changed difficulty target
        for i in range(len(self.blocks)):
            if self.blocks[i] < self.v2_START:
                self.time[i] = self.blocks[i] * self.XMR_DIFFICULTY_TARGET_V1
                self.date[i] = np.datetime64(int(self.time[i] + self.launch_time), 's')
            else:
                self.time[i] = self.time[i-1] + self.block_time * self.block_skip
                self.date[i] = np.datetime64(int(self.time[i] + self.launch_time), 's')
        # Calculate Monero emission
        self.already_generated_coins = 0
        for i in range(len(self.blocks)):
            if self.blocks[i] < self.v2_START:
                target_minutes = self.XMR_DIFFICULTY_TARGET_V1 / 60
            else:
                target_minutes = self.XMR_DIFFICULTY_TARGET_V2 / 60
            emission_speed_factor = self.XMR_EMISSION_SPEED_FACTOR_PER_MINUTE - (target_minutes - 1)
            reward = (self.MONEY_SUPPLY - int(self.already_generated_coins)) >> int(emission_speed_factor)
            if reward < self.XMR_FINAL_SUBSIDY_PER_MINUTE * target_minutes:
                reward = self.XMR_FINAL_SUBSIDY_PER_MINUTE * target_minutes
            self.already_generated_coins += reward * self.block_skip
            self.reward[i] = reward*1e-12 * self.block_skip
            self.cum_reward[i] = self.already_generated_coins*1e-12 
        
import blockchain
import numpy as np

class Bitcoin(blockchain.Blockchain):
    def __init__(self, number_of_blocks=7e6, block_skip=100, block_time=600, launch_time=1231006505):
        super().__init__(number_of_blocks, block_skip, block_time, launch_time)
        # Calculate Bitcoin emission
        for i in range(len(self.blocks)):
            self.reward[i] = ((np.uint(50e8)//2**((i*self.block_skip)//210000))*1e-8) * self.block_skip
            self.cum_reward[i] = self.cum_reward[i-1] + self.reward[i] if i > 0 else self.reward[i]

        # Historical data for bitcoin emission
        self.date_historical = [np.datetime64('2009-01-03'), np.datetime64('2012-11-28'), np.datetime64('2016-07-09'), np.datetime64('2024-04-20')]
        for i in range(30):
            next_date = self.date_historical[-1] + np.timedelta64(1461, 'D')
            self.date_historical.append(next_date)
        self.reward_historical = np.zeros(len(self.date_historical))
        self.cum_reward_historical = np.zeros(len(self.date_historical))
        for i in range(len(self.date_historical)):
            self.reward_historical[i] = 210000*(np.uint(50e8)//2**i)*1e-8
            if i < len(self.date_historical)-1:
                self.cum_reward_historical[i+1] = self.cum_reward_historical[i] + self.reward_historical[i]
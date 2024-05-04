import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

# Importing the classes
import bitcoin
import monero
import wownero
# Instance classes with specified number of blocks and block skip
btc = bitcoin.Bitcoin(7e6, 10)
xmr = monero.Monero(40e6, 100)
wow = wownero.Wownero(15e6, 100)

# Adjusting the date to start at the same time
xmr.date = xmr.date - (xmr.date[0] - btc.date_historical[0])
wow.date = wow.date - (wow.date[0] - btc.date_historical[0])
# Normalizing the data by the total number of coins (or 18.132e6 for Monero)
btc.cum_reward_historical = btc.cum_reward_historical / btc.cum_reward_historical[-1]
xmr.cum_reward = xmr.cum_reward / 18.132e6
wow.cum_reward = wow.cum_reward / wow.cum_reward[-1]

# Plotting the data
plt.plot(btc.date_historical, btc.cum_reward_historical, '-', color='orange', label='Bitcoin')
plt.plot(xmr.date, xmr.cum_reward, '--', color='grey', label='Monero')
plt.plot(wow.date, wow.cum_reward, '-.', color='pink', label='Wownero')

# Adding labels, grid, legend, etc
plt.xlabel('Time (years)')
plt.ylabel('% total coins emitted (pre-tail emission)')
plt.grid()
plt.legend()

# Displaying the plot
plt.show()
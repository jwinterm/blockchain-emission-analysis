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
btc.time = (btc.time - btc.time[0])/60/60/24/365
xmr.time = (xmr.time - xmr.time[0])/60/60/24/365
wow.time = (wow.time - wow.time[0])/60/60/24/365
# Normalizing the data by the total number of coins (or 18.132e6 for Monero)
btc.cum_reward = btc.cum_reward / btc.cum_reward[-1]
xmr.cum_reward = xmr.cum_reward / 18.132e6
wow.cum_reward = wow.cum_reward / wow.cum_reward[-1]

# Plotting the data
plt.plot(btc.time, btc.cum_reward, '-', color='orange', label='Bitcoin')
plt.plot(xmr.time, xmr.cum_reward, '--', color='grey', label='Monero')
plt.plot(wow.time, wow.cum_reward, '-.', color='pink', label='Wownero')

# Adding labels, grid, legend, etc
plt.xlabel('Time since launch (years)')
plt.ylabel('Total coins emitted (pre-tail emission)')
plt.grid()
plt.legend()

# Displaying the plot
plt.show()
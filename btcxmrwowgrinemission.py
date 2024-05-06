# Importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Importing our classes
import bitcoin
import monero
import wownero
import grin


# Instance classes 
btc = bitcoin.Bitcoin(number_of_blocks=6.4e6, block_skip=1000, block_time=600, launch_time=1231006505)
xmr = monero.Monero(number_of_blocks=2e7, block_skip=1000, block_time=120, launch_time=1397793600)
wow = wownero.Wownero(number_of_blocks=1e7, block_skip=1000, block_time=300, launch_time=1521598527)
grin = grin.Grin(number_of_blocks=6e7, block_skip=10000, block_time=60, launch_time=1547576904)


# Plotting the rewards data normalized to final supply or pre-tail emission for xmr or 100 years for grin
plt.plot(btc.time/(365.25*86400), btc.cum_reward/btc.cum_reward[-1], '-', color='orange', label='Bitcoin')
plt.plot(xmr.time/(365.25*86400), xmr.cum_reward/18.13e6, '--', color='grey', label='Monero')
plt.plot(wow.time/(365.25*86400), wow.cum_reward/wow.cum_reward[-1], '-.', color='pink', label='Wownero')
plt.plot(grin.time/(365.25*86400), grin.cum_reward/(100*365.25*86400), ':', color='black', label='Grin')

# Adding labels, grid, legend, etc
plt.xlabel('Time since launch (years)')
plt.ylabel('Total supply (coins)')
plt.title('Normalized total supply (18.1M for XMR, 100 years for Grin)')
plt.grid()
plt.legend()

# Displaying the plot
plt.show()
plt.close()

# Plotting the inflation data
print("Getting BTC inflation rate and plotting")
plt.semilogy(btc.time/(86400*365.25), btc.get_inflation_rate() , '-', color='orange', label='Bitcoin')
print("Getting XMR inflation rate and plotting")
plt.semilogy(xmr.time/(86400*365.25), xmr.get_inflation_rate() , '--', color='grey', label='Monero')
print("Getting WOW inflation rate and plotting")
plt.semilogy(wow.time/(86400*365.25), wow.get_inflation_rate() , '-.', color='pink', label='Wownero')
print("Getting GRIN inflation rate and plotting")
plt.semilogy(grin.time/(86400*365.25), grin.get_inflation_rate() , ':', color='black', label='Grin')

# Adding labels, grid, legend, etc
plt.xlabel('Time since launch (years)')
plt.ylabel('Annual inflation rate (%)')
plt.title('Next year supply divided by current supply')
plt.grid()
plt.legend()

# Displaying the plot
plt.show()
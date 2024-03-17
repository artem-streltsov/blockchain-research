---
title: 'Navigating the Blockchain: Block Explorers'
date: 2024-03-17
permalink: /posts/2024/03/block-explorers/
tags:
  - blockchain
  - block explorers
---

## What is a Block Explorer?
In the world of cryptocurrencies and blockchain, there is a helpful tool called a block explorer. A block explorer is like a search engine for blockchain data. It is a website where you can look up stuff about transactions, blocks, and addresses on a blockchain network.

## How do Block Explorers work?
When you make a transaction in the blockchain world, it gets recorded in a block along with other transactions. These blocks are linked together in a chain, forming the blockchain. A block explorer fetches data from these blocks and shows it to you in an easy-to-understand way.

## What can you do with Block Explorers?
### Track Transactions
You can use block explorers to see where your transaction is and check details like who sent it, who received it, and the amount.

### Explore Blocks
Look at individual blocks to see things like when they were created, how many transactions are in them, and how much crypto was moved around.

### Check Addresses
You can search for wallet addresses to see their transaction history and current balance.

### See Network Stats
Block explorers also show cool stats about the blockchain network, like how many transactions are happening and how fast it is going.

## Examples of Block Explorers
### <a href="https://blockchain.com">Blockchain.com</a>
Blockchain.com is the most popular Bitcoin block explorer and transaction search engine.

### <a href="https://etherscan.io">Etherscan</a>
Etherscan is a popular block explorer specifically designed for the Ethereum blockchain.

### <a href="https://voyager.online">Voyager</a>
Voyager is a block explorer for Starknet, a Layer 2 network over Ethereum.

## Example use of Etherscan API
Many Block Explorers, e.g. Etherscan, have an API (Application Programming Interface), which you can use to retrieve blockchain data and analyse it further or use in dApps (decentralised applications).

As an example, I used Etherscan API to plot MEV (Maximum Extractable Value) distribution in Etherium blocks. I followed these steps:
- Sign up to <a href="etherscan.io">Etherscan</a> and get a free api key. 
- Create a new project directory called `eth_mev_distribution`
- Create the `api_key.txt` file and paste the api key inside
- Make sure python3 is installed on your computer
- Create a virtual environment:<br>
  `$ python3 -m venv venv`<br>
  `$ source venv/bin/activate`
- Install libraries:<br>
  `$ pip install requests matplotlib`
- Create the `eth_mev_distribution.py` file and paste the following code inside:

```python
import requests
import matplotlib.pyplot as plt

# Function to fetch Ethereum block data using Etherscan API
def get_ethereum_block_data(block_number):
    with open("api_key.txt") as file:
        api_key = file.read().strip()

    url = f"https://api.etherscan.io/api?module=block&action=getblockreward&blockno={block_number}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to calculate MEV from Ethereum block data
def calculate_eth_mev(block_data):
    miner_reward = int(block_data['result']['blockReward'], 16)
    uncle_reward = int(block_data['result']['uncleInclusionReward'], 16)
    mev = miner_reward + uncle_reward
    return mev

# Function to fetch MEV distribution over blocks
def fetch_mev_distribution(start_block, end_block):
    mev_distribution = []
    for block_number in range(start_block, end_block+1):
        block_data = get_ethereum_block_data(block_number)
        mev = calculate_eth_mev(block_data)
        mev_distribution.append(mev)
    return mev_distribution

# Set the range of blocks to analyze
start_block = 13400000
end_block = 13400005
block_numbers = range(start_block, end_block+1)

# Fetch MEV distribution over blocks
mev_distribution = fetch_mev_distribution(start_block, end_block)

# Plot MEV distribution over blocks
plt.figure(figsize=(10, 6))
plt.plot(block_numbers, mev_distribution, color='blue')
plt.title('Maximum Extractable Value (MEV) Distribution Over Time')
plt.xlabel('Block Number')
plt.ylabel('MEV (wei)')
plt.xticks(block_numbers, [str(b) for b in block_numbers])
plt.grid(True)
plt.show()
```

- Now run `$ python3 eth_mev_distribution.py` and you should get the following graph:
![Etherium MEV distribution graph](/images/eth_mev_distribution.png)

- Deactivate the virtual environment:<br>
`$ deactivate`

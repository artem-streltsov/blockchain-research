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

# Fetch MEV distribution over blocka
mev_distribution = fetch_mev_distribution(start_block, end_block)

# Plot MEV distribution over blocks
plt.figure(figsize=(10, 6))
plt.plot(block_numbers, mev_distribution, color='blue')
plt.title('Maximum Extractable Value (MEV) Distribution Over Blocks')
plt.xlabel('Block Number')
plt.ylabel('MEV (wei)')
plt.xticks(block_numbers, [str(b) for b in block_numbers])
plt.grid(True)
plt.show()


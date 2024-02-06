import requests

# Function to fetch Ethereum block data using Etherscan API
def get_ethereum_block_data(block_number):
    api_key = open("api_key.txt").read().strip()
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

# Example usage
block_number = 13456789  # Replace with desired block number
block_data = get_ethereum_block_data(block_number)
mev = calculate_eth_mev(block_data)
print(f"MEV for block {block_number}: {mev} wei")


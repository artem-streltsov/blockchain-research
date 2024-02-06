import requests

# Function to fetch Ethereum transactions from Etherscan API
def fetch_ethereum_transactions(address, start_block=0, end_block=99999999):
    api_key = open("api_key.txt").read().strip()
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={start_block}&endblock={end_block}&sort=desc&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['result']

# Function to analyze MEV-generating addresses
def analyze_mev_sources(transactions, num_sources=10):
    address_mev = {}
    for tx in transactions:
        from_address = tx['from']
        gas_used = int(tx['gasPrice']) * int(tx['gasUsed'])
        if from_address in address_mev:
            address_mev[from_address] += gas_used
        else:
            address_mev[from_address] = gas_used
    sorted_addresses = sorted(address_mev.items(), key=lambda x: x[1], reverse=True)
    top_sources = sorted_addresses[:num_sources]
    return top_sources

# Get user input for Ethereum address and number of top MEV-generating addresses
address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
start_block = 0
end_block = 99999999
num_sources = 10

# Fetch Ethereum transactions
transactions = fetch_ethereum_transactions(address, start_block, end_block)

# Analyze top MEV-generating addresses
top_sources = analyze_mev_sources(transactions, num_sources)

# Print top MEV-generating addresses
print("Top MEV-generating addresses:")
for address, mev in top_sources:
    print(f"{address}: {mev} wei")


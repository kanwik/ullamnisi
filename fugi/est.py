from web3.auto import w3

# Get the balance of an account
balance = w3.eth.get_balance('0x0000000000000000000000000000000000000000')

# Send a transaction
tx_hash = w3.eth.send_transaction({
    'from': '0x0000000000000000000000000000000000000000',
    'to': '0x0000000000000000000000000000000000000001',
    'value': 1000000000000000000,
})

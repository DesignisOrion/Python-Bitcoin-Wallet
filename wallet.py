
from bitcoinlib.wallets import HDWallet  # importing bitcoinlib
wallet = HDWallet.create('Wallet1')  # creating a new crypto wallet
key1 = wallet.new_key()  # Geenrating a new HD Key
print(key1.address)  # create a new address

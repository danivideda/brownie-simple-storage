from brownie import accounts, config, SimpleStorage

PRIVATE_KEY = config["wallets"]["private_key"]

def init_accounts():
    global account
    account = accounts.add(PRIVATE_KEY)
    print("My Account: \n", account)

    print("All account: ")
    for i in range(len(accounts)):
        print(accounts[i])

def deploy_simple_storage():
    init_accounts()

    print("Deploying contracts...")
    simple_storage = SimpleStorage.deploy({"from": account})

    print(simple_storage)

def main():
    deploy_simple_storage()
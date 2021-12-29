from brownie import accounts, config, SimpleStorage, network

PRIVATE_KEY = config["wallets"]["private_key"]


def init_accounts():
    global account

    if network.show_active() == "development":
        account = accounts[0]

        print("My Account: \n", account)
        print("All account: ")

        for i in range(len(accounts)):
            print(accounts[i])

        print("==========")
    else:
        account = accounts.add(PRIVATE_KEY)


def deploy_simple_storage():
    init_accounts()

    print("Deploying contracts...")
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Contract deployed:", simple_storage)

    stored_value = simple_storage.retrieve()
    print("Stored value:", stored_value)

    print("Updating favorite number...")
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("Updated Stored value:", updated_stored_value)


def main():
    deploy_simple_storage()

from brownie import accounts
import os

def init_accounts():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print("My Account: \n", account)

    print("All account: ")
    for i in range(len(accounts)):
        print(accounts[i])

def deploy_simple_storage():
    init_accounts()

def main():
    deploy_simple_storage()
from brownie import accounts
import os

def deploy_simple_storage():
    accounts.add(os.getenv("PRIVATE_KEY"))
    for i in range(len(accounts)):
        print(accounts[i])

def main():
    deploy_simple_storage()
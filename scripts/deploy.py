from brownie import accounts, network, config, SimpleStorage

def main():
    # Load deployer from private key in brownie-config.yaml -> wallets.from_key -> .env
    pk = config["wallets"]["from_key"]
    acct = accounts.add(pk)

    print(f"Network: {network.show_active()}")
    print(f"Deployer: {acct.address}")

    # Deploy and verify on Etherscan (publish_source=True)
    contract = SimpleStorage.deploy(
        {"from": acct},
        publish_source=True
    )
    print(f"Deployed at: {contract.address}")

from web3 import Web3
from web3.middleware import geth_poa_middleware
from zksync2.manage_contracts.gas_provider import StaticGasProvider
from zksync2.core.types import Token
from zksync2.provider.eth_provider import EthereumProvider

from instance import eth_web3, zkSync_web3
from signer import account

def deposit():
    #geth_poa_middleware is used to connect to geth --dev.
    eth_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    #calculate  gas fees
    gas_provider = StaticGasProvider(Web3.toWei(1, "gwei"), 555000)

    #Create the ethereum provider for interacting with ethereum node, initialize zkSync signer and deposit funds.
    eth_provider = EthereumProvider.build_ethereum_provider(zksync=zkSync_web3,
                                                            eth=eth_web3,
                                                            account=account,
                                                            gas_provider=gas_provider)
    tx_receipt = eth_provider.deposit(Token.create_eth(),
                                    eth_web3.toWei("0.01", "ether"),
                                    account.address)
    # Show the output of the transaction details.
    print(f"tx status: {tx_receipt['status']}")


if __name__ == "__main__":
    deposit()

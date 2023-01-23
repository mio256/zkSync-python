from web3 import Web3
from zksync2.module.module_builder import ZkSyncBuilder

URL_TO_ETH_NETWORK = "https://rpc.ankr.com/eth_goerli"
ZKSYNC_NETWORK_URL = "https://zksync2-testnet.zksync.dev"

eth_web3 = Web3(Web3.HTTPProvider(URL_TO_ETH_NETWORK))
zkSync_web3 = ZkSyncBuilder.build(ZKSYNC_NETWORK_URL)
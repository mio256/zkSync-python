from zksync2.core.types import EthBlockParams

from instance import zkSync_web3
from signer import account

def get_account_balance():
    zk_balance = zkSync_web3.zksync.get_balance(account.address, EthBlockParams.LATEST.value)
    print(f"zkSync balance: {zk_balance}")


if __name__ == "__main__":
    get_account_balance()
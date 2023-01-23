from eth_typing import HexStr
from web3 import Web3
from zksync2.module.request_types import EIP712Meta, Transaction
from zksync2.core.types import ZkBlockParams

from zksync2.signer.eth_signer import PrivateKeyEthSigner
from zksync2.transaction.transaction712 import Transaction712

from instance import zkSync_web3
from signer import account


def transfer_to_self():
    chain_id = zkSync_web3.zksync.chain_id
    signer = PrivateKeyEthSigner(account, chain_id)

    nonce = zkSync_web3.zksync.get_transaction_count(account.address, ZkBlockParams.COMMITTED.value)
    tx = Transaction(from_=account.address,
                     to=account.address,
                     ergs_price=0,
                     ergs_limit=0,
                     data=HexStr("0x"),
                     eip712Meta=EIP712Meta)
    estimate_gas = int(zkSync_web3.zksync.eth_estimate_gas(tx))
    gas_price = zkSync_web3.zksync.gas_price

    print(f"Fee for transaction is: {estimate_gas * gas_price}")

    tx_712 = Transaction712(chain_id=chain_id,
                            nonce=nonce,
                            gas_limit=estimate_gas,
                            to=tx["to"],
                            value=Web3.toWei(0.01, 'ether'),
                            data=tx["data"],
                            maxPriorityFeePerGas=100000000,
                            maxFeePerGas=gas_price,
                            from_=account.address,
                            meta=tx["eip712Meta"])

    singed_message = signer.sign_typed_data(tx_712.to_eip712_struct())
    msg = tx_712.encode(singed_message)
    tx_hash = zkSync_web3.zksync.send_raw_transaction(msg)
    tx_receipt = zkSync_web3.zksync.wait_for_transaction_receipt(tx_hash, timeout=240, poll_latency=0.5)
    print(f"tx status: {tx_receipt['status']}")


if __name__ == "__main__":
    transfer_to_self()

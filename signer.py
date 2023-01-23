from eth_account import Account
from eth_account.signers.local import LocalAccount
from zksync2.signer.eth_signer import PrivateKeyEthSigner

# DON'T COMMIT REAL SECRET KEY
PRIVATE_KEY = '98b05edb1a99312202a8c2629e4bef2570d764a59791a60a32d654c95eadefa6'

chain_id = 5

account: LocalAccount = Account.from_key(PRIVATE_KEY)
signer = PrivateKeyEthSigner(account, chain_id)

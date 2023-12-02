## lncli

BASE:
```
lncli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Lnd/data/chain/bitcoin/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443
```

# Wallet create
`lncli --macaroonpath=/mnt/volume-nyc1-05-part1/Lnd/data/chain/bitcoin/testnet/admin.macaroon --tlscertpath=/mnt/volume-nyc1-05-part1/Lnd/tls.cert create`

# Wallet unlock
`lncli --macaroonpath=/mnt/volume-nyc1-05-part1/Lnd/data/chain/bitcoin/testnet/admin.macaroon --tlscertpath=/mnt/volume-nyc1-05-part1/Lnd/tls.cert unlock`

# New address < type >
`lncli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Lnd/data/chain/bitcoin/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 newaddress p2tr`


## tapcli
COPY BASE: 
```
tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lnd/tls.cert --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=localhost:10009 
```

# Get info
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lnd/tls.cert --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=localhost:10009  getinfo`

# List assets
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 assets list`

# List universes
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 universe federation list`

# Add universe to federation
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 universe federation add --universe_host testnet.laisee.org`

# Sync to specifc universe
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 universe sync --universe_host testnet.laisee.org`

# Get universe root (known assets?)
`tapcli --tlscertpath=/mnt/volume-nyc1-05-part1/Lit/letsencrypt/node.fulminologylabs.co --macaroonpath=/mnt/volume-nyc1-05-part1/Tapd/data/testnet/admin.macaroon --rpcserver=node.fulminologylabs.co:8443 universe roots`
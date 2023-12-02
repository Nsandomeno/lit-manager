# LiT Manager
A service for managing Lightning Terminal via `litd`, `lnd`, `pool`, `faraday`, `loop`, and `tapd` RPC API's.

# Versions
```
LiT: v0.12.1-alpha
LND: v0.17.1-beta
TAPD: v0.3.1-alpha
Loop: v0.26.5-beta
Pool: v0.6.4-beta
Faraday: v0.2.11-alpha
```

## Download gRPC service definitions
Ensure you are downloading the protos from the tagged branch that matches the version of the Tapd instance running in the deployed LiT bundle.

Currently requiring
```
# LND
lightning.proto

# TAPD
taprootassets.proto
assetwalletrpc/assetwallet.proto
mintrpc/mint.proto
universerpc/universe.proto
```

# LND proto links (check versions/tags!)
```
https://raw.githubusercontent.com/lightningnetwork/lnd/v0.17.1-beta/lnrpc/lightning.proto
```

# Tapd proto links (check versions/tags!)
```
https://raw.githubusercontent.com/lightninglabs/taproot-assets/v0.3.1/taprpc/taprootassets.proto
https://raw.githubusercontent.com/lightninglabs/taproot-assets/v0.3.1/taprpc/assetwalletrpc/assetwallet.proto
https://raw.githubusercontent.com/lightninglabs/taproot-assets/v0.3.1/taprpc/mintrpc/mint.proto
https://raw.githubusercontent.com/lightninglabs/taproot-assets/v0.3.1/taprpc/universerpc/universe.proto
```

# Install
Template
`curl -o ./proto/< RPC NAME >.proto https://raw.githubusercontent.com/lightninglabs/< DAEMON REPO >/< VERSION TAG >/< RPC NAME >/< RPC NAME >.proto`

Example
`curl -o ./lit/proto/assetwallet.proto https://raw.githubusercontent.com/lightninglabs/taproot-assets/v0.3.1/taprpc/assetwalletrpc/assetwallet.proto`

# Compile
Template
`lnd/bin/python -m grpc_tools.protoc -I ./proto/ --proto_path=googleapis:. --mypy_out=./app/lit --python_out=./app/lit --grpc_python_out=./app/lit < RPC NAME >.proto`

Example
`lnd/bin/python -m grpc_tools.protoc -I ./proto/ --proto_path=googleapis:. --mypy_out=./app/lit --python_out=./app/lit --grpc_python_out=./app/lit  ./proto/taprootassets.proto`

Bulk
`lnd/bin/python -m grpc_tools.protoc -I ./proto/ --proto_path=googleapis:. --mypy_out=./app/lit --python_out=./app/lit --grpc_python_out=./app/lit ./proto/*.proto`

# Python module imports
``

## Download security materials

# [ TODO ] - this download feels wrong and I'm very interested to find a better way of sharing this material.

According to `https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md`, 
`tlsextraip` or `tlsextradomain` should be set with `lit.conf`. That will create `tls.cert`s
that accomodate remote access. 

`scp < user >@< node ip >:/< path >/< to >/Lnd/tls.key  .`
`scp < user >@< node ip >:/< path >/< to >/Lnd/tls.cert  .`
`scp < user >@< node ip >:/< path >/< to >/Lnd/data/chain/bitcoin/< mode >/admin.macaroon `

And then one last for `Tapd`

`scp < user >@< node ip >:/< path >/< to >/Tapd/data/< mode >/admin.macaroon .`

## Demo 
`python -m app.demo.demo`
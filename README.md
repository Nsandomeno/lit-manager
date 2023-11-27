# lit-manager
A service for managing Lightning Terminal via `litd`, `lnd`, `pool`, `faraday`, `loop`, and `tapd` RPC API's.

# download gRPC service definitions
Install
`curl -o assetwallet.proto https://github.com/lightninglabs/taproot-assets/taprpc/assetwalletrpc/assetwallet.proto`

Compile
`python -m grpc_tools.protoc --proto_path=googleapis:. --mypy_out=. --python_out=. --grpc_python_out=. assetwallet.proto`

# download security materials

# [ TODO ] - this download feels wrong and I'm very interested to find a better way of sharing this material.

According to `https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md`, 
`tlsextraip` or `tlsextradomain` should be set with `lit.conf`. That will create `tls.cert`s
that accomodate remote access. 

`scp < user >@< node ip >:/< path >/< to >/Lnd/tls.key  .`
`scp < user >@< node ip >:/< path >/< to >/Lnd/tls.cert  .`
`scp < user >@< node ip >:/< path >/< to >/Lnd/data/chain/bitcoin/< mode >/admin.macaroon `

And then one last for `Tapd`

`scp < user >@< node ip >:/< path >/< to >/Tapd/data/< mode >/admin.macaroon .`
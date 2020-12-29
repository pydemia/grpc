# grpc
gRPC implementations

## Set env

```bash
CONDA_ENV_NM="grpc-py37"
PY_VER="3.7"

conda create -n "$CONDA_ENV_NM" python="$PY_VER" --quiet -y
# conda env create  --quiet \
#     -n $CONDA_ENV_NM \
#     python=$PY_VER \
#     --file $BASE_ENVFILE

conda activate "$CONDA_ENV_NM"

pip install grpcio grpcio-tools protobuf
```

## Components

* Proto file
* gRPC client
* gRPC server

## Type of gRPC implementations
* Unary

```grpc
rpc HelloServer(RequestMessage) returns (ResponseMessage);
```

* Streaming
  * Server Streaming

```grpc
rpc HelloServer(RequestMessage) returns (stream ResponseMessage);
```

  * Client Streaming

```grpc
rpc HelloServer(stream RequestMessage) returns (ResponseMessage);
```

  * Bidirectional Streaming

```grpc
rpc HelloServer(stream RequestMessage) returns (stream ResponseMessage);
```


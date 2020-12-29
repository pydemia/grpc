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

## Types

https://developers.google.com/protocol-buffers/docs/proto3

* Defining A Message Type
* [Scalar Value Types](https://developers.google.com/protocol-buffers/docs/proto3#scalar)
  - double
  - float
  - int32
  - int64
  - uint32
  - uint64
  - sint32
  - sint64
  - fixed32
  - fixed64
  - sfixed32
  - sfixed64
  - bool
  - string
  - bytes
  - 

| .proto Type | Notes                                                                                                                                           | C++ Type | Java Type  | Python Type[2] | Go Type | Ruby Type                      | C# Type    | PHP Type          | Dart Type |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------|----------------|---------|--------------------------------|------------|-------------------|-----------|
| float       |                                                                                                                                                 | float    | float      | float          | float32 | Float                          | float      | float             | double    |
| int32       | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| int64       | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| uint32      | Uses variable-length encoding.                                                                                                                  | uint32   | int[1]     | int/long[3]    | uint32  | Fixnum or Bignum (as required) | uint       | integer           | int       |
| uint64      | Uses variable-length encoding.                                                                                                                  | uint64   | long[1]    | int/long[3]    | uint64  | Bignum                         | ulong      | integer/string[5] | Int64     |
| sint32      | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s.                            | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| sint64      | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s.                            | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| fixed32     | Always four bytes. More efficient than uint32 if values are often greater than 228.                                                             | uint32   | int[1]     | int/long[3]    | uint32  | Fixnum or Bignum (as required) | uint       | integer           | int       |
| fixed64     | Always eight bytes. More efficient than uint64 if values are often greater than 256.                                                            | uint64   | long[1]    | int/long[3]    | uint64  | Bignum                         | ulong      | integer/string[5] | Int64     |
| sfixed32    | Always four bytes.                                                                                                                              | int32    | int        | int            | int32   | Fixnum or Bignum (as required) | int        | integer           | int       |
| sfixed64    | Always eight bytes.                                                                                                                             | int64    | long       | int/long[3]    | int64   | Bignum                         | long       | integer/string[5] | Int64     |
| bool        |                                                                                                                                                 | bool     | boolean    | bool           | bool    | TrueClass/FalseClass           | bool       | boolean           | bool      |
| string      | A string must always contain UTF-8 encoded or 7-bit ASCII text, and cannot be longer than 232.                                                  | string   | String     | str/unicode[4] | string  | String (UTF-8)                 | string     | string            | String    |
| bytes       | May contain any arbitrary sequence of bytes no longer than 232.                                                                                 | string   | ByteString | str            | []byte  | String (ASCII-8BIT)            | ByteString | string            | List      |


* Default Values
* Enumerations
* Using Other Message Types
* Nested Types
* Updating A Message Type
* Unknown Fields
* Any
* Oneof
* Maps
* Packages
* Defining Services
* JSON Mapping
* Options
* Generating Your Classes
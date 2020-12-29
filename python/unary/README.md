
# Python Implementations

## Unary

1. Prepare a Proto file(Unary)

`grpc_impl_unary.proto`:

```grpc
syntax = "proto3";

package grpc_impl_unary;

service Unary{
    // A simple RPC.
    //
    // Obtains the MessageResponse at a given position.
    rpc GetServerResponse(Message) returns (MessageResponse) {}

}

message Message{
    string message = 1;
}

message MessageResponse{
    string message = 1;
    bool received = 2;
}
```

2. Create stub files for `client` & `server`.

```bash
python -m grpc_tools.protoc \
  ./grpc_impl_unary.proto \
  --proto_path=. \
  --python_out=. \
  --grpc_python_out=.
```

Then, it creates 2 files:
* Server: `{proto_filename}_pb2.py` 
* Client: `{proto_filename}_pb2_grpc.py`

In this case:
* Server: `grpc_impl_unary_pb2.py`
* Client: `grpc_impl_unary_pb2_grpc.py`

3. Implements a server

```python
import grpc
from concurrent import futures
import time
import grpc_impl_unary_pb2_grpc as pb2_grpc
import grpc_impl_unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Server: Request received: "{message}"'
        
        # This dict keys should be equal to fields in proto
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
```

4. Implement a client

```python
import grpc
import grpc_impl_unary_pb2_grpc as pb2_grpc
import grpc_impl_unary_pb2 as pb2


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = UnaryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')
```

5. Run the server

```bash
python3 server.py
```

6. Run the client to send a request

```bash
$ python3 client.py

message: "Hello Server you there?"

message: "Server: Request received: \"Hello Server you there?\""
received: true
```

# Python Implementations

## Unary

1. Prepare a Proto file(Bidirectional)

`grpc_impl_bidirectional.proto`:

```grpc
syntax = "proto3";

package bidirectional;

service Bidirectional {
    // A Bidirectional streaming RPC.
    //
    // Accepts a stream of Message sent while a route is being traversed,
    rpc GetServerResponse(stream Message) returns (stream Message) {}
}

message Message {
    string message = 1;
}
```

2. Create stub files for `client` & `server`.

```bash
python -m grpc_tools.protoc \
  ./grpc_impl_bidirectional.proto \
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
from concurrent import futures

import grpc
import grpc_impl_bidirectional_pb2_grpc as bidirectional_pb2_grpc


class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):

    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            yield message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
```

4. Implement a client

```python
from __future__ import print_function

import grpc
import grpc_impl_bidirectional_pb2_grpc as bidirectional_pb2_grpc
import grpc_impl_bidirectional_pb2 as bidirectional_pb2


def make_message(message):
    return bidirectional_pb2.Message(
        message=message
    )


def generate_messages():
    messages = [
        make_message("First message"),
        make_message("Second message"),
        make_message("Third message"),
        make_message("Fourth message"),
        make_message("Fifth message"),
    ]
    for msg in messages:
        print("Request: Hello Server Sending you the %s" % msg.message)
        yield msg


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("Response: Hello from the server received your %s" % response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()
```

5. Run the server

```bash
python3 server.py
```

6. Run the client to send a request

```bash
$ python3 client.py

Request: Hello Server Sending you the First message
Request: Hello Server Sending you the Second message
Request: Hello Server Sending you the Third message
Request: Hello Server Sending you the Fourth message
Request: Hello Server Sending you the Fifth message
Response: Hello from the server received your First message
Response: Hello from the server received your Second message
Response: Hello from the server received your Third message
Response: Hello from the server received your Fourth message
Response: Hello from the server received your Fifth message
```
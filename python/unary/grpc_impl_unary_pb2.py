# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_impl_unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_impl_unary.proto',
  package='grpc_impl_unary',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15grpc_impl_unary.proto\x12\x0fgrpc_impl_unary\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32Z\n\x05Unary\x12Q\n\x11GetServerResponse\x12\x18.grpc_impl_unary.Message\x1a .grpc_impl_unary.MessageResponse\"\x00\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='grpc_impl_unary.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_impl_unary.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=68,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='grpc_impl_unary.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc_impl_unary.MessageResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received', full_name='grpc_impl_unary.MessageResponse.received', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'grpc_impl_unary_pb2'
  # @@protoc_insertion_point(class_scope:grpc_impl_unary.Message)
  })
_sym_db.RegisterMessage(Message)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'grpc_impl_unary_pb2'
  # @@protoc_insertion_point(class_scope:grpc_impl_unary.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)



_UNARY = _descriptor.ServiceDescriptor(
  name='Unary',
  full_name='grpc_impl_unary.Unary',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=124,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='grpc_impl_unary.Unary.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNARY)

DESCRIPTOR.services_by_name['Unary'] = _UNARY

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NamespacesMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NamespacesMessage.proto',
  package='org.apache.hadoop.hbase_rest.rest.protobuf.generated',
  syntax='proto2',
  serialized_pb=_b('\n\x17NamespacesMessage.proto\x12/org.apache.hadoop.hbase_rest.rest.protobuf.generated\"\x1f\n\nNamespaces\x12\x11\n\tnamespace\x18\x01 \x03(\t')
)




_NAMESPACES = _descriptor.Descriptor(
  name='Namespaces',
  full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Namespaces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.Namespaces.namespace', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Namespaces'] = _NAMESPACES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Namespaces = _reflection.GeneratedProtocolMessageType('Namespaces', (_message.Message,), dict(
  DESCRIPTOR = _NAMESPACES,
  __module__ = 'NamespacesMessage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.hadoop.hbase_rest.rest.protobuf.generated.Namespaces)
  ))
_sym_db.RegisterMessage(Namespaces)


# @@protoc_insertion_point(module_scope)

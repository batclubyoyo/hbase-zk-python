# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NamespacePropertiesMessage.proto

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
  name='NamespacePropertiesMessage.proto',
  package='org.apache.hadoop.hbase_rest.rest.protobuf.generated',
  syntax='proto2',
  serialized_pb=_b('\n NamespacePropertiesMessage.proto\x12/org.apache.hadoop.hbase_rest.rest.protobuf.generated\"\x9b\x01\n\x13NamespaceProperties\x12\\\n\x05props\x18\x01 \x03(\x0b\x32M.org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.Property\x1a&\n\x08Property\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t')
)




_NAMESPACEPROPERTIES_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.Property.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.Property.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=203,
  serialized_end=241,
)

_NAMESPACEPROPERTIES = _descriptor.Descriptor(
  name='NamespaceProperties',
  full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='props', full_name='org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.props', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NAMESPACEPROPERTIES_PROPERTY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=241,
)

_NAMESPACEPROPERTIES_PROPERTY.containing_type = _NAMESPACEPROPERTIES
_NAMESPACEPROPERTIES.fields_by_name['props'].message_type = _NAMESPACEPROPERTIES_PROPERTY
DESCRIPTOR.message_types_by_name['NamespaceProperties'] = _NAMESPACEPROPERTIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamespaceProperties = _reflection.GeneratedProtocolMessageType('NamespaceProperties', (_message.Message,), dict(

  Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(
    DESCRIPTOR = _NAMESPACEPROPERTIES_PROPERTY,
    __module__ = 'NamespacePropertiesMessage_pb2'
    # @@protoc_insertion_point(class_scope:org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties.Property)
    ))
  ,
  DESCRIPTOR = _NAMESPACEPROPERTIES,
  __module__ = 'NamespacePropertiesMessage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.hadoop.hbase_rest.rest.protobuf.generated.NamespaceProperties)
  ))
_sym_db.RegisterMessage(NamespaceProperties)
_sym_db.RegisterMessage(NamespaceProperties.Property)


# @@protoc_insertion_point(module_scope)

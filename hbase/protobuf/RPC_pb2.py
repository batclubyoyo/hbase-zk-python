# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RPC.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Tracing_pb2 as Tracing__pb2
from . import HBase_pb2 as HBase__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RPC.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tRPC.proto\x1a\rTracing.proto\x1a\x0bHBase.proto\"<\n\x0fUserInformation\x12\x16\n\x0e\x65\x66\x66\x65\x63tive_user\x18\x01 \x02(\t\x12\x11\n\treal_user\x18\x02 \x01(\t\"\xb6\x01\n\x10\x43onnectionHeader\x12#\n\tuser_info\x18\x01 \x01(\x0b\x32\x10.UserInformation\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x1e\n\x16\x63\x65ll_block_codec_class\x18\x03 \x01(\t\x12#\n\x1b\x63\x65ll_block_compressor_class\x18\x04 \x01(\t\x12\"\n\x0cversion_info\x18\x05 \x01(\x0b\x32\x0c.VersionInfo\"\x1f\n\rCellBlockMeta\x12\x0e\n\x06length\x18\x01 \x01(\r\"|\n\x11\x45xceptionResponse\x12\x1c\n\x14\x65xception_class_name\x18\x01 \x01(\t\x12\x13\n\x0bstack_trace\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x14\n\x0c\x64o_not_retry\x18\x05 \x01(\x08\"\xa6\x01\n\rRequestHeader\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\r\x12\x1d\n\ntrace_info\x18\x02 \x01(\x0b\x32\t.RPCTInfo\x12\x13\n\x0bmethod_name\x18\x03 \x01(\t\x12\x15\n\rrequest_param\x18\x04 \x01(\x08\x12\'\n\x0f\x63\x65ll_block_meta\x18\x05 \x01(\x0b\x32\x0e.CellBlockMeta\x12\x10\n\x08priority\x18\x06 \x01(\r\"q\n\x0eResponseHeader\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\r\x12%\n\texception\x18\x02 \x01(\x0b\x32\x12.ExceptionResponse\x12\'\n\x0f\x63\x65ll_block_meta\x18\x03 \x01(\x0b\x32\x0e.CellBlockMetaB<\n*org.apache.hadoop.hbase.protobuf.generatedB\tRPCProtosH\x01\xa0\x01\x01')
  ,
  dependencies=[Tracing__pb2.DESCRIPTOR,HBase__pb2.DESCRIPTOR,])




_USERINFORMATION = _descriptor.Descriptor(
  name='UserInformation',
  full_name='UserInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effective_user', full_name='UserInformation.effective_user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real_user', full_name='UserInformation.real_user', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=101,
)


_CONNECTIONHEADER = _descriptor.Descriptor(
  name='ConnectionHeader',
  full_name='ConnectionHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='ConnectionHeader.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ConnectionHeader.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_block_codec_class', full_name='ConnectionHeader.cell_block_codec_class', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_block_compressor_class', full_name='ConnectionHeader.cell_block_compressor_class', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_info', full_name='ConnectionHeader.version_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=104,
  serialized_end=286,
)


_CELLBLOCKMETA = _descriptor.Descriptor(
  name='CellBlockMeta',
  full_name='CellBlockMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='CellBlockMeta.length', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=288,
  serialized_end=319,
)


_EXCEPTIONRESPONSE = _descriptor.Descriptor(
  name='ExceptionResponse',
  full_name='ExceptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exception_class_name', full_name='ExceptionResponse.exception_class_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='ExceptionResponse.stack_trace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ExceptionResponse.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ExceptionResponse.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_not_retry', full_name='ExceptionResponse.do_not_retry', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=321,
  serialized_end=445,
)


_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_id', full_name='RequestHeader.call_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_info', full_name='RequestHeader.trace_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='RequestHeader.method_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_param', full_name='RequestHeader.request_param', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_block_meta', full_name='RequestHeader.cell_block_meta', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='RequestHeader.priority', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=448,
  serialized_end=614,
)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call_id', full_name='ResponseHeader.call_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exception', full_name='ResponseHeader.exception', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_block_meta', full_name='ResponseHeader.cell_block_meta', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=616,
  serialized_end=729,
)

_CONNECTIONHEADER.fields_by_name['user_info'].message_type = _USERINFORMATION
_CONNECTIONHEADER.fields_by_name['version_info'].message_type = HBase__pb2._VERSIONINFO
_REQUESTHEADER.fields_by_name['trace_info'].message_type = Tracing__pb2._RPCTINFO
_REQUESTHEADER.fields_by_name['cell_block_meta'].message_type = _CELLBLOCKMETA
_RESPONSEHEADER.fields_by_name['exception'].message_type = _EXCEPTIONRESPONSE
_RESPONSEHEADER.fields_by_name['cell_block_meta'].message_type = _CELLBLOCKMETA
DESCRIPTOR.message_types_by_name['UserInformation'] = _USERINFORMATION
DESCRIPTOR.message_types_by_name['ConnectionHeader'] = _CONNECTIONHEADER
DESCRIPTOR.message_types_by_name['CellBlockMeta'] = _CELLBLOCKMETA
DESCRIPTOR.message_types_by_name['ExceptionResponse'] = _EXCEPTIONRESPONSE
DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInformation = _reflection.GeneratedProtocolMessageType('UserInformation', (_message.Message,), dict(
  DESCRIPTOR = _USERINFORMATION,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:UserInformation)
  ))
_sym_db.RegisterMessage(UserInformation)

ConnectionHeader = _reflection.GeneratedProtocolMessageType('ConnectionHeader', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTIONHEADER,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionHeader)
  ))
_sym_db.RegisterMessage(ConnectionHeader)

CellBlockMeta = _reflection.GeneratedProtocolMessageType('CellBlockMeta', (_message.Message,), dict(
  DESCRIPTOR = _CELLBLOCKMETA,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:CellBlockMeta)
  ))
_sym_db.RegisterMessage(CellBlockMeta)

ExceptionResponse = _reflection.GeneratedProtocolMessageType('ExceptionResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXCEPTIONRESPONSE,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:ExceptionResponse)
  ))
_sym_db.RegisterMessage(ExceptionResponse)

RequestHeader = _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTHEADER,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:RequestHeader)
  ))
_sym_db.RegisterMessage(RequestHeader)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEHEADER,
  __module__ = 'RPC_pb2'
  # @@protoc_insertion_point(class_scope:ResponseHeader)
  ))
_sym_db.RegisterMessage(ResponseHeader)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\tRPCProtosH\001\240\001\001'))
# @@protoc_insertion_point(module_scope)
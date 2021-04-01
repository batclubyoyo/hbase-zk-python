# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Aggregate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Client_pb2 as Client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Aggregate.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x41ggregate.proto\x1a\x0c\x43lient.proto\"k\n\x10\x41ggregateRequest\x12\x1e\n\x16interpreter_class_name\x18\x01 \x02(\t\x12\x13\n\x04scan\x18\x02 \x02(\x0b\x32\x05.Scan\x12\"\n\x1ainterpreter_specific_bytes\x18\x03 \x01(\x0c\"<\n\x11\x41ggregateResponse\x12\x12\n\nfirst_part\x18\x01 \x03(\x0c\x12\x13\n\x0bsecond_part\x18\x02 \x01(\x0c\x32\xef\x02\n\x10\x41ggregateService\x12/\n\x06GetMax\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12/\n\x06GetMin\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12/\n\x06GetSum\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12\x32\n\tGetRowNum\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12/\n\x06GetAvg\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12/\n\x06GetStd\x12\x11.AggregateRequest\x1a\x12.AggregateResponse\x12\x32\n\tGetMedian\x12\x11.AggregateRequest\x1a\x12.AggregateResponseBE\n*org.apache.hadoop.hbase.protobuf.generatedB\x0f\x41ggregateProtosH\x01\x88\x01\x01\xa0\x01\x01')
  ,
  dependencies=[Client__pb2.DESCRIPTOR,])




_AGGREGATEREQUEST = _descriptor.Descriptor(
  name='AggregateRequest',
  full_name='AggregateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interpreter_class_name', full_name='AggregateRequest.interpreter_class_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scan', full_name='AggregateRequest.scan', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interpreter_specific_bytes', full_name='AggregateRequest.interpreter_specific_bytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=33,
  serialized_end=140,
)


_AGGREGATERESPONSE = _descriptor.Descriptor(
  name='AggregateResponse',
  full_name='AggregateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_part', full_name='AggregateResponse.first_part', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_part', full_name='AggregateResponse.second_part', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=142,
  serialized_end=202,
)

_AGGREGATEREQUEST.fields_by_name['scan'].message_type = Client__pb2._SCAN
DESCRIPTOR.message_types_by_name['AggregateRequest'] = _AGGREGATEREQUEST
DESCRIPTOR.message_types_by_name['AggregateResponse'] = _AGGREGATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AggregateRequest = _reflection.GeneratedProtocolMessageType('AggregateRequest', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATEREQUEST,
  __module__ = 'Aggregate_pb2'
  # @@protoc_insertion_point(class_scope:AggregateRequest)
  ))
_sym_db.RegisterMessage(AggregateRequest)

AggregateResponse = _reflection.GeneratedProtocolMessageType('AggregateResponse', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATERESPONSE,
  __module__ = 'Aggregate_pb2'
  # @@protoc_insertion_point(class_scope:AggregateResponse)
  ))
_sym_db.RegisterMessage(AggregateResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\017AggregateProtosH\001\210\001\001\240\001\001'))

_AGGREGATESERVICE = _descriptor.ServiceDescriptor(
  name='AggregateService',
  full_name='AggregateService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=205,
  serialized_end=572,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMax',
    full_name='AggregateService.GetMax',
    index=0,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMin',
    full_name='AggregateService.GetMin',
    index=1,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSum',
    full_name='AggregateService.GetSum',
    index=2,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRowNum',
    full_name='AggregateService.GetRowNum',
    index=3,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAvg',
    full_name='AggregateService.GetAvg',
    index=4,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStd',
    full_name='AggregateService.GetStd',
    index=5,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMedian',
    full_name='AggregateService.GetMedian',
    index=6,
    containing_service=None,
    input_type=_AGGREGATEREQUEST,
    output_type=_AGGREGATERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGGREGATESERVICE)

DESCRIPTOR.services_by_name['AggregateService'] = _AGGREGATESERVICE

# @@protoc_insertion_point(module_scope)

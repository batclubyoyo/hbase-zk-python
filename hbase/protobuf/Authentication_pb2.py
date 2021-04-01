# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Authentication.proto

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
  name='Authentication.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x14\x41uthentication.proto\"E\n\x11\x41uthenticationKey\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x17\n\x0f\x65xpiration_date\x18\x02 \x02(\x03\x12\x0b\n\x03key\x18\x03 \x02(\x0c\"\xbc\x01\n\x0fTokenIdentifier\x12#\n\x04kind\x18\x01 \x02(\x0e\x32\x15.TokenIdentifier.Kind\x12\x10\n\x08username\x18\x02 \x02(\x0c\x12\x0e\n\x06key_id\x18\x03 \x02(\x05\x12\x12\n\nissue_date\x18\x04 \x01(\x03\x12\x17\n\x0f\x65xpiration_date\x18\x05 \x01(\x03\x12\x17\n\x0fsequence_number\x18\x06 \x01(\x03\"\x1c\n\x04Kind\x12\x14\n\x10HBASE_AUTH_TOKEN\x10\x00\">\n\x05Token\x12\x12\n\nidentifier\x18\x01 \x01(\x0c\x12\x10\n\x08password\x18\x02 \x01(\x0c\x12\x0f\n\x07service\x18\x03 \x01(\x0c\"\x1f\n\x1dGetAuthenticationTokenRequest\"7\n\x1eGetAuthenticationTokenResponse\x12\x15\n\x05token\x18\x01 \x01(\x0b\x32\x06.Token\"\x0f\n\rWhoAmIRequest\"7\n\x0eWhoAmIResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0b\x61uth_method\x18\x02 \x01(\t2\x9d\x01\n\x15\x41uthenticationService\x12Y\n\x16GetAuthenticationToken\x12\x1e.GetAuthenticationTokenRequest\x1a\x1f.GetAuthenticationTokenResponse\x12)\n\x06WhoAmI\x12\x0e.WhoAmIRequest\x1a\x0f.WhoAmIResponseBJ\n*org.apache.hadoop.hbase.protobuf.generatedB\x14\x41uthenticationProtosH\x01\x88\x01\x01\xa0\x01\x01')
)



_TOKENIDENTIFIER_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='TokenIdentifier.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HBASE_AUTH_TOKEN', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=256,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_TOKENIDENTIFIER_KIND)


_AUTHENTICATIONKEY = _descriptor.Descriptor(
  name='AuthenticationKey',
  full_name='AuthenticationKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='AuthenticationKey.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_date', full_name='AuthenticationKey.expiration_date', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='AuthenticationKey.key', index=2,
      number=3, type=12, cpp_type=9, label=2,
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
  serialized_start=24,
  serialized_end=93,
)


_TOKENIDENTIFIER = _descriptor.Descriptor(
  name='TokenIdentifier',
  full_name='TokenIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='TokenIdentifier.kind', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='TokenIdentifier.username', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key_id', full_name='TokenIdentifier.key_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_date', full_name='TokenIdentifier.issue_date', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_date', full_name='TokenIdentifier.expiration_date', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='TokenIdentifier.sequence_number', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOKENIDENTIFIER_KIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=284,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Token.identifier', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='Token.password', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='Token.service', index=2,
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
  serialized_start=286,
  serialized_end=348,
)


_GETAUTHENTICATIONTOKENREQUEST = _descriptor.Descriptor(
  name='GetAuthenticationTokenRequest',
  full_name='GetAuthenticationTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=350,
  serialized_end=381,
)


_GETAUTHENTICATIONTOKENRESPONSE = _descriptor.Descriptor(
  name='GetAuthenticationTokenResponse',
  full_name='GetAuthenticationTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='GetAuthenticationTokenResponse.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=383,
  serialized_end=438,
)


_WHOAMIREQUEST = _descriptor.Descriptor(
  name='WhoAmIRequest',
  full_name='WhoAmIRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=440,
  serialized_end=455,
)


_WHOAMIRESPONSE = _descriptor.Descriptor(
  name='WhoAmIResponse',
  full_name='WhoAmIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='WhoAmIResponse.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_method', full_name='WhoAmIResponse.auth_method', index=1,
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
  serialized_start=457,
  serialized_end=512,
)

_TOKENIDENTIFIER.fields_by_name['kind'].enum_type = _TOKENIDENTIFIER_KIND
_TOKENIDENTIFIER_KIND.containing_type = _TOKENIDENTIFIER
_GETAUTHENTICATIONTOKENRESPONSE.fields_by_name['token'].message_type = _TOKEN
DESCRIPTOR.message_types_by_name['AuthenticationKey'] = _AUTHENTICATIONKEY
DESCRIPTOR.message_types_by_name['TokenIdentifier'] = _TOKENIDENTIFIER
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['GetAuthenticationTokenRequest'] = _GETAUTHENTICATIONTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetAuthenticationTokenResponse'] = _GETAUTHENTICATIONTOKENRESPONSE
DESCRIPTOR.message_types_by_name['WhoAmIRequest'] = _WHOAMIREQUEST
DESCRIPTOR.message_types_by_name['WhoAmIResponse'] = _WHOAMIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthenticationKey = _reflection.GeneratedProtocolMessageType('AuthenticationKey', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONKEY,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:AuthenticationKey)
  ))
_sym_db.RegisterMessage(AuthenticationKey)

TokenIdentifier = _reflection.GeneratedProtocolMessageType('TokenIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _TOKENIDENTIFIER,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:TokenIdentifier)
  ))
_sym_db.RegisterMessage(TokenIdentifier)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
  DESCRIPTOR = _TOKEN,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:Token)
  ))
_sym_db.RegisterMessage(Token)

GetAuthenticationTokenRequest = _reflection.GeneratedProtocolMessageType('GetAuthenticationTokenRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAUTHENTICATIONTOKENREQUEST,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:GetAuthenticationTokenRequest)
  ))
_sym_db.RegisterMessage(GetAuthenticationTokenRequest)

GetAuthenticationTokenResponse = _reflection.GeneratedProtocolMessageType('GetAuthenticationTokenResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETAUTHENTICATIONTOKENRESPONSE,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:GetAuthenticationTokenResponse)
  ))
_sym_db.RegisterMessage(GetAuthenticationTokenResponse)

WhoAmIRequest = _reflection.GeneratedProtocolMessageType('WhoAmIRequest', (_message.Message,), dict(
  DESCRIPTOR = _WHOAMIREQUEST,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:WhoAmIRequest)
  ))
_sym_db.RegisterMessage(WhoAmIRequest)

WhoAmIResponse = _reflection.GeneratedProtocolMessageType('WhoAmIResponse', (_message.Message,), dict(
  DESCRIPTOR = _WHOAMIRESPONSE,
  __module__ = 'Authentication_pb2'
  # @@protoc_insertion_point(class_scope:WhoAmIResponse)
  ))
_sym_db.RegisterMessage(WhoAmIResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\024AuthenticationProtosH\001\210\001\001\240\001\001'))

_AUTHENTICATIONSERVICE = _descriptor.ServiceDescriptor(
  name='AuthenticationService',
  full_name='AuthenticationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=515,
  serialized_end=672,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAuthenticationToken',
    full_name='AuthenticationService.GetAuthenticationToken',
    index=0,
    containing_service=None,
    input_type=_GETAUTHENTICATIONTOKENREQUEST,
    output_type=_GETAUTHENTICATIONTOKENRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WhoAmI',
    full_name='AuthenticationService.WhoAmI',
    index=1,
    containing_service=None,
    input_type=_WHOAMIREQUEST,
    output_type=_WHOAMIRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHENTICATIONSERVICE)

DESCRIPTOR.services_by_name['AuthenticationService'] = _AUTHENTICATIONSERVICE

# @@protoc_insertion_point(module_scope)

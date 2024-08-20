# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: errors/error_details.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='errors/error_details.proto',
  package='errors',
  syntax='proto3',
  serialized_options=b'Z7github.com/liferod/protobuf/protoc-gen-go/errors;errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x65rrors/error_details.proto\x12\x06\x65rrors\x1a\x1egoogle/protobuf/duration.proto\":\n\tRetryInfo\x12-\n\nretryDelay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"1\n\tDebugInfo\x12\x14\n\x0cstackEntries\x18\x01 \x03(\t\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"u\n\x0cQuotaFailure\x12\x32\n\nviolations\x18\x01 \x03(\x0b\x32\x1e.errors.QuotaFailure.Violation\x1a\x31\n\tViolation\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x91\x01\n\x13PreconditionFailure\x12\x39\n\nviolations\x18\x01 \x03(\x0b\x32%.errors.PreconditionFailure.Violation\x1a?\n\tViolation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"~\n\nBadRequest\x12:\n\x0f\x66ieldViolations\x18\x01 \x03(\x0b\x32!.errors.BadRequest.FieldViolation\x1a\x34\n\x0e\x46ieldViolation\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"5\n\x0bRequestInfo\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x13\n\x0bservingData\x18\x02 \x01(\t\"^\n\x0cResourceInfo\x12\x14\n\x0cresourceType\x18\x01 \x01(\t\x12\x14\n\x0cresourceName\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"R\n\x04Help\x12 \n\x05links\x18\x01 \x03(\x0b\x32\x11.errors.Help.Link\x1a(\n\x04Link\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"3\n\x10LocalizedMessage\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\".\n\x0cHttpLocation\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x10\n\x08location\x18\x02 \x01(\tB9Z7github.com/liferod/protobuf/protoc-gen-go/errors;errorsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_RETRYINFO = _descriptor.Descriptor(
  name='RetryInfo',
  full_name='errors.RetryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='retryDelay', full_name='errors.RetryInfo.retryDelay', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=128,
)


_DEBUGINFO = _descriptor.Descriptor(
  name='DebugInfo',
  full_name='errors.DebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stackEntries', full_name='errors.DebugInfo.stackEntries', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='errors.DebugInfo.detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=130,
  serialized_end=179,
)


_QUOTAFAILURE_VIOLATION = _descriptor.Descriptor(
  name='Violation',
  full_name='errors.QuotaFailure.Violation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subject', full_name='errors.QuotaFailure.Violation.subject', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='errors.QuotaFailure.Violation.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=249,
  serialized_end=298,
)

_QUOTAFAILURE = _descriptor.Descriptor(
  name='QuotaFailure',
  full_name='errors.QuotaFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='violations', full_name='errors.QuotaFailure.violations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUOTAFAILURE_VIOLATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=298,
)


_PRECONDITIONFAILURE_VIOLATION = _descriptor.Descriptor(
  name='Violation',
  full_name='errors.PreconditionFailure.Violation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='errors.PreconditionFailure.Violation.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='errors.PreconditionFailure.Violation.subject', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='errors.PreconditionFailure.Violation.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=383,
  serialized_end=446,
)

_PRECONDITIONFAILURE = _descriptor.Descriptor(
  name='PreconditionFailure',
  full_name='errors.PreconditionFailure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='violations', full_name='errors.PreconditionFailure.violations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PRECONDITIONFAILURE_VIOLATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=446,
)


_BADREQUEST_FIELDVIOLATION = _descriptor.Descriptor(
  name='FieldViolation',
  full_name='errors.BadRequest.FieldViolation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='errors.BadRequest.FieldViolation.field', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='errors.BadRequest.FieldViolation.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=522,
  serialized_end=574,
)

_BADREQUEST = _descriptor.Descriptor(
  name='BadRequest',
  full_name='errors.BadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldViolations', full_name='errors.BadRequest.fieldViolations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BADREQUEST_FIELDVIOLATION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=574,
)


_REQUESTINFO = _descriptor.Descriptor(
  name='RequestInfo',
  full_name='errors.RequestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='errors.RequestInfo.requestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='servingData', full_name='errors.RequestInfo.servingData', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=576,
  serialized_end=629,
)


_RESOURCEINFO = _descriptor.Descriptor(
  name='ResourceInfo',
  full_name='errors.ResourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resourceType', full_name='errors.ResourceInfo.resourceType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resourceName', full_name='errors.ResourceInfo.resourceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='errors.ResourceInfo.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='errors.ResourceInfo.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=631,
  serialized_end=725,
)


_HELP_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='errors.Help.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='errors.Help.Link.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='errors.Help.Link.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=769,
  serialized_end=809,
)

_HELP = _descriptor.Descriptor(
  name='Help',
  full_name='errors.Help',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='links', full_name='errors.Help.links', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELP_LINK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=727,
  serialized_end=809,
)


_LOCALIZEDMESSAGE = _descriptor.Descriptor(
  name='LocalizedMessage',
  full_name='errors.LocalizedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locale', full_name='errors.LocalizedMessage.locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='errors.LocalizedMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=811,
  serialized_end=862,
)


_HTTPLOCATION = _descriptor.Descriptor(
  name='HttpLocation',
  full_name='errors.HttpLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='errors.HttpLocation.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='errors.HttpLocation.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=864,
  serialized_end=910,
)

_RETRYINFO.fields_by_name['retryDelay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_QUOTAFAILURE_VIOLATION.containing_type = _QUOTAFAILURE
_QUOTAFAILURE.fields_by_name['violations'].message_type = _QUOTAFAILURE_VIOLATION
_PRECONDITIONFAILURE_VIOLATION.containing_type = _PRECONDITIONFAILURE
_PRECONDITIONFAILURE.fields_by_name['violations'].message_type = _PRECONDITIONFAILURE_VIOLATION
_BADREQUEST_FIELDVIOLATION.containing_type = _BADREQUEST
_BADREQUEST.fields_by_name['fieldViolations'].message_type = _BADREQUEST_FIELDVIOLATION
_HELP_LINK.containing_type = _HELP
_HELP.fields_by_name['links'].message_type = _HELP_LINK
DESCRIPTOR.message_types_by_name['RetryInfo'] = _RETRYINFO
DESCRIPTOR.message_types_by_name['DebugInfo'] = _DEBUGINFO
DESCRIPTOR.message_types_by_name['QuotaFailure'] = _QUOTAFAILURE
DESCRIPTOR.message_types_by_name['PreconditionFailure'] = _PRECONDITIONFAILURE
DESCRIPTOR.message_types_by_name['BadRequest'] = _BADREQUEST
DESCRIPTOR.message_types_by_name['RequestInfo'] = _REQUESTINFO
DESCRIPTOR.message_types_by_name['ResourceInfo'] = _RESOURCEINFO
DESCRIPTOR.message_types_by_name['Help'] = _HELP
DESCRIPTOR.message_types_by_name['LocalizedMessage'] = _LOCALIZEDMESSAGE
DESCRIPTOR.message_types_by_name['HttpLocation'] = _HTTPLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetryInfo = _reflection.GeneratedProtocolMessageType('RetryInfo', (_message.Message,), {
  'DESCRIPTOR' : _RETRYINFO,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.RetryInfo)
  })
_sym_db.RegisterMessage(RetryInfo)

DebugInfo = _reflection.GeneratedProtocolMessageType('DebugInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGINFO,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.DebugInfo)
  })
_sym_db.RegisterMessage(DebugInfo)

QuotaFailure = _reflection.GeneratedProtocolMessageType('QuotaFailure', (_message.Message,), {

  'Violation' : _reflection.GeneratedProtocolMessageType('Violation', (_message.Message,), {
    'DESCRIPTOR' : _QUOTAFAILURE_VIOLATION,
    '__module__' : 'errors.error_details_pb2'
    # @@protoc_insertion_point(class_scope:errors.QuotaFailure.Violation)
    })
  ,
  'DESCRIPTOR' : _QUOTAFAILURE,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.QuotaFailure)
  })
_sym_db.RegisterMessage(QuotaFailure)
_sym_db.RegisterMessage(QuotaFailure.Violation)

PreconditionFailure = _reflection.GeneratedProtocolMessageType('PreconditionFailure', (_message.Message,), {

  'Violation' : _reflection.GeneratedProtocolMessageType('Violation', (_message.Message,), {
    'DESCRIPTOR' : _PRECONDITIONFAILURE_VIOLATION,
    '__module__' : 'errors.error_details_pb2'
    # @@protoc_insertion_point(class_scope:errors.PreconditionFailure.Violation)
    })
  ,
  'DESCRIPTOR' : _PRECONDITIONFAILURE,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.PreconditionFailure)
  })
_sym_db.RegisterMessage(PreconditionFailure)
_sym_db.RegisterMessage(PreconditionFailure.Violation)

BadRequest = _reflection.GeneratedProtocolMessageType('BadRequest', (_message.Message,), {

  'FieldViolation' : _reflection.GeneratedProtocolMessageType('FieldViolation', (_message.Message,), {
    'DESCRIPTOR' : _BADREQUEST_FIELDVIOLATION,
    '__module__' : 'errors.error_details_pb2'
    # @@protoc_insertion_point(class_scope:errors.BadRequest.FieldViolation)
    })
  ,
  'DESCRIPTOR' : _BADREQUEST,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.BadRequest)
  })
_sym_db.RegisterMessage(BadRequest)
_sym_db.RegisterMessage(BadRequest.FieldViolation)

RequestInfo = _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTINFO,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.RequestInfo)
  })
_sym_db.RegisterMessage(RequestInfo)

ResourceInfo = _reflection.GeneratedProtocolMessageType('ResourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEINFO,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.ResourceInfo)
  })
_sym_db.RegisterMessage(ResourceInfo)

Help = _reflection.GeneratedProtocolMessageType('Help', (_message.Message,), {

  'Link' : _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
    'DESCRIPTOR' : _HELP_LINK,
    '__module__' : 'errors.error_details_pb2'
    # @@protoc_insertion_point(class_scope:errors.Help.Link)
    })
  ,
  'DESCRIPTOR' : _HELP,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.Help)
  })
_sym_db.RegisterMessage(Help)
_sym_db.RegisterMessage(Help.Link)

LocalizedMessage = _reflection.GeneratedProtocolMessageType('LocalizedMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZEDMESSAGE,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.LocalizedMessage)
  })
_sym_db.RegisterMessage(LocalizedMessage)

HttpLocation = _reflection.GeneratedProtocolMessageType('HttpLocation', (_message.Message,), {
  'DESCRIPTOR' : _HTTPLOCATION,
  '__module__' : 'errors.error_details_pb2'
  # @@protoc_insertion_point(class_scope:errors.HttpLocation)
  })
_sym_db.RegisterMessage(HttpLocation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/containers/proto/classifications.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework.formats import classification_pb2 as mediapipe_dot_framework_dot_formats_dot_classification__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDmediapipe/tasks/cc/components/containers/proto/classifications.proto\x12+mediapipe.tasks.components.containers.proto\x1a\x30mediapipe/framework/formats/classification.proto\"z\n\x0f\x43lassifications\x12:\n\x13\x63lassification_list\x18\x04 \x01(\x0b\x32\x1d.mediapipe.ClassificationList\x12\x12\n\nhead_index\x18\x02 \x01(\x05\x12\x11\n\thead_name\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02\"\x83\x01\n\x14\x43lassificationResult\x12U\n\x0f\x63lassifications\x18\x01 \x03(\x0b\x32<.mediapipe.tasks.components.containers.proto.Classifications\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\x42N\n6com.google.mediapipe.tasks.components.containers.protoB\x14\x43lassificationsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.components.containers.proto.classifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n6com.google.mediapipe.tasks.components.containers.protoB\024ClassificationsProto'
  _globals['_CLASSIFICATIONS']._serialized_start=167
  _globals['_CLASSIFICATIONS']._serialized_end=289
  _globals['_CLASSIFICATIONRESULT']._serialized_start=292
  _globals['_CLASSIFICATIONRESULT']._serialized_end=423
# @@protoc_insertion_point(module_scope)

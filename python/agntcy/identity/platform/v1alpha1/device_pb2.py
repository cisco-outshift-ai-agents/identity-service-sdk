# Copyright 2025 Cisco Systems, Inc. and its affiliates
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agntcy/identity/platform/v1alpha1/device.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.agntcy/identity/platform/v1alpha1/device.proto\x12!agntcy.identity.platform.v1alpha1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf7\x02\n\x13\x41pprovalRequestInfo\x12\"\n\ncaller_app\x18\x01 \x01(\tH\x00R\tcallerApp\x88\x01\x01\x12\"\n\ncallee_app\x18\x02 \x01(\tH\x01R\tcalleeApp\x88\x01\x01\x12 \n\ttool_name\x18\x03 \x01(\tH\x02R\x08toolName\x88\x01\x01\x12\x15\n\x03otp\x18\x04 \x01(\tH\x03R\x03otp\x88\x01\x01\x12 \n\tdevice_id\x18\x05 \x01(\tH\x04R\x08\x64\x65viceId\x88\x01\x01\x12\"\n\nsession_id\x18\x06 \x01(\tH\x05R\tsessionId\x88\x01\x01\x12\x31\n\x12timeout_in_seconds\x18\x07 \x01(\x03H\x06R\x10timeoutInSeconds\x88\x01\x01\x42\r\n\x0b_caller_appB\r\n\x0b_callee_appB\x0c\n\n_tool_nameB\x06\n\x04_otpB\x0c\n\n_device_idB\r\n\x0b_session_idB\x15\n\x13_timeout_in_seconds\"\x8a\x02\n\x06\x44\x65vice\x12\x13\n\x02id\x18\x01 \x01(\tH\x00R\x02id\x88\x01\x01\x12\x1c\n\x07user_id\x18\x02 \x01(\tH\x01R\x06userId\x88\x01\x01\x12\x32\n\x12subscription_token\x18\x03 \x01(\tH\x02R\x11subscriptionToken\x88\x01\x01\x12\x17\n\x04name\x18\x04 \x01(\tH\x03R\x04name\x88\x01\x01\x12>\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x04R\tcreatedAt\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_user_idB\x15\n\x13_subscription_tokenB\x07\n\x05_nameB\r\n\x0b_created_at\"\x92\x02\n\x0cNotification\x12\x17\n\x04\x62ody\x18\x01 \x01(\tH\x00R\x04\x62ody\x88\x01\x01\x12L\n\x04type\x18\x02 \x01(\x0e\x32\x33.agntcy.identity.platform.v1alpha1.NotificationTypeH\x01R\x04type\x88\x01\x01\x12o\n\x15\x61pproval_request_info\x18\x03 \x01(\x0b\x32\x36.agntcy.identity.platform.v1alpha1.ApprovalRequestInfoH\x02R\x13\x61pprovalRequestInfo\x88\x01\x01\x42\x07\n\x05_bodyB\x07\n\x05_typeB\x18\n\x16_approval_request_info*y\n\x10NotificationType\x12!\n\x1dNOTIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16NOTIFICATION_TYPE_INFO\x10\x01\x12&\n\"NOTIFICATION_TYPE_APPROVAL_REQUEST\x10\x02\x42\xc6\x02\n%com.agntcy.identity.platform.v1alpha1B\x0b\x44\x65viceProtoP\x01Zigithub.com/agntcy/identity-platform/api/server/agntcy/identity/platform/v1alpha1;identity_platform_sdk_go\xa2\x02\x03\x41IP\xaa\x02!Agntcy.Identity.Platform.V1alpha1\xca\x02!Agntcy\\Identity\\Platform\\V1alpha1\xe2\x02-Agntcy\\Identity\\Platform\\V1alpha1\\GPBMetadata\xea\x02$Agntcy::Identity::Platform::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agntcy.identity.platform.v1alpha1.device_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.agntcy.identity.platform.v1alpha1B\013DeviceProtoP\001Zigithub.com/agntcy/identity-platform/api/server/agntcy/identity/platform/v1alpha1;identity_platform_sdk_go\242\002\003AIP\252\002!Agntcy.Identity.Platform.V1alpha1\312\002!Agntcy\\Identity\\Platform\\V1alpha1\342\002-Agntcy\\Identity\\Platform\\V1alpha1\\GPBMetadata\352\002$Agntcy::Identity::Platform::V1alpha1'
  _globals['_NOTIFICATIONTYPE']._serialized_start=1042
  _globals['_NOTIFICATIONTYPE']._serialized_end=1163
  _globals['_APPROVALREQUESTINFO']._serialized_start=119
  _globals['_APPROVALREQUESTINFO']._serialized_end=494
  _globals['_DEVICE']._serialized_start=497
  _globals['_DEVICE']._serialized_end=763
  _globals['_NOTIFICATION']._serialized_start=766
  _globals['_NOTIFICATION']._serialized_end=1040
# @@protoc_insertion_point(module_scope)

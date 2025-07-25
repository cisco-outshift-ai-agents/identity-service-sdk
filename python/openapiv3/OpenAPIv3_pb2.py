# Copyright 2025 Cisco Systems, Inc. and its affiliates
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openapiv3/OpenAPIv3.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19openapiv3/OpenAPIv3.proto\x12\nopenapi.v3\x1a\x19google/protobuf/any.proto\"\x90\x01\n\x18\x41\x64\x64itionalPropertiesItem\x12O\n\x13schema_or_reference\x18\x01 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceH\x00R\x11schemaOrReference\x12\x1a\n\x07\x62oolean\x18\x02 \x01(\x08H\x00R\x07\x62ooleanB\x07\n\x05oneof\"E\n\x03\x41ny\x12*\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value\x12\x12\n\x04yaml\x18\x02 \x01(\tR\x04yaml\"y\n\x0f\x41nyOrExpression\x12#\n\x03\x61ny\x18\x01 \x01(\x0b\x32\x0f.openapi.v3.AnyH\x00R\x03\x61ny\x12\x38\n\nexpression\x18\x02 \x01(\x0b\x32\x16.openapi.v3.ExpressionH\x00R\nexpressionB\x07\n\x05oneof\"\x88\x01\n\x08\x43\x61llback\x12-\n\x04path\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedPathItemR\x04path\x12M\n\x17specification_extension\x18\x02 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x89\x01\n\x13\x43\x61llbackOrReference\x12\x32\n\x08\x63\x61llback\x18\x01 \x01(\x0b\x32\x14.openapi.v3.CallbackH\x00R\x08\x63\x61llback\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"r\n\x15\x43\x61llbacksOrReferences\x12Y\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32$.openapi.v3.NamedCallbackOrReferenceR\x14\x61\x64\x64itionalProperties\"\xac\x05\n\nComponents\x12\x39\n\x07schemas\x18\x01 \x01(\x0b\x32\x1f.openapi.v3.SchemasOrReferencesR\x07schemas\x12?\n\tresponses\x18\x02 \x01(\x0b\x32!.openapi.v3.ResponsesOrReferencesR\tresponses\x12\x42\n\nparameters\x18\x03 \x01(\x0b\x32\".openapi.v3.ParametersOrReferencesR\nparameters\x12<\n\x08\x65xamples\x18\x04 \x01(\x0b\x32 .openapi.v3.ExamplesOrReferencesR\x08\x65xamples\x12L\n\x0erequest_bodies\x18\x05 \x01(\x0b\x32%.openapi.v3.RequestBodiesOrReferencesR\rrequestBodies\x12\x39\n\x07headers\x18\x06 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferencesR\x07headers\x12R\n\x10security_schemes\x18\x07 \x01(\x0b\x32\'.openapi.v3.SecuritySchemesOrReferencesR\x0fsecuritySchemes\x12\x33\n\x05links\x18\x08 \x01(\x0b\x32\x1d.openapi.v3.LinksOrReferencesR\x05links\x12?\n\tcallbacks\x18\t \x01(\x0b\x32!.openapi.v3.CallbacksOrReferencesR\tcallbacks\x12M\n\x17specification_extension\x18\n \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x94\x01\n\x07\x43ontact\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\x12M\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"f\n\x0b\x44\x65\x66\x61ultType\x12\x18\n\x06number\x18\x01 \x01(\x01H\x00R\x06number\x12\x1a\n\x07\x62oolean\x18\x02 \x01(\x08H\x00R\x07\x62oolean\x12\x18\n\x06string\x18\x03 \x01(\tH\x00R\x06stringB\x07\n\x05oneof\"\xb2\x01\n\rDiscriminator\x12#\n\rproperty_name\x18\x01 \x01(\tR\x0cpropertyName\x12-\n\x07mapping\x18\x02 \x01(\x0b\x32\x13.openapi.v3.StringsR\x07mapping\x12M\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xc9\x03\n\x08\x44ocument\x12\x18\n\x07openapi\x18\x01 \x01(\tR\x07openapi\x12$\n\x04info\x18\x02 \x01(\x0b\x32\x10.openapi.v3.InfoR\x04info\x12,\n\x07servers\x18\x03 \x03(\x0b\x32\x12.openapi.v3.ServerR\x07servers\x12\'\n\x05paths\x18\x04 \x01(\x0b\x32\x11.openapi.v3.PathsR\x05paths\x12\x36\n\ncomponents\x18\x05 \x01(\x0b\x32\x16.openapi.v3.ComponentsR\ncomponents\x12;\n\x08security\x18\x06 \x03(\x0b\x32\x1f.openapi.v3.SecurityRequirementR\x08security\x12#\n\x04tags\x18\x07 \x03(\x0b\x32\x0f.openapi.v3.TagR\x04tags\x12=\n\rexternal_docs\x18\x08 \x01(\x0b\x32\x18.openapi.v3.ExternalDocsR\x0c\x65xternalDocs\x12M\n\x17specification_extension\x18\t \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x8e\x02\n\x08\x45ncoding\x12!\n\x0c\x63ontent_type\x18\x01 \x01(\tR\x0b\x63ontentType\x12\x39\n\x07headers\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferencesR\x07headers\x12\x14\n\x05style\x18\x03 \x01(\tR\x05style\x12\x18\n\x07\x65xplode\x18\x04 \x01(\x08R\x07\x65xplode\x12%\n\x0e\x61llow_reserved\x18\x05 \x01(\x08R\rallowReserved\x12M\n\x17specification_extension\x18\x06 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"[\n\tEncodings\x12N\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedEncodingR\x14\x61\x64\x64itionalProperties\"\xe2\x01\n\x07\x45xample\x12\x18\n\x07summary\x18\x01 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12%\n\x05value\x18\x03 \x01(\x0b\x32\x0f.openapi.v3.AnyR\x05value\x12%\n\x0e\x65xternal_value\x18\x04 \x01(\tR\rexternalValue\x12M\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x85\x01\n\x12\x45xampleOrReference\x12/\n\x07\x65xample\x18\x01 \x01(\x0b\x32\x13.openapi.v3.ExampleH\x00R\x07\x65xample\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"p\n\x14\x45xamplesOrReferences\x12X\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32#.openapi.v3.NamedExampleOrReferenceR\x14\x61\x64\x64itionalProperties\"W\n\nExpression\x12I\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x14\x61\x64\x64itionalProperties\"\x91\x01\n\x0c\x45xternalDocs\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12M\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x8a\x04\n\x06Header\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08required\x18\x02 \x01(\x08R\x08required\x12\x1e\n\ndeprecated\x18\x03 \x01(\x08R\ndeprecated\x12*\n\x11\x61llow_empty_value\x18\x04 \x01(\x08R\x0f\x61llowEmptyValue\x12\x14\n\x05style\x18\x05 \x01(\tR\x05style\x12\x18\n\x07\x65xplode\x18\x06 \x01(\x08R\x07\x65xplode\x12%\n\x0e\x61llow_reserved\x18\x07 \x01(\x08R\rallowReserved\x12\x35\n\x06schema\x18\x08 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x06schema\x12)\n\x07\x65xample\x18\t \x01(\x0b\x32\x0f.openapi.v3.AnyR\x07\x65xample\x12<\n\x08\x65xamples\x18\n \x01(\x0b\x32 .openapi.v3.ExamplesOrReferencesR\x08\x65xamples\x12\x30\n\x07\x63ontent\x18\x0b \x01(\x0b\x32\x16.openapi.v3.MediaTypesR\x07\x63ontent\x12M\n\x17specification_extension\x18\x0c \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x81\x01\n\x11HeaderOrReference\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x12.openapi.v3.HeaderH\x00R\x06header\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"n\n\x13HeadersOrReferences\x12W\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedHeaderOrReferenceR\x14\x61\x64\x64itionalProperties\"\xc9\x02\n\x04Info\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12(\n\x10terms_of_service\x18\x03 \x01(\tR\x0etermsOfService\x12-\n\x07\x63ontact\x18\x04 \x01(\x0b\x32\x13.openapi.v3.ContactR\x07\x63ontact\x12-\n\x07license\x18\x05 \x01(\x0b\x32\x13.openapi.v3.LicenseR\x07license\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12M\n\x17specification_extension\x18\x07 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\x12\x18\n\x07summary\x18\x08 \x01(\tR\x07summary\"Z\n\tItemsItem\x12M\n\x13schema_or_reference\x18\x01 \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x11schemaOrReference\"~\n\x07License\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\x12M\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xe8\x02\n\x04Link\x12#\n\roperation_ref\x18\x01 \x01(\tR\x0coperationRef\x12!\n\x0coperation_id\x18\x02 \x01(\tR\x0boperationId\x12;\n\nparameters\x18\x03 \x01(\x0b\x32\x1b.openapi.v3.AnyOrExpressionR\nparameters\x12>\n\x0crequest_body\x18\x04 \x01(\x0b\x32\x1b.openapi.v3.AnyOrExpressionR\x0brequestBody\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12*\n\x06server\x18\x06 \x01(\x0b\x32\x12.openapi.v3.ServerR\x06server\x12M\n\x17specification_extension\x18\x07 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"y\n\x0fLinkOrReference\x12&\n\x04link\x18\x01 \x01(\x0b\x32\x10.openapi.v3.LinkH\x00R\x04link\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"j\n\x11LinksOrReferences\x12U\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32 .openapi.v3.NamedLinkOrReferenceR\x14\x61\x64\x64itionalProperties\"\xad\x02\n\tMediaType\x12\x35\n\x06schema\x18\x01 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x06schema\x12)\n\x07\x65xample\x18\x02 \x01(\x0b\x32\x0f.openapi.v3.AnyR\x07\x65xample\x12<\n\x08\x65xamples\x18\x03 \x01(\x0b\x32 .openapi.v3.ExamplesOrReferencesR\x08\x65xamples\x12\x31\n\x08\x65ncoding\x18\x04 \x01(\x0b\x32\x15.openapi.v3.EncodingsR\x08\x65ncoding\x12M\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"]\n\nMediaTypes\x12O\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1a.openapi.v3.NamedMediaTypeR\x14\x61\x64\x64itionalProperties\"E\n\x08NamedAny\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x0f.openapi.v3.AnyR\x05value\"e\n\x18NamedCallbackOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.CallbackOrReferenceR\x05value\"O\n\rNamedEncoding\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.openapi.v3.EncodingR\x05value\"c\n\x17NamedExampleOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32\x1e.openapi.v3.ExampleOrReferenceR\x05value\"a\n\x16NamedHeaderOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.openapi.v3.HeaderOrReferenceR\x05value\"]\n\x14NamedLinkOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.openapi.v3.LinkOrReferenceR\x05value\"Q\n\x0eNamedMediaType\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x15.openapi.v3.MediaTypeR\x05value\"g\n\x19NamedParameterOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32 .openapi.v3.ParameterOrReferenceR\x05value\"O\n\rNamedPathItem\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.openapi.v3.PathItemR\x05value\"k\n\x1bNamedRequestBodyOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32\".openapi.v3.RequestBodyOrReferenceR\x05value\"e\n\x18NamedResponseOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.ResponseOrReferenceR\x05value\"a\n\x16NamedSchemaOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x05value\"q\n\x1eNamedSecuritySchemeOrReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\x05value\x18\x02 \x01(\x0b\x32%.openapi.v3.SecuritySchemeOrReferenceR\x05value\"[\n\x13NamedServerVariable\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32\x1a.openapi.v3.ServerVariableR\x05value\"7\n\x0bNamedString\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"U\n\x10NamedStringArray\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x17.openapi.v3.StringArrayR\x05value\"\xf2\x01\n\tOauthFlow\x12+\n\x11\x61uthorization_url\x18\x01 \x01(\tR\x10\x61uthorizationUrl\x12\x1b\n\ttoken_url\x18\x02 \x01(\tR\x08tokenUrl\x12\x1f\n\x0brefresh_url\x18\x03 \x01(\tR\nrefreshUrl\x12+\n\x06scopes\x18\x04 \x01(\x0b\x32\x13.openapi.v3.StringsR\x06scopes\x12M\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xcd\x02\n\nOauthFlows\x12\x31\n\x08implicit\x18\x01 \x01(\x0b\x32\x15.openapi.v3.OauthFlowR\x08implicit\x12\x31\n\x08password\x18\x02 \x01(\x0b\x32\x15.openapi.v3.OauthFlowR\x08password\x12\x44\n\x12\x63lient_credentials\x18\x03 \x01(\x0b\x32\x15.openapi.v3.OauthFlowR\x11\x63lientCredentials\x12\x44\n\x12\x61uthorization_code\x18\x04 \x01(\x0b\x32\x15.openapi.v3.OauthFlowR\x11\x61uthorizationCode\x12M\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"S\n\x06Object\x12I\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x14\x61\x64\x64itionalProperties\"\x96\x05\n\tOperation\x12\x12\n\x04tags\x18\x01 \x03(\tR\x04tags\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\rexternal_docs\x18\x04 \x01(\x0b\x32\x18.openapi.v3.ExternalDocsR\x0c\x65xternalDocs\x12!\n\x0coperation_id\x18\x05 \x01(\tR\x0boperationId\x12@\n\nparameters\x18\x06 \x03(\x0b\x32 .openapi.v3.ParameterOrReferenceR\nparameters\x12\x45\n\x0crequest_body\x18\x07 \x01(\x0b\x32\".openapi.v3.RequestBodyOrReferenceR\x0brequestBody\x12\x33\n\tresponses\x18\x08 \x01(\x0b\x32\x15.openapi.v3.ResponsesR\tresponses\x12?\n\tcallbacks\x18\t \x01(\x0b\x32!.openapi.v3.CallbacksOrReferencesR\tcallbacks\x12\x1e\n\ndeprecated\x18\n \x01(\x08R\ndeprecated\x12;\n\x08security\x18\x0b \x03(\x0b\x32\x1f.openapi.v3.SecurityRequirementR\x08security\x12,\n\x07servers\x18\x0c \x03(\x0b\x32\x12.openapi.v3.ServerR\x07servers\x12M\n\x17specification_extension\x18\r \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xb1\x04\n\tParameter\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02in\x18\x02 \x01(\tR\x02in\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08required\x18\x04 \x01(\x08R\x08required\x12\x1e\n\ndeprecated\x18\x05 \x01(\x08R\ndeprecated\x12*\n\x11\x61llow_empty_value\x18\x06 \x01(\x08R\x0f\x61llowEmptyValue\x12\x14\n\x05style\x18\x07 \x01(\tR\x05style\x12\x18\n\x07\x65xplode\x18\x08 \x01(\x08R\x07\x65xplode\x12%\n\x0e\x61llow_reserved\x18\t \x01(\x08R\rallowReserved\x12\x35\n\x06schema\x18\n \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x06schema\x12)\n\x07\x65xample\x18\x0b \x01(\x0b\x32\x0f.openapi.v3.AnyR\x07\x65xample\x12<\n\x08\x65xamples\x18\x0c \x01(\x0b\x32 .openapi.v3.ExamplesOrReferencesR\x08\x65xamples\x12\x30\n\x07\x63ontent\x18\r \x01(\x0b\x32\x16.openapi.v3.MediaTypesR\x07\x63ontent\x12M\n\x17specification_extension\x18\x0e \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x8d\x01\n\x14ParameterOrReference\x12\x35\n\tparameter\x18\x01 \x01(\x0b\x32\x15.openapi.v3.ParameterH\x00R\tparameter\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"t\n\x16ParametersOrReferences\x12Z\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32%.openapi.v3.NamedParameterOrReferenceR\x14\x61\x64\x64itionalProperties\"\xfa\x04\n\x08PathItem\x12\x11\n\x04_ref\x18\x01 \x01(\tR\x03Ref\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\'\n\x03get\x18\x04 \x01(\x0b\x32\x15.openapi.v3.OperationR\x03get\x12\'\n\x03put\x18\x05 \x01(\x0b\x32\x15.openapi.v3.OperationR\x03put\x12)\n\x04post\x18\x06 \x01(\x0b\x32\x15.openapi.v3.OperationR\x04post\x12-\n\x06\x64\x65lete\x18\x07 \x01(\x0b\x32\x15.openapi.v3.OperationR\x06\x64\x65lete\x12/\n\x07options\x18\x08 \x01(\x0b\x32\x15.openapi.v3.OperationR\x07options\x12)\n\x04head\x18\t \x01(\x0b\x32\x15.openapi.v3.OperationR\x04head\x12+\n\x05patch\x18\n \x01(\x0b\x32\x15.openapi.v3.OperationR\x05patch\x12+\n\x05trace\x18\x0b \x01(\x0b\x32\x15.openapi.v3.OperationR\x05trace\x12,\n\x07servers\x18\x0c \x03(\x0b\x32\x12.openapi.v3.ServerR\x07servers\x12@\n\nparameters\x18\r \x03(\x0b\x32 .openapi.v3.ParameterOrReferenceR\nparameters\x12M\n\x17specification_extension\x18\x0e \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x85\x01\n\x05Paths\x12-\n\x04path\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedPathItemR\x04path\x12M\n\x17specification_extension\x18\x02 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"e\n\nProperties\x12W\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedSchemaOrReferenceR\x14\x61\x64\x64itionalProperties\"Z\n\tReference\x12\x11\n\x04_ref\x18\x01 \x01(\tR\x03Ref\x12\x18\n\x07summary\x18\x02 \x01(\tR\x07summary\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"y\n\x19RequestBodiesOrReferences\x12\\\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\'.openapi.v3.NamedRequestBodyOrReferenceR\x14\x61\x64\x64itionalProperties\"\xcc\x01\n\x0bRequestBody\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x30\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x16.openapi.v3.MediaTypesR\x07\x63ontent\x12\x1a\n\x08required\x18\x03 \x01(\x08R\x08required\x12M\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x96\x01\n\x16RequestBodyOrReference\x12<\n\x0crequest_body\x18\x01 \x01(\x0b\x32\x17.openapi.v3.RequestBodyH\x00R\x0brequestBody\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"\x9d\x02\n\x08Response\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x39\n\x07headers\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferencesR\x07headers\x12\x30\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x16.openapi.v3.MediaTypesR\x07\x63ontent\x12\x33\n\x05links\x18\x04 \x01(\x0b\x32\x1d.openapi.v3.LinksOrReferencesR\x05links\x12M\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x89\x01\n\x13ResponseOrReference\x12\x32\n\x08response\x18\x01 \x01(\x0b\x32\x14.openapi.v3.ResponseH\x00R\x08response\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"\xef\x01\n\tResponses\x12\x39\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x0b\x32\x1f.openapi.v3.ResponseOrReferenceR\x07\x64\x65\x66\x61ult\x12X\n\x15response_or_reference\x18\x02 \x03(\x0b\x32$.openapi.v3.NamedResponseOrReferenceR\x13responseOrReference\x12M\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"r\n\x15ResponsesOrReferences\x12Y\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32$.openapi.v3.NamedResponseOrReferenceR\x14\x61\x64\x64itionalProperties\"\xaf\x0b\n\x06Schema\x12\x1a\n\x08nullable\x18\x01 \x01(\x08R\x08nullable\x12?\n\rdiscriminator\x18\x02 \x01(\x0b\x32\x19.openapi.v3.DiscriminatorR\rdiscriminator\x12\x1b\n\tread_only\x18\x03 \x01(\x08R\x08readOnly\x12\x1d\n\nwrite_only\x18\x04 \x01(\x08R\twriteOnly\x12!\n\x03xml\x18\x05 \x01(\x0b\x32\x0f.openapi.v3.XmlR\x03xml\x12=\n\rexternal_docs\x18\x06 \x01(\x0b\x32\x18.openapi.v3.ExternalDocsR\x0c\x65xternalDocs\x12)\n\x07\x65xample\x18\x07 \x01(\x0b\x32\x0f.openapi.v3.AnyR\x07\x65xample\x12\x1e\n\ndeprecated\x18\x08 \x01(\x08R\ndeprecated\x12\x14\n\x05title\x18\t \x01(\tR\x05title\x12\x1f\n\x0bmultiple_of\x18\n \x01(\x01R\nmultipleOf\x12\x18\n\x07maximum\x18\x0b \x01(\x01R\x07maximum\x12+\n\x11\x65xclusive_maximum\x18\x0c \x01(\x08R\x10\x65xclusiveMaximum\x12\x18\n\x07minimum\x18\r \x01(\x01R\x07minimum\x12+\n\x11\x65xclusive_minimum\x18\x0e \x01(\x08R\x10\x65xclusiveMinimum\x12\x1d\n\nmax_length\x18\x0f \x01(\x03R\tmaxLength\x12\x1d\n\nmin_length\x18\x10 \x01(\x03R\tminLength\x12\x18\n\x07pattern\x18\x11 \x01(\tR\x07pattern\x12\x1b\n\tmax_items\x18\x12 \x01(\x03R\x08maxItems\x12\x1b\n\tmin_items\x18\x13 \x01(\x03R\x08minItems\x12!\n\x0cunique_items\x18\x14 \x01(\x08R\x0buniqueItems\x12%\n\x0emax_properties\x18\x15 \x01(\x03R\rmaxProperties\x12%\n\x0emin_properties\x18\x16 \x01(\x03R\rminProperties\x12\x1a\n\x08required\x18\x17 \x03(\tR\x08required\x12#\n\x04\x65num\x18\x18 \x03(\x0b\x32\x0f.openapi.v3.AnyR\x04\x65num\x12\x12\n\x04type\x18\x19 \x01(\tR\x04type\x12\x34\n\x06\x61ll_of\x18\x1a \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x05\x61llOf\x12\x34\n\x06one_of\x18\x1b \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x05oneOf\x12\x34\n\x06\x61ny_of\x18\x1c \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceR\x05\x61nyOf\x12$\n\x03not\x18\x1d \x01(\x0b\x32\x12.openapi.v3.SchemaR\x03not\x12+\n\x05items\x18\x1e \x01(\x0b\x32\x15.openapi.v3.ItemsItemR\x05items\x12\x36\n\nproperties\x18\x1f \x01(\x0b\x32\x16.openapi.v3.PropertiesR\nproperties\x12Y\n\x15\x61\x64\x64itional_properties\x18  \x01(\x0b\x32$.openapi.v3.AdditionalPropertiesItemR\x14\x61\x64\x64itionalProperties\x12\x31\n\x07\x64\x65\x66\x61ult\x18! \x01(\x0b\x32\x17.openapi.v3.DefaultTypeR\x07\x64\x65\x66\x61ult\x12 \n\x0b\x64\x65scription\x18\" \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06\x66ormat\x18# \x01(\tR\x06\x66ormat\x12M\n\x17specification_extension\x18$ \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\x81\x01\n\x11SchemaOrReference\x12,\n\x06schema\x18\x01 \x01(\x0b\x32\x12.openapi.v3.SchemaH\x00R\x06schema\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"n\n\x13SchemasOrReferences\x12W\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedSchemaOrReferenceR\x14\x61\x64\x64itionalProperties\"h\n\x13SecurityRequirement\x12Q\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1c.openapi.v3.NamedStringArrayR\x14\x61\x64\x64itionalProperties\"\xd3\x02\n\x0eSecurityScheme\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x0e\n\x02in\x18\x04 \x01(\tR\x02in\x12\x16\n\x06scheme\x18\x05 \x01(\tR\x06scheme\x12#\n\rbearer_format\x18\x06 \x01(\tR\x0c\x62\x65\x61rerFormat\x12,\n\x05\x66lows\x18\x07 \x01(\x0b\x32\x16.openapi.v3.OauthFlowsR\x05\x66lows\x12-\n\x13open_id_connect_url\x18\x08 \x01(\tR\x10openIdConnectUrl\x12M\n\x17specification_extension\x18\t \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xa2\x01\n\x19SecuritySchemeOrReference\x12\x45\n\x0fsecurity_scheme\x18\x01 \x01(\x0b\x32\x1a.openapi.v3.SecuritySchemeH\x00R\x0esecurityScheme\x12\x35\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00R\treferenceB\x07\n\x05oneof\"~\n\x1bSecuritySchemesOrReferences\x12_\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32*.openapi.v3.NamedSecuritySchemeOrReferenceR\x14\x61\x64\x64itionalProperties\"\xc6\x01\n\x06Server\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x39\n\tvariables\x18\x03 \x01(\x0b\x32\x1b.openapi.v3.ServerVariablesR\tvariables\x12M\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xaf\x01\n\x0eServerVariable\x12\x12\n\x04\x65num\x18\x01 \x03(\tR\x04\x65num\x12\x18\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\tR\x07\x64\x65\x66\x61ult\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12M\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"g\n\x0fServerVariables\x12T\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1f.openapi.v3.NamedServerVariableR\x14\x61\x64\x64itionalProperties\"q\n\x16SpecificationExtension\x12\x18\n\x06number\x18\x01 \x01(\x01H\x00R\x06number\x12\x1a\n\x07\x62oolean\x18\x02 \x01(\x08H\x00R\x07\x62oolean\x12\x18\n\x06string\x18\x03 \x01(\tH\x00R\x06stringB\x07\n\x05oneof\"#\n\x0bStringArray\x12\x14\n\x05value\x18\x01 \x03(\tR\x05value\"W\n\x07Strings\x12L\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x17.openapi.v3.NamedStringR\x14\x61\x64\x64itionalProperties\"\xc9\x01\n\x03Tag\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12=\n\rexternal_docs\x18\x03 \x01(\x0b\x32\x18.openapi.v3.ExternalDocsR\x0c\x65xternalDocs\x12M\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtension\"\xd6\x01\n\x03Xml\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1c\n\tnamespace\x18\x02 \x01(\tR\tnamespace\x12\x16\n\x06prefix\x18\x03 \x01(\tR\x06prefix\x12\x1c\n\tattribute\x18\x04 \x01(\x08R\tattribute\x12\x18\n\x07wrapped\x18\x05 \x01(\x08R\x07wrapped\x12M\n\x17specification_extension\x18\x06 \x03(\x0b\x32\x14.openapi.v3.NamedAnyR\x16specificationExtensionB\x99\x01\n\x0e\x63om.openapi.v3B\x0eOpenAPIv3ProtoP\x01Z.github.com/google/gnostic/openapiv3;openapi_v3\xa2\x02\x03OXX\xaa\x02\nOpenapi.V3\xca\x02\nOpenapi\\V3\xe2\x02\x16Openapi\\V3\\GPBMetadata\xea\x02\x0bOpenapi::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'openapiv3.OpenAPIv3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016com.openapi.v3B\016OpenAPIv3ProtoP\001Z.github.com/google/gnostic/openapiv3;openapi_v3\242\002\003OXX\252\002\nOpenapi.V3\312\002\nOpenapi\\V3\342\002\026Openapi\\V3\\GPBMetadata\352\002\013Openapi::V3'
  _globals['_ADDITIONALPROPERTIESITEM']._serialized_start=69
  _globals['_ADDITIONALPROPERTIESITEM']._serialized_end=213
  _globals['_ANY']._serialized_start=215
  _globals['_ANY']._serialized_end=284
  _globals['_ANYOREXPRESSION']._serialized_start=286
  _globals['_ANYOREXPRESSION']._serialized_end=407
  _globals['_CALLBACK']._serialized_start=410
  _globals['_CALLBACK']._serialized_end=546
  _globals['_CALLBACKORREFERENCE']._serialized_start=549
  _globals['_CALLBACKORREFERENCE']._serialized_end=686
  _globals['_CALLBACKSORREFERENCES']._serialized_start=688
  _globals['_CALLBACKSORREFERENCES']._serialized_end=802
  _globals['_COMPONENTS']._serialized_start=805
  _globals['_COMPONENTS']._serialized_end=1489
  _globals['_CONTACT']._serialized_start=1492
  _globals['_CONTACT']._serialized_end=1640
  _globals['_DEFAULTTYPE']._serialized_start=1642
  _globals['_DEFAULTTYPE']._serialized_end=1744
  _globals['_DISCRIMINATOR']._serialized_start=1747
  _globals['_DISCRIMINATOR']._serialized_end=1925
  _globals['_DOCUMENT']._serialized_start=1928
  _globals['_DOCUMENT']._serialized_end=2385
  _globals['_ENCODING']._serialized_start=2388
  _globals['_ENCODING']._serialized_end=2658
  _globals['_ENCODINGS']._serialized_start=2660
  _globals['_ENCODINGS']._serialized_end=2751
  _globals['_EXAMPLE']._serialized_start=2754
  _globals['_EXAMPLE']._serialized_end=2980
  _globals['_EXAMPLEORREFERENCE']._serialized_start=2983
  _globals['_EXAMPLEORREFERENCE']._serialized_end=3116
  _globals['_EXAMPLESORREFERENCES']._serialized_start=3118
  _globals['_EXAMPLESORREFERENCES']._serialized_end=3230
  _globals['_EXPRESSION']._serialized_start=3232
  _globals['_EXPRESSION']._serialized_end=3319
  _globals['_EXTERNALDOCS']._serialized_start=3322
  _globals['_EXTERNALDOCS']._serialized_end=3467
  _globals['_HEADER']._serialized_start=3470
  _globals['_HEADER']._serialized_end=3992
  _globals['_HEADERORREFERENCE']._serialized_start=3995
  _globals['_HEADERORREFERENCE']._serialized_end=4124
  _globals['_HEADERSORREFERENCES']._serialized_start=4126
  _globals['_HEADERSORREFERENCES']._serialized_end=4236
  _globals['_INFO']._serialized_start=4239
  _globals['_INFO']._serialized_end=4568
  _globals['_ITEMSITEM']._serialized_start=4570
  _globals['_ITEMSITEM']._serialized_end=4660
  _globals['_LICENSE']._serialized_start=4662
  _globals['_LICENSE']._serialized_end=4788
  _globals['_LINK']._serialized_start=4791
  _globals['_LINK']._serialized_end=5151
  _globals['_LINKORREFERENCE']._serialized_start=5153
  _globals['_LINKORREFERENCE']._serialized_end=5274
  _globals['_LINKSORREFERENCES']._serialized_start=5276
  _globals['_LINKSORREFERENCES']._serialized_end=5382
  _globals['_MEDIATYPE']._serialized_start=5385
  _globals['_MEDIATYPE']._serialized_end=5686
  _globals['_MEDIATYPES']._serialized_start=5688
  _globals['_MEDIATYPES']._serialized_end=5781
  _globals['_NAMEDANY']._serialized_start=5783
  _globals['_NAMEDANY']._serialized_end=5852
  _globals['_NAMEDCALLBACKORREFERENCE']._serialized_start=5854
  _globals['_NAMEDCALLBACKORREFERENCE']._serialized_end=5955
  _globals['_NAMEDENCODING']._serialized_start=5957
  _globals['_NAMEDENCODING']._serialized_end=6036
  _globals['_NAMEDEXAMPLEORREFERENCE']._serialized_start=6038
  _globals['_NAMEDEXAMPLEORREFERENCE']._serialized_end=6137
  _globals['_NAMEDHEADERORREFERENCE']._serialized_start=6139
  _globals['_NAMEDHEADERORREFERENCE']._serialized_end=6236
  _globals['_NAMEDLINKORREFERENCE']._serialized_start=6238
  _globals['_NAMEDLINKORREFERENCE']._serialized_end=6331
  _globals['_NAMEDMEDIATYPE']._serialized_start=6333
  _globals['_NAMEDMEDIATYPE']._serialized_end=6414
  _globals['_NAMEDPARAMETERORREFERENCE']._serialized_start=6416
  _globals['_NAMEDPARAMETERORREFERENCE']._serialized_end=6519
  _globals['_NAMEDPATHITEM']._serialized_start=6521
  _globals['_NAMEDPATHITEM']._serialized_end=6600
  _globals['_NAMEDREQUESTBODYORREFERENCE']._serialized_start=6602
  _globals['_NAMEDREQUESTBODYORREFERENCE']._serialized_end=6709
  _globals['_NAMEDRESPONSEORREFERENCE']._serialized_start=6711
  _globals['_NAMEDRESPONSEORREFERENCE']._serialized_end=6812
  _globals['_NAMEDSCHEMAORREFERENCE']._serialized_start=6814
  _globals['_NAMEDSCHEMAORREFERENCE']._serialized_end=6911
  _globals['_NAMEDSECURITYSCHEMEORREFERENCE']._serialized_start=6913
  _globals['_NAMEDSECURITYSCHEMEORREFERENCE']._serialized_end=7026
  _globals['_NAMEDSERVERVARIABLE']._serialized_start=7028
  _globals['_NAMEDSERVERVARIABLE']._serialized_end=7119
  _globals['_NAMEDSTRING']._serialized_start=7121
  _globals['_NAMEDSTRING']._serialized_end=7176
  _globals['_NAMEDSTRINGARRAY']._serialized_start=7178
  _globals['_NAMEDSTRINGARRAY']._serialized_end=7263
  _globals['_OAUTHFLOW']._serialized_start=7266
  _globals['_OAUTHFLOW']._serialized_end=7508
  _globals['_OAUTHFLOWS']._serialized_start=7511
  _globals['_OAUTHFLOWS']._serialized_end=7844
  _globals['_OBJECT']._serialized_start=7846
  _globals['_OBJECT']._serialized_end=7929
  _globals['_OPERATION']._serialized_start=7932
  _globals['_OPERATION']._serialized_end=8594
  _globals['_PARAMETER']._serialized_start=8597
  _globals['_PARAMETER']._serialized_end=9158
  _globals['_PARAMETERORREFERENCE']._serialized_start=9161
  _globals['_PARAMETERORREFERENCE']._serialized_end=9302
  _globals['_PARAMETERSORREFERENCES']._serialized_start=9304
  _globals['_PARAMETERSORREFERENCES']._serialized_end=9420
  _globals['_PATHITEM']._serialized_start=9423
  _globals['_PATHITEM']._serialized_end=10057
  _globals['_PATHS']._serialized_start=10060
  _globals['_PATHS']._serialized_end=10193
  _globals['_PROPERTIES']._serialized_start=10195
  _globals['_PROPERTIES']._serialized_end=10296
  _globals['_REFERENCE']._serialized_start=10298
  _globals['_REFERENCE']._serialized_end=10388
  _globals['_REQUESTBODIESORREFERENCES']._serialized_start=10390
  _globals['_REQUESTBODIESORREFERENCES']._serialized_end=10511
  _globals['_REQUESTBODY']._serialized_start=10514
  _globals['_REQUESTBODY']._serialized_end=10718
  _globals['_REQUESTBODYORREFERENCE']._serialized_start=10721
  _globals['_REQUESTBODYORREFERENCE']._serialized_end=10871
  _globals['_RESPONSE']._serialized_start=10874
  _globals['_RESPONSE']._serialized_end=11159
  _globals['_RESPONSEORREFERENCE']._serialized_start=11162
  _globals['_RESPONSEORREFERENCE']._serialized_end=11299
  _globals['_RESPONSES']._serialized_start=11302
  _globals['_RESPONSES']._serialized_end=11541
  _globals['_RESPONSESORREFERENCES']._serialized_start=11543
  _globals['_RESPONSESORREFERENCES']._serialized_end=11657
  _globals['_SCHEMA']._serialized_start=11660
  _globals['_SCHEMA']._serialized_end=13115
  _globals['_SCHEMAORREFERENCE']._serialized_start=13118
  _globals['_SCHEMAORREFERENCE']._serialized_end=13247
  _globals['_SCHEMASORREFERENCES']._serialized_start=13249
  _globals['_SCHEMASORREFERENCES']._serialized_end=13359
  _globals['_SECURITYREQUIREMENT']._serialized_start=13361
  _globals['_SECURITYREQUIREMENT']._serialized_end=13465
  _globals['_SECURITYSCHEME']._serialized_start=13468
  _globals['_SECURITYSCHEME']._serialized_end=13807
  _globals['_SECURITYSCHEMEORREFERENCE']._serialized_start=13810
  _globals['_SECURITYSCHEMEORREFERENCE']._serialized_end=13972
  _globals['_SECURITYSCHEMESORREFERENCES']._serialized_start=13974
  _globals['_SECURITYSCHEMESORREFERENCES']._serialized_end=14100
  _globals['_SERVER']._serialized_start=14103
  _globals['_SERVER']._serialized_end=14301
  _globals['_SERVERVARIABLE']._serialized_start=14304
  _globals['_SERVERVARIABLE']._serialized_end=14479
  _globals['_SERVERVARIABLES']._serialized_start=14481
  _globals['_SERVERVARIABLES']._serialized_end=14584
  _globals['_SPECIFICATIONEXTENSION']._serialized_start=14586
  _globals['_SPECIFICATIONEXTENSION']._serialized_end=14699
  _globals['_STRINGARRAY']._serialized_start=14701
  _globals['_STRINGARRAY']._serialized_end=14736
  _globals['_STRINGS']._serialized_start=14738
  _globals['_STRINGS']._serialized_end=14825
  _globals['_TAG']._serialized_start=14828
  _globals['_TAG']._serialized_end=15029
  _globals['_XML']._serialized_start=15032
  _globals['_XML']._serialized_end=15246
# @@protoc_insertion_point(module_scope)

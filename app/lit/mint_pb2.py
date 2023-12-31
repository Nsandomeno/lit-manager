# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import taprootassets_pb2 as taprootassets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmint.proto\x12\x07mintrpc\x1a\x13taprootassets.proto\"\xcd\x01\n\tMintAsset\x12%\n\nasset_type\x18\x01 \x01(\x0e\x32\x11.taprpc.AssetType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\nasset_meta\x18\x03 \x01(\x0b\x32\x11.taprpc.AssetMeta\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\tgroup_key\x18\x05 \x01(\x0c\x12\x14\n\x0cgroup_anchor\x18\x06 \x01(\t\x12+\n\rasset_version\x18\x07 \x01(\x0e\x32\x14.taprpc.AssetVersion\"f\n\x10MintAssetRequest\x12!\n\x05\x61sset\x18\x01 \x01(\x0b\x32\x12.mintrpc.MintAsset\x12\x17\n\x0f\x65nable_emission\x18\x02 \x01(\x08\x12\x16\n\x0eshort_response\x18\x03 \x01(\x08\"A\n\x11MintAssetResponse\x12,\n\rpending_batch\x18\x01 \x01(\x0b\x32\x15.mintrpc.MintingBatch\"}\n\x0cMintingBatch\x12\x11\n\tbatch_key\x18\x01 \x01(\x0c\x12\x12\n\nbatch_txid\x18\x02 \x01(\t\x12\"\n\x05state\x18\x03 \x01(\x0e\x32\x13.mintrpc.BatchState\x12\"\n\x06\x61ssets\x18\x04 \x03(\x0b\x32\x12.mintrpc.MintAsset\"@\n\x14\x46inalizeBatchRequest\x12\x16\n\x0eshort_response\x18\x01 \x01(\x08\x12\x10\n\x08\x66\x65\x65_rate\x18\x02 \x01(\r\"=\n\x15\x46inalizeBatchResponse\x12$\n\x05\x62\x61tch\x18\x01 \x01(\x0b\x32\x15.mintrpc.MintingBatch\"\x14\n\x12\x43\x61ncelBatchRequest\"(\n\x13\x43\x61ncelBatchResponse\x12\x11\n\tbatch_key\x18\x01 \x01(\x0c\"J\n\x10ListBatchRequest\x12\x13\n\tbatch_key\x18\x01 \x01(\x0cH\x00\x12\x17\n\rbatch_key_str\x18\x02 \x01(\tH\x00\x42\x08\n\x06\x66ilter\";\n\x11ListBatchResponse\x12&\n\x07\x62\x61tches\x18\x01 \x03(\x0b\x32\x15.mintrpc.MintingBatch*\x88\x02\n\nBatchState\x12\x17\n\x13\x42\x41TCH_STATE_UNKNOWN\x10\x00\x12\x17\n\x13\x42\x41TCH_STATE_PEDNING\x10\x01\x12\x16\n\x12\x42\x41TCH_STATE_FROZEN\x10\x02\x12\x19\n\x15\x42\x41TCH_STATE_COMMITTED\x10\x03\x12\x19\n\x15\x42\x41TCH_STATE_BROADCAST\x10\x04\x12\x19\n\x15\x42\x41TCH_STATE_CONFIRMED\x10\x05\x12\x19\n\x15\x42\x41TCH_STATE_FINALIZED\x10\x06\x12\"\n\x1e\x42\x41TCH_STATE_SEEDLING_CANCELLED\x10\x07\x12 \n\x1c\x42\x41TCH_STATE_SPROUT_CANCELLED\x10\x08\x32\xaa\x02\n\x04Mint\x12\x42\n\tMintAsset\x12\x19.mintrpc.MintAssetRequest\x1a\x1a.mintrpc.MintAssetResponse\x12N\n\rFinalizeBatch\x12\x1d.mintrpc.FinalizeBatchRequest\x1a\x1e.mintrpc.FinalizeBatchResponse\x12H\n\x0b\x43\x61ncelBatch\x12\x1b.mintrpc.CancelBatchRequest\x1a\x1c.mintrpc.CancelBatchResponse\x12\x44\n\x0bListBatches\x12\x19.mintrpc.ListBatchRequest\x1a\x1a.mintrpc.ListBatchResponseB8Z6github.com/lightninglabs/taproot-assets/taprpc/mintrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/lightninglabs/taproot-assets/taprpc/mintrpc'
  _globals['_BATCHSTATE']._serialized_start=881
  _globals['_BATCHSTATE']._serialized_end=1145
  _globals['_MINTASSET']._serialized_start=45
  _globals['_MINTASSET']._serialized_end=250
  _globals['_MINTASSETREQUEST']._serialized_start=252
  _globals['_MINTASSETREQUEST']._serialized_end=354
  _globals['_MINTASSETRESPONSE']._serialized_start=356
  _globals['_MINTASSETRESPONSE']._serialized_end=421
  _globals['_MINTINGBATCH']._serialized_start=423
  _globals['_MINTINGBATCH']._serialized_end=548
  _globals['_FINALIZEBATCHREQUEST']._serialized_start=550
  _globals['_FINALIZEBATCHREQUEST']._serialized_end=614
  _globals['_FINALIZEBATCHRESPONSE']._serialized_start=616
  _globals['_FINALIZEBATCHRESPONSE']._serialized_end=677
  _globals['_CANCELBATCHREQUEST']._serialized_start=679
  _globals['_CANCELBATCHREQUEST']._serialized_end=699
  _globals['_CANCELBATCHRESPONSE']._serialized_start=701
  _globals['_CANCELBATCHRESPONSE']._serialized_end=741
  _globals['_LISTBATCHREQUEST']._serialized_start=743
  _globals['_LISTBATCHREQUEST']._serialized_end=817
  _globals['_LISTBATCHRESPONSE']._serialized_start=819
  _globals['_LISTBATCHRESPONSE']._serialized_end=878
  _globals['_MINT']._serialized_start=1148
  _globals['_MINT']._serialized_end=1446
# @@protoc_insertion_point(module_scope)

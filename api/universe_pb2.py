# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: universe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import api.taprootassets_pb2 as taprootassets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0euniverse.proto\x12\x0buniverserpc\x1a\x13taprootassets.proto\"|\n\x10\x41ssetRootRequest\x12\x1a\n\x12with_amounts_by_id\x18\x01 \x01(\x08\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12-\n\tdirection\x18\x04 \x01(\x0e\x32\x1a.universerpc.SortDirection\"4\n\rMerkleSumNode\x12\x11\n\troot_hash\x18\x01 \x01(\x0c\x12\x10\n\x08root_sum\x18\x02 \x01(\x03\"\x90\x01\n\x02ID\x12\x12\n\x08\x61sset_id\x18\x01 \x01(\x0cH\x00\x12\x16\n\x0c\x61sset_id_str\x18\x02 \x01(\tH\x00\x12\x13\n\tgroup_key\x18\x03 \x01(\x0cH\x00\x12\x17\n\rgroup_key_str\x18\x04 \x01(\tH\x00\x12*\n\nproof_type\x18\x05 \x01(\x0e\x32\x16.universerpc.ProofTypeB\x04\n\x02id\"\xf6\x01\n\x0cUniverseRoot\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\x12.\n\nmssmt_root\x18\x03 \x01(\x0b\x32\x1a.universerpc.MerkleSumNode\x12\x12\n\nasset_name\x18\x04 \x01(\t\x12L\n\x13\x61mounts_by_asset_id\x18\x05 \x03(\x0b\x32/.universerpc.UniverseRoot.AmountsByAssetIdEntry\x1a\x37\n\x15\x41mountsByAssetIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\xaf\x01\n\x11\x41ssetRootResponse\x12I\n\x0euniverse_roots\x18\x01 \x03(\x0b\x32\x31.universerpc.AssetRootResponse.UniverseRootsEntry\x1aO\n\x12UniverseRootsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.universerpc.UniverseRoot:\x02\x38\x01\"-\n\x0e\x41ssetRootQuery\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\"w\n\x11QueryRootResponse\x12\x30\n\rissuance_root\x18\x01 \x01(\x0b\x32\x19.universerpc.UniverseRoot\x12\x30\n\rtransfer_root\x18\x02 \x01(\x0b\x32\x19.universerpc.UniverseRoot\".\n\x0f\x44\x65leteRootQuery\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\"\x14\n\x12\x44\x65leteRootResponse\"+\n\x08Outpoint\x12\x10\n\x08hash_str\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\"\x91\x01\n\x08\x41ssetKey\x12\x10\n\x06op_str\x18\x01 \x01(\tH\x00\x12#\n\x02op\x18\x02 \x01(\x0b\x32\x15.universerpc.OutpointH\x00\x12\x1a\n\x10script_key_bytes\x18\x03 \x01(\x0cH\x01\x12\x18\n\x0escript_key_str\x18\x04 \x01(\tH\x01\x42\n\n\x08outpointB\x0c\n\nscript_key\"\x81\x01\n\x14\x41ssetLeafKeysRequest\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\x12-\n\tdirection\x18\x04 \x01(\x0e\x32\x1a.universerpc.SortDirection\"A\n\x14\x41ssetLeafKeyResponse\x12)\n\nasset_keys\x18\x01 \x03(\x0b\x32\x15.universerpc.AssetKey\"8\n\tAssetLeaf\x12\x1c\n\x05\x61sset\x18\x01 \x01(\x0b\x32\r.taprpc.Asset\x12\r\n\x05proof\x18\x02 \x01(\x0c\";\n\x11\x41ssetLeafResponse\x12&\n\x06leaves\x18\x01 \x03(\x0b\x32\x16.universerpc.AssetLeaf\"S\n\x0bUniverseKey\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\x12\'\n\x08leaf_key\x18\x02 \x01(\x0b\x32\x15.universerpc.AssetKey\"\x94\x02\n\x12\x41ssetProofResponse\x12%\n\x03req\x18\x01 \x01(\x0b\x32\x18.universerpc.UniverseKey\x12\x30\n\runiverse_root\x18\x02 \x01(\x0b\x32\x19.universerpc.UniverseRoot\x12 \n\x18universe_inclusion_proof\x18\x03 \x01(\x0c\x12*\n\nasset_leaf\x18\x04 \x01(\x0b\x32\x16.universerpc.AssetLeaf\x12\x33\n\x0fmultiverse_root\x18\x05 \x01(\x0b\x32\x1a.universerpc.MerkleSumNode\x12\"\n\x1amultiverse_inclusion_proof\x18\x06 \x01(\x0c\"_\n\nAssetProof\x12%\n\x03key\x18\x01 \x01(\x0b\x32\x18.universerpc.UniverseKey\x12*\n\nasset_leaf\x18\x04 \x01(\x0b\x32\x16.universerpc.AssetLeaf\"\r\n\x0bInfoRequest\"\"\n\x0cInfoResponse\x12\x12\n\nruntime_id\x18\x01 \x01(\x03\")\n\nSyncTarget\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\"\x85\x01\n\x0bSyncRequest\x12\x15\n\runiverse_host\x18\x01 \x01(\t\x12\x30\n\tsync_mode\x18\x02 \x01(\x0e\x32\x1d.universerpc.UniverseSyncMode\x12-\n\x0csync_targets\x18\x03 \x03(\x0b\x32\x17.universerpc.SyncTarget\"\xa8\x01\n\x0eSyncedUniverse\x12\x31\n\x0eold_asset_root\x18\x01 \x01(\x0b\x32\x19.universerpc.UniverseRoot\x12\x31\n\x0enew_asset_root\x18\x02 \x01(\x0b\x32\x19.universerpc.UniverseRoot\x12\x30\n\x10new_asset_leaves\x18\x03 \x03(\x0b\x32\x16.universerpc.AssetLeaf\"\x0e\n\x0cStatsRequest\"E\n\x0cSyncResponse\x12\x35\n\x10synced_universes\x18\x01 \x03(\x0b\x32\x1b.universerpc.SyncedUniverse\"4\n\x18UniverseFederationServer\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"\x1e\n\x1cListFederationServersRequest\"W\n\x1dListFederationServersResponse\x12\x36\n\x07servers\x18\x01 \x03(\x0b\x32%.universerpc.UniverseFederationServer\"T\n\x1a\x41\x64\x64\x46\x65\x64\x65rationServerRequest\x12\x36\n\x07servers\x18\x01 \x03(\x0b\x32%.universerpc.UniverseFederationServer\"\x1d\n\x1b\x41\x64\x64\x46\x65\x64\x65rationServerResponse\"W\n\x1d\x44\x65leteFederationServerRequest\x12\x36\n\x07servers\x18\x01 \x03(\x0b\x32%.universerpc.UniverseFederationServer\" \n\x1e\x44\x65leteFederationServerResponse\"v\n\rStatsResponse\x12\x18\n\x10num_total_assets\x18\x01 \x01(\x03\x12\x18\n\x10num_total_groups\x18\x02 \x01(\x03\x12\x17\n\x0fnum_total_syncs\x18\x03 \x01(\x03\x12\x18\n\x10num_total_proofs\x18\x04 \x01(\x03\"\xfa\x01\n\x0f\x41ssetStatsQuery\x12\x19\n\x11\x61sset_name_filter\x18\x01 \x01(\t\x12\x17\n\x0f\x61sset_id_filter\x18\x02 \x01(\x0c\x12\x37\n\x11\x61sset_type_filter\x18\x03 \x01(\x0e\x32\x1c.universerpc.AssetTypeFilter\x12,\n\x07sort_by\x18\x04 \x01(\x0e\x32\x1b.universerpc.AssetQuerySort\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\r\n\x05limit\x18\x06 \x01(\x05\x12-\n\tdirection\x18\x07 \x01(\x0e\x32\x1a.universerpc.SortDirection\"\xc9\x01\n\x12\x41ssetStatsSnapshot\x12\x11\n\tgroup_key\x18\x01 \x01(\x0c\x12\x14\n\x0cgroup_supply\x18\x02 \x01(\x03\x12\x32\n\x0cgroup_anchor\x18\x03 \x01(\x0b\x32\x1c.universerpc.AssetStatsAsset\x12+\n\x05\x61sset\x18\x04 \x01(\x0b\x32\x1c.universerpc.AssetStatsAsset\x12\x13\n\x0btotal_syncs\x18\x05 \x01(\x03\x12\x14\n\x0ctotal_proofs\x18\x06 \x01(\x03\"\xd4\x01\n\x0f\x41ssetStatsAsset\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x15\n\rgenesis_point\x18\x02 \x01(\t\x12\x14\n\x0ctotal_supply\x18\x03 \x01(\x03\x12\x12\n\nasset_name\x18\x04 \x01(\t\x12%\n\nasset_type\x18\x05 \x01(\x0e\x32\x11.taprpc.AssetType\x12\x16\n\x0egenesis_height\x18\x06 \x01(\x05\x12\x19\n\x11genesis_timestamp\x18\x07 \x01(\x03\x12\x14\n\x0c\x61nchor_point\x18\x08 \x01(\t\"J\n\x12UniverseAssetStats\x12\x34\n\x0b\x61sset_stats\x18\x01 \x03(\x0b\x32\x1f.universerpc.AssetStatsSnapshot\"D\n\x12QueryEventsRequest\x12\x17\n\x0fstart_timestamp\x18\x01 \x01(\x03\x12\x15\n\rend_timestamp\x18\x02 \x01(\x03\"I\n\x13QueryEventsResponse\x12\x32\n\x06\x65vents\x18\x01 \x03(\x0b\x32\".universerpc.GroupedUniverseEvents\"T\n\x15GroupedUniverseEvents\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x13\n\x0bsync_events\x18\x02 \x01(\x04\x12\x18\n\x10new_proof_events\x18\x03 \x01(\x04\"\xaa\x01\n\x1eSetFederationSyncConfigRequest\x12\x44\n\x13global_sync_configs\x18\x01 \x03(\x0b\x32\'.universerpc.GlobalFederationSyncConfig\x12\x42\n\x12\x61sset_sync_configs\x18\x02 \x03(\x0b\x32&.universerpc.AssetFederationSyncConfig\"!\n\x1fSetFederationSyncConfigResponse\"~\n\x1aGlobalFederationSyncConfig\x12*\n\nproof_type\x18\x01 \x01(\x0e\x32\x16.universerpc.ProofType\x12\x19\n\x11\x61llow_sync_insert\x18\x02 \x01(\x08\x12\x19\n\x11\x61llow_sync_export\x18\x03 \x01(\x08\"n\n\x19\x41ssetFederationSyncConfig\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.universerpc.ID\x12\x19\n\x11\x61llow_sync_insert\x18\x02 \x01(\x08\x12\x19\n\x11\x61llow_sync_export\x18\x03 \x01(\x08\"?\n QueryFederationSyncConfigRequest\x12\x1b\n\x02id\x18\x01 \x03(\x0b\x32\x0f.universerpc.ID\"\xad\x01\n!QueryFederationSyncConfigResponse\x12\x44\n\x13global_sync_configs\x18\x01 \x03(\x0b\x32\'.universerpc.GlobalFederationSyncConfig\x12\x42\n\x12\x61sset_sync_configs\x18\x02 \x03(\x0b\x32&.universerpc.AssetFederationSyncConfig*Y\n\tProofType\x12\x1a\n\x16PROOF_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13PROOF_TYPE_ISSUANCE\x10\x01\x12\x17\n\x13PROOF_TYPE_TRANSFER\x10\x02*9\n\x10UniverseSyncMode\x12\x16\n\x12SYNC_ISSUANCE_ONLY\x10\x00\x12\r\n\tSYNC_FULL\x10\x01*\xd1\x01\n\x0e\x41ssetQuerySort\x12\x10\n\x0cSORT_BY_NONE\x10\x00\x12\x16\n\x12SORT_BY_ASSET_NAME\x10\x01\x12\x14\n\x10SORT_BY_ASSET_ID\x10\x02\x12\x16\n\x12SORT_BY_ASSET_TYPE\x10\x03\x12\x17\n\x13SORT_BY_TOTAL_SYNCS\x10\x04\x12\x18\n\x14SORT_BY_TOTAL_PROOFS\x10\x05\x12\x1a\n\x16SORT_BY_GENESIS_HEIGHT\x10\x06\x12\x18\n\x14SORT_BY_TOTAL_SUPPLY\x10\x07*@\n\rSortDirection\x12\x16\n\x12SORT_DIRECTION_ASC\x10\x00\x12\x17\n\x13SORT_DIRECTION_DESC\x10\x01*_\n\x0f\x41ssetTypeFilter\x12\x15\n\x11\x46ILTER_ASSET_NONE\x10\x00\x12\x17\n\x13\x46ILTER_ASSET_NORMAL\x10\x01\x12\x1c\n\x18\x46ILTER_ASSET_COLLECTIBLE\x10\x02\x32\xcf\x0b\n\x08Universe\x12K\n\nAssetRoots\x12\x1d.universerpc.AssetRootRequest\x1a\x1e.universerpc.AssetRootResponse\x12N\n\x0fQueryAssetRoots\x12\x1b.universerpc.AssetRootQuery\x1a\x1e.universerpc.QueryRootResponse\x12P\n\x0f\x44\x65leteAssetRoot\x12\x1c.universerpc.DeleteRootQuery\x1a\x1f.universerpc.DeleteRootResponse\x12U\n\rAssetLeafKeys\x12!.universerpc.AssetLeafKeysRequest\x1a!.universerpc.AssetLeafKeyResponse\x12>\n\x0b\x41ssetLeaves\x12\x0f.universerpc.ID\x1a\x1e.universerpc.AssetLeafResponse\x12G\n\nQueryProof\x12\x18.universerpc.UniverseKey\x1a\x1f.universerpc.AssetProofResponse\x12G\n\x0bInsertProof\x12\x17.universerpc.AssetProof\x1a\x1f.universerpc.AssetProofResponse\x12;\n\x04Info\x12\x18.universerpc.InfoRequest\x1a\x19.universerpc.InfoResponse\x12\x43\n\x0cSyncUniverse\x12\x18.universerpc.SyncRequest\x1a\x19.universerpc.SyncResponse\x12n\n\x15ListFederationServers\x12).universerpc.ListFederationServersRequest\x1a*.universerpc.ListFederationServersResponse\x12h\n\x13\x41\x64\x64\x46\x65\x64\x65rationServer\x12\'.universerpc.AddFederationServerRequest\x1a(.universerpc.AddFederationServerResponse\x12q\n\x16\x44\x65leteFederationServer\x12*.universerpc.DeleteFederationServerRequest\x1a+.universerpc.DeleteFederationServerResponse\x12\x46\n\rUniverseStats\x12\x19.universerpc.StatsRequest\x1a\x1a.universerpc.StatsResponse\x12P\n\x0fQueryAssetStats\x12\x1c.universerpc.AssetStatsQuery\x1a\x1f.universerpc.UniverseAssetStats\x12P\n\x0bQueryEvents\x12\x1f.universerpc.QueryEventsRequest\x1a .universerpc.QueryEventsResponse\x12t\n\x17SetFederationSyncConfig\x12+.universerpc.SetFederationSyncConfigRequest\x1a,.universerpc.SetFederationSyncConfigResponse\x12z\n\x19QueryFederationSyncConfig\x12-.universerpc.QueryFederationSyncConfigRequest\x1a..universerpc.QueryFederationSyncConfigResponseB<Z:github.com/lightninglabs/taproot-assets/taprpc/universerpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'universe_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:github.com/lightninglabs/taproot-assets/taprpc/universerpc'
  _UNIVERSEROOT_AMOUNTSBYASSETIDENTRY._options = None
  _UNIVERSEROOT_AMOUNTSBYASSETIDENTRY._serialized_options = b'8\001'
  _ASSETROOTRESPONSE_UNIVERSEROOTSENTRY._options = None
  _ASSETROOTRESPONSE_UNIVERSEROOTSENTRY._serialized_options = b'8\001'
  _globals['_PROOFTYPE']._serialized_start=4707
  _globals['_PROOFTYPE']._serialized_end=4796
  _globals['_UNIVERSESYNCMODE']._serialized_start=4798
  _globals['_UNIVERSESYNCMODE']._serialized_end=4855
  _globals['_ASSETQUERYSORT']._serialized_start=4858
  _globals['_ASSETQUERYSORT']._serialized_end=5067
  _globals['_SORTDIRECTION']._serialized_start=5069
  _globals['_SORTDIRECTION']._serialized_end=5133
  _globals['_ASSETTYPEFILTER']._serialized_start=5135
  _globals['_ASSETTYPEFILTER']._serialized_end=5230
  _globals['_ASSETROOTREQUEST']._serialized_start=52
  _globals['_ASSETROOTREQUEST']._serialized_end=176
  _globals['_MERKLESUMNODE']._serialized_start=178
  _globals['_MERKLESUMNODE']._serialized_end=230
  _globals['_ID']._serialized_start=233
  _globals['_ID']._serialized_end=377
  _globals['_UNIVERSEROOT']._serialized_start=380
  _globals['_UNIVERSEROOT']._serialized_end=626
  _globals['_UNIVERSEROOT_AMOUNTSBYASSETIDENTRY']._serialized_start=571
  _globals['_UNIVERSEROOT_AMOUNTSBYASSETIDENTRY']._serialized_end=626
  _globals['_ASSETROOTRESPONSE']._serialized_start=629
  _globals['_ASSETROOTRESPONSE']._serialized_end=804
  _globals['_ASSETROOTRESPONSE_UNIVERSEROOTSENTRY']._serialized_start=725
  _globals['_ASSETROOTRESPONSE_UNIVERSEROOTSENTRY']._serialized_end=804
  _globals['_ASSETROOTQUERY']._serialized_start=806
  _globals['_ASSETROOTQUERY']._serialized_end=851
  _globals['_QUERYROOTRESPONSE']._serialized_start=853
  _globals['_QUERYROOTRESPONSE']._serialized_end=972
  _globals['_DELETEROOTQUERY']._serialized_start=974
  _globals['_DELETEROOTQUERY']._serialized_end=1020
  _globals['_DELETEROOTRESPONSE']._serialized_start=1022
  _globals['_DELETEROOTRESPONSE']._serialized_end=1042
  _globals['_OUTPOINT']._serialized_start=1044
  _globals['_OUTPOINT']._serialized_end=1087
  _globals['_ASSETKEY']._serialized_start=1090
  _globals['_ASSETKEY']._serialized_end=1235
  _globals['_ASSETLEAFKEYSREQUEST']._serialized_start=1238
  _globals['_ASSETLEAFKEYSREQUEST']._serialized_end=1367
  _globals['_ASSETLEAFKEYRESPONSE']._serialized_start=1369
  _globals['_ASSETLEAFKEYRESPONSE']._serialized_end=1434
  _globals['_ASSETLEAF']._serialized_start=1436
  _globals['_ASSETLEAF']._serialized_end=1492
  _globals['_ASSETLEAFRESPONSE']._serialized_start=1494
  _globals['_ASSETLEAFRESPONSE']._serialized_end=1553
  _globals['_UNIVERSEKEY']._serialized_start=1555
  _globals['_UNIVERSEKEY']._serialized_end=1638
  _globals['_ASSETPROOFRESPONSE']._serialized_start=1641
  _globals['_ASSETPROOFRESPONSE']._serialized_end=1917
  _globals['_ASSETPROOF']._serialized_start=1919
  _globals['_ASSETPROOF']._serialized_end=2014
  _globals['_INFOREQUEST']._serialized_start=2016
  _globals['_INFOREQUEST']._serialized_end=2029
  _globals['_INFORESPONSE']._serialized_start=2031
  _globals['_INFORESPONSE']._serialized_end=2065
  _globals['_SYNCTARGET']._serialized_start=2067
  _globals['_SYNCTARGET']._serialized_end=2108
  _globals['_SYNCREQUEST']._serialized_start=2111
  _globals['_SYNCREQUEST']._serialized_end=2244
  _globals['_SYNCEDUNIVERSE']._serialized_start=2247
  _globals['_SYNCEDUNIVERSE']._serialized_end=2415
  _globals['_STATSREQUEST']._serialized_start=2417
  _globals['_STATSREQUEST']._serialized_end=2431
  _globals['_SYNCRESPONSE']._serialized_start=2433
  _globals['_SYNCRESPONSE']._serialized_end=2502
  _globals['_UNIVERSEFEDERATIONSERVER']._serialized_start=2504
  _globals['_UNIVERSEFEDERATIONSERVER']._serialized_end=2556
  _globals['_LISTFEDERATIONSERVERSREQUEST']._serialized_start=2558
  _globals['_LISTFEDERATIONSERVERSREQUEST']._serialized_end=2588
  _globals['_LISTFEDERATIONSERVERSRESPONSE']._serialized_start=2590
  _globals['_LISTFEDERATIONSERVERSRESPONSE']._serialized_end=2677
  _globals['_ADDFEDERATIONSERVERREQUEST']._serialized_start=2679
  _globals['_ADDFEDERATIONSERVERREQUEST']._serialized_end=2763
  _globals['_ADDFEDERATIONSERVERRESPONSE']._serialized_start=2765
  _globals['_ADDFEDERATIONSERVERRESPONSE']._serialized_end=2794
  _globals['_DELETEFEDERATIONSERVERREQUEST']._serialized_start=2796
  _globals['_DELETEFEDERATIONSERVERREQUEST']._serialized_end=2883
  _globals['_DELETEFEDERATIONSERVERRESPONSE']._serialized_start=2885
  _globals['_DELETEFEDERATIONSERVERRESPONSE']._serialized_end=2917
  _globals['_STATSRESPONSE']._serialized_start=2919
  _globals['_STATSRESPONSE']._serialized_end=3037
  _globals['_ASSETSTATSQUERY']._serialized_start=3040
  _globals['_ASSETSTATSQUERY']._serialized_end=3290
  _globals['_ASSETSTATSSNAPSHOT']._serialized_start=3293
  _globals['_ASSETSTATSSNAPSHOT']._serialized_end=3494
  _globals['_ASSETSTATSASSET']._serialized_start=3497
  _globals['_ASSETSTATSASSET']._serialized_end=3709
  _globals['_UNIVERSEASSETSTATS']._serialized_start=3711
  _globals['_UNIVERSEASSETSTATS']._serialized_end=3785
  _globals['_QUERYEVENTSREQUEST']._serialized_start=3787
  _globals['_QUERYEVENTSREQUEST']._serialized_end=3855
  _globals['_QUERYEVENTSRESPONSE']._serialized_start=3857
  _globals['_QUERYEVENTSRESPONSE']._serialized_end=3930
  _globals['_GROUPEDUNIVERSEEVENTS']._serialized_start=3932
  _globals['_GROUPEDUNIVERSEEVENTS']._serialized_end=4016
  _globals['_SETFEDERATIONSYNCCONFIGREQUEST']._serialized_start=4019
  _globals['_SETFEDERATIONSYNCCONFIGREQUEST']._serialized_end=4189
  _globals['_SETFEDERATIONSYNCCONFIGRESPONSE']._serialized_start=4191
  _globals['_SETFEDERATIONSYNCCONFIGRESPONSE']._serialized_end=4224
  _globals['_GLOBALFEDERATIONSYNCCONFIG']._serialized_start=4226
  _globals['_GLOBALFEDERATIONSYNCCONFIG']._serialized_end=4352
  _globals['_ASSETFEDERATIONSYNCCONFIG']._serialized_start=4354
  _globals['_ASSETFEDERATIONSYNCCONFIG']._serialized_end=4464
  _globals['_QUERYFEDERATIONSYNCCONFIGREQUEST']._serialized_start=4466
  _globals['_QUERYFEDERATIONSYNCCONFIGREQUEST']._serialized_end=4529
  _globals['_QUERYFEDERATIONSYNCCONFIGRESPONSE']._serialized_start=4532
  _globals['_QUERYFEDERATIONSYNCCONFIGRESPONSE']._serialized_end=4705
  _globals['_UNIVERSE']._serialized_start=5233
  _globals['_UNIVERSE']._serialized_end=6720
# @@protoc_insertion_point(module_scope)
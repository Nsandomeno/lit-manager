# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taprootassets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13taprootassets.proto\x12\x06taprpc\"Q\n\tAssetMeta\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.taprpc.AssetMetaType\x12\x11\n\tmeta_hash\x18\x03 \x01(\x0c\"W\n\x10ListAssetRequest\x12\x14\n\x0cwith_witness\x18\x01 \x01(\x08\x12\x15\n\rinclude_spent\x18\x02 \x01(\x08\x12\x16\n\x0einclude_leased\x18\x03 \x01(\x08\"\xaf\x01\n\nAnchorInfo\x12\x11\n\tanchor_tx\x18\x01 \x01(\x0c\x12\x19\n\x11\x61nchor_block_hash\x18\x03 \x01(\t\x12\x17\n\x0f\x61nchor_outpoint\x18\x04 \x01(\t\x12\x14\n\x0cinternal_key\x18\x05 \x01(\x0c\x12\x13\n\x0bmerkle_root\x18\x06 \x01(\x0c\x12\x19\n\x11tapscript_sibling\x18\x07 \x01(\x0c\x12\x14\n\x0c\x62lock_height\x18\x08 \x01(\r\"\xa5\x01\n\x0bGenesisInfo\x12\x15\n\rgenesis_point\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tmeta_hash\x18\x03 \x01(\x0c\x12\x10\n\x08\x61sset_id\x18\x04 \x01(\x0c\x12%\n\nasset_type\x18\x05 \x01(\x0e\x32\x11.taprpc.AssetType\x12\x14\n\x0coutput_index\x18\x06 \x01(\r\x12\x0f\n\x07version\x18\x07 \x01(\x05\"U\n\nAssetGroup\x12\x15\n\rraw_group_key\x18\x01 \x01(\x0c\x12\x19\n\x11tweaked_group_key\x18\x02 \x01(\x0c\x12\x15\n\rasset_witness\x18\x03 \x01(\x0c\"?\n\x0eGroupKeyReveal\x12\x15\n\rraw_group_key\x18\x01 \x01(\x0c\x12\x16\n\x0etapscript_root\x18\x02 \x01(\x0c\"A\n\rGenesisReveal\x12\x30\n\x13genesis_base_reveal\x18\x01 \x01(\x0b\x32\x13.taprpc.GenesisInfo\"\xb0\x03\n\x05\x41sset\x12%\n\x07version\x18\x01 \x01(\x0e\x32\x14.taprpc.AssetVersion\x12*\n\rasset_genesis\x18\x02 \x01(\x0b\x32\x13.taprpc.GenesisInfo\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\tlock_time\x18\x05 \x01(\x05\x12\x1a\n\x12relative_lock_time\x18\x06 \x01(\x05\x12\x16\n\x0escript_version\x18\x07 \x01(\x05\x12\x12\n\nscript_key\x18\t \x01(\x0c\x12\x1b\n\x13script_key_is_local\x18\n \x01(\x08\x12\'\n\x0b\x61sset_group\x18\x0b \x01(\x0b\x32\x12.taprpc.AssetGroup\x12(\n\x0c\x63hain_anchor\x18\x0c \x01(\x0b\x32\x12.taprpc.AnchorInfo\x12+\n\x0eprev_witnesses\x18\r \x03(\x0b\x32\x13.taprpc.PrevWitness\x12\x10\n\x08is_spent\x18\x0e \x01(\x08\x12\x13\n\x0blease_owner\x18\x0f \x01(\x0c\x12\x14\n\x0clease_expiry\x18\x10 \x01(\x03\x12\x0f\n\x07is_burn\x18\x11 \x01(\x08\"}\n\x0bPrevWitness\x12\'\n\x07prev_id\x18\x01 \x01(\x0b\x32\x16.taprpc.PrevInputAsset\x12\x12\n\ntx_witness\x18\x02 \x03(\x0c\x12\x31\n\x10split_commitment\x18\x03 \x01(\x0b\x32\x17.taprpc.SplitCommitment\"4\n\x0fSplitCommitment\x12!\n\nroot_asset\x18\x01 \x01(\x0b\x32\r.taprpc.Asset\"2\n\x11ListAssetResponse\x12\x1d\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\r.taprpc.Asset\"*\n\x10ListUtxosRequest\x12\x16\n\x0einclude_leased\x18\x01 \x01(\x08\"\x97\x01\n\x0bManagedUtxo\x12\x11\n\tout_point\x18\x01 \x01(\t\x12\x0f\n\x07\x61mt_sat\x18\x02 \x01(\x03\x12\x14\n\x0cinternal_key\x18\x03 \x01(\x0c\x12\x1a\n\x12taproot_asset_root\x18\x04 \x01(\x0c\x12\x13\n\x0bmerkle_root\x18\x05 \x01(\x0c\x12\x1d\n\x06\x61ssets\x18\x06 \x03(\x0b\x32\r.taprpc.Asset\"\xa1\x01\n\x11ListUtxosResponse\x12\x42\n\rmanaged_utxos\x18\x01 \x03(\x0b\x32+.taprpc.ListUtxosResponse.ManagedUtxosEntry\x1aH\n\x11ManagedUtxosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.taprpc.ManagedUtxo:\x02\x38\x01\"\x13\n\x11ListGroupsRequest\"\xc7\x01\n\x12\x41ssetHumanReadable\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x11\n\tlock_time\x18\x03 \x01(\x05\x12\x1a\n\x12relative_lock_time\x18\x04 \x01(\x05\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\x11\n\tmeta_hash\x18\x06 \x01(\x0c\x12\x1f\n\x04type\x18\x07 \x01(\x0e\x32\x11.taprpc.AssetType\x12%\n\x07version\x18\x08 \x01(\x0e\x32\x14.taprpc.AssetVersion\";\n\rGroupedAssets\x12*\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x1a.taprpc.AssetHumanReadable\"\x92\x01\n\x12ListGroupsResponse\x12\x36\n\x06groups\x18\x01 \x03(\x0b\x32&.taprpc.ListGroupsResponse.GroupsEntry\x1a\x44\n\x0bGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.taprpc.GroupedAssets:\x02\x38\x01\"z\n\x13ListBalancesRequest\x12\x12\n\x08\x61sset_id\x18\x01 \x01(\x08H\x00\x12\x13\n\tgroup_key\x18\x02 \x01(\x08H\x00\x12\x14\n\x0c\x61sset_filter\x18\x03 \x01(\x0c\x12\x18\n\x10group_key_filter\x18\x04 \x01(\x0c\x42\n\n\x08group_by\"K\n\x0c\x41ssetBalance\x12*\n\rasset_genesis\x18\x01 \x01(\x0b\x32\x13.taprpc.GenesisInfo\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x04\"7\n\x11\x41ssetGroupBalance\x12\x11\n\tgroup_key\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x04\"\xd5\x02\n\x14ListBalancesResponse\x12G\n\x0e\x61sset_balances\x18\x01 \x03(\x0b\x32/.taprpc.ListBalancesResponse.AssetBalancesEntry\x12R\n\x14\x61sset_group_balances\x18\x02 \x03(\x0b\x32\x34.taprpc.ListBalancesResponse.AssetGroupBalancesEntry\x1aJ\n\x12\x41ssetBalancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.taprpc.AssetBalance:\x02\x38\x01\x1aT\n\x17\x41ssetGroupBalancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.taprpc.AssetGroupBalance:\x02\x38\x01\"\x16\n\x14ListTransfersRequest\"A\n\x15ListTransfersResponse\x12(\n\ttransfers\x18\x01 \x03(\x0b\x32\x15.taprpc.AssetTransfer\"\xd0\x01\n\rAssetTransfer\x12\x1a\n\x12transfer_timestamp\x18\x01 \x01(\x03\x12\x16\n\x0e\x61nchor_tx_hash\x18\x02 \x01(\x0c\x12\x1d\n\x15\x61nchor_tx_height_hint\x18\x03 \x01(\r\x12\x1c\n\x14\x61nchor_tx_chain_fees\x18\x04 \x01(\x03\x12%\n\x06inputs\x18\x05 \x03(\x0b\x32\x15.taprpc.TransferInput\x12\'\n\x07outputs\x18\x06 \x03(\x0b\x32\x16.taprpc.TransferOutput\"[\n\rTransferInput\x12\x14\n\x0c\x61nchor_point\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\x0c\x12\x12\n\nscript_key\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\"\xb5\x01\n\x14TransferOutputAnchor\x12\x10\n\x08outpoint\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\x12\x14\n\x0cinternal_key\x18\x03 \x01(\x0c\x12\x1a\n\x12taproot_asset_root\x18\x04 \x01(\x0c\x12\x13\n\x0bmerkle_root\x18\x05 \x01(\x0c\x12\x19\n\x11tapscript_sibling\x18\x06 \x01(\x0c\x12\x1a\n\x12num_passive_assets\x18\x07 \x01(\r\"\x8d\x02\n\x0eTransferOutput\x12,\n\x06\x61nchor\x18\x01 \x01(\x0b\x32\x1c.taprpc.TransferOutputAnchor\x12\x12\n\nscript_key\x18\x02 \x01(\x0c\x12\x1b\n\x13script_key_is_local\x18\x03 \x01(\x08\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x16\n\x0enew_proof_blob\x18\x05 \x01(\x0c\x12\x1e\n\x16split_commit_root_hash\x18\x06 \x01(\x0c\x12\'\n\x0boutput_type\x18\x07 \x01(\x0e\x32\x12.taprpc.OutputType\x12+\n\rasset_version\x18\x08 \x01(\x0e\x32\x14.taprpc.AssetVersion\"\r\n\x0bStopRequest\"\x0e\n\x0cStopResponse\"5\n\x11\x44\x65\x62ugLevelRequest\x12\x0c\n\x04show\x18\x01 \x01(\x08\x12\x12\n\nlevel_spec\x18\x02 \x01(\t\")\n\x12\x44\x65\x62ugLevelResponse\x12\x13\n\x0bsub_systems\x18\x01 \x01(\t\"\x9d\x02\n\x04\x41\x64\x64r\x12\x0f\n\x07\x65ncoded\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\x0c\x12%\n\nasset_type\x18\x03 \x01(\x0e\x32\x11.taprpc.AssetType\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12\x11\n\tgroup_key\x18\x05 \x01(\x0c\x12\x12\n\nscript_key\x18\x06 \x01(\x0c\x12\x14\n\x0cinternal_key\x18\x07 \x01(\x0c\x12\x19\n\x11tapscript_sibling\x18\x08 \x01(\x0c\x12\x1a\n\x12taproot_output_key\x18\t \x01(\x0c\x12\x1a\n\x12proof_courier_addr\x18\n \x01(\t\x12+\n\rasset_version\x18\x0b \x01(\x0e\x32\x14.taprpc.AssetVersion\"`\n\x10QueryAddrRequest\x12\x15\n\rcreated_after\x18\x01 \x01(\x03\x12\x16\n\x0e\x63reated_before\x18\x02 \x01(\x03\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\"0\n\x11QueryAddrResponse\x12\x1b\n\x05\x61\x64\x64rs\x18\x01 \x03(\x0b\x32\x0c.taprpc.Addr\"\xe7\x01\n\x0eNewAddrRequest\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x0b\n\x03\x61mt\x18\x02 \x01(\x04\x12%\n\nscript_key\x18\x03 \x01(\x0b\x32\x11.taprpc.ScriptKey\x12+\n\x0cinternal_key\x18\x04 \x01(\x0b\x32\x15.taprpc.KeyDescriptor\x12\x19\n\x11tapscript_sibling\x18\x05 \x01(\x0c\x12\x1a\n\x12proof_courier_addr\x18\x06 \x01(\t\x12+\n\rasset_version\x18\x07 \x01(\x0e\x32\x14.taprpc.AssetVersion\"X\n\tScriptKey\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\'\n\x08key_desc\x18\x02 \x01(\x0b\x32\x15.taprpc.KeyDescriptor\x12\x11\n\ttap_tweak\x18\x03 \x01(\x0c\"3\n\nKeyLocator\x12\x12\n\nkey_family\x18\x01 \x01(\x05\x12\x11\n\tkey_index\x18\x02 \x01(\x05\"K\n\rKeyDescriptor\x12\x15\n\rraw_key_bytes\x18\x01 \x01(\x0c\x12#\n\x07key_loc\x18\x02 \x01(\x0b\x32\x12.taprpc.KeyLocator\"!\n\x11\x44\x65\x63odeAddrRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\":\n\tProofFile\x12\x16\n\x0eraw_proof_file\x18\x01 \x01(\x0c\x12\x15\n\rgenesis_point\x18\x02 \x01(\t\"\x98\x03\n\x0c\x44\x65\x63odedProof\x12\x16\n\x0eproof_at_depth\x18\x01 \x01(\r\x12\x18\n\x10number_of_proofs\x18\x02 \x01(\r\x12\x1c\n\x05\x61sset\x18\x03 \x01(\x0b\x32\r.taprpc.Asset\x12&\n\x0bmeta_reveal\x18\x04 \x01(\x0b\x32\x11.taprpc.AssetMeta\x12\x17\n\x0ftx_merkle_proof\x18\x05 \x01(\x0c\x12\x17\n\x0finclusion_proof\x18\x06 \x01(\x0c\x12\x18\n\x10\x65xclusion_proofs\x18\x07 \x03(\x0c\x12\x18\n\x10split_root_proof\x18\x08 \x01(\x0c\x12\x1d\n\x15num_additional_inputs\x18\t \x01(\r\x12\x19\n\x11\x63hallenge_witness\x18\n \x03(\x0c\x12\x0f\n\x07is_burn\x18\x0b \x01(\x08\x12-\n\x0egenesis_reveal\x18\x0c \x01(\x0b\x32\x15.taprpc.GenesisReveal\x12\x30\n\x10group_key_reveal\x18\r \x01(\x0b\x32\x16.taprpc.GroupKeyReveal\"Q\n\x13VerifyProofResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12+\n\rdecoded_proof\x18\x02 \x01(\x0b\x32\x14.taprpc.DecodedProof\"v\n\x12\x44\x65\x63odeProofRequest\x12\x11\n\traw_proof\x18\x01 \x01(\x0c\x12\x16\n\x0eproof_at_depth\x18\x02 \x01(\r\x12\x1b\n\x13with_prev_witnesses\x18\x03 \x01(\x08\x12\x18\n\x10with_meta_reveal\x18\x04 \x01(\x08\"B\n\x13\x44\x65\x63odeProofResponse\x12+\n\rdecoded_proof\x18\x01 \x01(\x0b\x32\x14.taprpc.DecodedProof\":\n\x12\x45xportProofRequest\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\x0c\x12\x12\n\nscript_key\x18\x02 \x01(\x0c\"\xe5\x01\n\tAddrEvent\x12\"\n\x1a\x63reation_time_unix_seconds\x18\x01 \x01(\x04\x12\x1a\n\x04\x61\x64\x64r\x18\x02 \x01(\x0b\x32\x0c.taprpc.Addr\x12\'\n\x06status\x18\x03 \x01(\x0e\x32\x17.taprpc.AddrEventStatus\x12\x10\n\x08outpoint\x18\x04 \x01(\t\x12\x14\n\x0cutxo_amt_sat\x18\x05 \x01(\x04\x12\x17\n\x0ftaproot_sibling\x18\x06 \x01(\x0c\x12\x1b\n\x13\x63onfirmation_height\x18\x07 \x01(\r\x12\x11\n\thas_proof\x18\x08 \x01(\x08\"Z\n\x13\x41\x64\x64rReceivesRequest\x12\x13\n\x0b\x66ilter_addr\x18\x01 \x01(\t\x12.\n\rfilter_status\x18\x02 \x01(\x0e\x32\x17.taprpc.AddrEventStatus\"9\n\x14\x41\x64\x64rReceivesResponse\x12!\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x11.taprpc.AddrEvent\"7\n\x10SendAssetRequest\x12\x11\n\ttap_addrs\x18\x01 \x03(\t\x12\x10\n\x08\x66\x65\x65_rate\x18\x02 \x01(\r\"\\\n\x0ePrevInputAsset\x12\x14\n\x0c\x61nchor_point\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\x0c\x12\x12\n\nscript_key\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\"<\n\x11SendAssetResponse\x12\'\n\x08transfer\x18\x01 \x01(\x0b\x32\x15.taprpc.AssetTransfer\"\x10\n\x0eGetInfoRequest\"\xba\x01\n\x0fGetInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0blnd_version\x18\x02 \x01(\t\x12\x0f\n\x07network\x18\x03 \x01(\t\x12\x1b\n\x13lnd_identity_pubkey\x18\x04 \x01(\t\x12\x12\n\nnode_alias\x18\x05 \x01(\t\x12\x14\n\x0c\x62lock_height\x18\x06 \x01(\r\x12\x12\n\nblock_hash\x18\x07 \x01(\t\x12\x15\n\rsync_to_chain\x18\x08 \x01(\x08\"%\n#SubscribeSendAssetEventNtfnsRequest\"\xb0\x01\n\x0eSendAssetEvent\x12\x41\n\x18\x65xecute_send_state_event\x18\x01 \x01(\x0b\x32\x1d.taprpc.ExecuteSendStateEventH\x00\x12R\n!proof_transfer_backoff_wait_event\x18\x02 \x01(\x0b\x32%.taprpc.ProofTransferBackoffWaitEventH\x00\x42\x07\n\x05\x65vent\">\n\x15\x45xecuteSendStateEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x12\n\nsend_state\x18\x02 \x01(\t\"\x8c\x01\n\x1dProofTransferBackoffWaitEvent\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0f\n\x07\x62\x61\x63koff\x18\x02 \x01(\x03\x12\x15\n\rtries_counter\x18\x03 \x01(\x03\x12\x30\n\rtransfer_type\x18\x04 \x01(\x0e\x32\x19.taprpc.ProofTransferType\"(\n&SubscribeReceiveAssetEventNtfnsRequest\"p\n\x11ReceiveAssetEvent\x12R\n!proof_transfer_backoff_wait_event\x18\x01 \x01(\x0b\x32%.taprpc.ProofTransferBackoffWaitEventH\x00\x42\x07\n\x05\x65vent\"z\n\x15\x46\x65tchAssetMetaRequest\x12\x12\n\x08\x61sset_id\x18\x01 \x01(\x0cH\x00\x12\x13\n\tmeta_hash\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0c\x61sset_id_str\x18\x03 \x01(\tH\x00\x12\x17\n\rmeta_hash_str\x18\x04 \x01(\tH\x00\x42\x07\n\x05\x61sset\"z\n\x10\x42urnAssetRequest\x12\x12\n\x08\x61sset_id\x18\x01 \x01(\x0cH\x00\x12\x16\n\x0c\x61sset_id_str\x18\x02 \x01(\tH\x00\x12\x16\n\x0e\x61mount_to_burn\x18\x03 \x01(\x04\x12\x19\n\x11\x63onfirmation_text\x18\x04 \x01(\tB\x07\n\x05\x61sset\"k\n\x11\x42urnAssetResponse\x12,\n\rburn_transfer\x18\x01 \x01(\x0b\x32\x15.taprpc.AssetTransfer\x12(\n\nburn_proof\x18\x02 \x01(\x0b\x32\x14.taprpc.DecodedProof*(\n\tAssetType\x12\n\n\x06NORMAL\x10\x00\x12\x0f\n\x0b\x43OLLECTIBLE\x10\x01*%\n\rAssetMetaType\x12\x14\n\x10META_TYPE_OPAQUE\x10\x00*:\n\x0c\x41ssetVersion\x12\x14\n\x10\x41SSET_VERSION_V0\x10\x00\x12\x14\n\x10\x41SSET_VERSION_V1\x10\x01*\xb0\x01\n\nOutputType\x12\x16\n\x12OUTPUT_TYPE_SIMPLE\x10\x00\x12\x1a\n\x16OUTPUT_TYPE_SPLIT_ROOT\x10\x01\x12#\n\x1fOUTPUT_TYPE_PASSIVE_ASSETS_ONLY\x10\x02\x12\"\n\x1eOUTPUT_TYPE_PASSIVE_SPLIT_ROOT\x10\x03\x12%\n!OUTPUT_TYPE_SIMPLE_PASSIVE_ASSETS\x10\x04*\xd0\x01\n\x0f\x41\x64\x64rEventStatus\x12\x1d\n\x19\x41\x44\x44R_EVENT_STATUS_UNKNOWN\x10\x00\x12*\n&ADDR_EVENT_STATUS_TRANSACTION_DETECTED\x10\x01\x12+\n\'ADDR_EVENT_STATUS_TRANSACTION_CONFIRMED\x10\x02\x12$\n ADDR_EVENT_STATUS_PROOF_RECEIVED\x10\x03\x12\x1f\n\x1b\x41\x44\x44R_EVENT_STATUS_COMPLETED\x10\x04*R\n\x11ProofTransferType\x12\x1c\n\x18PROOF_TRANSFER_TYPE_SEND\x10\x00\x12\x1f\n\x1bPROOF_TRANSFER_TYPE_RECEIVE\x10\x01\x32\x86\x0b\n\rTaprootAssets\x12\x41\n\nListAssets\x12\x18.taprpc.ListAssetRequest\x1a\x19.taprpc.ListAssetResponse\x12@\n\tListUtxos\x12\x18.taprpc.ListUtxosRequest\x1a\x19.taprpc.ListUtxosResponse\x12\x43\n\nListGroups\x12\x19.taprpc.ListGroupsRequest\x1a\x1a.taprpc.ListGroupsResponse\x12I\n\x0cListBalances\x12\x1b.taprpc.ListBalancesRequest\x1a\x1c.taprpc.ListBalancesResponse\x12L\n\rListTransfers\x12\x1c.taprpc.ListTransfersRequest\x1a\x1d.taprpc.ListTransfersResponse\x12\x37\n\nStopDaemon\x12\x13.taprpc.StopRequest\x1a\x14.taprpc.StopResponse\x12\x43\n\nDebugLevel\x12\x19.taprpc.DebugLevelRequest\x1a\x1a.taprpc.DebugLevelResponse\x12\x41\n\nQueryAddrs\x12\x18.taprpc.QueryAddrRequest\x1a\x19.taprpc.QueryAddrResponse\x12/\n\x07NewAddr\x12\x16.taprpc.NewAddrRequest\x1a\x0c.taprpc.Addr\x12\x35\n\nDecodeAddr\x12\x19.taprpc.DecodeAddrRequest\x1a\x0c.taprpc.Addr\x12I\n\x0c\x41\x64\x64rReceives\x12\x1b.taprpc.AddrReceivesRequest\x1a\x1c.taprpc.AddrReceivesResponse\x12=\n\x0bVerifyProof\x12\x11.taprpc.ProofFile\x1a\x1b.taprpc.VerifyProofResponse\x12\x46\n\x0b\x44\x65\x63odeProof\x12\x1a.taprpc.DecodeProofRequest\x1a\x1b.taprpc.DecodeProofResponse\x12<\n\x0b\x45xportProof\x12\x1a.taprpc.ExportProofRequest\x1a\x11.taprpc.ProofFile\x12@\n\tSendAsset\x12\x18.taprpc.SendAssetRequest\x1a\x19.taprpc.SendAssetResponse\x12@\n\tBurnAsset\x12\x18.taprpc.BurnAssetRequest\x1a\x19.taprpc.BurnAssetResponse\x12:\n\x07GetInfo\x12\x16.taprpc.GetInfoRequest\x1a\x17.taprpc.GetInfoResponse\x12\x65\n\x1cSubscribeSendAssetEventNtfns\x12+.taprpc.SubscribeSendAssetEventNtfnsRequest\x1a\x16.taprpc.SendAssetEvent0\x01\x12n\n\x1fSubscribeReceiveAssetEventNtfns\x12..taprpc.SubscribeReceiveAssetEventNtfnsRequest\x1a\x19.taprpc.ReceiveAssetEvent0\x01\x12\x42\n\x0e\x46\x65tchAssetMeta\x12\x1d.taprpc.FetchAssetMetaRequest\x1a\x11.taprpc.AssetMetaB0Z.github.com/lightninglabs/taproot-assets/taprpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'taprootassets_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/lightninglabs/taproot-assets/taprpc'
  _LISTUTXOSRESPONSE_MANAGEDUTXOSENTRY._options = None
  _LISTUTXOSRESPONSE_MANAGEDUTXOSENTRY._serialized_options = b'8\001'
  _LISTGROUPSRESPONSE_GROUPSENTRY._options = None
  _LISTGROUPSRESPONSE_GROUPSENTRY._serialized_options = b'8\001'
  _LISTBALANCESRESPONSE_ASSETBALANCESENTRY._options = None
  _LISTBALANCESRESPONSE_ASSETBALANCESENTRY._serialized_options = b'8\001'
  _LISTBALANCESRESPONSE_ASSETGROUPBALANCESENTRY._options = None
  _LISTBALANCESRESPONSE_ASSETGROUPBALANCESENTRY._serialized_options = b'8\001'
  _globals['_ASSETTYPE']._serialized_start=7281
  _globals['_ASSETTYPE']._serialized_end=7321
  _globals['_ASSETMETATYPE']._serialized_start=7323
  _globals['_ASSETMETATYPE']._serialized_end=7360
  _globals['_ASSETVERSION']._serialized_start=7362
  _globals['_ASSETVERSION']._serialized_end=7420
  _globals['_OUTPUTTYPE']._serialized_start=7423
  _globals['_OUTPUTTYPE']._serialized_end=7599
  _globals['_ADDREVENTSTATUS']._serialized_start=7602
  _globals['_ADDREVENTSTATUS']._serialized_end=7810
  _globals['_PROOFTRANSFERTYPE']._serialized_start=7812
  _globals['_PROOFTRANSFERTYPE']._serialized_end=7894
  _globals['_ASSETMETA']._serialized_start=31
  _globals['_ASSETMETA']._serialized_end=112
  _globals['_LISTASSETREQUEST']._serialized_start=114
  _globals['_LISTASSETREQUEST']._serialized_end=201
  _globals['_ANCHORINFO']._serialized_start=204
  _globals['_ANCHORINFO']._serialized_end=379
  _globals['_GENESISINFO']._serialized_start=382
  _globals['_GENESISINFO']._serialized_end=547
  _globals['_ASSETGROUP']._serialized_start=549
  _globals['_ASSETGROUP']._serialized_end=634
  _globals['_GROUPKEYREVEAL']._serialized_start=636
  _globals['_GROUPKEYREVEAL']._serialized_end=699
  _globals['_GENESISREVEAL']._serialized_start=701
  _globals['_GENESISREVEAL']._serialized_end=766
  _globals['_ASSET']._serialized_start=769
  _globals['_ASSET']._serialized_end=1201
  _globals['_PREVWITNESS']._serialized_start=1203
  _globals['_PREVWITNESS']._serialized_end=1328
  _globals['_SPLITCOMMITMENT']._serialized_start=1330
  _globals['_SPLITCOMMITMENT']._serialized_end=1382
  _globals['_LISTASSETRESPONSE']._serialized_start=1384
  _globals['_LISTASSETRESPONSE']._serialized_end=1434
  _globals['_LISTUTXOSREQUEST']._serialized_start=1436
  _globals['_LISTUTXOSREQUEST']._serialized_end=1478
  _globals['_MANAGEDUTXO']._serialized_start=1481
  _globals['_MANAGEDUTXO']._serialized_end=1632
  _globals['_LISTUTXOSRESPONSE']._serialized_start=1635
  _globals['_LISTUTXOSRESPONSE']._serialized_end=1796
  _globals['_LISTUTXOSRESPONSE_MANAGEDUTXOSENTRY']._serialized_start=1724
  _globals['_LISTUTXOSRESPONSE_MANAGEDUTXOSENTRY']._serialized_end=1796
  _globals['_LISTGROUPSREQUEST']._serialized_start=1798
  _globals['_LISTGROUPSREQUEST']._serialized_end=1817
  _globals['_ASSETHUMANREADABLE']._serialized_start=1820
  _globals['_ASSETHUMANREADABLE']._serialized_end=2019
  _globals['_GROUPEDASSETS']._serialized_start=2021
  _globals['_GROUPEDASSETS']._serialized_end=2080
  _globals['_LISTGROUPSRESPONSE']._serialized_start=2083
  _globals['_LISTGROUPSRESPONSE']._serialized_end=2229
  _globals['_LISTGROUPSRESPONSE_GROUPSENTRY']._serialized_start=2161
  _globals['_LISTGROUPSRESPONSE_GROUPSENTRY']._serialized_end=2229
  _globals['_LISTBALANCESREQUEST']._serialized_start=2231
  _globals['_LISTBALANCESREQUEST']._serialized_end=2353
  _globals['_ASSETBALANCE']._serialized_start=2355
  _globals['_ASSETBALANCE']._serialized_end=2430
  _globals['_ASSETGROUPBALANCE']._serialized_start=2432
  _globals['_ASSETGROUPBALANCE']._serialized_end=2487
  _globals['_LISTBALANCESRESPONSE']._serialized_start=2490
  _globals['_LISTBALANCESRESPONSE']._serialized_end=2831
  _globals['_LISTBALANCESRESPONSE_ASSETBALANCESENTRY']._serialized_start=2671
  _globals['_LISTBALANCESRESPONSE_ASSETBALANCESENTRY']._serialized_end=2745
  _globals['_LISTBALANCESRESPONSE_ASSETGROUPBALANCESENTRY']._serialized_start=2747
  _globals['_LISTBALANCESRESPONSE_ASSETGROUPBALANCESENTRY']._serialized_end=2831
  _globals['_LISTTRANSFERSREQUEST']._serialized_start=2833
  _globals['_LISTTRANSFERSREQUEST']._serialized_end=2855
  _globals['_LISTTRANSFERSRESPONSE']._serialized_start=2857
  _globals['_LISTTRANSFERSRESPONSE']._serialized_end=2922
  _globals['_ASSETTRANSFER']._serialized_start=2925
  _globals['_ASSETTRANSFER']._serialized_end=3133
  _globals['_TRANSFERINPUT']._serialized_start=3135
  _globals['_TRANSFERINPUT']._serialized_end=3226
  _globals['_TRANSFEROUTPUTANCHOR']._serialized_start=3229
  _globals['_TRANSFEROUTPUTANCHOR']._serialized_end=3410
  _globals['_TRANSFEROUTPUT']._serialized_start=3413
  _globals['_TRANSFEROUTPUT']._serialized_end=3682
  _globals['_STOPREQUEST']._serialized_start=3684
  _globals['_STOPREQUEST']._serialized_end=3697
  _globals['_STOPRESPONSE']._serialized_start=3699
  _globals['_STOPRESPONSE']._serialized_end=3713
  _globals['_DEBUGLEVELREQUEST']._serialized_start=3715
  _globals['_DEBUGLEVELREQUEST']._serialized_end=3768
  _globals['_DEBUGLEVELRESPONSE']._serialized_start=3770
  _globals['_DEBUGLEVELRESPONSE']._serialized_end=3811
  _globals['_ADDR']._serialized_start=3814
  _globals['_ADDR']._serialized_end=4099
  _globals['_QUERYADDRREQUEST']._serialized_start=4101
  _globals['_QUERYADDRREQUEST']._serialized_end=4197
  _globals['_QUERYADDRRESPONSE']._serialized_start=4199
  _globals['_QUERYADDRRESPONSE']._serialized_end=4247
  _globals['_NEWADDRREQUEST']._serialized_start=4250
  _globals['_NEWADDRREQUEST']._serialized_end=4481
  _globals['_SCRIPTKEY']._serialized_start=4483
  _globals['_SCRIPTKEY']._serialized_end=4571
  _globals['_KEYLOCATOR']._serialized_start=4573
  _globals['_KEYLOCATOR']._serialized_end=4624
  _globals['_KEYDESCRIPTOR']._serialized_start=4626
  _globals['_KEYDESCRIPTOR']._serialized_end=4701
  _globals['_DECODEADDRREQUEST']._serialized_start=4703
  _globals['_DECODEADDRREQUEST']._serialized_end=4736
  _globals['_PROOFFILE']._serialized_start=4738
  _globals['_PROOFFILE']._serialized_end=4796
  _globals['_DECODEDPROOF']._serialized_start=4799
  _globals['_DECODEDPROOF']._serialized_end=5207
  _globals['_VERIFYPROOFRESPONSE']._serialized_start=5209
  _globals['_VERIFYPROOFRESPONSE']._serialized_end=5290
  _globals['_DECODEPROOFREQUEST']._serialized_start=5292
  _globals['_DECODEPROOFREQUEST']._serialized_end=5410
  _globals['_DECODEPROOFRESPONSE']._serialized_start=5412
  _globals['_DECODEPROOFRESPONSE']._serialized_end=5478
  _globals['_EXPORTPROOFREQUEST']._serialized_start=5480
  _globals['_EXPORTPROOFREQUEST']._serialized_end=5538
  _globals['_ADDREVENT']._serialized_start=5541
  _globals['_ADDREVENT']._serialized_end=5770
  _globals['_ADDRRECEIVESREQUEST']._serialized_start=5772
  _globals['_ADDRRECEIVESREQUEST']._serialized_end=5862
  _globals['_ADDRRECEIVESRESPONSE']._serialized_start=5864
  _globals['_ADDRRECEIVESRESPONSE']._serialized_end=5921
  _globals['_SENDASSETREQUEST']._serialized_start=5923
  _globals['_SENDASSETREQUEST']._serialized_end=5978
  _globals['_PREVINPUTASSET']._serialized_start=5980
  _globals['_PREVINPUTASSET']._serialized_end=6072
  _globals['_SENDASSETRESPONSE']._serialized_start=6074
  _globals['_SENDASSETRESPONSE']._serialized_end=6134
  _globals['_GETINFOREQUEST']._serialized_start=6136
  _globals['_GETINFOREQUEST']._serialized_end=6152
  _globals['_GETINFORESPONSE']._serialized_start=6155
  _globals['_GETINFORESPONSE']._serialized_end=6341
  _globals['_SUBSCRIBESENDASSETEVENTNTFNSREQUEST']._serialized_start=6343
  _globals['_SUBSCRIBESENDASSETEVENTNTFNSREQUEST']._serialized_end=6380
  _globals['_SENDASSETEVENT']._serialized_start=6383
  _globals['_SENDASSETEVENT']._serialized_end=6559
  _globals['_EXECUTESENDSTATEEVENT']._serialized_start=6561
  _globals['_EXECUTESENDSTATEEVENT']._serialized_end=6623
  _globals['_PROOFTRANSFERBACKOFFWAITEVENT']._serialized_start=6626
  _globals['_PROOFTRANSFERBACKOFFWAITEVENT']._serialized_end=6766
  _globals['_SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST']._serialized_start=6768
  _globals['_SUBSCRIBERECEIVEASSETEVENTNTFNSREQUEST']._serialized_end=6808
  _globals['_RECEIVEASSETEVENT']._serialized_start=6810
  _globals['_RECEIVEASSETEVENT']._serialized_end=6922
  _globals['_FETCHASSETMETAREQUEST']._serialized_start=6924
  _globals['_FETCHASSETMETAREQUEST']._serialized_end=7046
  _globals['_BURNASSETREQUEST']._serialized_start=7048
  _globals['_BURNASSETREQUEST']._serialized_end=7170
  _globals['_BURNASSETRESPONSE']._serialized_start=7172
  _globals['_BURNASSETRESPONSE']._serialized_end=7279
  _globals['_TAPROOTASSETS']._serialized_start=7897
  _globals['_TAPROOTASSETS']._serialized_end=9311
# @@protoc_insertion_point(module_scope)

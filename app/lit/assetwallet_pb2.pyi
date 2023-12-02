"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
from . import taprootassets_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FundVirtualPsbtRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PSBT_FIELD_NUMBER: builtins.int
    RAW_FIELD_NUMBER: builtins.int
    psbt: builtins.bytes
    """
    Use an existing PSBT packet as the template for the funded PSBT.

    TODO(guggero): Actually implement this. We can't use the "reserved"
    keyword here because we're in a oneof, so we add the field but implement
    it later.
    """
    @property
    def raw(self) -> global___TxTemplate:
        """
        Use the asset outputs and optional asset inputs from this raw template.
        """
    def __init__(
        self,
        *,
        psbt: builtins.bytes = ...,
        raw: global___TxTemplate | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["psbt", b"psbt", "raw", b"raw", "template", b"template"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["psbt", b"psbt", "raw", b"raw", "template", b"template"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["template", b"template"]) -> typing_extensions.Literal["psbt", "raw"] | None: ...

global___FundVirtualPsbtRequest = FundVirtualPsbtRequest

@typing_extensions.final
class FundVirtualPsbtResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNDED_PSBT_FIELD_NUMBER: builtins.int
    CHANGE_OUTPUT_INDEX_FIELD_NUMBER: builtins.int
    funded_psbt: builtins.bytes
    """
    The funded but not yet signed PSBT packet.
    """
    change_output_index: builtins.int
    """
    The index of the added change output or -1 if no change was left over.
    """
    def __init__(
        self,
        *,
        funded_psbt: builtins.bytes = ...,
        change_output_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["change_output_index", b"change_output_index", "funded_psbt", b"funded_psbt"]) -> None: ...

global___FundVirtualPsbtResponse = FundVirtualPsbtResponse

@typing_extensions.final
class TxTemplate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class RecipientsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    INPUTS_FIELD_NUMBER: builtins.int
    RECIPIENTS_FIELD_NUMBER: builtins.int
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PrevId]:
        """
        An optional list of inputs to use. Every input must be an asset UTXO known
        to the wallet. The sum of all inputs must be greater than or equal to the
        sum of all outputs.

        If no inputs are specified, asset coin selection will be performed instead
        and inputs of sufficient value will be added to the resulting PSBT.
        """
    @property
    def recipients(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """
        A map of all Taproot Asset addresses mapped to the anchor transaction's
        output index that should be sent to.
        """
    def __init__(
        self,
        *,
        inputs: collections.abc.Iterable[global___PrevId] | None = ...,
        recipients: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["inputs", b"inputs", "recipients", b"recipients"]) -> None: ...

global___TxTemplate = TxTemplate

@typing_extensions.final
class PrevId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPOINT_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    SCRIPT_KEY_FIELD_NUMBER: builtins.int
    @property
    def outpoint(self) -> global___OutPoint:
        """
        The bitcoin anchor output on chain that contains the input asset.
        """
    id: builtins.bytes
    """
    The asset ID of the previous asset tree.
    """
    script_key: builtins.bytes
    """
    The tweaked Taproot output key committing to the possible spending
    conditions of the asset.
    """
    def __init__(
        self,
        *,
        outpoint: global___OutPoint | None = ...,
        id: builtins.bytes = ...,
        script_key: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["outpoint", b"outpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "outpoint", b"outpoint", "script_key", b"script_key"]) -> None: ...

global___PrevId = PrevId

@typing_extensions.final
class OutPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TXID_FIELD_NUMBER: builtins.int
    OUTPUT_INDEX_FIELD_NUMBER: builtins.int
    txid: builtins.bytes
    """
    Raw bytes representing the transaction id.
    """
    output_index: builtins.int
    """
    The index of the output on the transaction.
    """
    def __init__(
        self,
        *,
        txid: builtins.bytes = ...,
        output_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["output_index", b"output_index", "txid", b"txid"]) -> None: ...

global___OutPoint = OutPoint

@typing_extensions.final
class SignVirtualPsbtRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNDED_PSBT_FIELD_NUMBER: builtins.int
    funded_psbt: builtins.bytes
    """
    The PSBT of the virtual transaction that should be signed. The PSBT must
    contain all required inputs, outputs, UTXO data and custom fields required
    to identify the signing key.
    """
    def __init__(
        self,
        *,
        funded_psbt: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["funded_psbt", b"funded_psbt"]) -> None: ...

global___SignVirtualPsbtRequest = SignVirtualPsbtRequest

@typing_extensions.final
class SignVirtualPsbtResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIGNED_PSBT_FIELD_NUMBER: builtins.int
    SIGNED_INPUTS_FIELD_NUMBER: builtins.int
    signed_psbt: builtins.bytes
    """
    The signed virtual transaction in PSBT format.
    """
    @property
    def signed_inputs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """
        The indices of signed inputs.
        """
    def __init__(
        self,
        *,
        signed_psbt: builtins.bytes = ...,
        signed_inputs: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["signed_inputs", b"signed_inputs", "signed_psbt", b"signed_psbt"]) -> None: ...

global___SignVirtualPsbtResponse = SignVirtualPsbtResponse

@typing_extensions.final
class AnchorVirtualPsbtsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_PSBTS_FIELD_NUMBER: builtins.int
    @property
    def virtual_psbts(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """
        The list of virtual transactions that should be merged and committed to in
        the BTC level anchor transaction.
        """
    def __init__(
        self,
        *,
        virtual_psbts: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["virtual_psbts", b"virtual_psbts"]) -> None: ...

global___AnchorVirtualPsbtsRequest = AnchorVirtualPsbtsRequest

@typing_extensions.final
class NextInternalKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FAMILY_FIELD_NUMBER: builtins.int
    key_family: builtins.int
    def __init__(
        self,
        *,
        key_family: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_family", b"key_family"]) -> None: ...

global___NextInternalKeyRequest = NextInternalKeyRequest

@typing_extensions.final
class NextInternalKeyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERNAL_KEY_FIELD_NUMBER: builtins.int
    @property
    def internal_key(self) -> taprootassets_pb2.KeyDescriptor: ...
    def __init__(
        self,
        *,
        internal_key: taprootassets_pb2.KeyDescriptor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["internal_key", b"internal_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["internal_key", b"internal_key"]) -> None: ...

global___NextInternalKeyResponse = NextInternalKeyResponse

@typing_extensions.final
class NextScriptKeyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FAMILY_FIELD_NUMBER: builtins.int
    key_family: builtins.int
    def __init__(
        self,
        *,
        key_family: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key_family", b"key_family"]) -> None: ...

global___NextScriptKeyRequest = NextScriptKeyRequest

@typing_extensions.final
class NextScriptKeyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCRIPT_KEY_FIELD_NUMBER: builtins.int
    @property
    def script_key(self) -> taprootassets_pb2.ScriptKey: ...
    def __init__(
        self,
        *,
        script_key: taprootassets_pb2.ScriptKey | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["script_key", b"script_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["script_key", b"script_key"]) -> None: ...

global___NextScriptKeyResponse = NextScriptKeyResponse

@typing_extensions.final
class ProveAssetOwnershipRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSET_ID_FIELD_NUMBER: builtins.int
    SCRIPT_KEY_FIELD_NUMBER: builtins.int
    asset_id: builtins.bytes
    script_key: builtins.bytes
    def __init__(
        self,
        *,
        asset_id: builtins.bytes = ...,
        script_key: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_id", b"asset_id", "script_key", b"script_key"]) -> None: ...

global___ProveAssetOwnershipRequest = ProveAssetOwnershipRequest

@typing_extensions.final
class ProveAssetOwnershipResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROOF_WITH_WITNESS_FIELD_NUMBER: builtins.int
    proof_with_witness: builtins.bytes
    def __init__(
        self,
        *,
        proof_with_witness: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proof_with_witness", b"proof_with_witness"]) -> None: ...

global___ProveAssetOwnershipResponse = ProveAssetOwnershipResponse

@typing_extensions.final
class VerifyAssetOwnershipRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROOF_WITH_WITNESS_FIELD_NUMBER: builtins.int
    proof_with_witness: builtins.bytes
    def __init__(
        self,
        *,
        proof_with_witness: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["proof_with_witness", b"proof_with_witness"]) -> None: ...

global___VerifyAssetOwnershipRequest = VerifyAssetOwnershipRequest

@typing_extensions.final
class VerifyAssetOwnershipResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALID_PROOF_FIELD_NUMBER: builtins.int
    valid_proof: builtins.bool
    def __init__(
        self,
        *,
        valid_proof: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["valid_proof", b"valid_proof"]) -> None: ...

global___VerifyAssetOwnershipResponse = VerifyAssetOwnershipResponse

@typing_extensions.final
class RemoveUTXOLeaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPOINT_FIELD_NUMBER: builtins.int
    @property
    def outpoint(self) -> global___OutPoint:
        """The outpoint of the UTXO to remove the lease for."""
    def __init__(
        self,
        *,
        outpoint: global___OutPoint | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["outpoint", b"outpoint"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["outpoint", b"outpoint"]) -> None: ...

global___RemoveUTXOLeaseRequest = RemoveUTXOLeaseRequest

@typing_extensions.final
class RemoveUTXOLeaseResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RemoveUTXOLeaseResponse = RemoveUTXOLeaseResponse

"""
0: type: str: 4bytesmax
1: enc-mode: int: 0, 1, 2 (0=plaintext, 1=asymmetic, 2=symmetric).
2. Timestamp: int
encrypted with specified mode:
 3. signer: bytes (max 256bits)
 4. signature: bytes (max 256bits)
 5. app_metadata: JSON
\n
data: bytes

"""
from msgpack import packb

from .. import exceptions


def pack(data: bytes, data_type: 'KastenDataType',
         enc_mode: 'KastenEncryptionModeID',
         signer: bytes = None, signature: bytes = None,
         app_metadata: 'KastenSerializeableDict' = None) -> 'PreparedKasten':

    # Ensure data type does not exceed 4 characters
    if not data_type or len(data_type) > 4:
        raise exceptions.InvalidKastenTypeLength

    # Ensure encryption mode is valid (asymmetric, symmetric, plaintext)
    enc_mode = int(enc_mode)
    if enc_mode not in range(3):
        raise
    try:
        data = data.encode('utf8')
    except AttributeError:
        pass

    kasten_header = [data_type, enc_mode]
    if signer:
        if signature is None:
            raise ValueError("Signer specified without signature")
        kasten_header.extend((signer, signature))
    if app_metadata is not None:
        kasten_header.append(app_metadata)

    kasten_header = packb(kasten_header) + packb(b'\n')

    return kasten_header + data

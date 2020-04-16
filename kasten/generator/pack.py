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
from math import floor
from time import time

from msgpack import packb

from kasten import exceptions

from kasten.types import KastenPacked


def pack(data: bytes, data_type: 'KastenDataType',
         enc_mode: 'KastenEncryptionModeID',
         signer: bytes = None, signature: bytes = None,
         app_metadata: 'KastenSerializeableDict' = None,
         timestamp: int = None
         ) ->  KastenPacked:

    # Ensure data type does not exceed 4 characters
    if not data_type or len(data_type) > 4:
        raise exceptions.InvalidKastenTypeLength

    # Ensure encryption mode is in [0, 100)
    try:
        enc_mode = int(enc_mode)
    except (TypeError, ValueError):
        raise exceptions.InvalidEncryptionMode
    if not enc_mode >= 0 or enc_mode >= 100:
        raise exceptions.InvalidEncryptionMode

    try:
        data = data.encode('utf8')
    except AttributeError:
        pass
    if timestamp is None:
        timestamp = floor(time())
    timestamp = int(timestamp)

    kasten_header = [data_type, enc_mode, timestamp]
    if signer:
        if signature is None:
            raise ValueError("Signer specified without signature")
        kasten_header.extend((signer, signature))
    if app_metadata is not None:
        kasten_header.append(app_metadata)

    kasten_header = packb(kasten_header) + b'\n'
    print(kasten_header + data)
    return kasten_header + data

from typing import Tuple
from typing import NewType
from typing import NamedTuple

KastenDataType = NewType('KastenDataType', str)

class KastenDataType(str):

    pass


class KastenPacked(bytes):
    """Raw Kasten bytes that have not yet been passed through a KastenGenerator"""


class KastenChecksum(bytes):
    """hash or checksum of a Kasten object"""


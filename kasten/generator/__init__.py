from kasten.types import KastenPacked
from kasten.types import KastenChecksum
from kasten.exceptions import InvalidID

from hashlib import sha3_384
from ..main import Kasten


class KastenBaseGenerator:
    @classmethod
    def generate(cls, packed_bytes: KastenPacked) -> Kasten:
        return Kasten(sha3_384(packed_bytes).digest(), packed_bytes, cls,
                      auto_check_generator=False)

    @staticmethod
    def validate_id(hash: KastenChecksum, packed_bytes: KastenPacked) -> None:
        if not sha3_384(packed_bytes).digest() == hash:
            raise InvalidID
        return None
from .types import KastenChecksum
from .types import KastenPacked


class Kasten:
    def __init__(self, id: KastenChecksum,
                 packed_bytes: KastenPacked,
                 generator: 'KastenBaseGenerator',
                 auto_check_generator = False):  # noqa
        if auto_check_generator:
            generator.validate_id(id, packed_bytes)
        self.id = id
        self.packed_bytes = packed_bytes
        self.generator = generator

    def check_generator(self):
        self.generator.validate_id(self.id, self.packed_bytes)

from msgpack import unpackb

from .types import KastenChecksum
from .types import KastenPacked
from .generator import pack


class Kasten:
    def __init__(self, id: KastenChecksum,
                 packed_bytes: KastenPacked,
                 generator: 'KastenBaseGenerator',
                 auto_check_generator = True):  # noqa
        if auto_check_generator:
            generator.validate_id(id, packed_bytes)
        self.id = id
        self.generator = generator
        header, data = packed_bytes.split(b'\n', 1)
        header = unpackb(header, strict_map_key=True)
        self.header = header
        self.data = data

    def check_generator(self, generator=None):
        packed = self.get_packed()
        if generator is None:
            self.generator.validate_id(self.id, self.packed_bytes)
        else:
            generator(self.id, self.packed_bytes)

    # Getters are gross, but they are used here to preserve space

    def get_packed(self) -> KastenPacked:
        return pack.pack(self.data, self.get_data_type(),
                         self.get_encryption_mode(),
                         timestamp=self.get_timestamp())

    def get_data_type(self) -> str: return self.header[0]

    def get_encryption_mode(self): return self.header[1]

    def get_timestamp(self): return self.header[2]

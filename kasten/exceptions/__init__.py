class KastenException(Exception):
    pass


class InvalidKastenTypeLength(KastenException):
    pass

class InvalidEncryptionMode(KastenException):
    pass
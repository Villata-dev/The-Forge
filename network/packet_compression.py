import zlib
class PayloadCompressor:
    def compress_state(self, byte_data): return zlib.compress(byte_data)

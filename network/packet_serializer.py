import struct
class Serializer:
    def pack_position(self, x, y): return struct.pack('!ff', x, y)

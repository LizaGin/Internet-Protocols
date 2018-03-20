import struct


class Packet:
    def __init__(self, version_number=3, mode=3, stratum=0, poll=0, reference_t=0, receive_t=0, transmit_t=0):
        self.leap_indicator = 0
        self.version_number = version_number
        self.mode = mode
        self.stratum = stratum
        self.poll = poll
        self.precision = 0
        self.root_delay = 0
        self.root_dispersion = 0
        self.reference_identifier = 0
        self.reference_timestamp = reference_t
        self.originate_timestamp = 0
        self.receive_timestamp = receive_t
        self.transmit_timestamp = transmit_t

    def unpack(self, data):
        packet_format = '!3Bb3I4Q'
        try:
            unpacked_data = struct.unpack(packet_format, data[0:struct.calcsize(packet_format)])
            print(unpacked_data)
            first_byte = bin(unpacked_data[0])[2:].rjust(8, '0')
            self.leap_indicator = int(first_byte[:2], 2)
            self.version_number = int(first_byte[2:5], 2)
            self.mode = int(first_byte[5:], 2)
            self.stratum = unpacked_data[1]
            self.poll = unpacked_data[2]
            self.precision = unpacked_data[3]
            self.root_delay = unpacked_data[4]
            self.root_dispersion = unpacked_data[5]
            self.reference_identifier = unpacked_data[6]
            self.reference_timestamp = unpacked_data[7]
            self.originate_timestamp = unpacked_data[8]
            self.receive_timestamp = unpacked_data[9]
            self.transmit_timestamp = unpacked_data[10]
        except Exception:
            print('error: can`t unpack structure')

    def pack(self):
        packet_format = '!3Bb3I4Q'
        try:
            first_byte = int(
                self.to_bytes(self.leap_indicator, 2) + self.to_bytes(self.version_number, 3) + self.to_bytes(self.mode,
                                                                                                              3), 2)
            packed_data = struct.pack(packet_format, first_byte, self.stratum, self.poll, self.precision,
                                      self.root_delay,
                                      self.root_dispersion,
                                      self.reference_identifier, self.reference_timestamp, self.originate_timestamp,
                                      self.receive_timestamp, self.transmit_timestamp)
            return packed_data
        except Exception:
            print('error: can`t pack structure')

    @staticmethod
    def time_to_sntp_format(time):
        begin_unix = 2208988800
        seconds, milli_seconds = str(time + begin_unix).split('.')
        sntp_time = int(seconds) * 2 ** 32
        return sntp_time

    @staticmethod
    def reference_identifier_to_sntp_format(identify):
        id_numbers = identify.split('.')
        l_id = []
        for i in id_numbers:
            l_id.append(str((bin(int(i))))[2:].rjust(8, '0'))
        return int(''.join(l_id), 2)

    @staticmethod
    def to_bytes(number, n):
        return str((bin(number)))[2:].rjust(n, '0')


if __name__ == '__main__':
    """
        packet = Packet()
        packet.unpack(
        b'\x1c\x02\x00\xe9\x00\x00\x1eq\x00\x00\x04H\x80\x8a\x8d\xac\xdeM\x1c\x13\xb8\xa21\xee\x00\x00\x00\x00\x00\x00\x00\x00\xdeM\x1cl\x08\x81Mr\xdeM\x1cl\x08\x81\x86}')
        print(packet.leap_indicator,
          packet.version_number,
          packet.mode,
          packet.stratum,
          packet.poll,
          packet.precision,
          packet.root_delay,
          packet.root_dispersion,
          packet.reference_identifier,
          packet.reference_timestamp,
          packet.originate_timestamp,
          packet.receive_timestamp,
          packet.transmit_timestamp
          )
    """

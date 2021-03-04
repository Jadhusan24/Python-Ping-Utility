import socket
import struct
import random
import sys

ICMP_ECHO_REQUEST = 8
ICMP_STRUCTURE_FMT = '!BBHHH'

class ICMPPacket:
    def __init__(self, icmp_id, data=b'', icmp_type=ICMP_ECHO_REQUEST, icmp_code=0, checksum=0, icmp_seq=1):
        self.icmp_type = icmp_type
        self.icmp_code = icmp_code
        self.checksum = checksum
        self.icmp_id = icmp_id
        self.icmp_seq = icmp_seq
        self.data = data
        self.header = b""
        self.create_icmp_field()

    # creates an icmp field
    def create_icmp_field(self):
        # create a dummy header to create a valid checksum
        self.header = struct.pack(ICMP_STRUCTURE_FMT, self.icmp_type,
                                  self.icmp_code, self.checksum, self.icmp_id, self.icmp_seq)

        # calculate checksum
        self.checksum = self.chksum(self.header + self.data)

        # usable header once a valid checksum is created
        self.header = struct.pack(ICMP_STRUCTURE_FMT, self.icmp_type,
                                  self.icmp_code, self.checksum, self.icmp_id, self.icmp_seq)
        return

    # calculates the checksum for the packet
    def chksum(self, source_string):
        # https://tools.ietf.org/html/rfc1071
        # https://stackoverflow.com/questions/55218931/calculating-checksum-for-icmp-echo-request-in-python
        countTo = (int(len(source_string)/2))*2
        sum = 0
        count = 0

        # Handle bytes in pairs (decoding as short ints)
        loByte = 0
        hiByte = 0
        while count < countTo:
            if (sys.byteorder == "little"):
                loByte = source_string[count]
                hiByte = source_string[count + 1]
            else:
                loByte = source_string[count + 1]
                hiByte = source_string[count]
            try:     # For Python3
                sum = sum + (hiByte * 256 + loByte)
            except:  # For Python2
                sum = sum + (ord(hiByte) * 256 + ord(loByte))
            count += 2

        # Handle last byte if applicable (odd-number of bytes)
        # Endianness should be irrelevant in this case
        if countTo < len(source_string):  # Check for odd length
            loByte = source_string[len(source_string)-1]
            try:      # For Python3
                sum += loByte
            except:   # For Python2
                sum += ord(loByte)

        # Truncate sum to 32 bits (a variance from ping.c, which
        sum &= 0xffffffff
        # uses signed ints, but overflow is unlikely in ping)

        sum = (sum >> 16) + (sum & 0xffff)    # Add high 16 bits to low 16 bits
        sum += (sum >> 16)                    # Add carry from above (if any)
        answer = ~sum & 0xffff                # Invert and truncate to 16 bits
        answer = socket.htons(answer)

        return answer

    # used for visualisation of the packet
    # extract the packet and return a dict
    def extract_icmp_header(self):
        icmph = struct.unpack(ICMP_STRUCTURE_FMT, self.header)
        data = {
            'type':   icmph[0],
            'code':   icmph[1],
            'checksum': icmph[2],
            'id':   icmph[3],
            'seq':   icmph[4],
        }
        return data

    def __str__(self):
        return f"{self.extract_icmp_header()}"

# returns a random ID within the ICMP scope
def generate_id(timeout=2):
    return int((id(timeout) * random.random()) % 65535)
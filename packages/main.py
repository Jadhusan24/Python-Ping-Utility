# import custom classes and variables
from packages.icmp import ICMPPacket, generate_id, ICMP_STRUCTURE_FMT
import socket
import select
import time
import struct

# simple dict containing the socket error keys and their meaning values
# used when there is a permission error
ERROR_DESCR = {
    1: ' - Note that ICMP messages can only be '
       'sent from processes running as root.',
    10013: ' - Note that ICMP messages can only be sent by'
           ' users or processes with administrator rights.'
}

# icmp codes with their meaning
# http://www.rhyshaden.com/icmp.htm
ICMP_ERROR_CODES = {
    0: 'Reply',
    3: 'Destination unreachale',
    5: 'Redirect',
    8: 'Request',
    9: 'Router Advertisement',
    13: 'Timeout exceeded'
}

def receive_ping(sock, packet_id, timeout):
    sock.settimeout(timeout)  # set the timeout for the socket
    try:
        time_received = time.time()  # start time
        # Receive the ping from the socket.
        rec_packet, _ = sock.recvfrom(2048)
        # end time, round to milliseconds
        end = round((time.time() - time_received)*1000.0, 2)

        # unpack the IP header
        ip_header = rec_packet[:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
        # get the ip adddress bytes and convert it to an IP
        src_addr = socket.inet_ntoa(iph[8])
        ttl = iph[5]

        # unpack the icmp header
        icmp_header = rec_packet[20:28]
        icmph = struct.unpack(ICMP_STRUCTURE_FMT, icmp_header)

        # unpack the header in packed form
        icmp_type = icmph[0]
        icmp_pid = icmph[3]
        icmp_seq = icmph[4]

        # if the recieved packet is the same as the packet we're listening for
        if icmp_pid == packet_id:
            # for more types check the ICMP_ERROR_CODES dict above
            if icmp_type == 0:
                # print response
                delay = round(end, 2)
                print(
                    f"Reply from {src_addr} : icmp_seq={icmp_seq} ttl={ttl} time={delay} ms")
    except socket.timeout:
        print(f"Timeout exceeded {timeout} ms")
        return
    except KeyboardInterrupt:
        exit()

def do_one(dst: str, icmp_packet: ICMPPacket, timeout=2):
    ICMP_CODE = socket.getprotobyname('icmp')  # get the protocol code

    try:
        # create a socket instance
        # NOTE: socket.SOCK_RAW requires sudo/root privileges
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
        # get the host by ip
        host = socket.gethostbyname(dst)
    except socket.error as e:
        if e.errno in ERROR_DESCR:
            # Operation not permitted
            print(f'{e.args[1]} {ERROR_DESCR[e.errno]}')
        else:
            print(e.args[1])  # probably is the provided dst address is invalid
        exit()  # exit program if there is a socket error
    except socket.gaierror:
        return
    except Exception as e:
        print(e)  # catch and show any other exception
        return

    # create a packet by adding the header and the data
    packet = icmp_packet.header + icmp_packet.data
    while packet:
        # ICMP doesn't need a special port so a dummy port is given to send a ping request
        sent = sock.sendto(packet, (dst, 1))  # returns the sent amount
        # slice the packet by the amount sent until fully sent
        packet = packet[sent:]

    # wait for a reply
    receive_ping(sock, icmp_packet.icmp_id, timeout)
    sock.close()  # close connection

def pingg(dst: str, timeout=2, count=4, wait=1):
    payload = 64 * b"q"  # create an abituary payload of 64 bytes
    packet_id = generate_id()  # generate a random ICMP packet ID
    print(f'PING {dst} with {len(payload)} bytes of data')

    # create a packet and send one ping every one second for the count of times
    for i in range(1, count+1):
        # create a packet with the according sequence
        icmp = ICMPPacket(data=payload, icmp_id=packet_id, icmp_seq=i)
        do_one(dst, icmp, timeout)  # make one ping
        try:
            time.sleep(wait)  # sleep for a second for delay
        except KeyboardInterrupt:
            exit()
    print('')
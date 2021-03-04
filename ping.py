import argparse
from packages.main import pingg

# Create the parser
my_parser = argparse.ArgumentParser(allow_abbrev=False, description="Custom ping tool with python")

# # Add the arguments
my_parser.add_argument('destination', help='Destination address')
my_parser.add_argument('--count', '-c', action='store', type=int,default=4, help="The number of packets to send (default 4)")
my_parser.add_argument('--timeout', '-t', action='store', type=int,default=2, help="The timeout duration between pings in seconds (default 2s)")
my_parser.add_argument('--wait', '-w', action='store', type=int,default=1, help="The waiting/pause duration between pings in seconds (default 1s)")

# Execute the parse_args() method
args = my_parser.parse_args()
count, dst, timeout, wait = args.count, args.destination, args.timeout, args.wait
pingg(dst, timeout, count, wait)

# parse arguments from command line

import argparse
parser = argparse.ArgumentParser(description='Great Description To Be Here')

parser.add_argument("-f", type=int, dest='src_file', help="Source file name")
parser.add_argument("-d", type=int, dest='dst_file', help="Destination file name")

args = parser.parse_args()

print('Source:', args.src_file)
print('Destination:', args.dst_file)
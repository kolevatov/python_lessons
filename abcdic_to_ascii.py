# To convert file abcdic to ascii
import argparse

parser = argparse.ArgumentParser(description='file converter from EBCDIC to ASCII')
parser.add_argument("-f", dest='src_file', help="Source file name")
parser.add_argument("-d", dest='dst_file', help="Destination file name")
parser.add_argument("-b", type=int, dest='block_size', help="Block length. Default 1500 bytes", default=1500)
args = parser.parse_args()

block_size = args.block_size

src_file = open(args.src_file, 'rb', block_size)
dst_file = open(args.dst_file, 'wb', block_size)
str = ""

while True:
    block = src_file.read(block_size)
    if not block: break
    str = block.decode('cp500') + '\r\n'

    str = str.encode('UTF-8')
    dst_file.write(str)


src_file.close()
dst_file.close()
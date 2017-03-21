# Config file parser
# File has format "key = value" or "key : value".
COMMENT = '#'
SEPARATOR = '='

def parse_config(filename):
    options = {}
    f = open(filename)
    for line in f:
        line = line.replace(':',SEPARATOR)
        if not (line[0] is COMMENT) and (SEPARATOR in line):
            option, value = line.split(SEPARATOR, 1)
            # strip spaces:
            option = option.strip()
            value = value.strip()
            # store in dictionary:
            options[option] = value
    f.close()
    return options


options = parse_config('D:\\Python\\config.properties')
print (options)


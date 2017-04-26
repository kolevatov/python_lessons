import shelve

sfile = "..//pickles.dat"
def dump(key, element):
    s = shelve.open(sfile)
    s[key] = element
    s.sync()
    s.close

def load(key):
    s = shelve.open(sfile)
    print(s[key])
    s.close

def main():
    dump ("first", [1,2,3,4,5])
    dump("second", {"1":1,"2":2})
    load("first")

main()

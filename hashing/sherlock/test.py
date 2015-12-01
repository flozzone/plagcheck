#!/usr/bin/python

import sherlock, sys, os.path, json

def main(file):
    dbfile = "db.json"
    db = dict()
    if os.path.isfile(dbfile):
        with open(dbfile) as f:
            db = json.load(f)

    print "db size: " + str(len(db))
    print db

    sig = sherlock.signature(file)

    print "class name: " + sig.__class__.__name__
    print "size: " + str(len(sig))

    same_sig = 0
    for hash in sig:
        if str(hash) in db:
            same_sig += 1
        else:
            pass
            #print "hash not found " + str(hash)
            #break

    print "same_sig: " + str(same_sig)

    percent = 100.0/len(sig)*same_sig

    print "percent: " + str(percent)

    for hash in sig:
        if hash in db:
            db[str(hash)] += 1
        else:
            db[str(hash)] = 1;

    with open(dbfile, 'w') as f:
        json.dump(db, f)

if __name__ == "__main__":
   main(sys.argv[1])
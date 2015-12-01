#!/usr/bin/python3.4

import sherlock, sys, os.path, json

def load_db(dbfile):
    db = dict()
    if os.path.isfile(dbfile):
        with open(dbfile) as f:
            db = json.load(f)
    return db

def writeback_db(dbfile, db):
    with open(dbfile, 'w') as f:
            json.dump(db, f)

def main(file):
    dbfile = "db.json"
    db = load_db(dbfile)

    # create signature
    sig = sherlock.signature(file)

    # check for equal signatures
    same_sig = 0
    for hash in sig:
        if str(hash) in db:
            same_sig += 1

    percent = 100.0/len(sig)*same_sig

    print("db size: " + str(len(db)));
    print("number of signatures: " + str(len(sig)));
    print("number of equal signatures: " + str(same_sig));
    print("similarity: %s%%" % str(percent));

    # insert signatures of this document into db
    for hash in sig:
        # here we would leave a reference to this document
        # inside the dataset instead or just incrementing a counter
        if str(hash) in db:
            db[str(hash)] += 1
        else:
            db[str(hash)] = 1;

    writeback_db(dbfile, db)

if __name__ == "__main__":
   main(sys.argv[1])

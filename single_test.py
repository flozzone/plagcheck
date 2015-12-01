import sys

from db.plagdb import *
from hashing.sherlock import sherlock


def main(file):
    jsondb = JsonPlagDB("db.json")

    # create signature
    print("Creating signatures")
    sig = sherlock.signature(file)
    print("Signatures created")

    # check for equal signatures
    same_sig = 0
    for _hash in sig:
        hash = str(_hash)
        ret = jsondb.lookup(hash)
        if ret is not None:
            same_sig += 1

    percent = 100.0/len(sig)*same_sig

    print("number of signatures: " + str(len(sig)));
    print("number of equal signatures: " + str(same_sig));
    print("similarity: %s%%" % str(percent));

    # insert signatures of this document into db
    ref = PlagReference(file)
    for _hash in sig:
        hash = str(_hash)
        jsondb.update(hash, ref)

if __name__ == "__main__":
   main(sys.argv[1])

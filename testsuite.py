import glob
import sys

#from db.JsonPlagDB import JsonPlagDB
from db.plag_lmdb import LmdbPlagDB
from db.plagdb import PlagReference
from hashing.sherlock import sherlock

source_pattern = "source-document"
suspicious_pattern = "suspicious-document"
max_docs = 10000

def main(testset_path):
    #db = JsonPlagDB("db.json")
    db = LmdbPlagDB("/tmp/plagdb.lmdb")

    source_list = glob.glob(testset_path + "/" + source_pattern + "*.txt")
    suspicious_list = glob.glob(testset_path + "/" + suspicious_pattern + "*.txt")

    # create signatures
    i = 0
    for file in source_list:
        i += 1
        if i == max_docs:
            break

        ref = PlagReference(file)
        print("Create signature for " + ref.filename)
        sig = sherlock.signature(file)

        db.update_batch(sig, ref)

        #for _hash in sig:
        #    hash = str(_hash)
        #    db.update(hash, ref)

    # check for equal signatures
    i = 0
    for file in suspicious_list:
        i += 1
        if i == max_docs:
            break
        sig = sherlock.signature(file)
        same_sig = 0
        for _hash in sig:
            hash = str(_hash)
            ret = db.lookup(hash)
            if ret is not None:
                same_sig += 1

        percent = 100.0/len(sig)*same_sig
        print("similarity: %s%%" % str(percent));

if __name__ == "__main__":
   main(sys.argv[1])
import lmdb, json
from io import StringIO, BytesIO

try:
    import cPickle as pickle
except:
    import pickle

from db.plagdb import PlagDB, PlagReference

class LmdbPlagDB(PlagDB):

    def __init__(self, file):
        self.db = lmdb.open(file, map_size=4000*1000*1000)

    def __del__(self):
        if self.db is not None:
            self.db.close()

    def lookup(self, hash):
        with self.db.begin() as txn:
            data = txn.get(hash.encode("ascii"))

        if data is None:
            return None

        return json.loads(data.decode("ascii"))

    def update_batch(self, sig, reference):
        with self.db.begin(write=True, buffers=True) as txn:

            file = reference.filename

            for _hash in sig:
                hash = str(_hash).encode("ascii")
                buf = txn.get(hash)

                io = BytesIO(buf)

                ref_list = None
                if buf is not None:

                    ref_list = pickle.load(io)
                    if file in ref_list:
                        ref_list[file] += 1
                    else:
                        ref_list[file] = 1
                else:
                    ref_list = dict()
                    ref_list[file] = 1

                pickle.dump(ref_list, io)

                txn.put(hash, data.encode("ascii"))


    def update(self, hash, reference):

        print("  updating " + hash)

        with self.db.begin(write=True) as txn:
            existing = txn.get(hash.encode("ascii"))

            file = reference.filename

            ref_list = None
            if existing is not None:
                ref_list = json.loads(existing.decode("ascii"))
                if file in ref_list:
                    ref_list[file] += 1
                else:
                    ref_list[file] = 1
            else:
                ref_list = dict()
                ref_list[file] = 1

            data = json.dumps(ref_list)

            txn.put(hash.encode("ascii"), data.encode("ascii"))
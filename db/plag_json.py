from db.plagdb import PlagDB, PlagReference
import os.path, json

class JsonPlagDB(PlagDB):

    tmp_dir = "/tmp/plagtest"

    def __init__(self, dbfile):
        if not os.path.isdir(JsonPlagDB.tmp_dir):
            os.makedirs(JsonPlagDB.tmp_dir)

    def __del__(self):
        pass

    @staticmethod
    def ref_path(hash):
        dir = hash[0:4]
        return JsonPlagDB.tmp_dir + "/" + dir + "/" + hash + ".json"

    @staticmethod
    def load_ref_list(hash):
        path = JsonPlagDB.ref_path(hash)

        if not os.path.isfile(path):
            return None

        with open(path) as f:
            ref = json.load(f)

        return ref

    def lookup(self, hash):
        return JsonPlagDB.load_ref_list(hash)

    def update(self, hash, reference):
        file = reference.filename.replace("source-document", "")
        ref_list = JsonPlagDB.load_ref_list(hash)
        if ref_list is not None:
            if file in ref_list:
                ref_list[file] += 1
            else:
                ref_list[file] = 1
        else:
            ref_list = dict()
            ref_list[file] = 1

        JsonPlagDB.write(hash, ref_list)

    @staticmethod
    def write(hash, ref_list):

        path = JsonPlagDB.ref_path(hash)
        dir = os.path.dirname(path)

        if not os.path.isdir(dir):
            os.makedirs(dir)

        with open(path, 'w') as f:
            json.dump(ref_list, f)
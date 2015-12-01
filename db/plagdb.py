import os.path

class PlagReference:
    def __init__(self, filename):
        self.filename = os.path.basename(filename)

class PlagDB:
    def __init__(self):
        """
        Open connection to DB
        """
        raise NotImplementedError( "Should have implemented this" )

    def __del__(self):
        """
        Close DB connection
        """

        raise NotImplementedError( "Should have implemented this" )

    def lookup(self, hash):
        """
        Lookup a hash in the DB

        :param hash: Hash as a string to lookup
        :return: List of PlagReferences or None otherwise
        """
        raise NotImplementedError( "Should have implemented this" )

    def update_batch(self, sig, reference):
        """
        Update signatures in batch mode

        :param sig: List of signatures for reference
        :param reference: Reference of original document
        :return: List of PlagReferences or None otherwise
        """
        raise NotImplementedError( "Should have implemented this" )

    def update(self, hash, reference):
        """
        Updates a dataset with the given reference

        :param hash: Hash as a string to be updated
        :param reference: Reference to be added
        :return:
        """
        raise NotImplementedError( "Should have implemented this" )


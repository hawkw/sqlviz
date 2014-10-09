#! usr/bin/env python3
from docopt import docopt
from matplotlib import pyplot


class Schema:
    """
    Wraps the SQL source code for a schema and provides methods to get information about that schema.
    """

    def __init__(self, source):
        """
        Creates a new instance of Schema for the specified source code string.
        """
        self.source = source

    def n_tables(self):
        """
        Returns the number of tables defined in the schema
        """
        pass

    def n_keys(self):
        """
        Returns the number of keys defined in the schema
        """
        pass

    def n_datatypes(self):
        """
        Returns the number of each data type in the schema.
        """
        pass

    def lengths(self):
        """
        Returns a dictionary mapping each data type in the schema
        to a list of the lengths of those data types.
        """
        pass

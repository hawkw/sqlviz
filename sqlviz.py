#! usr/bin/env python3
from docopt import docopt
from matplotlib import pyplot
import re

"""SQLViz

Usage:
    sqlviz [-hkdlpo DIR]
    sqlviz no-graph [-hkdlo DIR]

Options:
    -h --help       Display this help file
    -k --keys       Graph the number of foreign keys vs primary keys
    -d --datatypes  Graph the distribution of datatypes
    -l --lengths    Graph the distribution of lengths for each data type
    -p --print      Print text to the console as well as creating graphs
    -o DIR          Output graphs to the specified directory

"""

class Schema:
    """
    Wraps the SQL source code for a schema and provides methods to get information about that schema.
    """

    table_def = re.compile(r"CREATE TABLE|create table")
    primary_key = re.compile(r"PRIMARY KEY|primary key")
    foreign_key = re.compile(r"FOREIGN KEY|foreign key")
    varchar = re.compile(r"VARCHAR|varchar \((?P<n>\n+)\)")
    decimal = re.compile(r"DECIMAL|decimal \((?P<p>\n+),(?P<d>\n+)\)")
    integer = re.compile(r"INT|int")

    def __init__(self, source):
        """
        Creates a new instance of Schema for the specified source code string.
        """
        self.source = source

    def n_tables(self):
        """
        Returns the number of tables defined in the schema
        """
        return len(Schema.table_def.findall(self.source))

    def n_keys(self):
        """
        Returns the number of keys defined in the schema
        """
        return {"PRIMARY KEY": len(Schema.primary_key.findall(self.source)),
                "FOREIGN KEY": len(Schema.foreign_key.findall(self.source))}

    def n_datatypes(self):
        """
        Returns the number of each data type in the schema.
        """
        return {"INT": len(Schema.integer.findall(self.source)),
                "DECIMAL": len(Schema.decimal.findall(self.source)),
                "VARCHAR": len(Schema.varchar.findall(self.source))}

    def lengths(self):
        """
        Returns a dictionary mapping each data type in the schema
        to a list of the lengths of those data types.
        """
        pass #TODO: not yet implementend
    
if __name__ == "__main__":
    opts = docopt(__doc__, help=True, version="0.1")

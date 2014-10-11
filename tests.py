#! usr/bin/env python3


import unittest
from sqlviz import Schema

# Tests will go here...eventually

class InventorySchemaSpec (unittest.TestCase):

    def setUp (self):
        self.schema = Schema(
            """DROP TABLE Inventory;

            CREATE TABLE Inventory
            (
            id INT PRIMARY KEY,
            product VARCHAR(50) UNIQUE,
            quantity INT,
            price DECIMAL(18,2)
            );""")

    def test_n_tables(self):
        self.assertEqual(self.schema.n_tables(),  1,
                        "The Inventory schema should contain 1 table.")

    def test_n_keys(self):
        self.assertEqual(self.schema.n_keys(),  {"PRIMARY KEY": 1, "FOREIGN KEY": 0},
                        "The Inventory schema should contain 1 primary key and 0 foreign keys.")

    def test_n_datatypes(self):
        self.assertEqual(self.schema.n_datatypes(), {"INT": 2, "VARCHAR": 1, "DECIMAL": 1},
                        "The Inventory schema should contain two INTs, one VARCHAR, and one DECIMAL")

    def test_lengths(self):
        self.assertEqual(self.schema.lengths(), {"VARCHAR": [50], "DECIMAL": [(18,2)]},
                        "The Inventory schema should contain one VARCHAR(50) and one DECIMAL(18,2)")

if __name__ == '__main__':
    unittest.main()

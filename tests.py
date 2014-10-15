#! usr/bin/env python3


import unittest
from sqlviz import Schema


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
        self.assertEqual(self.schema.n_datatypes(), {"INT": 2, "DECIMAL": 1, "NUMERIC": 0, "VARCHAR": 1, "TEXT": 0},
                        "The Inventory schema should contain two INTs, one VARCHAR, and one DECIMAL")

    def test_lengths(self):
        self.assertEqual(self.schema.lengths(), {"VARCHAR": [50], "DECIMAL": [(18,2)], "NUMERIC": []},
                        "The Inventory schema should contain one VARCHAR(50) and one DECIMAL(18,2)")

class WritersSchemaSpec (unittest.TestCase):


    def setUp (self):
        with open ("resources/test/Writers.sql", "r") as f:
            source = f.read()
        self.schema = Schema(source)

    def test_n_tables(self):
        self.assertEqual(self.schema.n_tables(),  5,
                        "The Writers schema should contain 5 tables.")

    def test_n_keys(self):
        self.assertEqual(self.schema.n_keys(),  {"PRIMARY KEY": 3, "FOREIGN KEY": 5},
                        "The Writers schema should contain 3 primary keys and 5 foreign keys.")

    def test_n_datatypes(self):
        self.assertEqual(self.schema.n_datatypes(), {"INT": 7, "DECIMAL": 0, "NUMERIC": 1, "VARCHAR": 10,  "TEXT": 1},
                        "The Writers schema should contain 7 INTs, 10 VARCHARs, 1 NUMERIC, and 1 TEXT")

    def test_lengths(self):
        self.assertEqual(self.schema.lengths(),
            {"VARCHAR": [15, 15, 15, 10, 10, 20, 60, 20, 15, 9],
             "DECIMAL": [],
             "NUMERIC": [(4,0)]})


if __name__ == '__main__':
    unittest.main()

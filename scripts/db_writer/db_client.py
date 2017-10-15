"""
DB client:
- RAW QUERY
"""

import psycopg2

PUB_COLS = ["pub_key", "pub_class", "pub_type", "title_abbrev", "title", "year", "month"]
MORE_COLS = {
    "article" : ["pub_key", "volume", "journal", "number"],
    "book" : ["pub_key", "publisher", "series", "volume"],
    "incollection" : ["pub_key", "booktitle"],
    "proceedings" : ["pub_key", "booktitle", "publisher"],
    "inproceedings" : ["pub_key", "booktitle"]
}
AUTHOR_COLS = ["name", "last_name"]
PUB_AUTH_COLS = ["pub_key", "author"]

class DBClient:
    """ DB Client Class """

    def __init__(self, host, dbname, user, password):
        conn_string = "host='%s' dbname='%s' user='%s' password='%s'"%(host, dbname, user, password)
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()

    def init_tables(self):
        """ init tables in databases """

    def insert_pub(self, info):
        """ insert publication to db """
        pub_insert_cols = []
        pub_insert_values = []
        for col in PUB_COLS:
            if col in info:
                pub_insert_cols.append(col)
                pub_insert_values.append(info[col])
        self.insert_row("publication", pub_insert_cols, pub_insert_values, "pub_key")

        for auth in info["authors"]:
            self.insert_row("author", AUTHOR_COLS, [auth, auth.split(" ")[-1]], "name")
            self.insert_row("pub_auth", PUB_AUTH_COLS, [info["pub_key"], auth], "pub_key, author")

        insert_cols = []
        insert_values = []

        if info["pub_class"] in MORE_COLS:
            for col in MORE_COLS[info["pub_class"]]:
                if col in info:
                    insert_cols.append(col)
                    insert_values.append(info[col])
            self.insert_row(info["pub_class"], insert_cols, insert_values, "pub_key")

        self.commit()

    def insert_row(self, table, cols, values, unique_col=""):
        insert_str = "INSERT INTO " + table 
        insert_str += " (" + ",".join(cols) + ") "
        insert_str += "VALUES (" + ", ".join(['%s' for i in range(len(values))]) + ")"
        if unique_col != "":
            insert_str += " ON CONFLICT (%s) DO NOTHING"%unique_col
        self.execute_raw(insert_str, values)

    def execute_raw(self, query_str, values):
        """ execute raw query """
        return self.cursor.execute(query_str, values)

    def fetch_all(self):
        """ fetch all from cursor """
        return self.cursor.fetch_all()

    def commit(self):
        """ commit transaction """
        return self.conn.commit()
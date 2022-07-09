import psycopg2
from psycopg2 import Error

# Підключення до бази данних

conn = psycopg2.connect(dbname="test_db", password="axbsl286", user="postgres")

# Вибір символу для відповідної команди

print("""c - Create
r - Read
u - Update
d - Delete""")
sep_symbol = str(input("Input the sign of command :"))

create = "c"
read = "r"
update = "u"
delete = "d"

# Блок виконання команди Create

if sep_symbol == create:

    # Введення символу для визначення створюваного об'єкту

    print("Table - t")
    print("Insert values - i")
    create_symbol = str(input("Input the sign of create operation:"))
    create_table = "t"
    insert_val = "i"
    tab_name = str(input("Input the table name:"))

    # Блок створення таблиці

    if create_symbol == create_table:
        with conn:
            with conn.cursor() as cur:
                try:
                    tab_set = str(input("Input the table column settings:"))
                    tab_set = list(tab_set)
                    tab_set.insert(len(tab_set), ")")
                    tab_set.insert(0, "(")
                    tab_set = "".join(tab_set)
                    cur.execute(f"DROP TABLE IF EXISTS {tab_name}", )
                    cur.execute(f"CREATE TABLE {tab_name} {tab_set}", )


                except (Exception, Error):
                    print("Error while working with PostgreSQL", Error)

                finally:
                    print(f"Table {tab_name}  has been created successfully")

    # Блок створення нового рядка таблиці

    elif create_symbol == insert_val:
        with conn:
            with conn.cursor() as cur:
                try:
                    str_cont = input("Input the string content:")
                    column_name = input("Input the column names:")
                    cur.execute(f"INSERT INTO {tab_name} {column_name} VALUES {str_cont}")
                except (Exception, Error):
                    print("Error while working with PostgreSQL", Error)

                finally:
                    print(f"In the table {tab_name} new values has been inserted successfully")

# Блок виконання команди Read

elif sep_symbol == read:
    with conn:
        with conn.cursor() as cur:
            try:
                tab_name = str(input("Input the table name for reading:"))
                cur.execute(f"SELECT * FROM {tab_name}", )

            except (Exception, Error):
                print("Error while working with PostgreSQL", Error)

            finally:
                print("The table content:")
                full_fetch = cur.fetchall()
                for record in full_fetch:
                    print(record)

# Блок виконання команди Update

elif sep_symbol == update:
    with conn:
        with conn.cursor() as cur:
            try:
                tab_name = str(input("Input the table name for update:"))
                col_name = str(input("Input the mutable column name:"))
                col_chenge = str(input("Input the chenges:"))
                rev_col_name = str(input("Input the relevant column name:"))
                str_chenge = str(input("Input the string name:"))
                cur.execute(f"""UPDATE {tab_name}
                               SET {col_name} = {col_chenge}
                               WHERE {rev_col_name} = {str_chenge}""")

            except (Exception, Error):
                print("Error while working with PostgreSQL", Error)

            finally:

                print(f"The table {tab_name}  has been updated successfully")


# Блок виконання команди Delete

elif sep_symbol == delete:

    # Введення символу для вибору об'єкту видалення

    print("Drop table - t")
    print("Delete string - s")
    delete_symbol = str(input("Input the sign of delete operation:"))
    drop_table = "t"
    delete_string = "s"
    tab_name = str(input("Input the table name:"))

    # Блок видалення таблиці

    if delete_symbol == drop_table:
        with conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(f"DROP TABLE IF EXISTS {tab_name}", )

                except (Exception, Error):
                    print("Error while working with PostgreSQL", Error)

                finally:
                    print(f"Table {tab_name}  has been dropped successfully")

    # Блок видалення рядка

    elif delete_symbol == delete_string:
        with conn:
            with conn.cursor() as cur:
                try:
                    rev_col_name = str(input("Input  relevant column name:"))
                    str_name = str(input("Input string name:"))

                    cur.execute(f"""DELETE FROM {tab_name}
                                    WHERE {rev_col_name} = {str_name}""")

                except (Exception, Error):
                    print("Error while working with PostgreSQL", Error)

                finally:
                    print(f"The string {str_name} from {tab_name}  has been deleted successfully")
else:
    print("Unsupported command")
    conn.close()
conn.close()

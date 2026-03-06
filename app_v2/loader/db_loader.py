# view from apollo helpdesk kb, complete with the action taken

import psycopg2


def load_db_kb():

    conn = psycopg2.connect(
        host="localhost",
        dbname="apollo",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT title, content
        FROM apollo_kb_view
    """)

    rows = cur.fetchall()

    docs = []

    for title, content in rows:

        docs.append(f"{title}\n{content}")

    return docs
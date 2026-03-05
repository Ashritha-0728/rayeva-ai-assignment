import sqlite3

def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        primary_category TEXT,
        sub_category TEXT,
        seo_tags TEXT,
        sustainability_filters TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_metadata(product_name, data):

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO product_metadata
    (product_name, primary_category, sub_category, seo_tags, sustainability_filters)
    VALUES (?, ?, ?, ?, ?)
    """, (
        product_name,
        data["primary_category"],
        data["sub_category"],
        ",".join(data["seo_tags"]),
        ",".join(data["sustainability_filters"])
    ))

    conn.commit()
    conn.close()
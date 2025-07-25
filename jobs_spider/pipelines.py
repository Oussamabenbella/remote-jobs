import sqlite3              
class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("jobs.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS jobs(
                link TEXT PRIMARY KEY,
                title TEXT,
                company TEXT,
                date TEXT,
                tags TEXT
            )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT OR IGNORE INTO jobs VALUES (?,?,?,?,?)
        """, (item["link"], item["title"], item["company"],
              item["date"], item["tags"]))
        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

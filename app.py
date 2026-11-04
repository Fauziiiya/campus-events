import sqlite3
from flask import Flask

app = Flask(__name__)
DATABASE = "events.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            venue TEXT,
            event_date TEXT NOT NULL,
            event_time TEXT,
            capacity INTEGER,
            organiser_name TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            attendee_name TEXT NOT NULL,
            attendee_email TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return "Campus Events app is running!"


init_db()

if __name__ == "__main__":
    app.run(debug=True)
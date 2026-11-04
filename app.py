import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret")
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
    return redirect(url_for("list_events"))


@app.route("/events")
def list_events():
    conn = get_db()
    events = conn.execute("SELECT * FROM events ORDER BY event_date").fetchall()
    conn.close()
    return render_template("events.html", events=events)


@app.route("/events/new", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        event_date = request.form.get("event_date", "").strip()

        if not title or not event_date:
            flash("Title and date are required.", "error")
            return render_template("event_form.html", form=request.form)

        capacity = request.form.get("capacity", "").strip()
        capacity = int(capacity) if capacity.isdigit() else None

        conn = get_db()
        conn.execute(
            "INSERT INTO events (title, description, venue, event_date, event_time, capacity, organiser_name) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                title,
                request.form.get("description", "").strip(),
                request.form.get("venue", "").strip(),
                event_date,
                request.form.get("event_time", "").strip(),
                capacity,
                request.form.get("organiser_name", "").strip(),
            ),
        )
        conn.commit()
        conn.close()

        flash("Event created successfully!", "success")
        return redirect(url_for("list_events"))

    return render_template("event_form.html", form={})


@app.route("/events/<int:event_id>/edit", methods=["GET", "POST"])
def edit_event(event_id):
    conn = get_db()
    event = conn.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()

    if event is None:
        conn.close()
        flash("Event not found.", "error")
        return redirect(url_for("list_events"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        event_date = request.form.get("event_date", "").strip()

        if not title or not event_date:
            conn.close()
            flash("Title and date are required.", "error")
            return render_template("event_edit.html", form=request.form)

        capacity = request.form.get("capacity", "").strip()
        capacity = int(capacity) if capacity.isdigit() else None

        conn.execute(
            "UPDATE events SET title = ?, description = ?, venue = ?, event_date = ?, "
            "event_time = ?, capacity = ?, organiser_name = ? WHERE id = ?",
            (
                title,
                request.form.get("description", "").strip(),
                request.form.get("venue", "").strip(),
                event_date,
                request.form.get("event_time", "").strip(),
                capacity,
                request.form.get("organiser_name", "").strip(),
                event_id,
            ),
        )
        conn.commit()
        conn.close()

        flash("Event updated successfully!", "success")
        return redirect(url_for("list_events"))

    conn.close()
    return render_template("event_edit.html", form=dict(event))


init_db()

if __name__ == "__main__":
    app.run(debug=True)
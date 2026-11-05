# Campus Events

A web app for creating, browsing and registering for campus events.

**Live app:** https://fauziii.pythonanywhere.com

## Problem being solved

Students often miss campus events because details are scattered across group chats and posters, and organisers have no simple way to see who plans to attend. This app gives organisers one place to publish events and gives students a place to browse them and register.

## Features

- Create an event (title and date required, other details optional)
- View a list of all events, sorted by date
- Edit an event
- Delete an event (with a confirmation prompt; its registrations are removed too)
- Register for an event with a name and email
- View the list of people registered for each event
- Validation with clear error and success messages

## Technology stack

- Python 3 and Flask (backend)
- SQLite (database)
- HTML with Jinja2 templates (frontend)
- Git and GitHub (version control)
- PythonAnywhere (hosting)

## Setup and installation

1. Clone the repository:
   ```
   git clone https://github.com/Fauziiiya/campus-events.git
   cd campus-events
   ```
2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python3 app.py
   ```
5. Open http://127.0.0.1:5000 in your browser.

## Environment variables

See `.env.example`. The app uses one variable:

- `SECRET_KEY`: used by Flask to show messages after a form is submitted. If it is not set, a development default is used. Set your own value in production.

## Database setup

The app uses SQLite. The database file (`events.db`) and its tables are created automatically the first time the app starts, so no manual setup is needed.

- `events`: id, title, description, venue, event_date, event_time, capacity, organiser_name
- `registrations`: id, event_id (links to events), attendee_name, attendee_email

## Testing instructions

Test each of these in the browser:

1. **Create:** add an event. It should appear in the list.
2. **Create (invalid):** submit the form with no title or date. An error message should appear and nothing is saved.
3. **Read:** open an event's page to see its details.
4. **Update:** click Edit, change a field, save. The change should show in the list.
5. **Update (invalid):** clear the title and save. An error should appear and nothing changes.
6. **Register:** sign up with a name and email. The name should appear in the attendee list.
7. **Register (invalid):** submit empty or with an email missing "@". An error should appear.
8. **Delete:** click Delete and confirm. The event should disappear.
9. **Persistence:** refresh the page. The data should still be there.

## Live deployment URL

https://fauziii.pythonanywhere.com

## Screenshots

(Add screenshots of the events list, create form, event page and edit page here.)
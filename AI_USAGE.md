# AI Usage Report

## 1. AI tools used

I used Claude (made by Anthropic) in a chat as my main AI tool. I used it to plan the project, explain concepts I didn't know (CRUD, virtual environments, Flask routes, SQL queries, deployment), generate code, and debug errors.

## 2. Important prompts

- Shared the assessment guide and asked for help understanding what was required, since I had not opened it yet.
- Told Claude I was a beginner who felt more comfortable with Python than JavaScript. It suggested Flask with SQLite.
- Asked how to check whether Python and Git were installed, and how to set up my project folder and push to GitHub.
- Asked for each feature one small step at a time: the database tables, then Create, Read, Update, Delete for events, then registrations.
- Asked how to deploy, then followed the PythonAnywhere steps after checking its free plan.
- Pasted error messages (such as the GitHub token error and the "Address already in use" error) and asked what they meant.

## 3. Features or code generated with AI

- The Flask app structure and the SQLite database tables (`events` and `registrations`)
- Routes to create, list, edit and delete events, and an event page with a registration form
- The HTML templates for each page
- Validation for empty titles, dates, names and invalid emails
- A draft of the README and the `.env.example` file
- The deployment steps for PythonAnywhere (virtual environment and WSGI file)

## 4. Changes I made to AI-generated code

I mostly used the code as Claude generated it, because I’m a beginner and wanted to get a working app first. What I did myself was choose Project 3, choose Python and Flask because I have little knowledge in it and not JavaScript, test every feature, fix my project structure, and set up the deployment. I read through each part after Claude explained it, and I can explain how Create, Read, Update, Delete and registration work.

## 5. Errors and how I resolved them

- **`python` not found:** My computer didn't recognise `python`. I found that `python3 --version` worked, so I used `python3` from then on.
- **GitHub rejected my password:** `git push` said password authentication is not supported. I created a personal access token on GitHub and used that instead.
- **`app.py` was not on GitHub:** My file had been saved inside the `venv` folder, which `.gitignore` tells Git to skip. I checked the file path, moved `app.py` up into the main project folder, and pushed again.
- **`.gitignore` already existed:** The one I edited was inside `venv`, so it did not apply to my project. I created a proper `.gitignore` in the main folder and stopped tracking `events.db`.
- **"Address already in use":** An old copy of my app was still running on port 5000. I closed the extra terminal and started the app again.
- **Blank edit page:** My `event_edit.html` was empty because I had two files with that name. I pasted the code into the one inside the `templates` folder.
- **Deployment:** My PythonAnywhere console closed while I was installing, so I reopened it and checked what had been saved before continuing. I also picked a Python version that didn't match my virtual environment, so I tested the site first and only planned to rebuild the environment if it failed. It worked.

## 6. How I tested and verified AI-generated code

- I tested each feature in the browser after adding it, before committing.
- I tested invalid input: an empty form for creating an event, an empty title when editing, and an empty or invalid registration. Each showed an error and saved nothing.
- I tested Delete with both Cancel and OK in the confirmation pop-up.
- After deploying, I repeated Create, Read, Update, Register and Delete on the live site.
- I reloaded the live app and checked that my data was still there.

## 7. What I learned

- CRUD stands for Create, Read, Update, and Delete, which are the four basic operations used to manage data in an application. 
- The .gitignore file is important because it prevents unnecessary files, such as temporary files and environment settings, from being uploaded to GitHub. 
- Secrets like passwords and API keys should never be uploaded to GitHub because someone could access them and misuse them. 
- Testing with both good and bad input helps identify errors and ensures that the application handles unexpected situations correctly.


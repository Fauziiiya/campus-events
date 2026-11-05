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

I mostly used the code as Claude generated it, because I’m a beginner and wanted to get a working app first. What I did myself was choose Project 3, choose Python and Flask because I have little knowledge in it and not JavaScript, test every feature, fix my project structure, and set up the deployment. I read through each part after Claude explained it, and I can explain how Create, Read, Update, Delete and registration work. I noticed that the project brief required each event to have a category, and my app didn't have one, so I decided to add it. Claude wrote the code for it, and I applied it to app.py and the three templates, then tested it myself. Along the way I found that my events.html file hadn't saved, because my commit only listed two changed files when it should have listed three. I replaced the file and tested again. I also updated the live site by pulling the code onto PythonAnywhere and reloading, then checked that my old events still showed up.

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

Building this project taught me that CRUD, which stands for Create, Read, Update and Delete, is the basic set of operations behind almost any app that manages data, and I now understand how each one works in my own code. I also learned why a .gitignore file matters: it keeps files like my virtual environment, temporary files and my database out of GitHub. Secrets such as passwords and API keys must never be uploaded to GitHub, because anyone who finds them could misuse them, which is why my secret key is only set on PythonAnywhere and not in my repository. Testing with both good and bad input showed me that an app has to handle mistakes properly and not just work when everything is typed correctly. Using AI helped me move faster as a beginner, but I still had to read the code, test it and sort out problems myself.


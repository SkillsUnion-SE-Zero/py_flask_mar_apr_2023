# Python PT - outline for Week 7: Tuesday, April 18, 2023

## Reminders:
- For this course, you need the following to pass:
    - Minimum 15 out of 16 core assignments done
    - At least 11 out of 16 discussion topics done - this week's is due by 11:59 PM this Sunday night!
    - Pass the belt exam with any belt (orange, red or black)
- Don't forget about the 20-minute rule and Dojo Hall!

## IMPORTANT announcements:
- Make sure when you submit your Flask projects to submit your Pipfile and Pipfile.lock files!  When you submit projects that use a database, make sure you include your .mwb file!  For the exam, you will need to include these 3 files, along with the application itself!
- Code from the belt review project will NOT be pushed to GitHub, and the same with the wireframe

## Outline for today and tomorrow:
- NOTE: We will start with the same working login/registration from last week!  (There is one slight tweak: the first name and last name must be 2 or more characters instead of 3 or more; everything else is the same.)
- Lay down foundation: look at wireframe for review project
    - Identify routes for project
    - Figure out additional tables, columns and relationships in our schema
    - Add the following:
        - HTML file(s)
        - New model file(s)
        - Controller file(s) - don't forget to import your controllers in your server file!  Let's render template where needed and add logic to ensure only logged in users can access routes where you must be registered
- Build out schema in MySQL Workbench:
    - Do a "Save As..." first to create a new model (.mwb) file
    - Add new table(s) and column(s)
    - Forward-engineer
    - Make sure you have the correct schema name in your app!
    - If not done yet: add `__init__` method to new model(s)
- Add CRUD to app:
    - Create portion(s)

- Will cover in tomorrow's lecture:
    - Read portions
    - Update portion(s)
    - Delete portion(s)
- At the end (if we have time in Wednesday's lecture): drop schema and test app fully again
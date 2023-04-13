# Python PT - outline for Week 6: Wednesday, April 12, 2023

## Reminders:
- Please remember to get an early start with assignments and discussion topics every week!
- Don't forget about the 20-minute rule and Dojo Hall!
- Remember to read the material BEFORE the lecture that day!

## Core assignments this week:
- Login and registration
- Recipes (belt review assignment) - HIGHLY recommended

Need at least 15 out of 16 done total this course to satisfy this requirement and to be eligible for the exam!  **The exam period starts this Friday, April 14, so let's get to it!**

For those of you behind: if you submit the Users CRUD Modularized assignment BEFORE submitting the Users CR assignment, make sure you submit for BOTH assignments!!  The same code for both is fine.

## IMPORTANT announcements:
- Make sure when you submit your Flask projects to submit your Pipfile and Pipfile.lock files!  When you submit projects that use a database, make sure you include your .mwb file!  For the exam, you will need to include these 3 files, along with the application itself!
- Code from lecture this week and part of next week will NOT be pushed to GitHub.  The following will NOT be pushed:
    - Standalone login/registration
    - Adding login/registration to class project
    - Belt review project

## Discussion topics reminder:
- Due Sunday by 11:59 PM Pacific!

Need at least 11 (recommended 12) out of 16 discussion topics to satisfy this requirement!

## Outline for today and Thursday:
- Login/registration demo (continued):
    - Finish adding registration (with Bcrypt)
    - Adding logout
    - Adding logic to ensure only logged in users can access pages
    - Add validation for unique email
    - Adding login
- Adding validations for (show updated wireframe):
    - Companies (creating and updating)
    - Electronics (creating and updating)

- Saved for Thursday:
    - Adding login/registration to our class project:
        - Adding user table to our schema (plus foreign keys) - and forward-engineering again - make sure you select "Generate drop schema"!  Also pay attention to any changes that might need to be made with your users table/model!
        - Adding new user model and controller to project - with new attributes and imports added in the models
        - Don't forget to install a new package as we now have login/registration! 
        - Updating logic for checking if someone is logged in through the app
    - Linking Users to Companies and Electronics when...:
        - Creating a company
        - Showing all companies - with name of user who added included, plus conditional rendering of links
        - Showing one company - with name of user who added included, plus conditional rendering of links
        - Creating an electronic
        - Showing all electronics - with name of user who added included, plus conditional rendering of links
        - Showing one electronic item - with name of user who added included, plus conditional rendering of links
    - Logic for ensuring only the creator can access routes that involve editing or deleting
- If we have time Thursday: Showing a user's companies and electronics

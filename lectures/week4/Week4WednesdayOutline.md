# Python PT - outline for Week 4: Wednesday, March 29, 2023

## Reminders:
- Please remember to get an early start with assignments and discussion topics every week!
- Don't forget about the 20-minute rule and Dojo Hall!
- Remember to read the material BEFORE the lecture that day!

## Core assignments this week:
- HTML Table
- Counter
- Dojo Survey
- Users CR

Need at least 15 out of 16 done total this course to satisfy this requirement and to be eligible for the exam at the end of week 6!

## IMPORTANT announcements:
- If you do Users CR first, make sure you submit that BEFORE working on Users CRUD Modularized!
- If you submit the Users CRUD Modularized assignment BEFORE submitting the Users CR assignment, make sure you submit for BOTH assignments!!  The same code for both is fine.
- Dojo Hall hours are changing starting Monday, April 3: 1 PM to 8 PM Pacific (still 11 AM to 8 PM Pacific through this Sunday).  TAs will be available on Discord starting at 11 AM Pacific, so you're encouraged to ask your channel in one of the channels.  Please keep the DMs to a minimum.

## Discussion topics reminder:
- Due Sunday by 11:59 PM Pacific!

Need at least 11 (recommended 12) out of 16 discussion topics to satisfy this requirement!

## Outline for today:
- Review modularization and recap yesterday briefly
- Checking to see whether someone is logged in via session
- Logging out (temporary version until we add login/registration down the road)
- Creating a company - the add form
    - Saving form data in session
        - WARNING: Just for today (and yesterday for that matter), we will use session to hold form data.  This is NOT the primary purpose of session, as we're using it as a placeholder for our database.  Session data will only be used to hold data that will be available across your app that doesn't need to be saved to a database, primarily identifying who's logged in.
- Showing all companies - initially saved in session (we'll later on use our database instead of session)
- If time permits (will cover tomorrow if we can't make it today):
    - Connecting to our database
        - We'll need a new package for our project
    - Adding our Company model
- Saved for tomorrow:
    - Saving a new company to the database (CREATE)
    - Showing all companies from the database (READ all)
    - Showing one company from the database in our app (READ one) - initially without any electronics
    - Editing one company with a form and talking to the database (UPDATE)
    - Deleting one company from the database through our app (DELETE)
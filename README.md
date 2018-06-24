This is a readme file

The database used here is django sqlite  which is by default database

for running the project, create a virtual environment and pull the code using the command

`git pull https://github.com/sheshant/rest_api_user.git`

then run the command `pip install -r requirements.txt` and `python3 manage.py migrate`

By default there are 2 tables created already `UserProfile` and `UserActionLog`

Go to the url `/api/users/` to get the list of all users currently in the database

You can create a new user from that page after after sending post request 
to search a term, got to url `/api/users/?query=sh` where sh is the term to search
all the actions will be recorded in the `UserActionLog` table

To get the stats go to UserActionLog admin page and you can search on the basis of action whether it is 'created_user' or 'search_user' and also you can filter it out on the basis of action_time whether action happened last day or week or month 





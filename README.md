## email-magnet

# Challenge
Create a command line program that will take an internet domain name (i.e. "web.mit.edu") and print out a list of the email addresses that were found on that website only.

# Setup
The only requirements are the lxml and Requests python libraries. These libaries and the correct versions can be found in 'requirements.txt'. The other libraries used in the project are standard Python 2 libaries.

To use pip to install, run in command line:
```
> pip install -r requirements.txt
```

# Usage
To run, use the command line interface:
```
# For web.mit.edu:
> python find_email_addresses.py web.mit.edu
```

"web.mit.edu" can be replaced with any domain name you like.

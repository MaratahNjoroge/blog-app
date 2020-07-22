# Blog-app

##A web application that allows the users to post blogs, delete and close on blogs.

## By [MaratahNjoroge](https://github.com/)


## Description
This is a web application that allows various users to submit a short blog. Users can also be able to view other blogs from other users, delete and close. For a user to do any of that, they need to have registered.

## User Stories
* As a user I would like to view the different blogs.
* As a user I would like to see the blogs other people have posted.
* As a user I would like to comment on the different blogs and leave feedback.
* As a user I would like to submit a blog in any category.
* As a user I would like to vote on the blog they liked and give it a delete or close.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Blogs  | N/A | Various blogs  |
|Display Blogs | **Click** on a Category| A page with a list of blogs |
|Add new blog | **Click** New pitch | User Should register/sign in to add new blog |
|View Blogs | **Click** on a pitch | View a blog and comments |
|Comment on a blog | **Click** Comment | Registered User displays a form where a user can comment on a certain blog |
|Delete a blog | **Click** glyphicon delete| Delete a specific blog increases |
|Close a blog | **Click** glyphicon close | Close a specific blog decreases |

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* $ git clone https://github.com/MaratahNjoroge/blog-app
* $ cd blog-app
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh


# How it works

* A user needs to sign up
* A user the needs to sign in to blog and post blog

# CREDITS

#### Google.com, StackOverflow.com and Miguel Grinberg -author of 'Flask Web Development, 2nd Edition'


# Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through maratah7@gmail.com or leave a commit here on github.


## Known Bugs
User image avartar does not function properly.

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap
- PostgreSQL

### License

**[MIT](./LICENSE)** (c) 2017 **[MaratahNjoroge](https://maratahnjoroge.github.io/Portfolio-LP/)**

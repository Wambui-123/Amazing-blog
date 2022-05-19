# Amazing-blog

# Author
Yvonne Muthui

# Description
A flask application that has people can post, delete and comment on blogs that they desire from there own account and can view for others as well. It also auto generates quotes every time you login in to your blog.


## User Story ( BDD ) 
The user would like to.... :
+  to see various blogs on the homepage of the application.
+  see all blogs that have been posted by me and others in the application.
+  update my profile.
+  delete a post i no longer want.

## [Live Link](https://amazinggggggg.herokuapp.com/quote) click to view


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3
* flask
* gunicorn
* bootstrap
* SQlAlchemy

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ``https://github.com/Wambui-123/Amazing-blog.git``



* cd my_news_flask

* Vs code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:
 * #### create flask environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ chmod +x launcher.py
        $ ./launcher.py
* #### Install Flask and other dependencies/Modules
        $ pip install flask
        $ pip install flask-Bootstrap ( optional)
* #### set up the API KEY
        + create account in [https://amazing-blog.org] and key will be issued
        + in root fold of your app create  a folder,config file in it and paste you API key and add it to .gitignore
        + alternatively have any python file in root folder and :
            export NEWS_API_KEY='<Your-Api-Key goes here>'
            python3 manage.py server
* #### Run app using vs terminal or main terminal
        $ chmod +x launch.sh
        $ ./launch.sh


## Technologies Used
  
* Python3
* Flask Webframework
* HTML
* CSS  
   


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions, please email me at [yvonnewambui28@gmail.com](yvonnewambui28@gmail.com)




Portfolio- [Yvonne](https://github.com/Wambui-123)
# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Yvonne Muthui

![white_logo_iCoach.PNG](images%2Fwhite_logo_iCoach.PNG)
# iCoach

The main idea of this project is to create convenient app for management sport academies of the group sports.
This database stores information about all players, coaches of the teams. Service provides easy access and share of all
information between administrative and manager staff. 

## Features
* Authentication functionality for Coach/Administrator
* New teams and players profiles can be added and kept in one list 
* Registered coach can assign himself to the team in Team detail page 
* Team detail page automatically counts number of players in the team 
* Each player, coach and team have they own detail page 
* Players can be filtered by last name 
* Custom admin panel

## Getting started

Python3 must be installed

```shell
git clone https://github.com/anastasiia-tsurkan/iCoach.git
cd iCoach 
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
```

copy .env_sample -> .env and populate with all required data

```shell
python manage.py migrate
python manage.py runserver
```

## Try it out

Use the following user to log in and check the functionality of the admin site:
```shell
login: admin.user
password: 1qazcde3
```
Use this one to log in and try functionality of the Website

```shell
login: user
password: user12345
```

### Deploying 

[Library project deployed to Render](https://icoach.onrender.com)

## Demo
![demo_home.png](images%2Fdemo_home.png)
![demo_players.png](images%2Fdemo_players.png)

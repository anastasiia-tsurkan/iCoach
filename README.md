# iCoach

The main idea of this project is to create convenient app for management sport academies of the group sports.
This database stores information about all players, coaches of the teams. Service provides easy access and share of all
information between administrative and manager staff. 

Use the following user to log in and check the functionality of the website:
login: admin.user
password: 1qazcde3

Features of the webserver:
1. Authentication functionality for Coach/Administrator
2. New teams and players profiles can be added and kept in one list
3. Registered coach can assign himself to the team in Team detail page
4. Team detail page automatically counts number of players in the team
5. Each player, coach and team have they own detail page
6. Players can be filtered by last name 
7. Custom admin panel

Installation and requirements: 
- Python3

git clone https://github.com/anastasiia-tsurkan/iCoach.git
cd iCoach
python3 -m venv venv
source venv/bin/activate  # on macOS
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
copy .env.sample -> .env and populate with all required data
python manage.py migrate
python manage.py runserver


# Trip Split 
## Django web application for the commuters and road trips 

A web application designed to help plan and assist road trip planners. The idea was originally started with the intent of easing the gas splitting for drivers and passangers. A user will select their current car from our database, select their route, and input the passengers (which will automatically allow the user to create a Venmo or Paypal request). Once the trip has been split, the user will have further cheap gas options and other events to visit while on their road trip. 

This repository is currently running as a RESTful API for the VueJSCarApp repository. The project has taken on a more client-side approach while utilizing Django Rest Framework. 

## To Run the Front End
``` bash
cd Front-end
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

## To Run the Back End
``` bash
# Set up your Virtual Environment
cd Back-end
virtualenv -p python3 .
Source bin/activate
pip install -r requirements.txt

# Set up Django
python3 manage.py migrate
python3 manage.py loaddata fixtures/data.json

# build for production with minification
python3 manage.py runserver
```
## Current Setup
Front: Vue.JS, Webpack
Back: Django, Django-rest-framework
Database: Sqlite (Don't need Postgres Anymore)

## Current UI Design 
![](/ui/slide0.png)
![](/ui/Slide1.png)
![](/ui/slide2.png)
![](/ui/slide3.png)


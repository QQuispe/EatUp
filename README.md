# EatUp

EatUp is an interactive web application to find the nearest restaurants between two people.

## Built With:
* Django
* Python 
* Bootstrap 4

## Prerequisites

This web app uses Google's Places, Geocoding, and Maps Javascript API's. Optain your Google API key [here](https://cloud.google.com).

It also uses a Yelp API key to obtain restaurant information. Get your Yelp API key [here](https://www.yelp.com/developers).

Once you have both you will need to place them in a `.env` file later. You can copy the `.env.example` template for this.

## Getting Started

Clone project
```
git clone https://github.com/QQuispe/EatUp
```

Install dependencies in a virtual environment
```
cd EatUp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file in root directory and add your API keys from earlier
```
GOOGLE_MAPS_KEY="YOUR_API_KEY"
YELP_KEY="YOUR_API_KEY"
...
```

Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Run server
```
python manage.py runserver
```

## Demo

![Home page](https://github.com/QQuispe/EatUp/blob/master/EatUp/readme_assets/EatUp_home.png?raw=true)


![Results page](https://github.com/QQuispe/EatUp/blob/master/EatUp/readme_assets/EatUp_results.png?raw=true)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This project was initially created with the help of Farshad, Farhan, and Colin.
[![Build Status](https://travis-ci.org/osya/tryTen.svg)](https://travis-ci.org/osya/tryTen)

Django-based eCommerce project, created during the video series [Learn Python and Django - Build an eCommerce Website Step by Step from Scratch](https://www.youtube.com/watch?v=9Wbfk16jEOk)

Used technologies:
- Testing: Selenium & PhantomJS & Factory Boy
- Assets management: NPM & Webpack
- Travis CI
- Deployed at [Heroku](https://tryten.herokuapp.com/)

Installation:
```
    https://github.com/osya/tryTen
    cd tryTen
    pip install -r requirements.txt
    npm install
    node node_modules/webpack/bin/webpack.js
    python manage.py collectstatic
    python manage.py runserver
```

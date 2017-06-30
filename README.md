# Movies Trailers

Movies Trailers is a web based application to display movies trailers. The app admin will store the movies entries in the admin page and users will be able to see the movie cover, its title and a brief sinopse. If the user then clicks in the movie cover, then the movie trailer will be displayed in a modal.

## Requirements

In order to properly get this application up and running, please make sure you have the following requirements on place:

* Django 1.10
* Python 3 or greater (project created in Python 3.6.0)
* Git

## Quickstart

To get the project source code, clone it on your local machine:

`$ git clone https://github.com/wederribas/movies-trailers.git`

It's not required, but strongly recommended, that you use a virtual environment to work in Python projects. To acomplish that, install **virtualenv** and create a new environment:

```
# Install package
$ pip install virtualenv

# Create new env
$ virtualenv movies_trailers

# Activate it
$ source my_project/bin/activate
```

Install Django:

`$ pip install Django==1.10`

Run the local development server (inside the project root folder):

`$ python manage.py runserver`

## Attention

This project has already a sample data **(stored in db.sqlite3 file)** with some sample movies already registered. To create new entries or edit the existing ones, access the admin page with the password **udacityfsnd**.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/wederribas/movies-trailers/blob/master/LICENSE) file for details.

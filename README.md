# ImgQuik

ImgQuik is a web app that can create placeholder images on the fly based on certain parameters.

For example:-
  - imgquik.herokuapp.com/100x200 will create an image of width 100 px and height 200 px.
  - imgquik.herokuapp.com/100x200/FF0000 will give it a red background color additionally.
  - imgquik.herokuapp.com/100x200/FF0000/FFFFFF will furthermore give it a white foreground color.

### Local Installation

ImgQuik requires [Django](https://www.djangoproject.com/) to run.

Install the dependencies from the `requirements.txt` file.

```sh
$ cd imgquik
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the app home, or add paramters to it as shown above to generate images.
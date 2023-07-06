# We are making up an online library.

In the project we study the basics of layout `Bootstrap` and template engine `Jinga2`.

In the previous project we learned how to parse data from the online library tululu.org
1. [By page and category](https://github.com/nekto007/books_library_restyle)


We use the data (downloaded books and book covers) and the data structure in the format `json` in this project.


# How to install

Download the code from the repository.

Python3 must already be installed. 
Then use pip (or pip3 if there is a conflict with Python2) to install the dependencies:

```Python.
pip install -r requirements.txt
```

## Example run

```Python
python render_website.py
``` 
After run render_website.py: http://127.0.0.1:5500/pages/index1.html

## Offline run book library
After download project open file pages/index1.html

The script generates website pages in the ``pages`` directory.  
The finished pages can run locally.

To see an example of how the site works, visit [GitHub Pages](https://nekto007.github.io/books-library-restyle-3/pages/index1.html)

## Project goals

The code is written for educational purposes - it's a lesson in a course on Python and web development at [Devman](https://dvmn.org).

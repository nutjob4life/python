# 🐍 Python Junk Drawer

This is a small Python virtual environment that is basically my more-or-less current [Python](https://www.python.org/) "junk drawer", full of miscellaneous tools—written in Python—that I fairly often. It's basically a `requirements.txt` file you can shove into a [virtual environment](https://docs.python.org/3/tutorial/venv.html) of Python.

This includes tools that are "mutually compatible". Some tools don't "play well" and have to have their own environments.


## 📀 Installation

Do something like the following:

```console
$ git clone …
$ cd python
$ python3 -m venv .
$ bin/pip install --quiet --upgrade setuptools wheel pip build
$ bin/pip install --requirement requirements.txt
$ bin/python make-links.py
```

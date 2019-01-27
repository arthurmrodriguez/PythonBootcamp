# Python modules and packages: PyPi and pip

There's a very useful tool called **pip** which allows us to **manage third-party Python packages**, this is, a set of tools developed by the community that are stored over the PyPi repo. In order to install (and further use) Python packages from PyPi, we will have to use the following command ```pip install <package_name>```.

But what if we wanted to create our own **Python Packages (collection of modules)** or **modules** and upload it so the community could use it? We'll se a bit of it in this notebook.

- We first create to Python scripts **mymodule.py** and **myprogram.py** in a working directory.

- Then we create a folder called **MyMainPackage** and a subfolder called *SubPackage* within it. It is necessary to have a file called **__init__.py** inside every single folder of our package so that Python recognizes the hierarchy of folders of our package.

- This is how we organize our files in directories for better and more efficient use (and in behalf of readability). Check **myprogram.py** for syntax on how to import modules from our subpackage.

As stated before, **packages are just a collection of modules (.py scripts)** so now we have our own Python package. While we learn more and more Python, we would also learn how to better organize our scripts in a *package format* that could be used by third-parties.

# Tree Menu
---
 __Installing__
```bash
$ python -m venv venv
```
```bash
Linux:
  $ source venv/bin/activate
Windows:
  $ venv/Scripts/activate
```
```bash
$ pip install -r requirements.txt
# помимо django устанавливается django_debug_toolbar
$ cd tree_menu
$ python manage.py migrate
```
***
__Running__

&emsp;После установки нужно перейти в директорию проекта tree_menu и в консоли ввести:
```bash
$ python manage.py runserver
```
&emsp;Для создания суперпользователя из той же директории ввести в консоль:
```bash
$ python manage.py createsuperuser
```
&emsp;После этого в предложенных полях ввести соответсвующие данные(поле email можно оставить пустым нажав enter).

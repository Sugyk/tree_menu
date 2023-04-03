# Tree Menu
---
 __Installing__
```bash
# клоинруем репозиторий и создаем виртуальное окружение
$ git clone https://github.com/Sugyk/tree_menu.git
$ cd tree_menu
$ python -m venv venv
```
```bash
# активируем виртуальное окружение
Linux:
  $ source venv/bin/activate
Windows:
  $ venv/Scripts/activate
```
```bash
# устанавливаем необходимые библиотеки и выполняем миграции
$ pip install -r requirements.txt
# помимо django устанавливается django_debug_toolbar
$ cd tree_menu
$ python manage.py migrate
```
***
__Running__

&emsp;После установки и активации виртуальной среды нужно перейти в директорию проекта tree_menu с файлом <span>manage.py</span> и в консоли ввести:
```bash
$ python manage.py runserver
```
&emsp;Для создания суперпользователя из той же директории ввести в консоль:
```bash
$ python manage.py createsuperuser
```
&emsp;После этого в предложенных полях ввести соответсвующие данные(поле email можно оставить пустым нажав enter).

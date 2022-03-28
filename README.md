# TodoDRF - будь максимально продуктивным

<p align="left">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pycqa.github.io/isortE"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>


## Что может приложение?
- смотреть список задач
- создавать новую задачу
- детализированный просмотр задачи
- изменение одной задачи
- удаление задачи


## Зависимости (requirements)
```
django<4

black==21.6b0
isort==5.9.1
```


## Установка и локальный запуск
Клонируем:
```
$ git clone https://github.com/AlexKhlybov/gb_drf.git
$ cd gb_drf
```

Создаем и активируем виртуальное окружение:
```
$ python -m venv venv  # use `virtualenv venv` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
```

Устанавливаем зависимости:
```
$ pip install -r requirements.txt
```

Запускаем приложение:
```
$ make run
```


## Pytest
Для запуска тестов, вы можете использовать [pytest](https://docs.pytest.org/en/7.0.x/):
```bash
$ pytest
.......
----------------------------------------------------------------------
Ran 7 tests in 0.076s

OK
```


## Лицензия
MIT


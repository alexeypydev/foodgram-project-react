адрес: 84.201.162.226
обычный юзер: b@b.ru 1234bb1234
админ: c@c.com 1234cc1234

### Проект Foodgram – Продуктовый помощник
Это сервис где вы можете найти любой рецепт по вашему вкусу или поделиться своим, чтобы миллионы людей узнали о нем.

#### Локальный запуск проекта

- Склонируйте удаленный репозиторий
- Создайте виртуальное окружение и установите зависимости
```bash
cd backend
python -m venv venv
. venv/Scripts/activate (for Windows)
. venv/bin/activate (for MacOS/Linux)
pip install -r -requirements.txt
```
- В файле foodgram/settings.py замените БД на дефолтную SQLite
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
- Выполните миграции и соберите статику
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```
- Наполните БД тестовыми данными
```bash
python manage.py load_data
```
- Запустите сервер
```bash
python manage.py runserver 
```

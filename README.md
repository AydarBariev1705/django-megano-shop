# MEGANO ONLINE SHOP

<h3 align="center">Интернет магазин Megano</h3>
Проект разработан на фреймворке Django. 
Обращение к данным происходит по API. API реализован на Django Rest Framework.
За отображение страниц отвечает приложение frontend.
 

## Установка и запуск проекта
1. Клонировать репозиторий, создать и войти в виртуальное окружение
2. `pip install -r requirements.txt` - установка зависимостей
3. Установка frontend:
    * `pip install ./dist/diploma-frontend-0.6.tar.gz` - установка фронтенда
4. Создание бд и загрузка фикстур:
    * `cd ../megano && python manage.py make migrations` - создание миграций
    * `python manage.py migrate` - миграция 
    * `python manage.py loaddata ./fixtures/* ` - установка фикстур
5. `python manage.py runserver` - запуск сервера


В фикстурах созданы товары,заказы,пользователи.
К товарам добавлены тэги, спецификации и отзывы.
У пользователей есть аватарки.


**superuser**

*Логин:* admin

*Пароль:* 12345


**users**

1. *Логин:* sam

   *Пароль:* Sam9350!

2. *Логин:* Lola

   *Пароль:* Lola9350!

3. *Логин:* john

   *Пароль:* john9350!

4. *Логин:* nick

   *Пароль:* nick9350!

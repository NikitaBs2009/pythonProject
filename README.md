# Прикиньте будущую зарплату
## Описание
Проект создан для загрузки данных о зарплатах различных программистов в зависимости от языка программирования. Посик производится по [hh.ru](https://kashira.hh.ru/?ysclid=ljef5hkktp2851748)  и [SuperJob](https://www.superjob.ru/?ysclid=ljef6x0js0186243869).
## Установка 
Скачайте необходимые файлы, затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже. Создайте бота у отца ботов . Создайте новый канал в Telegram.


Установите зависимости командой:
```
pip install -r requirements
```
## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.


Для получения необходимых изображений необходимо написать:
```
python table.py
```
## Переменные окружения 
Часть настроек проетка берётся из переменных окружения. Переменные окружения - Это переменные, значения которых присваются программе Python извне. Чтобы их определить, создайте файл .env рядом с main.py и запишите туда данные в такое формате: ПЕРЕМЕННАЯ=значение.


Пример содержания файла .env:
```
SJ_KEY='SJ_KEY'
```
Получить токен SJ_KEY можно на сайте [API SuperJob](https://api.superjob.ru/?click_id=979Z1YOfpoZB4uf&utm_source=cityads&utm_medium=cpa&utm_campaign=2Keh)
## Цель проетка 
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/) 

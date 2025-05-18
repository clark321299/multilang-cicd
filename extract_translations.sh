#!/bin/bash

# Витягнення рядків для перекладу
pybabel extract -F babel.cfg -o translations/messages.pot .

# Оновлення існуючих перекладів
pybabel update -i translations/messages.pot -d translations

# Або можна ініціалізувати нові мови:
# pybabel init -i translations/messages.pot -d translations -l uk
# pybabel init -i translations/messages.pot -d translations -l en
# pybabel init -i translations/messages.pot -d translations -l de

# Компіляція перекладів
pybabel compile -d translations

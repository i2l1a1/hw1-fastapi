### Просто запуск проекта

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`uvicorn main:app --reload`

### Запуск тестов

`source venv/bin/activate`

`pytest`

Для генерации Allure-отчёта:

1. `pytest` или `rm -rf allure-results && pytest` (чтобы удалить результаты предыдущих прогонов тестов).
2. `allure serve allure-results`, чтобы открыть HTML-отчёт.

> Все скрины находятся в папке `screenshots`.

### Просто запуск проекта

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`uvicorn main:app --reload`

### Запуск тестов

`source venv/bin/activate`

`pytest`

> Покрытие тестами выводится в консоль, а также сохраняется в `coverage.xml`. Сейчас покрытие тестами составляет 98%.

Для генерации Allure-отчёта:

1. `pytest` или `rm -rf allure-results && pytest` (чтобы удалить результаты предыдущих прогонов тестов).
2. `allure serve allure-results`, чтобы открыть HTML-отчёт.

### pre-commit

1. `pre-commit install`.
2. Перед коммитом `pre-commit` запустит `ruff`, `black` и `isort`. При необходимости можно запустить вручную: `pre-commit run --all-files`.

### Инструменты
#### ruff
`ruff check .`

_Результат выполнения я показал на скрине `ruff_check_results.png`._

#### black
`black .`

_Результат выполнения я показал на скрине `black_results.png`._

#### isort
`isort .`

_Результат выполнения я показал на скрине `isort_results.png`._

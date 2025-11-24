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
2. Перед коммитом `pre-commit` запустит `ruff`, `black` и `isort`. При необходимости можно запустить
   вручную: `pre-commit run --all-files`.

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

### mypy

_Результат выполнения `mypy .` до рефакторинга я показал на скрине `mypy_results.png`, а после рефакторинга — на скрине `mypy_results_after_refactor.png`._

Что я поменял, чтобы команда `mypy .` выполнялась без ошибок:

**question.py:**

- Изменил тип поля `id: int` на `id: int | None = None`
- Изменил тип поля `body: str` на `body: str = ""`

**db.py:**

- Добавил импорт `from sqlalchemy.orm import DeclarativeMeta`
- Изменил `Base = declarative_base()` на `Base: DeclarativeMeta = declarative_base()`

**services.py:**

- Добавил `from typing import Optional`
- Изменил параметр конструктора `repo: QuestionRepository = None` на `repo: Optional[QuestionRepository] = None`
- Добавил типы возвращаемых
  значений: `create_question(...) -> QuestionRead`, `get_question(...) -> Optional[QuestionRead]`
- Добавил тип параметра `qid: int` для метода `get_question`
- Добавил проверки `if saved.id is None` и `if q.id is None` с выбросом `ValueError`
- Добавил тип возвращаемого значения `-> QuestionService` для функции `get_question_service`

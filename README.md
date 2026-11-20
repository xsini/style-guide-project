# Стайлгайд Travel Buddy Finder

Учебный проект по лабораторной работе № 3 дисциплины «Проектная документация». Объект — документация Travel Buddy Finder: бизнес-процессы, пользовательские истории, ТЗ, UML-модели и описание клиентского прототипа. Требования целевой системы отделены от реализации по ПР 10.

## Содержимое

В `docs/` находятся правила стиля, словарь, шаблоны и два примера применения с редакторской оценкой. `mkdocs.yml` задаёт сайт и навигацию. `.github/workflows/docs.yml` проверяет документацию и публикует сайт при изменениях в main.

## Подготовка среды

Требуются Python 3.12, Node.js 22, npm и Git. Откройте PowerShell в корне проекта.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm install
```

## Проверка и локальный просмотр

```powershell
npm run lint:md
.\.venv\Scripts\python.exe scripts/check_docs.py
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe -m mkdocs serve
```

Откройте локальный адрес, напечатанный MkDocs. Для macOS и Linux используйте `.venv/bin/python` вместо пути к python.exe.

## Публикация

После создания репозитория `xsini/style-guide-project` выберите в Settings → Pages → Build and deployment источник GitHub Actions. Публикация выполняется после успешных проверок push в main. Для PR запускаются только проверки и сборка, публикация не выполняется.

Ожидаемый адрес после успешного деплоя: `https://xsini.github.io/style-guide-project/`. Само наличие этого адреса в конфигурации не подтверждает публикацию.

## Участие

Порядок создания ветки, коммитов, ревью и добавления раздела описан в [CONTRIBUTING](CONTRIBUTING.md). Раздел доступности добавляется отдельной веткой в рамках задания на PR.

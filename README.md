# Практическая работа № 10

Flask-приложение отвечает на `/` текстом `DevOps CI app`, а на `/health` возвращает JSON `{"status":"ok"}`.

## Локальная проверка

```sh
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m pytest
docker build -t devops-ci-app .
docker run --rm -p 127.0.0.1:8000:8000 devops-ci-app
```

После запуска адрес проверки контейнера — `http://127.0.0.1:8000/health`.

## GitHub Actions

Задания идут в порядке `lint → test → image`. В pull request workflow собирает образ и проверяет оба маршрута. При push в `main` он выполняет те же проверки, затем пытается опубликовать образ `ghcr.io/sonyasot/devops-ci-app` с полным SHA коммита и тегом `latest`.

Для первого запуска токен имеет только `contents: read`. Ожидаемый отказ GHCR при публикации нужно зафиксировать в журнале задания `image`. [Запуски CI](https://github.com/SonyaSot/devops-ci-app/actions/workflows/ci.yml)

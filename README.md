# Практическая работа № 10

Flask-приложение возвращает JSON `{"service":"devops-ci-app","version":"1.0.0","status":"running"}` на `/` и `{"status":"ok"}` на `/health`.

## Локальная проверка

```sh
python -m pip install -r requirements-dev.txt
python -m pylint app tests/test_app.py
python -m pytest
docker build -t devops-ci-app .
docker run --rm -p 127.0.0.1:5000:5000 devops-ci-app
```

После запуска адрес проверки контейнера — `http://127.0.0.1:5000/health`.

## GitHub Actions

Задания идут в порядке `lint → test → image`. В pull request workflow собирает образ, выводит в журнал результат `docker exec ci-app id` и проверяет `/health` на порту `5000`. При push в `main` он выполняет те же проверки, затем пытается опубликовать образ `ghcr.io/sonyasot/devops-ci-app` с полным SHA коммита и тегом `latest`.

Для первого запуска токен имеет только `contents: read`. Ожидаемый отказ GHCR при публикации нужно зафиксировать в журнале задания `image`. [Запуски CI](https://github.com/SonyaSot/devops-ci-app/actions/workflows/ci.yml)

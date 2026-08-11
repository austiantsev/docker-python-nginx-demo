    # Docker Python Nginx Demo

## Описание

Проект запускает простое Python web-приложение за Nginx reverse proxy через Docker Compose.

Nginx принимает запросы от браузера и перенаправляет их во внутренний контейнер с Python-приложением.

## Архитектура

Схема работы:

браузер → localhost:8080 → nginx:80 → app:8080

Где:

- localhost:8080 — порт на хосте
- nginx:80 — Nginx внутри контейнера
- app:8080 — Python-приложение внутри Docker-сети

## Файлы проекта

- app.py — простое Python web-приложение
- Dockerfile — инструкция для сборки Docker image с Python app
- nginx.conf — конфигурация Nginx reverse proxy
- docker-compose.yml — описание сервисов app и nginx, портов, env и volumes
- .dockerignore — список файлов, которые не нужно добавлять в build context

## Запуск

```bash
docker-compose up -d
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
```

## Диагностика

### Если сайт не открывается:

### 1. Проверить статус контейнеров:

```bash
docker-compose ps
```
### 2. Проверить логи nginx:

```bash
docker-compose logs nginx
```

### 3. Проверить логи app:

```bash
docker-compose logs app
```
### 4. Проверить конфигурацию nginx внутри контейнера:

```bash
docker exec -it test-nginx nginx -t
```
### 5. Проверить proxy_pass в nginx.conf:

```bash
cat nginx.conf
```

### 6. Проверить переменную PORT внутри app-контейнера:

```bash
docker exec -it my-app sh -c 'echo $PORT'
```

### 7. Проверить, какой порт указан в app.py:

```bash
cat app.py
```

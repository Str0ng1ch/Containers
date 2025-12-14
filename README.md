# lab2:

## Docker Compose

1. **Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему,
   если да, то как?**
    - Да, можно. Например:
   ```yaml
   services:
     app:
       resources:
         limits:
           cpus: 500m
           memory: 512M
         reservations:
           cpus: 500m
           memory: 128M
   ```

2. **Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные**
    - docker-compose up <service_name>. Например:
   ```bash 
   docker-compose up app
   ```
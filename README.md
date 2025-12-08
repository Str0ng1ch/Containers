# lab2:

## Docker Compose

1. **Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему,
если да, то как?**  
   - Да, можно. Например
   
```yaml
services:
  app:
    image: myapp:latest
    resources:
      limits:
        cpus: '0.5'
        memory: 512M
      reservations:
        cpus: '0.1'
        memory: 128M
```

2. **Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные**  
   - docker-compose up <service_name>. Например docker-compose up app
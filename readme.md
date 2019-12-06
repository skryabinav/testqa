## Пример автотеста
### Запуск
Нужно учитывать, что переменная окружения UID в некоторых сборках является readonly, поэтому может возникнуть предупреждение
```bash
export UID=$(id -u)
export GID=$(id -g)
docker-compose -f docker-compose.yml up
```
### Результаты
Результатами автотеста является набор скриншотов, который сохраняется в директории app/report/ и текстовый файл app/report/expsys.log

В случае ошибки там же формируется картинка с именем step_error.png и файл /app/report/expsys_error.log

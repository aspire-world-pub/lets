## LETS с Aspire world

- Происхождение: https://zxq.co/ripple/lets
- Зеркало: https://github.com/osuripple/lets

## Последний необходимый сервер Tatoe
Этот сервер обрабатывает каждую функцию клиента не в реальном времени, поэтому:
- Внутриигровые табло
- Представление баллов
- скриншоты
- повторы
- osu! direct, благодаря [cheesegull](https://github.com/osuripple/cheesegull)
- Tillerino-подобный API (частично сломанный)
- osu! standard и Taiko pp для расчета с [oppai-ng](https://github.com/francesco149/oppai-ng), сделанные Франком [e] sco
- osu! mania pp расчет с немного отредактированной версией [osu-tools](https://github.com/ppy/osu-tools), сделанной osu! команда
- поймать подсчет количества ударов с помощью [catch-the-pp](https://github.com/osuripple/catch-the-pp), сделанного Sunpy и цитонизированного Nyo

## Требования
- Python 3.6
- Cython
- компилятор C

## Как настроить LETS
Прежде всего, инициализируйте и обновите подмодули
```
$ git submodule init && git submodule update
```

После этого установите необходимые зависимости с помощью pip.

```
$ pip install -r needs.txt
```

скомпилируйте все файлы `* .pyx` в файлы` * .so` или `* .dll`, используя` setup.py` (файл distutils).
Это также компилирует `catch-the-pp`.
```
$ python3.6 setup.py build_ext --inplace
```

затем запустите LETS один раз, чтобы создать файл конфигурации по умолчанию и отредактировать его
```
$ python3.6 lets.py
$ nano config.ini
```

наконец, скомпилируйте oppai-ng (внутри pp / oppai-ng) и osu-tools (внутри pp / maniapp-osu-tools).

## tomejerry.py
`tomejerry.py` - это инструмент, который позволяет вам вычислить pp для конкретных результатов. Очень полезно делать массовые пересчеты ПП, если вы что-то напутали. Он использует конфигурации и пакеты lets, поэтому перед его использованием убедитесь, что lets установлен и настроен правильно.

```
использование:tomejerry.py [-h]
                    [-r | -z | -i ID | -М МОДЫ | -g GAMEMODE | -u USERID | -b BEATMAPID | -fhd]
                    [-w WORKERS] [-cs CHUNKSIZE] [-v]
                    

PP Recalc инструмент для пульсации, новая версия.

необязательные аргументы:
  -h, --help показать это справочное сообщение и выйти
  -r, --recalc вычисляет pp для всех рекордов
  -z, --zero вычисляет pp для рекордов 0 pp
  -i ID, --id ID вычисляет pp для счета с этим score_id
  -m MODS, --mods MODS вычисляет pp для высоких результатов с этими модами (флаги)
  -g GAMEMODE, --gamemode GAMEMODE
                        вычисляет pp для очков, сыгранных в этом режиме игры
                        (стандартный: 0, тайко: 1, ctb: 2, мания: 3)
  -u USERID, --userid USERID
                        вычисляет pp для рекордов, установленных конкретным пользователем
                        (Логин пользователя)
  -b BEATMAPID, --beatmapid BEATMAPID
                        вычисляет pp для рекордов, сыгранных на конкретном
                        beatmap (beatmap_id)
  -fhd, --fixstdhd вычисляет pp для рекордов std hd (14/05/2018 pp
                        алгоритм меняется)
  -W WORKERS, -workers WORKERS
                        количество работников. 16 по умолчанию. Макс 32
  -cs CHUNKSIZE, --chunksize CHUNKSIZE
                        размер кусков
  -v, --verbose подробный / режим отладки
```

## Лицензия
Этот проект лицензирован под лицензией GNU AGPL 3.
Смотрите файл "ЛИЦЕНЗИЯ" для получения дополнительной информации.

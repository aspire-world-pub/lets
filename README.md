## LETS [![Code Health](https://landscape.io/github/osuripple/lets/master/landscape.svg?style=flat)](https://landscape.io/github/osuripple/lets/master)

- Origin: https://zxq.co/ripple/lets
- Mirror: https://github.com/osuripple/lets

## Latest Essential Tatoe Server
This server handles every non real time client feature, so:
- Ingame scoreboards
- Score submission
- Screenshots
- Replays
- osu!direct, thanks to [cheesegull](https://github.com/osuripple/cheesegull)
- Tillerino-like API (partially broken)
- osu!standard and taiko pp calculation with [oppai-ng](https://github.com/francesco149/oppai-ng), made by Franc[e]sco
- osu!mania pp calculation with a slightly edited version of [osu-tools](https://github.com/ppy/osu-tools), made by the osu! team
- catch the beat pp calculation with [catch-the-pp](https://github.com/osuripple/catch-the-pp), made by Sunpy and cythonized by Nyo

## Requirements
- Python 3.6
- Cython
- C compiler

## How to set up LETS
First of all, initialize and update the submodules
```
$ git submodule init && git submodule update
```
afterwards, install the required dependencies with pip
```
$ pip install -r requirements.txt
```
compile all `*.pyx` files to `*.so` or `*.dll` files using `setup.py` (distutils file).
This compiles `catch-the-pp` as well.
```
$ python3 setup.py build_ext --inplace
```
then, run LETS once to create the default config file and edit it
```
$ python3 lets.py
$ nano config.ini
```
finally, compile oppai-ng (inside pp/oppai-ng) and osu-tools (inside pp/maniapp-osu-tools).

## tomejerry.py
`tomejerry.py` is a tool that allows you to calculate pp for specific scores. It's extremely useful to do mass PP recalculations if you mess something up. It uses lets' config and packages, so make sure lets is installed and configured correctly before using it.
```
usage: tomejerry.py [-h]
                    [-r | -z | -i ID | -m MODS | -g GAMEMODE | -u USERID | -b BEATMAPID | -fhd]
                    [-w WORKERS] [-cs CHUNKSIZE] [-v]

pp recalc tool for ripple, new version.

optional arguments:
  -h, --help            show this help message and exit
  -r, --recalc          calculates pp for all high scores
  -z, --zero            calculates pp for 0 pp high scores
  -i ID, --id ID        calculates pp for the score with this score_id
  -m MODS, --mods MODS  calculates pp for high scores with these mods (flags)
  -g GAMEMODE, --gamemode GAMEMODE
                        calculates pp for scores played on this game mode
                        (std:0, taiko:1, ctb:2, mania:3)
  -u USERID, --userid USERID
                        calculates pp for high scores set by a specific user
                        (user_id)
  -b BEATMAPID, --beatmapid BEATMAPID
                        calculates pp for high scores played on a specific
                        beatmap (beatmap_id)
  -fhd, --fixstdhd      calculates pp for std hd high scores (14/05/2018 pp
                        algorithm changes)
  -w WORKERS, --workers WORKERS
                        number of workers. 16 by default. Max 32
  -cs CHUNKSIZE, --chunksize CHUNKSIZE
                        score chunks size
  -v, --verbose         verbose/debug mode
```

## License
This project is licensed under the GNU AGPL 3 License.  
See the "LICENSE" file for more information.  

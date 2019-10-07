"""
omppc binding
maked by semyon442
last ver
"""
import subprocess

from common import generalUtils
from common.constants import bcolors
from common.ripple import scoreUtils
from constants import exceptions
from helpers import consoleHelper
from helpers import osuapiHelper
from objects import glob
from common.log import logUtils as log
from helpers import mapsHelper


class OmppcError(Exception):
    pass


class Omppc:

    OMPPC_FOLDER = ".data/omppc"

    def __init__(self, beatmap_, score_):
        self.beatmap = beatmap_
        self.score = score_
        self.pp = 0
        self.getPP()

    def _runProcess(self):
        # Run with dotnet
        command = \
            "luajit /root/osu_aspire/lets-aspire/pp/omppc/omppc.lua " \
            "-b {map} " \
			"-s {score_.score} " \
			"-a {acc} " \
			"-m {score_.mods} ".format(
				map=self.mapPath,
				score_=self.score,
				acc=self.score.accuracy * 100
			)
        log.debug("omppc ~> running {}".format(command))
        process = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE)

        # Get pp from output
        output = process.stdout.decode("utf-8", errors="ignore")
        log.debug("omppc ~> output: {}".format(output))
        pp = 0
        try:
            pp = float(output)
        except ValueError:
            raise OmppcError(
                "Invalid 'pp' value (got '{}', expected a float)".format(output))

        log.debug("omppc ~> returned pp: {}".format(pp))
        return pp

    def getPP(self):
        try:
            # Reset pp
            self.pp = 0

            # Cache map
            mapsHelper.cacheMap(self.mapPath, self.beatmap)

            # Calculate pp
            self.pp = self._runProcess()
        except Exception as e1:
            print(e1)
        except OmppcError as e:
            log.warning("Invalid beatmap {}".format(
                self.beatmap.beatmapID))
            self.pp = 0
        finally:
            return self.pp

    @property
    def mapPath(self):
        return mapsHelper.cachedMapPath(self.beatmap.beatmapID)
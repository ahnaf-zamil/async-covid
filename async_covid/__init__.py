# -*- coding: utf-8 -*-
from async_covid.john_hopkins import Covid as JohnHopkinsCovid
from async_covid.john_hopkins import CovidModel as JohnHopkinsCovidModel
from async_covid.worldometers import Covid as WorldometersCovid
from async_covid import config

__author__ = "K.M Ahnaf Zamil"
__copyright__ = "Copyright 2020, K.M Ahnaf Zamil"
__license__ = "MIT"
__version__ = "0.0.11"


def Covid(source=config.JOHN_HOPKINS):
    if source == config.JOHN_HOPKINS:
        return JohnHopkinsCovid()

    if source == config.WORLDOMETERS:
        return WorldometersCovid()

    raise ValueError(f"Allowed sources are {', '.join(config.SOURCES)}")

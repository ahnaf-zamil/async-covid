# -*- coding: utf-8 -*-
from async_covid.john_hopkins import Covid as JohnHopkinsCovid
from async_covid.john_hopkins import CovidModel as JohnHopkinsCovidModel
from async_covid.worldometers import Covid as WorldometersCovid
from async_covid import config

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "2.4.0"


def Covid(source=config.JOHN_HOPKINS):
    if source == config.JOHN_HOPKINS:
        return JohnHopkinsCovid()

    if source == config.WORLDOMETERS:
        return WorldometersCovid()

    raise ValueError(f"Allowed sources are {', '.join(config.SOURCES)}")

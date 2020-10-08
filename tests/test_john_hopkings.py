# -*- coding: utf-8 -*-
""" tests module
"""
import pytest
from async_covid import Covid
from unittest.mock import patch


class MockRequestData:
    @staticmethod
    async def json():
        return {"key": "value"}


async def test_all_data():
    covid = Covid()
    data = await covid.get_data()
    assert data is not None
    assert type(data) == list
    element = data[0].dict()
    assert "country" in element
    assert "confirmed" in element
    assert "deaths" in element
    assert "recovered" in element
    assert "latitude" in element
    assert "longitude" in element
    assert "last_update" in element


async def test_get_by_country_id():
    covid = Covid()
    countries = covid.list_countries()
    country = filter(lambda country: country.name == "Sweden", countries)
    country = next(country)
    data = await covid.get_status_by_country_id(country.id).dict()
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "Sweden"


async def test_get_by_country_name():
    covid = Covid()
    data = await covid.get_status_by_country_name("sweden").dict()
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "Sweden"


async def test_get_by_country_name_initials():
    covid = Covid()
    data = await covid.get_status_by_country_name("US").dict()
    assert type(data) is dict
    assert "country" in data
    assert "confirmed" in data
    assert "active" in data
    assert "deaths" in data
    assert "recovered" in data
    assert "latitude" in data
    assert "longitude" in data
    assert "last_update" in data
    assert data["country"] == "US"


async def test_get_by_country_invalid_name():
    covid = Covid()
    with pytest.raises(ValueError):
        await covid.get_status_by_country_name("USA").dict()


async def test_total_active_cases():
    covid = Covid()
    data = await covid.get_total_active_cases()
    assert type(data) is int


async def test_total_confirmed_cases():
    covid = Covid()
    data = await covid.get_total_confirmed_cases()
    assert type(data) is int


async def test_total_deaths():
    covid = Covid()
    data = await covid.get_total_deaths()
    assert type(data) is int


async def test_total_recovered():
    covid = Covid()
    data = await covid.get_total_recovered()
    assert type(data) is int


async def test_list_countries():
    covid = Covid()
    countries = covid.list_countries()
    assert type(countries) == list


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_get_total_active_cases(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_total_active_cases()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_get_total_confirmed_cases(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_total_confirmed_cases()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_get_total_recovered(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_total_recovered()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_total_deaths(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_total_deaths()


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_get_country_by_id(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_status_by_country_id(50)


@patch("covid.john_hopkins.covid.requests.get", return_value=MockRequestData())
async def test_exception_rasied_on_get_country_by_name(mock):
    covid = Covid()
    with pytest.raises(Exception):
        await covid.get_status_by_country_name("italy")

# -*- coding: utf-8 -*-
""" Covid coronavirus statistics based on John Hopkins University statistics

"""
from async_covid.john_hopkins.models import CovidModel, CountryModel
import requests
import aiohttp
import json
from async_covid import config

BASE_URL = "https://services1.arcgis.com"
PATH = (
    "/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query"
)
URL = BASE_URL + PATH
SOURCE = config.JOHN_HOPKINS

async def fetch(session, url, params):

    response = await session.get(url, params=params)
    response = await response.read()
    return json.loads(response)

class Covid:
    """Class handells all functionality

    """

    def __init__(self):
        self.source = SOURCE

    @staticmethod
    async def __get_total_cases_by_country_id(object_id: str) -> dict:
        """Method formats and encodes the URL for a specific country information regarding Covid
        
        Args:
            object_id (str): Country ID e.g. 14 for Bangladesh
        
        Returns:
            dict: Country related information regarding Coronavirus
            example:
                    {
                        'country': 'Sweden',
                        'confirmed': 355,
                        'active': 334,
                        'deaths': 0,
                        'recovered': 1,
                        'latitude': 63.0,
                        'longitude': 16.0,
                        'last_update': 1583893094000
                    }
        """

        params = dict(
            f="json",
            where=f"OBJECTID = {object_id}",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            resultOffset="0",
            resultRecordCount="1",
            cacheHint="true",
        )
        async with aiohttp.ClientSession() as session:
            response = await fetch(session, URL, params=params)
        try:
            return response["features"][0]["attributes"]
        except KeyError:
            raise Exception(response)

    async def __get_total_by_case(self, case: str) -> int:
        """Method fetchs the total value of a specific case (Deaths, Confirmed cases and Recovered cases)
        
        Args:
            case (str): cases = "Deaths", "Confirmed" and "Recovered"
        
        Returns:
            int: Total value
        """
        params = dict(
            f="json",
            where="Confirmed > 0",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            outStatistics=str(
                [
                    {
                        "statisticType": "sum",
                        "onStatisticField": f"{case}",
                        "outStatisticFieldName": "value",
                    }
                ]
            ),
            cacheHint="true",
        )
        async with aiohttp.ClientSession() as session:
            response = await fetch(session, URL, params=params)
        try:
            return int(response["features"][0]["attributes"]["value"])
        except KeyError:
            raise Exception(response)

    async def __get_all_cases(self) -> list:
        """Method fetches all data related to Covid
        
        Returns:
            list: list of Covid data
                example:
                        [
                            {
                                'id': '53',
                                'country': 'China',
                                'confirmed': 81020,
                                'active': 9960,
                                'deaths': 3217,
                                'recovered': 67843,
                                'latitude': 30.5928,
                                'longitude': 114.3055,
                                'last_update': 1584097775000
                            }
        """
        params = dict(
            f="json",
            where="Confirmed > 0",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            orderByFields="Confirmed desc",
            resultOffset="0",
            resultRecordCount="200",
            cacheHint="true",
        )
        async with aiohttp.ClientSession() as session:
            response = await fetch(session, URL, params=params)
        try:
            return response["features"]
        except KeyError:
            raise Exception(response)

    async def get_data(self) -> list:
        """Method fetches all data related to Covid
        """

        cases = await self.__get_all_cases()
        return [CovidModel(**case["attributes"]) for case in cases]

    async def get_total_active_cases(self) -> int:
        """Method fetches and returns total number of active cases
        
        Returns:
            int: Total number of active at this time
        """
        return await self.__get_total_by_case("Active")

    async def get_total_deaths(self) -> int:
        """Method fetches and returns total deaths number
        
        Returns:
            int: Total number of deaths at this time
        """
        return await self.__get_total_by_case("Deaths")

    async def get_total_confirmed_cases(self) -> int:
        """Method fetches and returns the total number of confirmed cases
        
        Returns:
            int: Total number of confirmed cases at this time
        """
        return await self.__get_total_by_case("Confirmed")

    async def get_total_recovered(self) -> int:
        """Method fetches and returns the total number of recovered cases
        
        Returns:
            int: Total number of recovered cases at this time
        """
        return await self.__get_total_by_case("Recovered")

    async def list_countries(self) -> list:
        """Method returns the names of all countries available, so that it can be used when
        querying status by a specific country

        Returns:
            list[async_covid.JohnHopkinsCovidModel]: list of country models
        """
        cases = await self.__get_all_cases()
        return [CountryModel(**case["attributes"]) for case in cases]

    async def get_status_by_country_id(self, country_id) -> dict:
        """Method fetches and returns specific country information related to coronavirus
        
        Args:
            country_id (str):  Country ID e.g. 14 for Bangladesh
        
        Returns:
            async_covid.JohnHopkinsCovidModel: Country related information regarding Coronavirus
            example:
                    CovidModel<id=14, country=Bangladesh, confirmed=374592, active=80816, deaths=5460, recovered=288316, latitude=23.685, longitude=90.3563, last_update=1602159825000>
        """

        case = await self.__get_total_cases_by_country_id(country_id)
        return CovidModel(**case)

    async def get_status_by_country_name(self, country_name) -> dict:
        """Method fetches and returns specific country information related to coronavirus
        
        Args:
            country_name (str):  Country name e.g. "sweden"
        
        Returns:
            async_covid.JohnHopkinsCovidModel: Country related information regarding Coronavirus
            example:
                    CovidModel<id=14, country=Bangladesh, confirmed=374592, active=80816, deaths=5460, recovered=288316, latitude=23.685, longitude=90.3563, last_update=1602159825000>
        """

        country = filter(
            lambda country: country.name.lower() == country_name.lower(),
            await self.list_countries(),
        )
        try:
            country = next(country)
        except StopIteration:
            raise ValueError(
                f"There is no country called '{country_name}', to check available country names use `list_countries()`"
            )
        case = await self.__get_total_cases_by_country_id(country.id)
        return CovidModel(**case)

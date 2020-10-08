# -*- coding: utf-8 -*-
"""Sample example used for testing purposes

"""

from async_covid import Covid
import asyncio

async def johnhopkinsdata(covid):
    print("John Hopkins University data\n\n")
    deaths = await covid.get_total_deaths()
    confirmed = await covid.get_total_confirmed_cases()
    recovered = await covid.get_total_recovered()

    print(f"Confirmed: {confirmed:,}")
    print(f"Deaths: {deaths:,}")
    print(f"Recovered: {recovered:,}")
    cases = await covid.get_status_by_country_id(14)
    print(f"Bangladesh Cases: {cases}")
    cases = await covid.get_status_by_country_name("US")
    print(f"USA Cases: {cases}")

async def worldometersdata(covid):
    print("\n\nWorldometers data\n\n")
    deaths = await covid.get_total_deaths()
    confirmed = await covid.get_total_confirmed_cases()
    recovered = await covid.get_total_recovered()
    active = await covid.get_total_active_cases()

    print(f"Confirmed: {confirmed:,}")
    print(f"Deaths: {deaths:,}")
    print(f"Recovered: {recovered:,}")
    print(f"Active: {active:,}")
    cases = await covid.get_status_by_country_name("Bangladesh")
    print(f"Bangladesh Cases: {cases}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    hopkins = Covid(source="john_hopkins")
    loop.run_until_complete(johnhopkinsdata(hopkins))
    """
    Warning: Instantiate this(worldometer) object only when necessary, the worldometers source collects
    "all" of the data at once when instantiated so it will slow down your code everytime you make an instance
    of this object. But it's not an issue with john hopkins source.
    """
    worldometer = Covid(source="worldometers") 
    loop.run_until_complete(worldometersdata(worldometer))
    loop.close()
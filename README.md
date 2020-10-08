# Async Covid

Based on Ahmednafies' COVID [module](https://github.com/ahmednafies/covid).

## Description

An async Python package to get information regarding the novel corona virus provided
by Johns Hopkins university and worldometers.info

Documentation not ready yet, but everything is shown in this README file.

![corona.jpeg](docs/img/corona.jpeg)

## Requirements

    python >= 3.6

## How to install

    pip install async-covid

## Dependencies

    pydantic
    asyncio
    aiohttp

## How to use

## John Hopkins University API

![john_hopkins](docs/img/john_hopkins.png)

### Get All Data

```python
from async_covid import Covid

covid = Covid()
# Make sure you are using an async function
print(await covid.get_data())
```

#### Result

```python
[
    CovidModel<
        id=175, 
        country=US, 
        confirmed=7554434, 
        active=4342532, 
        deaths=211905, 
        recovered=2999895, 
        latitude=40.0, 
        longitude=-100.0, 
        last_update=1602163423000
        >,
    CovidModel<
        id=14, 
        country=Bangladesh,
        confirmed=374592, 
        active=80816,
        deaths=5460,
        recovered=288316,
        latitude=23.685, 
        longitude=90.3563, 
        last_update=1602163423000
        >,
    ...
]
```

### List Countries

This comes in handy when you need to know the available names of countries
when using `get_status_by_country_name`, eg. "The Republic of Moldova" or just "Moldova"
So use this when you need to know the country exact name that you can use.

```python
# Make sure you are using an async function
countries = await covid.list_countries()
```

#### Result

```python
[
    CountryModel<id=175, name=US>, 
    CountryModel<id=80, name=India>,
    ...
]
```

### Get Status By Country ID

```python
italy_cases = await covid.get_status_by_country_id(14)
```

#### Result

```python
CovidModel<
    id=14, 
    country=Bangladesh, 
    confirmed=374592,
    active=80816,
    deaths=5460, 
    recovered=288316,
    latitude=23.685,
    longitude=90.3563,
    last_update=1602163423000
>
```

### Get Status By Country Name

```python
italy_cases = await covid.get_status_by_country_name("bangladesh")
```

#### Result

```python
CovidModel<
    id=14, 
    country=Bangladesh, 
    confirmed=374592,
    active=80816,
    deaths=5460, 
    recovered=288316,
    latitude=23.685,
    longitude=90.3563,
    last_update=1602163423000
>
```

### Get Total Active cases

```python
active = await covid.get_total_active_cases()
```

### Get Total Confirmed cases

```python
confirmed = await covid.get_total_confirmed_cases()
```

### Get Total Recovered cases

```python
recovered = await covid.get_total_recovered()
```

### Get Total Deaths

```python
deaths = await covid.get_total_deaths()
```

## Getting data from Worldometers.info

![worldometers](docs/img/worldometers.png)

```python
covid = Covid(source="worldometers")
```

### Get Data

```python
await covid.get_data()
```

#### Result

```python
[
    CovidModel<
    country=North America, 
    confirmed=9332106, 
    new_cases=10355, 
    deaths=322513, 
    recovered=6101706,
    active=2907887, 
    critical=17932,
    new_deaths=512,
    total_tests=0,
    total_tests_per_million=0,
    total_cases_per_million=0, 
    total_deaths_per_million=0,
    population=0>
    ...
]

```

### Get Status By Country Name

```python
await covid.get_status_by_country_name("india")
```

#### Result

```python
CovidModel<
country=India,
confirmed=6835655,
new_cases=2667,
deaths=105554,
recovered=5827704,
active=902397,
critical=8944,
new_deaths=0, 
total_tests=83465975
>
```

### List Countries

```python
countries = await covid.list_countries()
```

#### Result

```python
[
    'china',
    'italy',
    'usa',
    'spain',
    'germany',
...
]
```

### Get Total Active cases

```python
active = await covid.get_total_active_cases()
```

### Get Total Confirmed cases

```python
confirmed = await covid.get_total_confirmed_cases()
```

### Get Total Recovered cases

```python
recovered = await covid.get_total_recovered()
```

### Get Total Deaths

```python
deaths = await covid.get_total_deaths()
```

```

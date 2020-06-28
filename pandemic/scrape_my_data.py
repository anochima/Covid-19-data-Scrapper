from .models import *
from bs4 import BeautifulSoup
import requests


def scrapeNigeria():
    page = requests.get('https://covid19.ncdc.gov.ng/report')
    soup = BeautifulSoup(page.content, 'html.parser')
    nigerian_pandemic_table = soup.find('table', id='custom1')
    pandemic_data = nigerian_pandemic_table.find_all('td')

    states = []
    total = []
    active = []
    discharge = []
    deaths = []
    zipped_record = (zip(states, total, active, discharge, deaths))
    # Getting cases per state and appending to each respective list
    i = 1
    for data in pandemic_data:
        if i % 5 == 1:
            states.append(data.text.strip())
        if i % 5 == 2:
            total.append(data.text.strip())
        if i % 5 == 3:
            active.append(data.text.strip())
        if i % 5 == 4:
            discharge.append(data.text.strip())
        if i % 5 < 1:
            deaths.append(data.text.strip())
        i += 1

    # moving records gotten to database
    try:
        for (state, totals, actives, discharges, death) in zipped_record:
            if not NigerianCases.objects.filter(states=state, total_cases=totals, active_cases=actives,
                                                discharged=discharges, death_cases=death):
                NigerianCases.objects.create(states=state,
                                             total_cases=totals,
                                             active_cases=actives,
                                             discharged=discharges,
                                             death_cases=death)
    except:
        print('Records already exists')

    # Getting record for overall total, actives, discharged and death
    every_case = []
    all_cases = soup.find_all('h2', class_='text-right text-white')
    # Getting general total cases
    for each_case in all_cases:
        each_case.find_all('span')
        every_case.append(each_case.text.strip())
    tested_samples = every_case[0]
    confirmed_cases = every_case[1]
    total_active = every_case[2]
    total_discharged = every_case[3]
    total_death = every_case[4]
    try:
        if not NigeriaTotalCases.objects.filter(nigeria_total_cases=confirmed_cases,
                                                nigeria_active_cases=total_active,
                                                nigeria_total_discharge=total_discharged,
                                                nigeria_total_deaths=total_death):
            NigeriaTotalCases.objects.update(nigeria_total_cases=confirmed_cases,
                                             nigeria_active_cases=total_active,
                                             nigeria_total_discharge=total_discharged,
                                             nigeria_total_deaths=total_death)
    except:
        print('Error Uploading record')


def scrapeGlobal():
    # Rough data list
    countries_content = []
    country_data = []

    # Main data list to work with
    country_name = []
    country_total_case = []
    country_total_deaths = []
    country_total_recovery = []

    zip_country_record = zip(country_name, country_total_case, country_total_deaths, country_total_recovery)
    page = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid19-container')
    soup = BeautifulSoup(page.text, 'html.parser')
    globaltable = soup.find(id='thetable')
    content = globaltable.find('tbody')
    table_header_in_content = content.find_all('th')

    # Getting Countries names contained in the Table header
    for a_tag in table_header_in_content:
        countries_content.append(a_tag.text.strip())

    # Sanitizing data for countries name
    for i in countries_content:
        if i == '':
            countries_content.remove(i)
    for name in countries_content:
        country_data.append(name.split('[')[0])
    for k in country_data[10:]:
        country_name.append(k)
    global_case_summary = country_data[6]
    global_death_summary = country_data[7]
    global_recovery_summary = country_data[8]
    print(global_case_summary)
    # Getting the each country's case
    country_case_records = content.find_all('td')
    i = 1
    for each_record in country_case_records:
        if i % 4 == 1:
            country_total_case.append(each_record.text.strip())
        if i % 4 == 2:
            country_total_deaths.append(each_record.text.strip())
        if i % 4 == 3:
            country_total_recovery.append(each_record.text.strip())
        i += 1
    last_element = country_total_deaths[-1]
    country_total_deaths.remove(last_element)
    try:
        # Pushing country records gotten to database
        for (country_name, country_totals, country_recoveries, country_death) in zip_country_record:
            if not GlobalCases.objects.filter(country=country_name,
                                              country_total_cases=country_totals,
                                              country_recovery=country_recoveries,
                                              country_total_deaths=country_death):
                GlobalCases.objects.create(country=country_name, country_total_cases=country_totals,
                                           country_recovery=country_recoveries,
                                           country_total_deaths=country_death, )

        if not GlobalTotalCases.objects.filter(global_total_cases=global_case_summary,
                                               global_total_recovery=global_recovery_summary,
                                               global_total_deaths=global_death_summary):
            GlobalTotalCases.objects.update(global_total_cases=global_case_summary,
                                             global_total_recovery=global_recovery_summary,
                                             global_total_deaths=global_death_summary)
    except:
        print('Error Uploading record')

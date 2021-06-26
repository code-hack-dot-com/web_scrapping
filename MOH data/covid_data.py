from requests_html import HTMLSession
import csv
from datetime import date
import schedule
import time

url = 'https://infogram.com/copy-s-dashboard-ringkas-1h706ep50q1745y'
# url ='https://e.infogram.com/40f9ebf7-de33-4859-8a35-6eff09e30eae?parent_url=http%3A%2F%2Fcovid-19.moh.gov.my%2F&src=embed#async_embed'

sess = HTMLSession()
req = sess.get(url)

req.html.render(sleep=1)
print("status code is: ", req.status_code)

total_cases_throughout = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[30]/div/div/div/div/div/div/div/div/div/div/div/h2/div',
    first=True).text
# total_cases_throughout = req.html.xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[30]/div/div/div/div/div/div/div/div/div/div/div/h2/div/span/span', first=True).text
print(total_cases_throughout)

new_case = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[11]/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span',
    first=True).text
new_cases = new_case[new_case.find('+') + 1:]
print(new_cases)

total_discharged = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[20]/div/div/div/div/div/div/div/div/div/div/div/h2/div/span/span',
    first=True).text
print(total_discharged)

new_discharged_case = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[24]/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span',
    first=True).text
new_discharged_case = new_discharged_case[new_discharged_case.find('+') + 1:]
print(new_discharged_case)

percentage_discharged = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[39]/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span',
    first=True).text
percentage_discharged = percentage_discharged[:percentage_discharged.find('%')]
print(percentage_discharged)

active_cases = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[18]/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span',
    first=True).text
print(active_cases)

icu_patients = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[35]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/span/span',
    first=True).text
print(icu_patients)

respiratory_assistance = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[36]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/span/span',
    first=True).text
print(respiratory_assistance)

total_deaths = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[19]/div/div/div/div/div/div/div/div/div/div/div/h2/div/span/span',
    first=True).text
print(total_deaths)

new_death_cases = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[27]/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span',
    first=True).text
new_death_cases = new_death_cases[new_death_cases.find('+') + 1:]
print(new_death_cases)

percentage_death = req.html.xpath(
    '/html/body/div[1]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[38]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/span/span',
    first=True).text
percentage_death = percentage_death[:percentage_death.find('%')]
print(percentage_death)

# lets write the data to CSV file
today = date.today().strftime("%d/%m/%Y")
with open('covid_data_file.csv', 'w', newline='') as outcsv:
    writer = csv.DictWriter(outcsv,
                            fieldnames=["Date", "Total Cases", "New cases", "Total Discharged", "New Discharged Cases",
                                        "Percentage Discharged", "Active Cases", "ICU Patients",
                                        "Respiratory Assistance", "Total Death", "New Death Cases", "Percentage Death"])
    writer.writeheader()
with open(r'covid_data_file.csv', 'a', newline='') as csvfile:
    fieldnames = ["Date", "Total Cases", "New cases", "Total Discharged", "New Discharged Cases",
                  "Percentage Discharged", "Active Cases", "ICU Patients", "Respiratory Assistance", "Total Death",
                  "New Death Cases", "Percentage Death"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'Date': today, 'Total Cases': total_cases_throughout, 'New cases': new_cases,
                     'Total Discharged': total_discharged, 'New Discharged Cases': new_discharged_case,
                     'Percentage Discharged': percentage_discharged, 'Active Cases': active_cases,
                     'ICU Patients': icu_patients, 'Respiratory Assistance': respiratory_assistance,
                     'Total Death': total_deaths, 'New Death Cases': new_death_cases,
                     'Percentage Death': percentage_death})







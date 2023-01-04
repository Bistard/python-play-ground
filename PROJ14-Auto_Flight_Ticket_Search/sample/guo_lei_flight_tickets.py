from prettytable import PrettyTable
import requests
import json
from addresses import Address


def xie_cheng(dcity, acity, date):
    date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    headers = Address.headers
    city = Address.city
    url = 'https://flights.ctrip.com/itinerary/api/12808/products'
    request_payload = {"flightWay": "Oneway",
                       "army": "false",
                       "classType": "ALL",
                       "hasChild": 'false',
                       "hasBaby": 'false',
                       "searchIndex": 1,
                       "portingToken": "3fec6a5a249a44faba1f245e61e2af88",
                       "airportParams": [
                           {"dcity": city.get(dcity), "acity": city.get(acity), "dcityname": dcity, "acityname": acity,
                            "date": date}]}

    # 这里传进去的参数必须为 json
    response = requests.post(url, data=json.dumps(request_payload), headers=headers)
    response = response.text
    routeList = json.loads(response)["data"].get('routeList')
    table = PrettyTable(["Airline", "FlightNumber", "DepartureDate", "ArrivalDate", "PunctualityRate", "LowestPrice"])
    # print("123",routeList)
    for route in routeList:
        if len(route.get('legs')) == 1:
            info = {}
            legs = route.get('legs')[0]
            flight = legs.get('flight')
            info['Airline'] = flight.get('airlineName')
            info['FlightNumber'] = flight.get('flightNumber')
            info['DepartureDate'] = flight.get('departureDate')[-8:-3]
            info['ArrivalDate'] = flight.get('arrivalDate')[-8:-3]
            info['PunctualityRate'] = flight.get('punctualityRate')
            info['LowestPrice'] = legs.get('characteristic').get('lowestPrice')

            table.add_row(info.values())

    print(dcity, '------->', acity, date)
    print(table)


if __name__ == "__main__":
    dcity = input('请输入起点： ')
    acity = input('请输入终点： ')
    date = input('请输入出行日期： ')
    xie_cheng(dcity, acity, date)

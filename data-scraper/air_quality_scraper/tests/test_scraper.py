import unittest
from unittest.mock import patch
import requests
# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from scraper import get_all_stations, get_station_sensors


class TestAirQualityScraper(unittest.TestCase):
    @patch('requests.get')
    def test_get_all_stations_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 14, "stationName": "Działoszyn"}
        ]

        stations = get_all_stations()
        self.assertEqual(len(stations), 1)
        self.assertEqual(stations[0]['stationName'], "Działoszyn")

    @patch('requests.get')
    def test_get_all_stations_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        stations = get_all_stations()
        self.assertEqual(stations, [])

    @patch('requests.get')
    def test_get_station_sensors_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 92, "stationId": 14, "param": {"paramFormula": "PM10"}}
        ]

        sensors = get_station_sensors(14)
        self.assertEqual(len(sensors), 1)
        self.assertEqual(sensors[0]['param']['paramFormula'], "PM10")

    @patch('requests.get')
    def test_get_station_sensors_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        sensors = get_station_sensors(14)
        self.assertEqual(sensors, [])


if __name__ == '__main__':
    unittest.main()

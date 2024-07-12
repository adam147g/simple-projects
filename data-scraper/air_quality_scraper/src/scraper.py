# import sys
# import os
import requests
from threading import Thread, Lock
from config import STATIONS_URL, SENSORS_URL, DATA_URL

# Dodanie głównego katalogu projektu do ścieżki Pythona
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Zamiast tego, można: RB na "src" dir -> "Mark Directory as" -> "Sources Root"

print_lock = Lock()

def send_request(url, resource_type="", identifier=""):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {resource_type} {identifier}: {e}")
        return []

def get_all_stations():
    return send_request(STATIONS_URL, "stations")

def get_station_sensors(station_id):
    url = SENSORS_URL.format(stationId=station_id)
    return send_request(url, "sensors for station", station_id)

def get_sensor_data(sensor_id):
    url = DATA_URL.format(sensorId=sensor_id)
    return send_request(url, "data for sensor", sensor_id)

def count_mean(T):
    return sum(T)/len(T)

def process_station(station):
    station_id = station.get("id")
    station_name = station.get("stationName")
    if not station_id or not station_name:
        with print_lock:
            # Sekcja krytyczna
            print(f"Skipping station with invalid data: {station}")
            # Blokada jest automatycznie zwalniana po zakończeniu tego bloku
        return

    output = [f"Station #{station_id} ({station_name}):\n"]

    sensors = get_station_sensors(station_id)
    if not sensors:
        with print_lock:
            print(f"No sensors found for station {station_id}")
        return

    for sensor in sensors:
        sensor_id = sensor.get("id")
        param_formula = sensor.get("param", {}).get("paramFormula")
        if sensor_id and param_formula:
            output.append(f"Installation #{sensor_id}: '{param_formula}'")
        else:
            output.append(f"Skipping sensor with invalid data: {sensor}")
            continue

        sensor_data = get_sensor_data(sensor_id)
        values = sensor_data.get("values")
        if values:
            all_values = []
            for curr_value in values:
                next_value = curr_value.get("value")
                if next_value:
                    all_values.append(next_value)
            output.append(
                f"Mean: {round(count_mean(all_values), 3) if len(all_values) > 0 else None}")
        else:
            output.append("Error finding values")

    with print_lock:
        print("\n".join(output))
        print("\n")


def scrape_data():
    print("Start scraping...\n")
    stations = get_all_stations()
    threads = []
    for station in stations:
        thread = Thread(target=process_station, args=(station,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    scrape_data()

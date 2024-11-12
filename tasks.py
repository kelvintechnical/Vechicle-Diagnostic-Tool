import time
import random

dtc_codes = {
    "P0010": "Camshaft Position Actuator Circuit",
    "P0102": "Mass Air Flow Circuit Low",
    "P0128": "Coolant Thermostat Malfunction",
    "P0300": "Random/Multiple Cylinder Misfire",
}

def run_diagnostics():
    print("Starting vehicle diagnostics..")
    time.sleep(2)
    print("Scanning for error codes..")
    time.sleep(5)
    error_found = random.sample(list(dtc_codes.key()), 2)
    print("Error codes found")
    for code in error_found:
        print(f'{code}: {dtc_codes[code]}')
    print("Diagnostics complete. ")

run_diagnostics()
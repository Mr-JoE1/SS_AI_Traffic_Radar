import os
import time
import subprocess
from coral.enviro.board import EnviroBoard


def main():
    enviro = EnviroBoard()
    location = "window"
    interval = 1
    command = "chmod 777 install.sh && ./install.sh"

    # Run the command and capture its output and return code
    try:
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
        )
        return_code = 0  # 0 means success
    except subprocess.CalledProcessError as e:
        output = e.output
        return_code = e.returncode

    try:
        while True:
            iso = time.ctime()
            json_body = {
                {
                    "measurement": "temperature",
                    "tags": {
                        "sensor": "coral-enviro-temperature",
                        "location": location,
                        "unit": "celsius",
                    },
                    "time": iso,
                    "fields": {"value": enviro.temperature},
                },
                {
                    "measurement": "humidity",
                    "tags": {
                        "sensor": "coral-enviro-humidity",
                        "location": location,
                        "unit": "percentage",
                    },
                    "time": iso,
                    "fields": {"value": enviro.humidity},
                },
                {
                    "measurement": "ambient_light",
                    "tags": {
                        "sensor": "coral-enviro-ambient-light",
                        "location": location,
                        "unit": "lux",
                    },
                    "time": iso,
                    "fields": {"value": enviro.ambient_light},
                },
                {
                    "measurement": "pressure",
                    "tags": {
                        "sensor": "coral-enviro-pressure",
                        "location": location,
                        "unit": "kPa",
                    },
                    "time": iso,
                    "fields": {"value": enviro.pressure},
                },
            }
            print(str(json_body))

            time.sleep(interval)

    except KeyboardInterrupt:
        print("interrupted!")


if __name__ == "__main__":
    main()

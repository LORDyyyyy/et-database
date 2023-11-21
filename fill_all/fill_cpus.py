import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_cpus(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            core = entry['coreCount']
            preCore = entry['performanceCoreClock']
            preBoost = entry['performanceBoostClock']
            tdp = entry['tdp']
            apu = entry['integratedGraphics']
            smt = entry['smt']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO cpus\
                    (`imageUrl`, `name`, `coreCount`, `performanceCoreClock`,\
                    `performanceBoostClock`, `tdp`, `integratedGraphics`, \
                    `smt`, `price`, `manufactor`) \
                    VALUES \
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, core, preCore, preBoost, tdp, apu, smt,
                      price, man)
            cursor.execute(query, values)
            db_connection.commit()
            print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")
        db_connection.rollback()


def convert_price(value):
    try:
        float_value = float(value)
        return float_value
    except ValueError:
        return 0.0


if __name__ == "__main__":
    fill_cpus("../ready_files/new_cpu.json")
    print('Done')

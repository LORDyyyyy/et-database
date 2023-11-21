import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_gpus(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            chipset = entry['chipset']
            mem = entry['memory']
            core = entry['coreClock']
            boost = entry['boostClock']
            color = entry['color']
            len = entry['length']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO gpus\
                    (imageUrl, name, chipset, memory, coreClock,\
                     boostClock, color, length, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, chipset, mem, core, boost, color, len,
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
    fill_gpus("../ready_files/new_gpu.json")
    print('Done')

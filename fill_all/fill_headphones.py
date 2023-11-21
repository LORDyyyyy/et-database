import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_headphones(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            type = entry['type']
            freq = entry['frequencyResponse']
            micro = entry['microphone']
            wire = entry['wireless']
            enclo = entry['enclosureType']
            color = entry['color']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO headphones\
                    (imageUrl, name, type, frequencyResponse,\
                    microphone, wireless, enclosureType,\
                    color, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, type, freq, micro, wire, enclo, color,
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
    fill_headphones("../ready_files/new_headphone.json")
    print('Done')

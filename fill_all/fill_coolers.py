import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_cooler(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            fanRpm = entry['fanRpm']
            noise = entry['noiseLevel']
            color = entry['color']
            rad = entry['radiatorSize']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO coolers\
                    (imageUrl, name, fanRPM, noiseLevel, color,\
                    radiatorSize, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, fanRpm, noise, color, rad, price, man)
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
    fill_cooler("../ready_files/new_cooler.json")
    print('Done')

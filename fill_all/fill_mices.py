import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_mices(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            method = entry['trackingMethod']
            conn = entry['connectionType']
            dpi = parseInt(entry['maximumDpi'])
            hand = entry['handOrientation']
            color = entry['color']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO mices\
                    (imageUrl, name,trackingMethod, connectionType,\
                    maximumDpi, handOrientation, color, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, method, conn, dpi, hand, color, price, man)
            cursor.execute(query, values)
            db_connection.commit()
            print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")
        db_connection.rollback()


def parseInt(value):
    try:
        return (int(value))
    except ValueError:
        return 0


def convert_price(value):
    try:
        float_value = float(value)
        return float_value
    except ValueError:
        return 0.0


if __name__ == "__main__":
    fill_mices("../ready_files/new_mice.json")
    print('Done')

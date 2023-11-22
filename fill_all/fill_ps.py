import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_ps(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            type = entry['type']
            eff = entry['efficiencyRating']
            watt = entry['wattage']
            mod = entry['modular']
            color = entry['color']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO powersupplies\
                    (imageUrl, name, type, efficiencyRate, wattage,\
                    modular, color, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, type, eff, watt, mod, color,
                      price, man)
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
    fill_ps("../ready_files/new_ps.json")
    print('Done')

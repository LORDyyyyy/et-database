import json
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="lordy",
    password="",
    database="elite_tech"
)

cursor = db_connection.cursor()


def fill_monitors(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    try:
        for entry in data:
            url = entry['imageUrl']
            name = entry['name']
            screen = entry['screenSize']
            res = entry['resolution']
            ref = entry['refreshRate']
            restime = entry['responseTime(g2g)']
            restime = restime if restime != 'Response Time (G2G)' else 'NULL'
            panel = entry['panelType']
            aspect = entry['aspectRatio']
            price = convert_price(entry['price'][1:])
            man = entry['manufactor']

            query = "INSERT INTO monitors\
                    (imageUrl, name, screenSize, resolution, refreshRate,\
                    responseTimeG2G, panelType, aspectRatio, price, manufactor)\
                    VALUES\
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (url, name, screen, res, ref, restime, panel, aspect,
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
    fill_monitors("../ready_files/new_monitor.json")
    print('Done')

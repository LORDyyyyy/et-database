#!/usr/bin/python3
import json


if __name__ == "__main__":

    data = {}
    name = ''
    mans = []

    while True:
        name = input()
        if name == '-1':
            break
        mans.append(name)

    comp = 'monitor'
    with open(f"done/{comp}.json", 'r') as f:
        data = json.load(f)
        f.close()
    print(f'data len before: {len(data)}')
    id = 124
    cheaker = 0
    to_delete = []
    for index, cpu in enumerate(data):
        flag = 1
        for i in mans:
            if i.lower() in cpu['name'][:-1].lower():
                cpu['manufactor'] = i
                cpu['id'] = f'{comp}-{id}'
                id += 1
                if cpu['price'] == 'Add':
                    cpu['price'] = 'NULL'
                flag = 0
                cheaker += 1
                break
        if flag:
            to_delete.append(index)
    for i in to_delete[::-1]:
        data.pop(i)
    with open(f'ready_files/new_{comp}.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
        f.close()

    print(f'data len after: {len(data)}. cheaker = {cheaker}')

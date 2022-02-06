import json


def write_json(data):
    with open("./misc/json_practice/test.json", "w") as write_file:
        json.dump(data, write_file)


def read_json(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)
        print(data)


test_data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [{"firstName": "Alice", "age": 6}, {"firstName": "Bob", "age": 8}],
}

write_json(test_data)
read_json("./misc/json_practice/test.json")

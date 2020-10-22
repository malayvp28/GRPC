import json

import cars_pb2


def read_user_database():
    feature_list = []
    with open("database.json", 'r') as user_db_file:
        for item in json.load(user_db_file)["data"]:
            feature = {
                "id": int(item["id"]),
                "name": str(item["name"]),
                "price": str(item["price"])
                
            }
            feature_list.append(feature)
    return feature_list


def add_user_database(name, price):
    data = read_user_database()
    new_user = {
        "id": int(len(data)+1),
        "name": str(name),
        "price": str(price)
      
    }

    data = []
    with open("database.json", 'r') as user_db_file:
      data = json.load(user_db_file)["data"]
      data.append(new_user)
      user_db_file.close()

    print("*********************************************")
    print(data)
    new_data = {}
    new_data["data"] = data
    with open("database.json", 'w') as user_db_file:
        json.dump(new_data, user_db_file)
        user_db_file.close()
    return new_user


def update_user_database(user):
    data = read_user_database()
    isPresent = False
    # print("data fetched")
    index = 0
    # print("Len: ", len(data))
    
    for s in data:
        if s["id"] == user.id:
            isPresent = True
            break
        index+=1

    if not isPresent:
        return 0
    else:
	    
        data[index] = {
            "id": data[index]["id"],
            "name": str(user.name),
            "price": str(user.price)
            
        }

        new_data = {}
        new_data["data"] = data
        with open("database.json", 'w') as user_db_file:
            json.dump(new_data, user_db_file)
        return 1


def delete_user_database(user):
    data = read_user_database()
    new_data = []
    isPresent = False
    for request in data:
        if request["id"] is user.id:
            isPresent = True
            continue
        else:
            new_data.append(request)

    if isPresent:
        with open("database.json", 'w') as user_db_file:
            json.dump({"data":new_data}, user_db_file)
        return 1
    else:
        return 0
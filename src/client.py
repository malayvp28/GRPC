from __future__ import print_function

import random
import logging

import grpc

import resources
import cars_pb2
import cars_pb2_grpc


def getUserUtils(stub, userid):
    user = stub.GetUser(userid)
    
    if user.id == -1:
        print("Car Not found for the given ID\n")
    else:
        print("______User Found______")
        print("Car ID: ", user.id)
        print("Car Name: ", user.name)
        print("Car price : ", user.price)
       
        print("_____________________________________")


def handleGet(stub):
    uid = int(input("Enter Cars ID to get the details: "))
    getUserUtils(stub, cars_pb2.UserID(id=uid))

def handlePost(stub):
    print("________ Enter Car details to be added _________")
    cname = str(input("Car Name: "))
    cprice = str(input("Car price: "))
    
    
    user = stub.AddUser(cars_pb2.UserData(id=1, name=cname, price=cprice))

    if user:
        print("\nCar Added Succesfully")
        print(user)

    



def handlePut(stub):
    print("________ Enter Car details to be updated _________")
    uid = int(input("Car ID: "))
    cname = str(input("Car Name: "))
    cprice = str(input("Car price: "))
   

    updatedUser = stub.UpdateUser(cars_pb2.UserData(id=uid, name=cname, price=cprice))

    print(updatedUser)


def handleDelete(stub):
    print("________ Enter Car details to be deleted _________")
    uid = int(input("Car ID: "))

    deletedUser = stub.RemoveUser(cars_pb2.UserID(id = uid))

    print(deletedUser)
    

def run():
    with grpc.insecure_channel('localhost:9099') as channel:
        stub = cars_pb2_grpc.UserStub(channel)

        while True:
            in1 = str(input("1:GET\n2:POST\n3:PUT\n4:DELETE\n5:EXIT\n"))

            if in1=="1":
                handleGet(stub)
            elif in1=="2":
                handlePost(stub)
            elif in1=="3":
                handlePut(stub)
            elif in1=="4":
                handleDelete(stub)
            elif in1=="5":
                break
            else:
                print("Invalid input")



        # print("-------------- GetFeature --------------")
        # guide_get_feature(stub)
        # print("-------------- ListFeatures --------------")
        # guide_list_features(stub)
        # print("-------------- RecordRoute --------------")
        # guide_record_route(stub)
        # print("-------------- RouteChat --------------")
        # guide_route_chat(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()

from concurrent import futures
import time
import math
import logging

import grpc
import resources
import cars_pb2
import cars_pb2_grpc


def get_user(db, userid):
    for request in db:
        if request["id"] == userid:
            return request
    return None
# Inherit from example_pb2_grpc.ExampleServiceServicer
# ExampleServiceServicer is the server-side artifact.
class MyUserServicer(cars_pb2_grpc.UserServicer): 
    # def __init__(self):
    #     self.db = song_resources.read_song_database()

    '''POST Method Implementation'''
    def AddUser(self, request, context):
        name = str(request.name)
        age = str(request.price)
        print(name)
        print("POST request served")

        if name is None:
            print("Name is not provided")
        if age is None:
            print("price is not provided")        
       
       
        new_user = resources.add_user_database(name, age)

        return cars_pb2.UserData(
                id = new_user["id"],
                name = request.name,
                price = request.price
                
            )
    
    '''GET Method Implementation'''
    def GetUser(self, request, context):
        db = resources.read_user_database()
        request = get_user(db, request.id)
        
        print("GET request served")
        if request is None:
            return cars_pb2.UserData(
                id = -1,
                name = None,
                price = None
              
            )
        else:
            return cars_pb2.UserData(
                id = request["id"],
                name = request["name"],
                price = request["price"]
                
            )
    
    '''PUT Method Implementation'''
    def UpdateUser(self, request, context):
        id1 = str(request.id)
        print(id1,"....................................................................")
        res = resources.update_user_database(request)
        print("PUT request served")
        if res is 0:
            return cars_pb2.UserData(
                id = -1,
                name = "None",
                price = "None",
                
            )
        else:
           return cars_pb2.UserData(
                id = request.id,
                name = request.name,
                price = request.price
                
            )
    

    '''DELETE Method Implementation'''
    def RemoveUser(self, request, context):
        res = resources.delete_user_database(request)
        print("DELETE request served")
        if res == "-1":
            return cars_pb2.UserData(
                id = -1,
                name = "Car not found",
                price = None
                
            )
        else:
            return cars_pb2.UserData(
                id = -1,
                name = "Car deleted successfully",
                price = None
                
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cars_pb2_grpc.add_UserServicer_to_server(
        MyUserServicer(), server)
    server.add_insecure_port('[::]:9099')
    server.start()
    print("Server started on http://localhost:9099")
    server.wait_for_termination()




if __name__ == '__main__':
    logging.basicConfig()
    serve()
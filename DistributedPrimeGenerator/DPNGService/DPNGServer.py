#!/usr/bin/env python3

import socket
import threading
import time
from primeGenerator import PrimeGenerator
from utilChecker import UtilManager

HOST = '0.0.0.0'
PORT = 1337

def startGeneration(start, end):
    generator = PrimeGenerator()
    task = threading.Thread(target=generator.start, args=(start, end))
    task.start()
    return task, generator

def handleClient(conn, addr):
    # Utilization manager
    utilization = UtilManager()
    # Thread that generates primes
    generator : PrimeGenerator = None
    generatorTask : threading.Thread = None
    
    with conn:
        print(f'Connected to: {addr}')
        
        while True:
            data = conn.recv(1024)
            if not data:
                print(f'Disconnecting from: {addr}')
                break
            
            data = data.decode('utf-8').strip()

            data = data.split(' ')
            match data[0]:
                case '1':
                    if len(data) != 3:
                        break
                    print(f'Starting prime generation for {addr}')
                    generatorTask, generator = startGeneration(int(data[1]), int(data[2]))
                case '2':
                    if len(data) != 2:
                        break
                    print(f'Sending utilization logs to {addr}')
                    conn.sendall(str(utilization.getLogs(int(data[1]))).encode('utf-8'))
                case '3':
                    if generator == None:
                        break
                    print(f'Sending primes to {addr}')
                    conn.sendall(str(generator.get()).encode('utf-8'))
                case other:
                    print(f'Unknown command: {other}')
                    pass
                           
    if generatorTask:
        generatorTask.join()


def main():
    clients = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as service:
        service.bind((HOST, PORT))
        service.listen()
        
        while True:
            conn, addr = service.accept()
            client = threading.Thread(target=handleClient, args=(conn, addr))
            client.start()
            clients.append(client)
        
        threading.join(clients)
        
        
if __name__ == '__main__':
    main()
    
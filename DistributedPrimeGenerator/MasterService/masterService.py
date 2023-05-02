#!/usr/bin/env python3

import socket
import time
import datetime

HOSTS = ['dpng-1', 'dpng-2', 'dpng-3']
PORTS = [1337, 1338, 1339]

MAX_PRIME = 10 ** 12


def main():
    with open('log.csv', 'w') as logfile:
        logfile.write('time_stamp, cpu, memory\n')
    
    services = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in PORTS]
    
    for service, port, host in zip(services, PORTS, HOSTS):
        print (f'Connecting to {host}:{port}')
        service.connect((host, port))
        
    start = 0
    end = MAX_PRIME // len(services)
    
    for service in services:
        msg = f'1 {start} {end}\n'
        print(service.getpeername())
        print(msg, end='')
        service.sendall(msg.encode('utf-8'))
        start = end + 1
        end = end + MAX_PRIME // len(services)
    
    # Program loop
    while True:
    # Log CPU and memory usage every minute
        with open ('log.csv', 'a') as logfile:
            for service in services[1:]:
                service.sendall('2 1\n'.encode('utf-8'))
                data = service.recv(1024)
                if data:
                    data = data.decode('utf-8').strip().split(', ')
                    
                    data[0] = float(data[0][2:])
                    data[2] = float(data[2][:-2])
                    dt = datetime.datetime.fromtimestamp(data[0]).strftime('%Y-%m-%d %H:%M:%S')
                    logfile.write(f'{dt}, {data[1]}, {data[2]}')
                    logfile.write('\n')
                    logfile.flush()
                time.sleep(60)

        # After 2 minutes, get the list of primes from all services
        prime_list = []
        for service in services:
            service.sendall('3\n'.encode('utf-8'))
            msg = ''
            while True:
                data = service.recv(1024)
                if not data:
                    break
                
                msg += data.decode('utf-8')
                
                if len(data) < 1024:
                    break

            msg = msg.strip().split(', ')
            msg[0] = msg[0][1:]
            msg[-1] = msg[-1][:-1]
            try: 
                msg.remove('')
            except ValueError:
                pass
            msg = [int(x) for x in msg]

            if len(msg) > 0:
                prime_list.extend(msg)

        prime_list.sort()
        # print(prime_list)
           
    
if __name__ == '__main__':
    main()
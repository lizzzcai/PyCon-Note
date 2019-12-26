class IterableServer:
    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]

    def __init__(self):
        self.current_pos = 0
    
    def __iter__(self):
        # can return self, because __next__ implemented
        return self
    
    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos += 1
            if service['active']:
                return service['protocol'], service['port']
        raise StopIteration


class Server:
    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]
    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']

if __name__ == "__main__":
    for protocol, port in IterableServer():
        print(f"service {protocol} on port {port}")

    for protocol, port in Server():
        print(f"service {protocol} on port {port}")
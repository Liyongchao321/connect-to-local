import socket
# class Resolver:
#     def __init__(self):
#         self._cache = {}
    
#     def __call__(self, host):
#         if host not in self._cache:
#             self._cache[host] = socket.gethostbyname(host)
#         return self._cache[host]

if __name__ == '__main__':
    A = ['a c', 'b b', 'c c']
    B = sorted(A, key=lambda x:x.split()[-1])
    print(B)
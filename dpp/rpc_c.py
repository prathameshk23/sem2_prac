import xmlrpc.client

# Connect to RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call remote methods
print("Addition:", proxy.add(10, 5))
print("Subtraction:", proxy.subtract(10, 5))
print("Multiplication:", proxy.multiply(10, 5))
print("Division:", proxy.divide(10, 5))

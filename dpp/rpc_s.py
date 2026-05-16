from xmlrpc.server import SimpleXMLRPCServer

# Create RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")

# Define remote functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Run server
server.serve_forever()

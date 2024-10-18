import base64
import json

def prompt(message, predicate=lambda _: True, invalid_message="Invalid input", mapper=lambda x: x, exceptions_to_error_messages={}):
  while True:
    try:
      value = mapper(input(message))
      if predicate(value):
        return value
      else:
        print(invalid_message)
    except Exception as e:
      error_message = exceptions_to_error_messages.get(type(e), "An unexpected error occurred. " + str(e))
      print(error_message)

def write_bytes_to(file_name, content):
  with open(file_name, 'wb') as file:
    file.write(content)

def read_bytes_from(file_name):
  with open(file_name, 'rb') as file:
    return file.read()
  
def serialize_cypher_to_base64_bytes(cypher):
  return base64.b64encode(json.dumps(cypher).encode("utf-8"))

def deserialize_cypher_from_base64_bytes(serialized_cypher):
  return json.loads(base64.b64decode(serialized_cypher).decode("utf-8"))
# MAIN

from RSA_Encryption import RSA_Encryption
from PKCS_Serialization import PKCS_Serialization
from Util import read_bytes_from, write_bytes_to, prompt, serialize_cypher_to_base64_bytes, deserialize_cypher_from_base64_bytes
import json

# Mode Handlers

## Encryption

def encrypt(public_key):
  message = prompt(
    "Enter the message to encrypt: ",
    mapper=lambda message: message.strip(),
    predicate=lambda message: message != "",
    invalid_message="Message cannot be empty."
  )

  encrypted_message = RSA_Encryption.encrypt(message, public_key)
  serialized_cypher = serialize_cypher_to_base64_bytes(encrypted_message)

  prompt("Enter the path to store the cypher: ",
    mapper=lambda file_path: write_bytes_to(file_path, serialized_cypher),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )

  print("Encrypted message:", encrypted_message)

## Decryption

def decrypt(private_key):
  serialized_cypher = prompt(
    "Enter the path to the cypher storage: ",
    mapper=lambda file_path: read_bytes_from(file_path),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )

  cypher = deserialize_cypher_from_base64_bytes(serialized_cypher)
  decrypted_message = RSA_Encryption.decrypt(cypher, private_key)

  print("Decrypted message:", decrypted_message)

# Modes

ENCRYPT, DECRYPT = "e", "d"
MODES = [ENCRYPT, DECRYPT]

def choose_mode(public_key, private_key):
  mode = prompt(
    "Type 'e' to encrypt a message or 'd' to decrypt a message: ",
    mapper=lambda choice: choice.lower(),
    predicate=lambda choice: choice in MODES,
    invalid_message="Invalid mode.",
  )

  if mode == ENCRYPT:
    encrypt(public_key)
  else:
    decrypt(private_key)

GENERATE_NEW_KEYS, USE_EXISTING_KEYS = "g", "u"
KEY_GENERATION_OPTIONS = [GENERATE_NEW_KEYS, USE_EXISTING_KEYS]

# Keys Generation

def generate_keys():
  key_generation_mode = prompt(
    "Type 'g' to generate new keys or 'u' to use existing keys: ",
    mapper=lambda choice: choice.lower(),
    predicate=lambda choice: choice in KEY_GENERATION_OPTIONS,
    invalid_message="Invalid option."
  )

  if key_generation_mode == GENERATE_NEW_KEYS:
    return RSA_Encryption.generate_keys(1024)
  
  passphrase = prompt(
    "Enter the passphrase to decrypt the keys: ",
    mapper=lambda passphrase: passphrase.strip(),
    predicate=lambda passphrase: passphrase != "",
    invalid_message="Passphrase cannot be empty."
  )
 
  serialized_public_key = prompt(
    "Enter the path to the public key storage: ",
    mapper=lambda file_path: read_bytes_from(file_path),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )

  serialized_private_key = prompt(
    "Enter the path to the private key storage: ",
    mapper=lambda file_path: read_bytes_from(file_path),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )

  return PKCS_Serialization.deserialize_keys_from_pkcs(serialized_public_key, serialized_private_key, passphrase)

# Main

EXIT_CODE = "exit"

SAVE_KEYS, DONT_SAVE_KEYS = "y", "n"
KEY_SAVING_OPTIONS = [SAVE_KEYS, DONT_SAVE_KEYS]

def main(public_key, private_key):
  choose_mode(public_key, private_key)

  user_choice = prompt(
    "Type 'exit' to exit or any other key to continue: ",
    mapper=lambda choice: choice.lower(),
  )

  return user_choice != EXIT_CODE

if __name__ == "__main__":
  print("RSA Encryption")

  public_key, private_key = generate_keys()

  while main(public_key, private_key):
    pass

  save_keys = prompt(
    "Do you want to save the keys? (y/n): ",
    mapper=lambda choice: choice.lower(),
    predicate=lambda choice: choice in KEY_SAVING_OPTIONS,
    invalid_message="Invalid option."
  ) == SAVE_KEYS

  if not save_keys:
    print("Goodbye!")
    exit()

  passphrase = prompt(
    "Enter the passphrase to encrypt the keys: ",
    mapper=lambda passphrase: passphrase.strip(),
    predicate=lambda passphrase: passphrase != "",
    invalid_message="Passphrase cannot be empty."
  )
  
  serialized_public_key, serialized_private_key = PKCS_Serialization.serialize_keys_to_pkcs(public_key, private_key, passphrase)

  
  prompt(
    "Enter the path to the public key storage: ",
    mapper=lambda file_path: write_bytes_to(file_path, serialized_public_key),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )
  prompt(
    "Enter the path to the private key storage: ",
    mapper=lambda file_path: write_bytes_to(file_path, serialized_private_key),
    exceptions_to_error_messages={
      FileNotFoundError: "Invalid path."
    }
  )

  print("Goodbye!")
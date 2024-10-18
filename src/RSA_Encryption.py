from Crypto.Util.number import getPrime

class Compute:
  @staticmethod
  def extended_euclidean_algorithm(a, b):
    if a == 0:
      return b, 0, 1
    else:
      gcd, x, y = Compute.extended_euclidean_algorithm(b % a, a)
      return gcd, y - (b // a) * x, x

  @staticmethod
  def modular_inverse(a, m):
    gcd, x, y = Compute.extended_euclidean_algorithm(a, m)
    if gcd != 1:
      raise ValueError("Modular inverse does not exist")
    else:
      return x % m

class RSA_Encryption:
  @staticmethod
  def generate_keys(key_size=2048):
    if key_size < 1024:
      raise ValueError("Key size must be at least 1024 bits")

    p = getPrime(key_size)
    q = getPrime(key_size)
    while q == p:
      q = getPrime(key_size)
      
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = Compute.modular_inverse(e, phi)

    return (n, e), (n, d)

  @staticmethod
  def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

  @staticmethod
  def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)
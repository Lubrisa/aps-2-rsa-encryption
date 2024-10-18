### Introduction to RSA

RSA (Rivest-Shamir-Adleman) is a widely used public-key cryptographic system that provides secure data transmission. It relies on the mathematical properties of large prime numbers and modular arithmetic. The RSA algorithm involves three main steps: key generation, encryption, and decryption.

1. **Key Generation**: Two large prime numbers are selected and multiplied to produce a modulus. The totient of the modulus is calculated, and an encryption exponent is chosen. The decryption exponent is computed using the modular inverse of the encryption exponent.

2. **Encryption**: The message is converted into an integer and encrypted using the recipient's public key, resulting in ciphertext.

3. **Decryption**: The ciphertext is decrypted using the private key, recovering the original message.

### RSA_Encryption.py Class API

| Method                        | Description                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------------|
| `generate_keys(key_size=2048)`| Generates RSA public and private keys with the specified key size (minimum 1024 bits).         |
| `encrypt(message, public_key)`| Encrypts a message using the provided public key.                                             |
| `decrypt(encrypted_message, private_key)`| Decrypts an encrypted message using the provided private key.                       |

### Building and Running the Container

#### Building the Docker Image

To build the Docker image, navigate to the project directory and run:

```sh
docker build -t rsa-encryption-app .
```

#### Running the Container

To run the Docker container with volumes for keys and cyphers directories in interactive mode, use the following command:

```sh
docker run -it --rm \
    -v $(pwd)/keys:/app/keys \
    -v $(pwd)/cyphers:/app/cyphers \
    rsa-encryption-app
```

This command mounts the local `keys` and `cyphers` directories to the container, allowing the application to read and write data to these directories.

---

### Introdução ao RSA

RSA (Rivest-Shamir-Adleman) é um sistema criptográfico de chave pública amplamente utilizado que proporciona transmissão segura de dados. Ele se baseia nas propriedades matemáticas de grandes números primos e aritmética modular. O algoritmo RSA envolve três etapas principais: geração de chaves, criptografia e descriptografia.

1. **Geração de Chaves**: Dois grandes números primos são selecionados e multiplicados para produzir um módulo. O totiente do módulo é calculado, e um expoente de criptografia é escolhido. O expoente de descriptografia é calculado usando o inverso modular do expoente de criptografia.

2. **Criptografia**: A mensagem é convertida em um número inteiro e criptografada usando a chave pública do destinatário, resultando em um texto cifrado.

3. **Descriptografia**: O texto cifrado é descriptografado usando a chave privada, recuperando a mensagem original.

### API da Classe RSA_Encryption.py

| Método                          | Descrição                                                                                         |
|---------------------------------|---------------------------------------------------------------------------------------------------|
| `generate_keys(key_size=2048)`  | Gera chaves públicas e privadas RSA com o tamanho especificado (mínimo de 1024 bits).             |
| `encrypt(message, public_key)`  | Criptografa uma mensagem usando a chave pública fornecida.                                        |
| `decrypt(encrypted_message, private_key)` | Descriptografa uma mensagem criptografada usando a chave privada fornecida.              |

### Construindo e Executando o Container

#### Construindo a Imagem Docker

Para construir a imagem Docker, navegue até o diretório do projeto e execute:

```sh
docker build -t rsa-encryption-app .
```

#### Executando o Container

Para executar o container Docker com volumes para os diretórios de chaves e cifras em modo interativo, use o seguinte comando:

```sh
docker run -it --rm \
    -v $(pwd)/keys:/app/keys \
    -v $(pwd)/cyphers:/app/cyphers \
    rsa-encryption-app
```

Este comando monta os diretórios locais `keys` e `cyphers` no container, permitindo que o aplicativo leia e escreva dados nesses diretórios.

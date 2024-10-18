from Crypto.PublicKey import RSA

class PKCS_Serialization:
    @staticmethod
    def serialize_keys_to_pkcs(public_key, private_key, passphrase):
        if passphrase is None or passphrase == "":
            raise ValueError("Passphrase is required.")

        n, e = public_key
        n, d = private_key
        sk = RSA.construct((n, e, d))
        private_key_pkcs = sk.export_key(
            format="DER",
            pkcs=8,
            passphrase=passphrase,
            protection="PBKDF2WithHMAC-SHA1AndDES-EDE3-CBC"
        )
        public_key_pkcs = sk.publickey().export_key(format="DER")
        
        return public_key_pkcs, private_key_pkcs

    @staticmethod
    def deserialize_keys_from_pkcs(public_key_pkcs, private_key_pkcs, passphrase=None):
        if passphrase is None or passphrase == "":
            raise ValueError("Passphrase is required.")
        
        public_key = RSA.import_key(public_key_pkcs)
        private_key = RSA.import_key(private_key_pkcs, passphrase=passphrase)
        
        return (public_key.n, public_key.e), (private_key.n, private_key.d)
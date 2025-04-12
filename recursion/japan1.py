import hmac, hashlib, time, struct


def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode()
    timestep = 30
    T0 = 0
    t = int(time.time())
    counter = (t - T0) // timestep
    msg = struct.pack(">Q", counter)
    hmac_digest = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    code = (
        ((hmac_digest[offset] & 0x7F) << 24)
        | ((hmac_digest[offset + 1] & 0xFF) << 16)
        | ((hmac_digest[offset + 2] & 0xFF) << 8)
        | (hmac_digest[offset + 3] & 0xFF)
    )
    return str(code % 10**10).zfill(10)


email = "hanamesfin67@gmail.com"
print("TOTP:", generate_totp(email))

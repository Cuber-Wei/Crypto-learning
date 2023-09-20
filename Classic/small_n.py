from Crypto.Util.number import *

p, q = [getPrime(32) for _ in range(2)]
m = bytes_to_long(b'Cry')
assert m < p*q
e = 0x10001
d = inverse(e, (p - 1)*(q - 1))
c = pow(m, e, p*q)

print(f"n = {p*q}")
print(f"e = {e}")
print(f"c = {c}")

"""
n = 9796798126213516403
e = 65537
c = 5237062886782466589
"""

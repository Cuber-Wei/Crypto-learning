from Crypto.Util.number import *

n = 9796798126213516403
p = 2372043853
q = 4130108351
e = 65537
c = 5237062886782466589

phi = (p - 1)*(q - 1)
d = inverse(e, phi)
m = pow(c, d, p*q)

print(long_to_bytes(m))
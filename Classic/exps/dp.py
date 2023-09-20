from Crypto.Util.number import *

n = 72420941416897507344195907646920309661730004959244224317060010081022887298197298029410963868824906526816037793012174817624499788199140364628825200993340488098292339258916243079944245700109215168436193792041947063256156446746494797829618279252658045804780283320118189437445049199924110917211344791412878698341
e = 65537
c = 19219366139270460432670003504704195168147193331317857631842821959859035745904545503462384717783931343677763377415958879525009236319663394895749609879931971739961937039148481149951743760663597903631207575846376421003424012595275479999078426292320866088571325516267368567317391482714148470401534266067194466985
dp = 2390976089092706809361349626674921164284477609697943623350339293095798722286148183542458482306360880165285431540923185335663560152325196288609035337077473

for k in range(1, e):
    if (dp*e - 1) % k == 0:
        p = ((dp*e - 1) // k) + 1
        if n % p == 0:
            q = n // p
            phi = (p - 1)*(q - 1)
            d = inverse(e, phi)
            print(long_to_bytes(pow(c, d, n)))
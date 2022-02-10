
from Digital_Signaature.Signature import *


if __name__ == '__main__':
    pr,pu = key_gen()
    #print(pr)
    #print(pu)
    message = b"This is a sccret message"
    sig = sign(message,pr)
    #print(sig)
    correct = verify(message,sig,pu)

    if correct:
        print('good signature')
    else:
        print('Error!Signature is bad')

print("!-----------------------------------------!")

#Checking for bad signature

pr2,pu2 = key_gen()

sig2 = sign(message,pr2)

correct = verify(message,sig2,pu)

if correct:
    print('Error!!!!! Bad signature checks out!!1')
else:
    print("Success! Bad signature detected")

print("!---------------------------------------------!")

#message Tampering
badmess = message + b"Q"

correct = verify(badmess,sig,pu)

if correct:
    print('Error!!!!! Tampered message checks out!!!')
else:
    print("Success! Tambering detected")

print("!-------------------------------------------!")


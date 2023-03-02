# 4_wheels_encryption
#################################################################################################################
v0.0.1
Thursday - 2/3/2023

Minimum requirement:
- Free storage: 2Gb
- RAM         : 1Gb
- CPU         : Any single core 1.0GHz

#################################################################################################################

An encryption from wheel swapping alphabet

Encryption of a text is following this step:
1) search for the first character in a main wheel [character availability list]
2) use the index of the first character [add the first shift key] and search for a character from a wheel
3) use the new selected character and search for the character in next wheel
4) use the index of the cheracter [add the second shift key] and search for next character from next wheel
5) use the new selected character and search for the character in next wheel
6) use the index of the cheracter [add the third shift key] and search for next character from next wheel
7) use the new selected character and search for the character in next wheel
8) use the index of the cheracter [add the second shift key] and search for next character from previous wheel
9) use the new selected character and search for the character in main wheel
10) use the index of the cheracter [add the first shift key] and search for next character from main wheel

Decryption of an encrypted text is following this step:
1) search for the first character in a main wheel [character availability list]
2) use the index of the first character [check for additional key for adding 69/lenght of main wheel then
   subtract with first shift key] and search for a character from a wheel
3) use the new selected character and search for the character in next wheel
4) use the index of the cheracter [check for additional key for adding 69/lenght of main wheel then
   subtract with first shift key] and search for next character from next wheel
5) use the new selected character and search for the character in next wheel
6) use the index of the cheracter [check for additional key for adding 69/lenght of main wheel then
   subtract with first shift key] and search for next character from next wheel
7) use the new selected character and search for the character in next wheel
8) use the index of the cheracter [check for additional key for adding 69/lenght of main wheel then
   subtract with first shift key] and search for next character from previous wheel
9) use the new selected character and search for the character in main wheel
10) use the index of the cheracter [check for additional key for adding 69/lenght of main wheel then
   subtract with first shift key] and search for next character from main wheel

At the end of encryption, you will get the encrypted text and a list of additional key for each individual
characters. The decryption step will ask for encrypted text and a list of additional key to decrypt the text.
The encryption and decryption process wiil be succesful if the wheels combination and shift keys are correct.




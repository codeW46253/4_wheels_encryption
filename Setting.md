
Understanding the "order_setting" function:

The function are used to call back and reset system refrence wheels, shift key and lock bit for encryption and decryption
proccesses. It also set the lenght of run limit for encryption and decryption proccesses,

The function consist of "self.order" and "self.order_lenght" as the back bone of the proccesses.

Setting the "self.order":

You can adjust the order of referencing wheels by following this structure:
[
[ Read from ],
[ Read to ],
[ Lock bit ],
[ Shift key ]
]

- Read from: Enter the list of a wheel as a reference to find the character's index
- Read to  : Enter the list of a wheel as a reference to find a new character
- Lock bit : [Don't adjust] A reference bit to create/use an additional key
- Shift key: Enter the list of shift key

Lock bit can be edited only if you want to add or delete a step and should be different from each other. It also should be
inversed in "decryptor.py".

Setting the "self.order_lenght" method:

This method only preserves a lenght of encryption or decryption proccesses. This method should be setted the same as number
of all wheels [main, 1, 2, 3 and 4]

################################################################################################

For setting the referencing wheels, you can follow this:

Read from | Read to






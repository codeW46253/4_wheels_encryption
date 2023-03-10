# 4 Wheels Encryption

#################################################################################################################

Wheel encryption is an encryption that taking a set of wheels as an array of characters to swapping alphabet.

Minimum requirement:
- **Free storage: 2Gb**
- **RAM         : 1Gb**
- **CPU         : Any single core 1.0GHz**

#################################################################################################################



## Encryption of a text is following this step:
1) search for the first character in a `main_wheel`
2) add the `shift_key_1` and the index of the first character
   
   if the total is equal to or more than lenght of `main_wheel`, take a remainder of the total divided by lenght of `main_wheel`
   
   add `bit_1` to `create_additional_key`
   
3) search for a new character from `Wheel 1`
4) use the selected character and search for the character in `wheel_2`
5) add the `shift_key_2` and the index of the new character
   
   if the total is equal to or more than lenght of `main_wheel`, take a remainder of the total divided by lenght of `main_wheel`
   
   add `bit_2` to `create_additional_key`
   
6) search for a new character from `wheel_3`
7) use the selected character and search for the character in `wheel_4`
8) add the `shift key 3` and the index of the new character
   
   if the total is equal to or more than lenght of `main_wheel`, take a remainder of the total divided by lenght of `main_wheel`
   
   add `bit_3` to `create_additional_key`
   
9) search for next character from `wheel_3`
10) use the selected character and search for the character in `wheel_2`
11) add the `shift_key_2` and the index of the new character
   
   if the total is equal to or more than lenght of `main_wheel`, take a remainder of the total divided by lenght of `main_wheel`
   
   add `bit_4` to `create_additional_key`
   
12) search for next character from `wheel_1`
13) use the selected character and search for the character in `main_wheel`
14) add the `shift_key_1` and the index of the new character
   
   if the total is equal to or more than lenght of `main_wheel`, take a remainder of the total divided by lenght of `main_wheel`
   add `bit_5` to `create_additional_key`
   
15) search for final character from `main_wheel`

Repeat from the start and add 1 to `shift_key_1` for the next character in a text. If `shift_key_1` equal to or more than the lenght of `main_wheel`, take the remainder of the total divided by `main_wheel` and add 1 to `shift_key_2`. Then does the same to `shift_key_2` and `shift_key_3`.



## Decryption of an encrypted text is following this step:
1) search for the first character in `main_wheel`
2) subtract the index of the character and `shift_key_1`

   if `additional_key` & `lock_bit_1` not equal to 0, add index and lenght of `main_wheel`
   
3) search the character in `wheel_1`
4) search for the next character in `wheel_2`
5) subtract the index of the character and `shift_key_2`
   
   if `additional_key` & `lock_bit_2` not equal to 0, add index and lenght of `main_wheel`
   
6) search the character in `wheel_3`
7) search for the next character in `wheel_4`
8) subtract the index of the character and `shift_key_3`
   
   if `additional_key` & `lock_bit_3` not equal to 0, add index and lenght of `main_wheel`
   
9) search the character in `wheel_3`
10) search for the next character in `wheel_2`
11) subtract the index of the character and `shift_key_2`
   
   if `additional_key` & `lock_bit_4` not equal to 0, add index and lenght of `main_wheel`
   
12) search the character in `wheel_1`
13) search for the next character in `main_wheel`
14) subtract the index of the character and `shift_key_1`
   
   if `additional_key` & `lock_bit_5` not equal to 0, add index and lenght of `main_wheel`
   
15) search for final character from `main_wheel`

Repeat from the start and add 1 to `shift_key_1` for the next character in a text. If `shift_key_1` equal to or more than the lenght of `main_wheel`, take the remainder of the total divided by `main_wheel` and add 1 to `shift_key_2`. Then does the same to `shift_key_2` and `shift_key_3`.

**At the end of the encryption, you will get the encrypted text and a list of additional key for each individual characters. The decryption step will ask for encrypted text and a list of additional key to decrypt the text. The encryption and decryption process wiil be succesful if the wheels combination and shift keys are correct.**



## Understanding the `wheel_setup` library:

The `wheel_setup` library stores all encryption swap-wheels. The arrangement of characters should be randomized except for `main_wheel`. The arrangement also should be different from other wheels. All characters should be available in all wheel to avoid any error.

Each wheel can have different combination. The number of possible combination \[for 69 characters] is calculated in the table below:

|Wheel|Number of combination|
|:---|---:|
|Main|1|
|1|1.711224524e98 - 1|
|2|1.711224524e98 - 2|
|3|1.711224524e98 - 3|
|4|1.711224524e98 - 4|

To set a wheel's character arrangement, you can use `random_arrangement_generator.py`. You also can change the availability of any character by editting the content of `alpha` variable.





## Understanding the `order_setting` function in `Encryptor` and `Decryptor` classes:

The function are used **to call back and reset *system refrence wheels, shift key and lock bit*** for encryption and decryption proccesses. It also **set the lenght of run limit** for encryption and decryption proccesses.

The function consist of `self.order` and `self.order_lenght` as the back bone of the proccesses.

### Setting the `self.order`:

You can adjust the order of referencing wheels by following this structure:

\[
\[ **Read from** ],
\[ **Read to** ],
\[ **Lock bit** ],
\[ **Shift key** ]
]

|Tag|Description|Allowed Value|
|:---|:---|:---:|
|`Read from`|Enter the list of a wheel as a reference to find the character's index|List(str)|
|`Read to`|Enter the list of a wheel as a reference to find a new character|List(str)|
|`Lock bit`|\[***Don't adjust***] A reference bit to create/use an `additional_key`|List(Int)|
|`Shift key`|Enter the list of `shift_key`|List(Int \[0-lenght of `main_wheel`])|

Lock bit can be edited only if you want to add or delete a step and should be different from each other. It also should be
inversed in `decryptor.py`.

For setting the referencing wheels, you can follow this:

|Steps|Read from|Read to|Lock bit|Shift Key|
|:---|:---|:---|:---:|:---:|
|1|`Main wheel`|`Wheel 2`|0b00001|2: `shift_key_1`|
|2|`wheel 1`|`Wheel 2`|0b00010|3: `shift_key_2`|
|3|`wheel 3`|`Wheel 4`|0b00100|0: `shift_key_3`|
|4|`wheel 3`|`Wheel 2`|0b01000|3: `shift_key_2`|
|5|`Wheel 1`|`Main wheel`|0b10000|2: `shift_key_1`|

### Setting the `self.order_lenght` method:

This method only preserves the limit of encryption or decryption proccesses's steps. This method should be setted the same
as number wheels \[main, 1, 2, 3 and 4]

# Number of possible key combination \[basic settings]

|Type|Quantity|
|:---|---:|
|Number of shift key|3|
|Number of shift key's possible number| lenght of `main_wheel` \[69]|
|Number of changeable wheel step|4|

|Combination|Number|Quantity|
|:---|:---:|---:|
|Shift key|69 x 3|207|
|Wheels|4! = 4 x 3 x 2 x 1|24|
|Total|207 x 24|4968|

Number of possible encryption is 4968 combinations for a basic settings





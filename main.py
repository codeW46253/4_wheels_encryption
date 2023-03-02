
import encryptor, decryptor
import wheel_setup

################################################################################################
# Main
#
# Example for using encryptor and decryptor
#
#
################################################################################################


################################################################################################
# Example for Encryption
text = str(input(f"Please input some text according to this list:\n{wheel_setup.alpha_list}"))

system_selected = encryptor.Encryptor()
system_selected.wheel_setting(0,1,2,3)
system_selected.key_setting(0,0,0)

encrypted, key = system_selected.encryption(text) # text to encrypt

print(f"Encrypted text: {encrypted}") 
print(f"Additional key: {key})
      
        
################################################################################################
# Example for Decryption
system_selected = decryptor.Decryptor()
system_selected.wheel_setting(0,1,2,3)
system_selected.key_setting(0, 0, 0)

decrypted = system_selected.decryption(encrypted, # text to decrypt
                                       key)       # additional key

print(f"Decrypted text: {decrypted}")




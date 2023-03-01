import wheel_setup

class Encryptor:
    
# initial value & placeholder
    def __init__(self):
        self.encr_w1 = []
        self.encr_w2 = []
        self.encr_w3 = []
        self.encr_w4 = []
        self.alpha_list = wheel_setup.alpha_list
        
        self.encr_key1 = 0
        self.encr_key2 = 0
        self.encr_key3 = 0
        
    def order_setting(self):
        self.order = [[self.alpha_list, self.encr_w2, self.encr_w4, self.encr_w2, self.encr_w1], # from wheel
                      [self.encr_w1, self.encr_w3, self.encr_w3, self.encr_w1, self.alpha_list], # to_wheel
                      [0b00001, 0b00010, 0b00100, 0b01000, 0b10000], # lock
                      [self.encr_key1, self.encr_key2, self.encr_key3, self.encr_key2, self.encr_key1] # key
        ]
        
        self.order_lenght = 5

################################################################################################
# settings : 1) Wheel
#            2) Shift key

    def wheel_setting(self, w1, w2, w3, w4):
        wheels = [wheel_setup.wheel_1,
                  wheel_setup.wheel_2,
                  wheel_setup.wheel_3,
                  wheel_setup.wheel_4]
        
        self.encr_w1 = wheels[w1]
        self.encr_w2 = wheels[w2]
        self.encr_w3 = wheels[w3]
        self.encr_w4 = wheels[w4]
        
    def key_setting(self, key1, key2, key3):
        self.encr_key1 = key1 % 69
        self.encr_key2 = key2 % 69
        self.encr_key3 = key3 % 69
    
################################################################################################
# system for character/alphabet swap

    def change(self, from_wheel, to_wheel, code, shift_key):
        index_of_item = from_wheel.index(code)
        new_index = index_of_item + shift_key
        pass_key = False
        if new_index >= 69:
            new_index = new_index % 69
            pass_key = True
            
        print([index_of_item, new_index])
            
        return [to_wheel[new_index], pass_key]
    
################################################################################################
# system for encryption

    def encryption(self, code):
        code_parting = []
        for index in range(len(code)):
            code_parting.append(code[index].upper())
            
        encrypted = ""
        pswrd = []
        for i in range(len(code_parting)):
            create_pswrd = 0
            encr_alpha = code_parting[i]
            for j in range(self.order_lenght):
                result = self.change(self.order[0][j], self.order[1][j], encr_alpha, self.order[3][j])
                encr_alpha = result[0]
                if result[1]:
                    create_pswrd += self.order[2][j]
                    
                print(result)    
                
                self.order_setting() # update order setting
            
            print("\n")
            encrypted += encr_alpha
            pswrd.append(create_pswrd)
            
            # incrementer
            self.encr_key1 += 1
            if self.encr_key1 > 69:
                self.encr_key2 += 1
                if self.encr_key2 > 69:
                    self.encr_key3 += 1
                    if self.encr_key3 > 69:
                        self.encr_key3 = 0
                        
                    self.encr_key2 = 0
                    
                self.encr_key1 = 0
            
            self.order_setting()
        
        return [encrypted, pswrd]
    
################################################################################################

if __name__=="__main__":
    system_selected = Encryptor()
    system_selected.wheel_setting(0,1,2,3)
    system_selected.key_setting(0,0,0)
    system_selected.order_setting()
    
    encrypted, pswrd = system_selected.encryption("relax only")
    
    print(encrypted)
    print(pswrd)
    
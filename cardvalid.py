#Credit Card Validation
class Card_validator():
    
    def __init__(self,cardnum):
        self.number = cardnum
        self.valid_length = self.card_len(cardnum)
        
        #in case the ifs don't run, defaults for type and luhn test result
        self.type_of_card = "na"
        self.luhn_test_result = False
        self.card_is_valid = False
        
        if self.valid_length:
            self.type_of_card = self.card_type(cardnum)
        if self.type_of_card != "na":
            self.luhn_test_result = self.luhn(cardnum)
            
        if self.luhn_test_result:
            self.card_is_valid = True
    
    def card_len(self,cardnum):
        #cardnum1 = int(cardnum)
        cardnum = str(cardnum)
        if len(cardnum) == 16:
            return True
        elif len(cardnum) == 15:
            return True
        else:
            print("Not a valid number")
            return False

    def card_type(self,cardnum):
        # Creating tuples to validated card types
        cardnum = str(cardnum)
        
        vis = ("4")
        mas = ("51","52","53","54","55")
        amx = ("34","37")
        dis = ("6011")

        if cardnum[0] in vis:
            return "visa"
        elif cardnum[0:2:1] in mas:
            return "mast"
        elif cardnum[0:2:1] in amx:
            return "amex"
        elif cardnum[0:4:1] in dis:
            return "disc"
        else: 
            return "na"


    # Luhn Algo
    def luhn(self,cardnum):
        nums_as_str = list(cardnum)
        alist2 = []
        for index in range(0,len(nums_as_str),1):
            #print(index,nums_as_str[index])

            if index % 2 == 0: #handling numbers we want to double
                temp = int(nums_as_str[index]) * 2
                #print(temp)
                if temp >= 10:
                    temp = str(temp)
                    alist2.append(int(temp[0]))
                    alist2.append(int(temp[1]))
                else:
                    alist2.append(temp)
            else: #odd indexes (numbers we don't want to double)
                temp = nums_as_str[index]
                alist2.append(int(temp))

        #print(nums_as_str)
        #print(alist2)
        the_sum = sum(alist2)
        #print(the_sum)

        if the_sum % 10 == 0:
            return True
        else:
            return False
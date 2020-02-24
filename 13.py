def validate(n):
 n_str = str(n)
 if len(str(n)) > 16:
        print("it's not a credit card")
 else:
        if len(str(n)) % 2 == 0:
            for i in str(n[0::2]):
                digit = int(n_str) * 2
                while digit > 9:
                    digit = sum(map(int, str(digit)))
            dig_sum = sum(map(int, str(n)))
            if dig_sum % 10 == 0:
                print("it's a credit card")
            else:
                print("it's not a credit card")
        elif len(str(n)) % 2 != 0:
            for i in str(n[1::2]):
                digit = int(n_str) * 2
                while digit > 9:
                    digit = sum(map(int, str(digit)))
            dig_sum = sum(map(int, str(n)))
            if dig_sum % 10 == 0:
               print("it's a credit card")
            else:
                print("it's not a credit card") 
n= input("Give you number")
validate(n)

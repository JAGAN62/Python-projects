import random
import string
def generator():
    length=int(input('Enter the length of your password:'))
    if length < 4:
      return
        
    else:

            uppercase=input('include uppercase :yes or no ? ').strip()
            special=input('include special characters :yes or no ? ').strip()
            digits=input('include digits :yes or no ? ').strip()

            lower_case=string.ascii_lowercase
            upper_case=string.ascii_uppercase if uppercase == 'yes' else ""
            special_chars=string.punctuation if special == 'yes' else ""
            digit=string.digits if digits == 'yes' else ""
            all_characters=lower_case+upper_case+special_chars+digit
            
            
            required_password=[]
        
            if uppercase == "yes":
                required_password.append(random.choice(upper_case))
            if special == "yes":
                required_password.append(random.choice(special_chars))
            if digits == "yes":
                required_password.append(random.choice(digit))
            
            remaining_length=length - len(required_password)
            password=required_password
            for _ in range(remaining_length):
                chacter=random.choice(all_characters)
                password.append(chacter)
            random.shuffle(password)
            final_password=''.join(password)
            return final_password

    
    
    
    
result=generator()
print(result)
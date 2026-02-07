#Password Strength Validator

print("===== PASSWORD VALIDATOR =====")

while True:
    password = input("Enter a password: ")
    
    has_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
   
    if len(password) >= 8:
        has_length = True
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in "!@#$%^&*":
            has_special = True
    


    if has_length and has_upper and has_lower and has_digit and has_special:
        strength = "STRONG"
    elif has_length and has_lower and has_digit and has_upper:
        strength = "MEDIUM"
    else:
        strength = "WEAK"   # ← They forget MEDIUM!

    print("Password analysis:")
    
    if has_length:
        print("[OK] Length requirement met")
    else:
        print("[X] Too short (minimum 8 characters)")
    
    if has_upper:
        print("[OK] Contains uppercase letter")
    else:
        print("[X] Missing uppercase letter")
    
    if has_lower:
        print("[OK] Contains lowercase letter")
    else:
        print("[X] Missing lowercase letter")
    
    if has_digit:
        print("[OK] Contains digit")
    else:
        print("[X] Missing digit")
    
    if has_special:
        print("[OK] Contains special character")
    else:
        print("[X] Missing special character")
    
    print("Strength:", strength)
    
    if has_length and has_upper and has_lower and has_digit and has_special:
        print("Password accepted!")
        break
    else:
        print("Try again!")
        print("")
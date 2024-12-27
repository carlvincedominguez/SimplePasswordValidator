def is_valid_password(password):

  min_length = 8
  has_upper = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)

  if len(password) >= min_length and has_upper and has_lower and has_digit:
     return True
  return False

def main():
    password = input("Enter a password:")

    if is_valid_password(password):
      print("Password is valid.")
    else:
      print("Password is invalid. It must: ")
      print("- Be at least 8 characters long")
      print("- Include at least one uppercase letter")
      print("- Include at least one lowercase letter")
      print("- Include at least one digit")

if __name__ == "__main__":
    main()

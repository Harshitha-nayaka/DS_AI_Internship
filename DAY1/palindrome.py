text = input("Enter text: ").strip()
cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
      print("Not a palindrome")

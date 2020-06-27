def reverse(text):
    return text[::-1]

def is_palindrome(text):
    forbidden_chars = ' .,?!:;-—()[]\'"/\\'

    text = text.lower()

    for char in forbidden_chars:
        if char in text:
            text = text.replace(char, '')

    return text == reverse(text)

something = "Rise to vote, sir."

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")



import hashlib

try:
    text = input("Enter text to be converted: ")
    option = int(input("Hash options: \n     1) MD5 \n     2) SHA1 \n     3) SHA256 \n     4) SHA512 \nChoose an option: "))

    if (option == 1):
        hash = hashlib.md5(text.encode('utf-8'))
        print(f"Generated hash: {hash.hexdigest()}")

    if (option == 2):
        hash = hashlib.sha1(text.encode('utf-8'))
        print(f"Generated hash: {hash.hexdigest()}")

    if (option == 3):
        hash = hashlib.sha256(text.encode('utf-8'))
        print(f"Generated hash: {hash.hexdigest()}")

    if (option == 4):
        hash = hashlib.sha512(text.encode('utf-8'))
        print(f"Generated hash: {hash.hexdigest()}")
    else:
        print("Choose a valid option!")

except:
    print("Choose a valid option!")
import hashlib

def generate_md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Example usage
user_hash = "447d2c8dc25efbc493788a322f1a00e7"
passwd_hash = "827ccb0eea8a706c4c34a16891f84e7b"

# print(f"Original MD5 Hash (User): {user_hash}")
# print(f"Original MD5 Hash (Password): {passwd_hash}")

log_user_hash = input("Enter The MD5 hash of the user Name:")
user_md5_hash = generate_md5_hash(log_user_hash)

pass_user_hash = input("Enter The MD5 hash of the passwd:")
passwd_md5_hash = generate_md5_hash(pass_user_hash)


# Check if the entered MD5 hash values match the stored ones
if user_hash == user_md5_hash and passwd_md5_hash == passwd_hash:
    print("Correct! You are a root-user & Starting Youtube Automation Downloader")
    
else:
    print("Wrong! You are not a root-user")

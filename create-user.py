import hashlib

def generate_md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Example usage
user = "ankit"
user_md5_hash = generate_md5_hash(user)

passwd = "12345"  # Assuming password is a string
passwd_md5_hash = generate_md5_hash(passwd)

print(f"Original Text (User): {user}")
print(f"MD5 Hash (User): {user_md5_hash}")

print(f"Original Text (Password): {passwd}")
print(f"MD5 Hash (Password): {passwd_md5_hash}")

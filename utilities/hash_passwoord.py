from passlib.hash import bcrypt

hash_ = bcrypt.hash("password_user1")  # replace with your db user's password
hash2_ = bcrypt.hash("password_user2")

print("Hash1 generado:", hash_)
print("Hash2 generado:", hash2_)
print("Verificación correcta:", bcrypt.verify("password_user1", hash_))
print("Verificación incorrecta:", bcrypt.verify("another_password", hash_))

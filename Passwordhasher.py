from argon2 import PasswordHasher
from argon2.low_level import Type
from argon2.exceptions import VerifyMismatchError
import getpass
import time
import sys
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



# Argon2id parameters, change them as needed, but these are secure and recommended. I won't go into details here, but you can read online.
ph = PasswordHasher(
    time_cost=20,
    memory_cost=262144,
    parallelism=4,
    hash_len=32,
    salt_len=16,
    type=Type.ID
)
clear_screen()
print("DESPITE HASHING, DO *NOT* USE WEAK PASSWORDS, AND CHANGE THEM OFTEN!!")
time.sleep(3)
print("Please check the code to see the parameters aswell as ensuring the safty of this code... even though it is safe, check for yourself.")
time.sleep(3)
print("Press Ctrl+C to abort and check the code and parameters.")
time.sleep(2)
print("Oh and this is for personal use, don't actually use this in production, use a well tested library instead.")
time.sleep(1.5)
password_tohash = getpass.getpass("Enter Password for hashing (Plaintext is not stored): ")
start = time.time()
ph.hash("benchmark")
print(f"Benchmark: hashing took {time.time() - start:.2f} seconds with current parameters")



stored_hash = ph.hash(password_tohash)

with open("stored_hash.txt", "w") as f:
    f.write(stored_hash + "\n")
print(f"Hash written to: {os.path.abspath('stored_hash.txt')}")


if ph.check_needs_rehash(stored_hash):
    print("Hash needs to be updated with stronger parameters.")
print("Verifying hash...")
try:
    ph.verify(stored_hash, password_tohash)
    print("Password is correct")
except VerifyMismatchError:
    print("Invalid password")
print("Please store the hash somewhere safe, as it is only as secure as your storage of it.")
sys.exit(0)
# coding: utf-8
"""
Password Hash Tool Unit Tests

Unit tests for hashing the password to be stored in the SQLite
database.
"""
import hashlib


def test_hash_pwd_0000():
    password = '0000'
    right_hash = ('c6001d5b2ac3df314204a8f9d7a00e1503c9aba0fd453'
                  '8645de4bf4cc7e2555cfe9ff9d0236bf327ed3e907849'
                  'a98df4d330c4bea551017d465b4c1d9b80bcb0')
    pwd_hashed = hashlib.sha512(password.encode()).hexdigest()
    assert pwd_hashed == right_hash

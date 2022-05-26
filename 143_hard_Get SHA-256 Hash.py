"""
Get SHA-256 Hash
Hash algorithms are easy to do one way, but essentially impossible to do in reverse. For example, if you hash something simple, like password123, it will give you a long code, unique to that word or phrase. Ideally, there's no way to do this in reverse. You can't take the hash code and go back to the word or phrase you started with.

Make a function that returns the SHA-256 secure hash for a given string. The hash should be formatted in a hexadecimal digit string.

Examples
get_sha256_hash("password123") ➞ "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"

get_sha256_hash("Fluffy@home") ➞ "dcc1ac3a7148a2d9f47b7dbe3d733040c335b2a3d8adc7984e0c483c5b2c1665"

get_sha256_hash("Hey dude!") ➞ "14f997f08b8ad032dcb274198684f995d34043f9da00acd904dc72836359ae0f"
"""
import hashlib

def get_sha256_hash(txt):

	return hashlib.sha256(txt.encode('ascii')).hexdigest()

print(get_sha256_hash("password123"))
print(get_sha256_hash("Fluffy@home"))
print(get_sha256_hash("Hey dude!"))

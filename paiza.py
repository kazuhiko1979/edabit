def calculate_compatibility(name):
	num_seq = [ord(char) - ord('a') + 1 for char in name]

	while len(num_seq) > 1:
		new_seq = [sum(pair) % 101 for pair in zip(num_seq, num_seq[1:])]
		num_seq = new_seq
	return num_seq[0]

def calculate_larger_compatibility(name):
    name1, name2 = name.split()
    compatibility1 = calculate_compatibility(name1 + name2)
    compatibility2 = calculate_compatibility(name2 + name1)
    result = max(compatibility1, compatibility2)
    return result

def main():
    name = input()
    calculate_larger_compatibility(name)

if __name__ == "__main__":
	main()
# print(calculate_larger_compatibility('pa iza'))
# print(calculate_larger_compatibility('alice bob'))

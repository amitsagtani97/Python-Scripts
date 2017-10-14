import string

def main():
	cipherText = raw_input("Input your cipher text: ")
	shift = 0
	while shift < 26 :
		print "SHIFT: " + str(shift)
		caesarshift(cipherText, shift)
		shift+=1
		print "\n"


def caesarshift(cipherText, shift):
	cipherText.strip()
	alphabet_lower = string.ascii_lowercase
	alphabet_upper = string.ascii_uppercase

	shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
	shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

	alphabet = alphabet_lower + alphabet_upper
	shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

	table = string.maketrans(alphabet, shifted_alphabet)
	print cipherText.translate(table)

main()
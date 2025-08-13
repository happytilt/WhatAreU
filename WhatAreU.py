import sys
import re

print('\n------------------------')
print('  WhatAreU.py')
print('  Script by happytilt')
print('------------------------')

#Handles command arguements
if len(sys.argv) != 3:
    print("Usage: python WhatAreU.py <scheme-file-path> <string>")
    sys.exit(1)

#Converts string to all uppercase
string = sys.argv[2].upper()
print(f'Before: {string}')

if __name__ == "__main__":
    file_path = sys.argv[1]

#Defines section_lengths and creates dictionary from file_path
def LoadTextFile(file_path):
	with open(file_path, 'r') as file:
		lines = file.read().splitlines()
	lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
	section_lengths = list(map(int, lines[0].split(',')))

	dictionary = {}
	for line in lines[1:]:
		if '=' in line:
			key, value = line.split('=', 1)
			dictionary[key.strip()] = value.strip()

	return section_lengths, dictionary

#Cuts string up, as defined by section_lengths
def Slice(string, section_lengths):
	sliced_sections = []
	try:
		#replaced for loop with regex matching
		regex_pattern = '^' + ''.join(f'(.{{{length}}})' for length in section_lengths) + "$"
		sliced_sections = re.match(regex_pattern, string).groups()
	except:
		print('\n* Sectioning error, invalid string or scheme file error')
		print('------------------------\n')
		exit(1)
	'''
	#index = 0
	for i in section_lengths:
		sliced = string[index:index+i]
		index += i
		sliced_sections.append(sliced)
	'''
	return sliced_sections

#Translates sliced_sections using dictionary into full_translation

def Translate(sliced_sections, dictionary):
    translated_sections = [dictionary.get(i) or (print(f'\n* Dict Error: {i} not found\n') or f'({i})?') for i in sliced_sections]
    return ' '.join(translated_sections)

section_lengths, dictionary = LoadTextFile(file_path)
sliced_sections = Slice(string, section_lengths)
full_translation = Translate(sliced_sections, dictionary)

print(f'After: {full_translation}')
print('------------------------\n')
# WhatAreU
Python script for translating code names. Modular and easy to set up.

It takes a text file used as a naming scheme and turns it into a python dictionary on runtime to translate a given string.
Please message me on Discord (@happytilt) if you have suggestions, criticism, or come across any errors!

Usage: Usage: python WhatAreU.py <scheme-file-path> <string>


Naming Scheme Text File Formatting:
- First line will always section out the code name.
- Example:  2,3,4 means the given string will sectioned out like so: AABBBCCCC
- Empty lines and lines starting with '#' will be ignored. Utilizing them as comments, even before the first line.
- Key value pairs should be formatted so: CODE = Translation

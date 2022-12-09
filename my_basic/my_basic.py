import sys
from my_basic_lexer import *
from my_basic_parser import *

basic_file = open(sys.argv[1],"r")
Lines = basic_file.readlines()
file_length = len(Lines)

parser = yacc.yacc(debug=True)

# To see how PLY creates lexemes out of our source code file,
# uncommend the following part
for i in range(len(Lines)):
	lexer.input((Lines[i].strip()))
	print(Lines[i].strip())
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)
	result=parser.parse(Lines[i].strip())
	print(result)

#lexer.input("x")
# ~ parser = yacc.yacc(debug=True)
# ~ result = parser.parse("""
# ~ X = 10 + 2""")
# ~ print(result)	

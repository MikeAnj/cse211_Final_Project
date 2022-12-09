import ply.lex as lex

tokens = ["ID", "NUMBER","PRINT","INPUT","IF","THEN","ELSE","FOR","TO","NEXT","END"]

misc = ["NUMBER", "MULT", "PLUS", "MINUS", "DIV", "LPAR","RPAR","EQUAL","NEWLINE","QUOTE"]

t_PRINT = "print"
t_INPUT = "input"
t_IF = "if"
t_THEN = "then"
t_ELSE = "else"
t_FOR = "for"
t_TO = "to"
t_NEXT = "next"
t_END = "end"

t_MULT = '\*'
t_PLUS = '\+'
t_MINUS = '-'
t_DIV = '/'
t_LPAR = '\('
t_RPAR = '\)'
t_EQUAL = '='
t_QUOTE = '"'

t_ignore = '\n\t '

reserved = {
	'print'	:	'PRINT',
	'input'	:	'INPUT',
	'if'	:	'IF',
	'then'	:	'THEN',
	'else'	:	'ELSE',
	'for'	:	'FOR',
	'to'	:	'TO',
	'next'	:	'NEXT',
	'end'	:	'END'
}

tokens = ["ID"] + misc + list(reserved.values())

def t_ID(t):
    "[a-zA-Z]+"
    t.type = reserved.get(t.value, 'ID')
    return t
    
def t_NUMBER(t):
	"0|[1-9][0-9]*"
	return t
	
def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    print("line number: %d" %t.lexer.lineno)
    exit(1)

lexer = lex.lex()

# ~ basic_input = """
	# ~ FOR X=10 TO 100
	# ~ """

# basic input entry
# ~ def input_line(inp):
	# ~ lexer.input(inp)

#input_line(basic_input)

# ~ while True:
    # ~ tok = lexer.token()
    # ~ if not tok:
        # ~ break
    # ~ print(tok)

# The parser part of the basic interpreter
import ply.yacc as yacc

def t_op_print(t):
	"S: PRINT expr"
	print(p[2])

def p_expr_num(p):      # you can call this function anything you want
    "expr : NUMBER"
    p[0] = int(p[1])

def p_expr_plus(p):
    "expr : expr PLUS expr"
    p[0] = p[1] + int(p[3])

def p_expr_minus(p):
    "expr : expr MINUS expr"
    p[0] = p[1] - p[3]

def p_expr_mult(p):
    "expr : expr MULT expr"
    p[0] = p[1] * p[3]

def p_expr_div(p):
    "expr : expr DIV expr"
    if (p[3] == 0):
        print ("can't divide " +str(p[1]) + " by 0")
        exit(1)
    else:
        p[0] = p[1] / p[3]

def p_expr_par(p):
    "expr : LPAR expr RPAR"
    p[0] = p[2]


precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULT', 'DIV')
    )

# ~ parser = yacc.yacc(debug=True)

# ~ result = parser.parse("1+2")
# ~ print(result)



import ply.lex as lex
import ply.yacc as yacc
import sys

# Create a list to hold all of the token names
tokens = [

    'a',
    'b'

]

t_a = r'a'
t_b = r'b'


t_ignore = r' '


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()


# precedence = (

#     ('left', 'PLUS'),
#     ('left', 'MULTIPLY')

# )


# Define our grammar. We allow expressions, var_assign's and empty's.
def p_start(p):
    '''
    start : S
         | A
         | empty
    '''
    print((p[1]))




'''
𝑆 → 𝐴𝑆|𝑏
𝐴 → 𝑆𝐴|𝑎
'''



def p_r1(p):
    '''
    S : A S 
    '''
    p[0] = (p[1], p[2])

def p_r2(p):
    '''
    S : b
    '''
    p[0] = p[1]

def p_r3(p):
    '''
    S : S A 
    '''
    p[0] = (p[1], p[2])

def p_r4(p):
    '''
    A : a
    '''
    p[0] = p[1]





def p_error(p):
    print(str(p) + "Syntax error found!")


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None





parser = yacc.yacc()


while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)

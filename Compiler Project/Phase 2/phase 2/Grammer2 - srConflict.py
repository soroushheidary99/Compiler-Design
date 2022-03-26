import ply.lex as lex
import ply.yacc as yacc
import sys


tokens = [

    'if',
    'e',
    'then',
    'while',
    'do',
    'begin', 
    'end',
    's',
    'else',
    'semicolon'

]

t_if = r'if'
t_e = r'e'
t_then = r'then'
t_while = r'while'
t_do = r'do'
t_begin = r'begin'
t_end = r'end'
t_s = r's'
t_else = r'else'
t_semicolon = r';'


t_ignore = r' '



def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()




def p_start(p):
    '''
    start : Stmt
         | empty
    '''
    print((p[1]))




'''
𝑆𝑡𝑚𝑡 → 𝑖𝑓 𝑒 𝑡ℎ𝑒𝑛 𝑆𝑡𝑚𝑡 |𝑖𝑓 𝑒 𝑡ℎ𝑒𝑛 𝑆𝑡𝑚𝑡 𝑒𝑙𝑠𝑒 𝑆𝑡𝑚𝑡|𝑤ℎ𝑖𝑙𝑒 𝑒 𝑑𝑜 𝑆𝑡𝑚𝑡 | 𝑏𝑒𝑔𝑖𝑛 𝐿𝑖𝑠𝑡 𝑒𝑛𝑑 | 𝑠
𝐿𝑖𝑠𝑡 → ; 𝑙𝑖𝑠𝑡|𝑆𝑡𝑚𝑡
'''



def p_r1(p):
    '''
    Stmt : if e then Stmt
    '''
    p[0] = (p[1], p[2], p[3], p[4])

def p_r2(p):
    '''
    Stmt : if e then Stmt else Stmt
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])

def p_r3(p):
    '''
    Stmt : while e do Stmt
    '''
    p[0] = (p[1], p[2], p[3], p[4])

def p_r4(p):
    '''
    Stmt : begin List end
    '''
    p[0] = (p[1], p[2], p[3])

def p_r5(p):
    '''
    Stmt : s
    '''
    p[0] = p[1]

def p_r6(p):
    '''
    List : semicolon List
    '''
    p[0] = (p[1], p[2])

def p_r7(p):
    '''
    List : Stmt
    '''
    p[0] = p[1]






def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None





parser = yacc.yacc()

'''
if e then begin ; s end 
'''

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)

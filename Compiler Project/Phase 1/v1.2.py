from enum import Enum
import re


class findError(Exception):

    def __init__(self, expression):
        self.expression = expression


# for error test load errorExample.txt
def readFile():
    with open("Exampleava.txt", 'r') as file:
        data = file.read()
    return readString(data)


def readString(string):
    tokens = list()
    index = 0
    while index < len(string):
        token = tokenIdentify(string, index)
        if token is None:
            break   
        index = token.end
        tokens.append(token)
    if index != len(string):
        print('error is')
        print(string[index])
        raise findError('there is error in char :  '+str(index))

    return tokens


def tokenIdentify(string, begin):
    for type in Type:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, string, re.DOTALL)
        if match:
            end = match.end(1)
            if type == Type.STRING_LITERAL or type == Type.CHARACTER_LITERAL:
                end += 1
            return Token(begin, end, string[begin:end], type)
    return None


class Token:

    def __init__(self, begin, end, value, type):
        self.begin = begin
        self.end = end
        self.value = value
        self.type = type

    def __str__(self):
        return self.type.name + '  =  ' + self.value

    __repr__ = __str__


class Type(Enum):
    BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    LINE_COMMENT = "(//(.*?)[\r$]?\n).*"
    SPACE = "( ).*"
    OPEN_PAREN = "(\\().*"
    CLOSE_PAREN = "(\\)).*"
    SEMICOLON = "(;).*"
    COMMA = "(,).*"
    OPEN_CURLY_BRACE = "(\\{).*"
    CLOSE_CURLY_BRACE = "(\\}).*"
    OPEN_BRACE = "(\\[).*"
    CLOSE_BRACE = "(\\]).*"
    DOUBLE_CONSTANT = "\\b(\\d{1,9}\\.\\d{1,32})\\b.*"
    INT_CONSTANT = "\\b(\\d{1,9})\\b.*"
    VOID = "\\b(void)\\b.*"
    INT = "\\b(int)\\b.*"
    DOUBLE = "\\b(int|double)\\b.*"
    TAB = "(\\t).*"
    NEW_LINE = "(\\n).*"
    PUBLIC = "\\b(public)\\b.*"
    PRIVATE = "\\b(private)\\b.*"
    FALSE = "\\b(false)\\b.*" 
    TRUE = "\\b(true)\\b.*"
    NULL = "\\b(null)\\b.*"
    RETURN = "\\b(return)\\b.*"
    NEW = "\\b(new)\\b.*"
    CLASS = "\\b(class)\\b.*"
    IF = "\\b(if)\\b.*"
    ELSE = "\\b(else)\\b.*"
    WHILE = "\\b(while)\\b.*"
    STATIC = "\\b(static)\\b.*"
    STRING = "\\b(String)\\b.*"
    CHAR = "\\b(char)\\b.*"
    FINAL = "\\b(final)\\b.*"
    ABSTRACT = "\\b(abstract)\\b.*"
    CONTINUE = "\\b(continue)\\b.*"
    FOR = "\\b(for)\\b.*"
    SWITCH = "\\b(switch)\\b.*"
    ASSERT = "\\b(assert)\\b.*"
    DEFAULT = "\\b(default)\\b.*"
    GOTO = "\\b(goto)\\b.*"
    PACKAGE = "\\b(package)\\b.*"
    SYNCHRONIZED = "\\b(synchronized)\\b.*"
    BOOLEAN = "\\b(boolean)\\b.*"
    DO = "\\b(do)\\b.*"
    THIS = "\\b(this)\\b.*"
    BYTE = "\\b(byte)\\b.*"
    IMPORT = "\\b(import)\\b.*"
    THROWS = "\\b(throws)\\b.*"
    BREAK = "\\b(break)\\b.*"
    IMPLEMENTS = "\\b(implements)\\b.*"
    PROTECTED = "\\b(protected)\\b.*"
    THROW = "\\b(throw)\\b.*"
    CASE = "\\b(case)\\b.*"
    ENUM = "\\b(enum)\\b.*"
    INSTANCEOF = "\\b(instanceof)\\b.*"
    TRANSIENT = "\\b(transient)\\b.*"
    CATCH = "\\b(catch)\\b.*"
    EXTENDS = "\\b(extends)\\b.*"
    SHORT = "\\b(short)\\b.*"
    TRY = "\\b(try)\\b.*"
    INTERFACE = "\\b(INTERFACE)\\b.*"
    FINALLY = "\\b(FINALLY)\\b.*"
    LONG = "\\b(LONG)\\b.*"
    STRICTFP = "\\b(strictfp)\\b.*"
    VOLATILE = "\\b(volatile)\\b.*"
    CONST = "\\b(const)\\b.*"
    FLOAT = "\\b(float)\\b.*"
    NATIVE = "\\b(native)\\b.*"
    super = "\\b(super)\\b.*"
    EXPORTS = "\\b(exports)\\b.*"
    MODULE = "\\b(module)\\b.*"
    PROVIDES = "\\b(provides)\\b.*"
    POINT = "(\\.).*"
    PLUS = "(\\+{1}).*"
    MINUS = "(\\-{1}).*"
    MULTIPLY = "(\\*).*"
    DIVIDE = "(/).*"
    EQUAL = "(==).*"
    ASSIGNMENT = "(=).*"
    NOT_EQUAL = "(\\!=).*"
    CLOSE_CARET = "(>).*"
    OPEN_CARET = "(<).*"
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"
    STRING_LITERAL = '\"(\\.|[^\\"])*\"'
    CHARACTER_LITERAL = r"\'(\\.|[^\\'])*\'"


tokens = readFile()

for token in tokens:
    if token.type not in [Type.SPACE, Type.NEW_LINE]:
        print(token)
        print('-------------------------------------')

print("end of tokens")

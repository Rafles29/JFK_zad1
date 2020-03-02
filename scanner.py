import os
import re
import collections

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

class Scanner:

    def __init__(self, input):
        self.__tokens__ = []
        self.current_token_number = 0
        for token in self.tokenize(input):
            self.__tokens__.append(token)

    def print_tokens(self):
        print(self.__tokens__)

    def tokenize(self, file_name):
        with open(file_name, 'r') as file:
            input_string = file.read()

        token_specification = [
            ('NUMBER',  r'[0-9]+'),     # Integer or decimal number
            ('OB',      r'{'),          # Open bracket
            ('CB',      r'}'),          # Close bracket
            ('OSB',     r'\['),          # Open square bracket
            ('CSB',     r'\]'),          # Close square bracket
            ('COLON',   r':'),          # Open square bracket
            ('COMMA',   r','),          # Close square bracket
            ('STRING',  r'\".+?\"'),       # STRING
            ('NEWLINE', r'\n'),         # Line endings
            ('SKIP',    r'[ \t]'),      # Skip over spaces and tabs
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        line_number = 1
        current_position = line_start = 0
        match = get_token(input_string)
        while match is not None:
            type = match.lastgroup
            if type == 'NEWLINE':
                line_start = current_position
                line_number += 1
            elif type != 'SKIP':
                value = match.group(type)
                yield Token(type, value, line_number, match.start()-line_start)
            current_position = match.end()
            match = get_token(input_string, current_position)
        if current_position != len(input_string):
            raise RuntimeError('Error: Unexpected character %r on line %d' % \
                                (input_string[current_position], line_number))
        yield Token('EOF', '', line_number, current_position-line_start)

if __name__ == "__main__":
    scanner = Scanner('exampleFile.txt')
    scanner.print_tokens()
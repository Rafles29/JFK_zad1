class Parser:

    ##### Parser header #####
    def __init__(self, scanner):
        self.next_token = scanner.next_token
        self.token = self.next_token()

    def take_token(self, token_type):
        if self.token.type != token_type:
            self.error(f"Unexpected token: {token_type}, line: {self.token.line}, column: {self.token.column}")
        if token_type != 'EOF':
            self.token = self.next_token()

    def error(self,msg):
        raise RuntimeError(f'Parser error, {msg}')

    ##### Parser body #####
    # Starting symbol
    def start(self):
        # start -> hash EOF
        if self.token.type == 'OB':
            self.hash()
            self.take_token('EOF')
            print('FILE is good')
        else:
            self.error("Epsilon not allowed")

    def hash(self):
        # hash -> OB element hash_cont CB
        if self.token.type == 'OB':
            self.take_token('OB')
            self.element()
            self.hash_cont()
            self.take_token('CB')
        else:
            self.error("Epsilon not allowed")

    def hash_cont(self):
        # hash_cont -> COMMA element hash_xont
        if self.token.type == 'COMMA':
            self.take_token('COMMA')
            self.element()
            self.hash_cont()
        # hash_cont -> eps
        else:
            pass

    def value(self):
        # value -> STRING
        if self.token.type == 'STRING':
            self.take_token('STRING')
        # value -> NUMBER
        elif self.token.type == 'NUMBER':
            self.take_token('NUMBER')
        # value -> hash
        elif self.token.type == 'OB':
            self.hash()
        # value -> table
        elif self.token.type == 'OSB':
            self.table()
        else:
            self.error("Epsilon not allowed")

    def element(self):
        # element -> STRING COLON value
        if self.token.type == 'STRING':
            self.take_token('STRING')
            self.take_token('COLON')
            self.value()
        else:
            self.error("Epsilon not allowed")

    def table(self):
        # table -> OSB STRING table_cont CSB
        if self.token.type == 'OSB':
            self.take_token('OSB')
            self.take_token('STRING')
            self.table_cont()
            self.take_token('CSB')
        else:
            self.error("Epsilon not allowed")

    def table_cont(self):
        # table_cont -> COMMA STRING table_cont
        if self.token.type == 'COMMA':
            self.take_token('COMMA')
            self.take_token('STRING')
            self.table_cont()
        # table_cont -> eps
        else:
            pass

if __name__ == "__main__":
    pass
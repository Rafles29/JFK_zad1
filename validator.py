from scanner import Scanner
from parser import Parser

class JsonSchemaValidator:

    def validate(self, input_file):
        scanner = Scanner(input_file)
        scanner.print_file()

        parser = Parser(scanner)
        parser.start()

if __name__ == "__main__":
    validator = JsonSchemaValidator()
    validator.validate('exampleFile.txt')
    
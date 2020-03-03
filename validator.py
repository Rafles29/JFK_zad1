from scanner import *
from parser import *

def validate(input_file):
    scanner = Scanner(input_file)
    scanner.print_file()

    parser = Parser(scanner)
    parser.start()

if __name__ == "__main__":
    validate('exampleFile.txt')
    
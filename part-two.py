#!/usr/bin/env python3

import os
import string
from time import perf_counter_ns

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

number_names = list(numbers.keys())

def convert_numbers(input):
    for number in number_names:
        input = input.replace(number, f'{number}{numbers[number]}{number}')
    return input

def answer(input_file):
    start = perf_counter_ns()
    delchars = str.maketrans('', '', ''.join([chr for chr in string.printable if not chr.isnumeric()]))

    with open(input_file, "r") as input:
        data = input.read().split('\n')

    cleaned = [convert_numbers(item).translate(delchars) for item in data]
    answer = sum([int(f'{item[0]}{item[-1]}') for item in cleaned])
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)

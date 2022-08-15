#!/usr/bin/env python3

import prompt

def brain_games():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'"Hello, "{name}')

def main():
    brain_games()

if __name__ == '__main__':
    main()

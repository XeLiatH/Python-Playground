# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""


def bubble(numbers: list):
    input_length = len(numbers)
    for i in range(0, input_length):
        for j in range(i + 1, input_length):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


def visual_test():
    print(bubble([20, 5, 6, 3, 25, 15]))


if __name__ == "__main__":
    visual_test()

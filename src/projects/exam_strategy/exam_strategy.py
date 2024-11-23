#!/usr/bin/env python3
"""
`exam_strategy` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""

from collections import namedtuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: list[Item]) -> list[int]:
    """
    General Knapsack solution.

    :param capacity: total knapsack capacity
    :param items: the list of items (named tuples) to consider
    :return: a list of chosen indices

    knapsack algorithm pseudocode:

    """
    # TODO: Implement this function
    ...


def pick_questions_to_answer(filename: str) -> tuple[list[int], int]:
    """
    Main selection function:
    - info on how the files are formatted
        Each input file describes questions of such exam. The first line of the file contains two numbers,
        a floating point t (exam time limit), and an integer n (number of exam questions). The rest of the
        file contains the value (points) and weight (time complexity) of each of the question (item).
        Both values and weights will be integers.
    :param filename: file to process
    :return: the list of chosen indices and total point value of all selected questions
    """
    questions, exam_information = parse_file(filename)
    # implement knapsack from here


def parse_file(filename: str) -> tuple[list[tuple[int, int]], dict]:
    file = open(filename, "r")
    lines = file.readlines()
    # first line of the file
    exam_information = dict()
    exam_information["time_limit"], exam_information["number_of_questions"] = lines[0].split(" ")

    # rest of file
    questions = []
    for line in lines[1:]:
        points, weight = line.split(" ")
        questions.append((points, weight))

    return questions, exam_information


def main():
    """Entry point"""
    for i in range(1, 6):
        ###for debugging
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()

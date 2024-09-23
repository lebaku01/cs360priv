#!/usr/bin/env python3
"""
`classy` implementation and driver

@authors:
@version: 2022.9
"""


def classify(people: dict) -> list[str]:
    """
    Classify people by class

    :param people: group to classify
    :return list of people sorted by class
    """

    '''
    Nested class to handle the sorting of the classes
    '''
    class Class:
        def __init__(self, name, order):
            self.__MAX_DEPTH = 10
            self.name = name
            self.order = order
            self.rank = self.__convert()
        '''
        convert the order to a ternary number "rank" and 
        return the equivalent decimal number basically you can think of 
        the string "upper-middle-upper-middle-lower" as the base 3 number
        "21210" or the decimal number 210. this allows us to use 
        regular relational operations on the rank 
        '''
        def __convert(self):
            ternary = ""
            titles = self.order.split("-")
            for index in range(self.__MAX_DEPTH):
                if index < len(titles):
                    if titles[index] == "upper":
                        ternary += "2"
                    elif titles[index] == "middle":
                        ternary += "1"
                    else:
                        ternary += "0"
                else:
                    ternary += "0"
            return int(ternary, 3)
    '''
    construct new Class objects out of the key-value pairs and 
    sort the list using the rank
    '''
    pairs = people.items()
    output = []
    for pair in pairs:
        output.append(Class(pair[0], pair[1]))
    output.sort(key=lambda x: x.name, reverse=False)
    output.sort(key=lambda x: x.rank, reverse=True)
    for index in range(len(output)):
        #print(output[index].name + " " + str(output[index].order))
        output[index] = output[index].name
    return output


def read_file(filename: str) -> dict[str, str]:
    """
    Read data from the file into a dictionary

    :param filename: file to sort
    :return the {person: class} mapping
    """
    output = dict()
    file = open(filename)
    line = file.readline().split(": ")
    while line != ['']:
        line[1] = line[1].removesuffix(" class\n")
        output[line[0]] = line[1]
        line = file.readline().split(": ")
    return output


def main():
    """Entry point"""
    people = read_file("../../../data/projects/classy/classy03.txt")
    print(classify(people))


if __name__ == "__main__":
    main()

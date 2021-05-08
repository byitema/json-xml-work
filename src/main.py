from argumentparser import ArgumentParser
from jsonmerger import JSONMerger
from entities import Student, Room, CustomEncoder
import json


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    merger = JSONMerger(args[0], args[1])
    rooms = merger.merge()
    print(rooms)

    jsonStr = json.dumps(rooms, cls=CustomEncoder, indent=4)
    with open('./output/rooms.json', 'w') as f:
        f.write(jsonStr)
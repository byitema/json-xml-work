import json
from argumentparser import ArgumentParser
from filehandler import FileHandler
from jsonmerger import JSONMerger


def json2dict(filename):
    raw_data = FileHandler.read(filename)
    return json.loads(raw_data)


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    students_data = json2dict(args['students_file'])
    rooms_data = json2dict(args['rooms_file'])

    rooms = JSONMerger.merge(students_data, rooms_data)

    serialized_data = args['output_format_serializer'].serialize(rooms)

    FileHandler.write(serialized_data, './output/rooms' + '.' + args['output_format'])

from argumentparser import ArgumentParser
from filehandler import FileHandler
from jsonmerger import JSONMerger


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    students_data = FileHandler.read_json(args['students_file'])
    rooms_data = FileHandler.read_json(args['rooms_file'])

    rooms = JSONMerger.merge(students_data, rooms_data)

    serialized_data = args['output_format_serializer'].serialize(rooms)

    FileHandler.write(serialized_data, './output/rooms' + '.' + args['output_format'])

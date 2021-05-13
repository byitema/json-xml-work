from argumentparser import ArgumentParser
from jsonmerger import JSONMerger
from serializer import JSONSerializer, XMLSerializer
from filehandler import FileHandler


output_format_serializer = {
    'json': JSONSerializer,
    'xml': XMLSerializer
}


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    students_data = FileHandler.read_json(args['students_file'])
    rooms_data = FileHandler.read_json(args['rooms_file'])

    rooms = JSONMerger.merge(students_data, rooms_data)

    serialized_data = output_format_serializer[args['output_format']].serialize(rooms)

    FileHandler.write(serialized_data, './output/rooms' + '.' + args['output_format'])


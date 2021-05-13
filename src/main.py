from argumentparser import ArgumentParser
from jsonmerger import JSONMerger
from serializer import JSONSerializer, XMLSerializer


output_format_serializer = {
    'json': JSONSerializer,
    'xml': XMLSerializer
}


def serialize(serializable, serializer_type: str, filename):
    serializer_type = serializer_type.lower()

    sr = output_format_serializer[serializer_type]()
    sr.serialize(serializable)

    sr.write(filename + '.' + serializer_type)


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    merger = JSONMerger(args['students_file'], args['rooms_file'])
    rooms = merger.merge()

    serialize(rooms, args['output_format'], './output/rooms_test')



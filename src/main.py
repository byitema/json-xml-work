from argumentparser import ArgumentParser
from jsonmerger import JSONMerger
from entities import CustomEncoder
from serializer import JSONSerializer, XMLSerializer


def serialize(serializable, serializer_type: str, filename):
    serializer_type = serializer_type.lower()

    if serializer_type == 'json':
        sr = JSONSerializer()
        sr.serialize(serializable, CustomEncoder)
    elif serializer_type == 'xml':
        sr = XMLSerializer()
        sr.serialize(rooms)

    sr.write(filename + '.' + serializer_type)


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_arguments()

    merger = JSONMerger(args['students_file'], args['rooms_file'])
    rooms = merger.merge()

    serialize(rooms, args['output_format'], './output/rooms')

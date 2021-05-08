import argparse
import os


class BaseArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.add_arguments()

    def add_arguments(self):
        pass

    def parse_arguments(self):
        self

    @staticmethod
    def check_path(path: str):
        if os.path.isdir(path):
            return path
        else:
            raise argparse.ArgumentTypeError(f'{path} is not a valid path')


class ArgumentParser(BaseArgumentParser):
    def __init__(self):
        super().__init__()

    def add_arguments(self):
        self.parser.add_argument('--students',
                                 help='path to the students file directory',
                                 type=ArgumentParser.check_path)
        self.parser.add_argument('--rooms',
                                 help='path to the rooms file directory',
                                 type=ArgumentParser.check_path)
        self.parser.add_argument('--format',
                                 help='output format (XML or JSON)',
                                 type=ArgumentParser.check_output_format)

    def parse_arguments(self):
        args = self.parser.parse_args()
        return args.students, args.rooms, args.format

    @staticmethod
    def check_output_format(output_format: str):
        if output_format.upper() in ('XML', 'JSON'):
            return output_format
        else:
            raise argparse.ArgumentTypeError(
                f'{output_format} is not a valid output format (XML or JSON are only available)')


if __name__ == '__main__':
    parser = ArgumentParser()
    print(parser.parse_arguments())

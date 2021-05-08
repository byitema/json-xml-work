import json
from entities import Student, Room


class BaseJSONMerger:
    def merge(self):
        pass

    @staticmethod
    def json2dict(filename):
        with open(filename, 'r') as f:
            dictionary = json.loads(f.read())

        return dictionary


class JSONMerger(BaseJSONMerger):
    def __init__(self, student_filename, rooms_filename):
        self.students_data = JSONMerger.json2dict(student_filename)
        self.rooms_data = JSONMerger.json2dict(rooms_filename)

    def merge(self):
        rooms = []
        rooms_data_dict = dict()

        for room in self.rooms_data:
            r = Room(room['id'], room['name'])
            rooms.append(r)
            rooms_data_dict[r.id] = r

        for student in self.students_data:
            st = Student(student['id'], student['name'], student['room'])
            rooms_data_dict[st.room].add_students(st)

        return rooms

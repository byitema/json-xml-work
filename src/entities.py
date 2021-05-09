import json


class Student:
    def __init__(self, id: int, name: str, room: int):
        self.id = id
        self.name = name
        self.room = room

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, room: {self.room}'


class Room:
    def __init__(self, id: int, name: str, *args):
        self.id = id
        self.name = name
        self.students = list(args)

    def add_students(self, *students):
        for student in students:
            if student.room == self.id:
                self.students.append(student)
            else:
                raise WrongStudentsRoomIdError(self.id, student.room)

    def __repr__(self):
        room_str = f'id: {self.id}, name: {self.name}, students:\n'
        for student in self.students:
            room_str += '\t'
            room_str += student.__repr__()
            room_str += '\n'

        return room_str[:-1]


class WrongStudentsRoomIdError(Exception):
    def __init__(self, room, students_room, message='Student is not from this room: '):
        self.room = room
        self.students_room = students_room
        self.message = message

        self.message += f'this room id = {self.room}, students room id = {self.students_room}'
        super().__init__(self.message)


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Room):
            return {'id': o.id, 'name': o.name, 'students': o.students}
        elif isinstance(o, Student):
            return {'id': o.id, 'name': o.name, 'room': o.room}

        return super(CustomEncoder, self).default(o)

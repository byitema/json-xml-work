from entities import Student, Room


class JSONMerger:
    @staticmethod
    def merge(students_data, rooms_data):
        rooms = []
        rooms_data_dict = dict()

        for room in rooms_data:
            r = Room(room['id'], room['name'])
            rooms.append(r)
            rooms_data_dict[r.id] = r

        for student in students_data:
            st = Student(student['id'], student['name'], student['room'])
            rooms_data_dict[st.room].add_students(st)

        return rooms

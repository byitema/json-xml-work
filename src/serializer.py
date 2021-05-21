import json
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
from entities import Student, Room


class BaseSerializer:
    @staticmethod
    def serialize(serializable):
        pass


class JSONSerializer(BaseSerializer):
    @staticmethod
    def serialize(serializable):
        rooms_dict = {'rooms': serializable}
        return json.dumps(rooms_dict, cls=CustomEncoder, indent=4)


class XMLSerializer(BaseSerializer):
    @staticmethod
    def serialize(serializable):
        data = ET.Element('data')
        rooms_xml = ET.SubElement(data, 'rooms')
        for room in serializable:
            room_xml = ET.SubElement(rooms_xml, 'room')

            room_id = ET.SubElement(room_xml, 'id')
            room_id.text = room.id.__str__()

            room_name = ET.SubElement(room_xml, 'name')
            room_name.text = room.name

            room_students = ET.SubElement(room_xml, 'students')
            for student in room.students:
                student_xml = ET.SubElement(room_students, 'student')

                student_id = ET.SubElement(student_xml, 'id')
                student_id.text = student.id.__str__()

                student_name = ET.SubElement(student_xml, 'name')
                student_name.text = student.name

                student_room = ET.SubElement(student_xml, 'room')
                student_room.text = student.room.__str__()

        data_root = ET.ElementTree(data).getroot()
        return minidom.parseString(ET.tostring(data_root)).toprettyxml()


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Room):
            return {'id': o.id, 'name': o.name, 'students': o.students}
        elif isinstance(o, Student):
            return {'id': o.id, 'name': o.name, 'room': o.room}

        return super(CustomEncoder, self).default(o)

import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


class BaseSerializer:
    def __init__(self):
        self.data = str()

    def serialize(self, serializable):
        pass

    def write(self, filename):
        with open(filename, 'w') as f:
            f.write(self.data)


class JSONSerializer(BaseSerializer):
    def serialize(self, serializable, custom_encoder=None):
        rooms_dict = {'rooms': serializable}
        self.data = json.dumps(rooms_dict, cls=custom_encoder, indent=4)


class XMLSerializer(BaseSerializer):
    def serialize(self, serializable):
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
        self.data = minidom.parseString(ET.tostring(data_root)).toprettyxml()

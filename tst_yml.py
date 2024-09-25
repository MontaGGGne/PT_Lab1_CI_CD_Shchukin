import yaml
import os
import statistics


yaml_content = """
- имя: Иванов Иван Иванович
  математика: 67
  литература: 100
- имя: Петров Петр Петрович
  математика: 78
  физика: 87
"""
        
with open('test.yaml', 'w', encoding='utf-8') as file:
    file.write(yaml_content)


# students = {}
# with open(os.path.join('data', 'data.yaml'), encoding='utf-8') as stream:
#     try:
#         students_list = yaml.safe_load(stream)
#         print(yaml.safe_load(stream))
#         print('ggg')
#     except yaml.YAMLError as exc:
#         print(exc)
# for student in students_list:
#     name = student['имя']
#     del student['имя']
#     students[name] = statistics.mean(student.values())
# quants = statistics.quantiles(students.values())
# rounded_quants = [round(q, 1) for q in quants]
# suitable_students = []
# for k, v in list(students.items()):
#     if rounded_quants[1]>v or v>=rounded_quants[-1]:
#         del students[k]
# print(suitable_students)
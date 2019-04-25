import json

def get_person_base_json(name, year, children, postdoc=0):
    base_json = {}
    base_json['born'] = year
    base_json['firstname'] = name
    base_json['children'] = []
    base_json['postdoc'] = 0
    if postdoc == 1:
        base_json['postdoc'] = 1
    if len(children) != 0:
        for child in children:
            base_json['children'].append(child)

    return base_json


sidney_children = []

sidney_children.append(get_person_base_json('Randy Sherwood McKnight', '1969', []))
sidney_children.append(get_person_base_json('Diandin Zhong', '1969', []))
sidney_children.append(get_person_base_json('Fernando Souto', '1970', []))
sidney_children.append(get_person_base_json('Michael Fontenot', '1970', []))
sidney_children.append(get_person_base_json('Randol Read', '1971', []))
sidney_children.append(get_person_base_json('Tien-Lin Chang', '1971', []))
sidney_children.append(get_person_base_json('Ramesh Agarwal', '1973', []))
sidney_children.append(get_person_base_json('Robert Meyer', '1974', []))
sidney_children.append(get_person_base_json('Jatinder Gulati', '1975', []))
sidney_children.append(get_person_base_json('Shuni Chu', '1981', []))
sidney_children.append(get_person_base_json('Charles Loeffler', '1982', []))
sidney_children.append(get_person_base_json('Howard Johnson', '1982', []))
sidney_children.append(get_person_base_json('Charles Loeffler', '1982', []))
sidney_children.append(get_person_base_json('Michael Heideman', '1982', []))
sidney_children.append(get_person_base_json('Henrik Sorenson', '1988', []))
sidney_children.append(get_person_base_json('Atmadji Soewito', '1990', []))
sidney_children.append(get_person_base_json('Ramesh Gopinath', '1992', []))
sidney_children.append(get_person_base_json('Jose Barreto', '1993', []))
sidney_children.append(get_person_base_json('Dong Wei', '1995', []))
sidney_children.append(get_person_base_json('Ivan Selesnick', '1996', []))
sidney_children.append(get_person_base_json('Jan Odegard', '1996', []))
sidney_children.append(get_person_base_json('Haitao Guo', '1997', []))
sidney_children.append(get_person_base_json('James Lewis', '1998', []))
sidney_children.append(get_person_base_json('Felix Fernandes', '2002', []))
sidney_children.append(get_person_base_json('Ricardo von Borries', '2004', []))
sidney_children.append(get_person_base_json('Ricardo Vargas', '2008', []))

sidney_json = get_person_base_json('', '1965', sidney_children)

with open('sidney.json', 'w') as outfile:
    json.dump(sidney_json, outfile)

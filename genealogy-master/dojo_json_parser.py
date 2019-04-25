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


dojo_children = []

dojo_children.append(get_person_base_json('Ilan Goodman', '2008', []))
dojo_children.append(get_person_base_json('Michael Lexa', '2008', []))
dojo_children.append(get_person_base_json('Jyoti Uppuluri', '2007', []))
dojo_children.append(get_person_base_json('Chris Rozell', '2007', []))
dojo_children.append(get_person_base_json('Mahsa Memarzadeh', '2007', []))
dojo_children.append(get_person_base_json('Sinan Sinanovic', '2006', []))
dojo_children.append(get_person_base_json('Mona Sheikh', '2006', []))
dojo_children.append(get_person_base_json('Courtney Lane', '2003', [], postdoc=1))


dojo_children.append(get_person_base_json('Charlotte Fruner', '1998', []))
dojo_children.append(get_person_base_json('Kang Lee', '1998', []))
dojo_children.append(get_person_base_json('Yue Lin', '1998', []))
dojo_children.append(get_person_base_json('Owen Kelly', '1996', []))
dojo_children.append(get_person_base_json('Jeffrey Smith', '1996', []))
#dojo_children.append(get_person_base_json('Chong Leang', '1994', []))
dojo_children.append(get_person_base_json('Dongmei Li', '1995', []))
dojo_children.append(get_person_base_json('Darren Melton', '1994', []))
dojo_children.append(get_person_base_json('Steven Reynolds', '1993', []))
dojo_children.append(get_person_base_json('Miriam Zacksenhouse', '1993', []))
dojo_children.append(get_person_base_json('Steven Reynolds', '1993', []))
dojo_children.append(get_person_base_json('Larry Ciscon', '1993', []))
dojo_children.append(get_person_base_json('Anand Dabak', '1992', []))
dojo_children.append(get_person_base_json('Srinivasa Rao', '1992', []))
dojo_children.append(get_person_base_json('Sandeep Sibal', '1990', []))
dojo_children.append(get_person_base_json('Anand Kumar', '1990', []))
dojo_children.append(get_person_base_json('Doug Williams', '1989', []))
dojo_children.append(get_person_base_json('Darel Linebarger', '1986', []))
dojo_children.append(get_person_base_json('Stuart DeGraaf', '1984', []))
dojo_children.append(get_person_base_json('Ananthram Swami', '1980', []))

dojo_json = get_person_base_json('', '1974', dojo_children)

with open('dojo.json', 'w') as outfile:
    json.dump(dojo_json, outfile)

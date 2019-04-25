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


tomPark_children = []
tomPark_children.append(get_person_base_json('Douglas Jones', '1987', []))
tomPark_children.append(get_person_base_json('Sergio Cabrera', '1985', []))
tomPark_children.append(get_person_base_json('David Schneibner', '1982', []))
tomPark_children.append(get_person_base_json('Gloria Boudeaux-Bortlels', '1980', []))
tomPark_children.append(get_person_base_json('Gulamabbas Merchant', '1978', []))
tomPark_children.append(get_person_base_json('Dean Kolba', '1979', []))
tomPark_children.append(get_person_base_json('Timothy Quilici', '1976', []))
tomPark_children.append(get_person_base_json('Thomas Scanio', '1972', []))
tomPark_children.append(get_person_base_json('James McClellan', '1972', []))
tomPark_children.append(get_person_base_json('Russell Meier', '1970', []))
tomPark_children.append(get_person_base_json('Yig-Guong Jan', '1970', []))
tomPark_children.append(get_person_base_json('Ralph Warmack', '1968', []))
#tomPark_children.append(get_person_base_json('Douglas Jones', '1987', []))
#tomPark_children.append(get_person_base_json('Galambos Merchant', '1987', []))
#omPark_children.append(get_person_base_json('James McClellan', '1973', []))
##tomPark_children.append(get_person_base_json('Dean Kolba', '1977', []))
#tomPark_children.append(get_person_base_json('Sergio Cabrera', '1985', []))

tomPark_json = get_person_base_json('', '1967', tomPark_children)

with open('tomParks.json', 'w') as outfile:
    json.dump(tomPark_json, outfile)

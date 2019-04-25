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

behnaam_children = []

behnaam_children.append(get_person_base_json('Corina Ionita', '2017', []))
behnaam_children.append(get_person_base_json('Gabriel Pivaro', '2017', []))
behnaam_children.append(get_person_base_json('David Ramirez', '2017', []))
behnaam_children.append(get_person_base_json('Rakesh Malladi', '2016', []))
behnaam_children.append(get_person_base_json('Qiang Xue', '2016', []))
behnaam_children.append(get_person_base_json('Nuwan Ferdinand', '2016', []))

sam_children = []
sam_children.append(get_person_base_json('Hannah Stealey', '2020', []))
sam_children.append(get_person_base_json('Jamieson Warner', '2020', []))
sam_children.append(get_person_base_json('Enrique Contreras', '2020', []))
behnaam_children.append(get_person_base_json('S. Summerson', '2014', sam_children))
behnaam_children.append(get_person_base_json('Matthew Nokleby', '2012', []))
behnaam_children.append(get_person_base_json('Gareth B. Middleton', '2011', []))
behnaam_children.append(get_person_base_json('Chris Steger', '2008', []))
behnaam_children.append(get_person_base_json('Arnab Chakrabarti', '2007', []))
behnaam_children.append(get_person_base_json('Nasir Ahmed', '2005', []))
behnaam_children.append(get_person_base_json('Amir Khojastepour', '2004', []))
behnaam_children.append(get_person_base_json('Tarik Muharemovic', '2004', []))
behnaam_children.append(get_person_base_json('Krishna Kiran Mukkavilli', '2003', []))
behnaam_children.append(get_person_base_json('M. Jaber Borran', '2003', []))
behnaam_children.append(get_person_base_json('Dinesh Rajan', '2002', []))
behnaam_children.append(get_person_base_json('Srikrishna Bhashyam', '2001', []))
behnaam_children.append(get_person_base_json('Suman Das', '2000', []))
behnaam_children.append(get_person_base_json('Chaitali Sengupta', '1999', []))
behnaam_children.append(get_person_base_json('Yile Guo', '1999', []))
behnaam_children.append(get_person_base_json('Jin Lu', '1999', []))
behnaam_children.append(get_person_base_json('Andrew Sendonaris', '1999', []))
behnaam_children.append(get_person_base_json('Raghu Madyastha', '1997', []))
behnaam_children.append(get_person_base_json('Lim Nguyen', '1996', []))
behnaam_children.append(get_person_base_json('Aris Papasakellariou', '1996', []))
behnaam_children.append(get_person_base_json('Narayan P. Mandayam', '1994', []))
behnaam_children.append(get_person_base_json('Maite Brandt-Pearce', '1993', []))
behnaam_children.append(get_person_base_json('Peter Paris', '1991', []))
behnaam_children.append(get_person_base_json('Geoffrey C. Orsak', '1990', []))
behnaam_children.append(get_person_base_json('Mahesh K. Varanasi', '1989', []))

behnaam_children.append(get_person_base_json('Suganya Karunakaran', '2014', [], postdoc=1))
behnaam_children.append(get_person_base_json('Gareth Middleton', '2011', [], postdoc=1))
behnaam_children.append(get_person_base_json('Anna Pentelidou', '2010', [], postdoc=1))
behnaam_children.append(get_person_base_json('Esa Kunnari', '2010', [], postdoc=1))
behnaam_children.append(get_person_base_json('M. Jaber Borran', '2004', [], postdoc=1))
behnaam_children.append(get_person_base_json('Alexandre de Baynast', '2002', [], postdoc=1))
behnaam_children.append(get_person_base_json('Ashutosh Sabharwal', '1999', [], postdoc=1))
behnaam_children.append(get_person_base_json('Marco Lops', '1998', [], postdoc=1))
behnaam_children.append(get_person_base_json('Elza Erkip', '1996', [], postdoc=1))
behnaam_children.append(get_person_base_json('Aria Nosratinia', '1996', [], postdoc=1))
behnaam_children.append(get_person_base_json('Akbar Sayeed', '1996', [], postdoc=1))
behnaam_children.append(get_person_base_json('Venu Veeravalli', '1994', [], postdoc=1))
behnaam_children.append(get_person_base_json('Markku Juntti', '1994', [], postdoc=1))
behnaam_children.append(get_person_base_json('Urs Fawer', '1993', [], postdoc=1))

behnaam_json = get_person_base_json('', '1985', behnaam_children)

with open('behnaam.json', 'w') as outfile:
    json.dump(behnaam_json, outfile)

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


ashok_children = []

# Research Group Alumni - PhD Students

ashok_children.append(get_person_base_json('Adithya Pediredla', '2020', []))
ashok_children.append(get_person_base_json('Ewa Nowara', '2020', []))
ashok_children.append(get_person_base_json('Yicheng Wu', '2020', []))
ashok_children.append(get_person_base_json('Jaehee Park', '2020', []))
ashok_children.append(get_person_base_json('Jasper Tan', '2020', []))
ashok_children.append(get_person_base_json('Vivek Boominathan', '2020', []))
ashok_children.append(get_person_base_json('George Chen', '2019', []))
ashok_children.append(get_person_base_json('Souptik Barua', '2019', []))
ashok_children.append(get_person_base_json('Mayank Kumar', '2018', []))
ashok_children.append(get_person_base_json('Li Niu', '2018', [], postdoc=1)) 
ashok_children.append(get_person_base_json('Temi Prioleau', '2017', [], postdoc=1)) #students?
ashok_children.append(get_person_base_json('Jason Hollaway', '2016', []))


#Alum
ashok_children.append(get_person_base_json('Ali Ayremlou', '2016', []))
ashok_children.append(get_person_base_json('Adam Samaniego', '2016', []))

salman_children =[]
ashok_children.append(get_person_base_json('Salman Asif', '2014', salman_children, postdoc=1)) #UC riverside

#postdoc
aswin_children = [] #self-resarch, CMU prof
"""
aswin_children.append(get_person_base_json('Vishwanath Saragadam', '2019', []))
aswin_children.append(get_person_base_json('Rick Chang', '2019', []))
aswin_children.append(get_person_base_json('Yi Hua', '2019', []))
aswin_children.append(get_person_base_json('Byeongjoo Ahn', '2019', []))
aswin_children.append(get_person_base_json('Vijay Rengarajan', '2019', [], postdoc=1))
aswin_children.append(get_person_base_json('Michael De Zeeuw', '2019', []))
aswin_children.append(get_person_base_json('Wei-Yu Chen', '2019', []))
#alum
aswin_children.append(get_person_base_json('Jian Wang', '2018', []))
aswin_children.append(get_person_base_json('Zhuo Hui', '2019', []))
aswin_children.append(get_person_base_json('Chia-Yin Tsai', '2019', []))
aswin_children.append(get_person_base_json('David Shaw', '2015', [], postdoc=1))
aswin_children.append(get_person_base_json('Canyi Lu', '2018', [],postdoc=1))
aswin_children.append(get_person_base_json('Kuldeep Kulkarni', '2019', [],postdoc=1))
"""
ashok_children.append(get_person_base_json('Aswin C Sankaranarayanan', '2012', aswin_children, postdoc=1)) 


kaushik_children = []
"""
kaushik_children.append(get_person_base_json('Prasan A Shedligeri', '2019', []))
kaushik_children.append(get_person_base_json('Gopi Raju Matta', '2019', []))
"""
#other MS students
ashok_children.append(get_person_base_json('Kaushik Mitra', '2011', kaushik_children, postdoc=1)) #2011-2014





ashok_json = get_person_base_json('', '2009', ashok_children) #finished PhD in 2008

with open('ashok.json', 'w') as outfile:
    json.dump(ashok_json, outfile)

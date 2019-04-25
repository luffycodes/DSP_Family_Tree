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


jcavallaro_children = []

# Research Group Alumni - PhD Students
jcavallaro_children.append(get_person_base_json('Nadya Mohamed', '2020', []))
jcavallaro_children.append(get_person_base_json('Chance Tarver', '2020', []))
jcavallaro_children.append(get_person_base_json('Sepideh Nouri', '2020', []))
jcavallaro_children.append(get_person_base_json('Kaipeng Li', '2019', [])) #defended? Amazon
jcavallaro_children.append(get_person_base_json('Michael Wu', '2017', [])) #defended? Xilinx

jcavallaro_children.append(get_person_base_json('Aida Vosoughi', '2016', []))
jcavallaro_children.append(get_person_base_json('Bei Yin', '2014', []))
jcavallaro_children.append(get_person_base_json('Gouhui Wang', '2014', [])) #defended, snapchat
jcavallaro_children.append(get_person_base_json('Johnanna Ketonen', '2012', [])) #nokia
jcavallaro_children.append(get_person_base_json('Markus Myllyla', '2011', [])) #nokia
jcavallaro_children.append(get_person_base_json('Yang Sun', '2011', []))

jcavallaro_children.append(get_person_base_json('Kiarash Amiri', '2011', []))

studer_children = []
"""
studer_children.append(get_person_base_json('Alexandra Gallyas-Sanhueza', '2020', []))
studer_children.append(get_person_base_json('Seyed Hadi Mirfarshbafan', '2020', []))
studer_children.append(get_person_base_json('Brian Rappaport', '2020', []))
studer_children.append(get_person_base_json('Oscar Castaneda', '2020', []))
studer_children.append(get_person_base_json('Emre Gonultas', '2020', []))
studer_children.append(get_person_base_json('Ramina Ghods', '2020', []))
studer_children.append(get_person_base_json('Michael Pelissier', '2020', []))
studer_children.append(get_person_base_json('Charles Jeon', '2020', []))
studer_children.append(get_person_base_json('Igor Labutov', '2020', []))
"""
jcavallaro_children.append(get_person_base_json('Christoph Studer', '2010', studer_children, postdoc=1)) #Richb coadvised


jcavallaro_children.append(get_person_base_json('Manik Gadhiok', '2008', []))

jcavallaro_children.append(get_person_base_json('Marjan Karkooti', '2009', []))
jcavallaro_children.append(get_person_base_json('Predrag Radosavljevic', '2008', []))




jcavallaro_children.append(get_person_base_json('Vikram Chandrasekhar', '2008', [])) 



jcavallaro_children.append(get_person_base_json('Michael Brogioli', '2007', []))
jcavallaro_children.append(get_person_base_json('Alex de Baynast', '2005', [], postdoc=1)) #joint with behnam.
jcavallaro_children.append(get_person_base_json('Yuanbin Guo', '2005', []))
jcavallaro_children.append(get_person_base_json('Sridhar Rajagopal', '2004', []))
jcavallaro_children.append(get_person_base_json('Mani Vaya', '2003', [])) 
jcavallaro_children.append(get_person_base_json('Martin Leuschen', '2002', [])) 
jcavallaro_children.append(get_person_base_json('Bryan Jones', '2002', []))  #at mississipi state but don't see students
jcavallaro_children.append(get_person_base_json('Kanu Chadha', '2001', [])) 
jcavallaro_children.append(get_person_base_json('Martin Leuschen', '2001', []))
jcavallaro_children.append(get_person_base_json('Suman Das', '2000', [])) #Behnam coadvised
jcavallaro_children.append(get_person_base_json('Vishwas Sundaramurthy', '1999', [])) 
jcavallaro_children.append(get_person_base_json('Gang Xu', '1998', [])) 
jcavallaro_children.append(get_person_base_json('Chaitali Sengupta', '1998', [])) 
jcavallaro_children.append(get_person_base_json('Chaitali Sengupta', '1998', [])) 
jcavallaro_children.append(get_person_base_json('Kishore Kota', '1996', [])) 
elza_children = [] #none listed on google doc
jcavallaro_children.append(get_person_base_json('Elza Erkip', '1996', [], postdoc=1)) #joint with behnam. now NYU. Technically PhD at stanford

jcavallaro_children.append(get_person_base_json('N. D. Hemkumar', '1994', [])) 
jcavallaro_children.append(get_person_base_json('Monica L. Visinsky', '1994', [])) 
jcavallaro_children.append(get_person_base_json('Nariankadu Hemkumar', '1992', [])) 




jcavallaro_json = get_person_base_json('', '1988', jcavallaro_children) #joined rice 1988

with open('jcavallaro.json', 'w') as outfile:
    json.dump(jcavallaro_json, outfile)

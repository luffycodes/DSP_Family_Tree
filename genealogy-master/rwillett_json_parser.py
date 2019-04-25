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


rwillett_children = []
# PhD students

rwillett_children.append(get_person_base_json('Ben Mark', '2020', []))

rwillett_children.append(get_person_base_json('Willem Marais', '2020', []))
rwillett_children.append(get_person_base_json('Davis Gilton', '2020', []))

rwillett_children.append(get_person_base_json('Jorge Silva', '2020', [], postdoc=1)) #industry
rwillett_children.append(get_person_base_json('Kwang-Sung Jun', '2017', [], postdoc=1)) #asu now, no students
rwillett_children.append(get_person_base_json('Amin Jalali', '2017', [], postdoc=1)) #industry
rwillett_children.append(get_person_base_json('Ravi Sastry', '2014', [], postdoc=1)) #industry
rwillett_children.append(get_person_base_json('Zachary Harmany', '2012', []))
rwillett_children.append(get_person_base_json('Kalyani Krishnamurthy', '2011', []))
rwillett_children.append(get_person_base_json('Eric Hall', '2015', []))
rwillett_children.append(get_person_base_json('Albert Oh', '2015', []))



# Research Group Alumni - postdocs
yao_children = [] #self-research
"""
yao_children.append(get_person_base_json('Shuang Li', '2020', []))
yao_children.append(get_person_base_json('Xi He', '2020', []))
yao_children.append(get_person_base_json('Liyan Xie', '2020', []))
yao_children.append(get_person_base_json('Shixiang Zhu', '2020', []))
yao_children.append(get_person_base_json('Rui Zhang', '2020', []))
yao_children.append(get_person_base_json('Henry Yuchi', '2020', []))

yao_children.append(get_person_base_json('Junzhuo Chen', '2020', [])) #alum
yao_children.append(get_person_base_json('Yang Cao', '2020', [])) #alum
"""
rwillett_children.append(get_person_base_json('Yao Xie', '2013', yao_children, postdoc=1))

jsalmon_children=[] #self-research
"""
jsalmon_children.append(get_person_base_json('Mathurin Massias', '2020', []))
jsalmon_children.append(get_person_base_json('Jerome-Alexis Chevalier', '2020', []))
jsalmon_children.append(get_person_base_json('Evgenii Chzhen', '2020', []))
jsalmon_children.append(get_person_base_json('Quentin Bertrand', '2020', []))
jsalmon_children.append(get_person_base_json('Nidham Gazagnadou', '2020', []))
jsalmon_children.append(get_person_base_json('Eugene Ndiaye', '2020', []))
jsalmon_children.append(get_person_base_json('Jean Lafond', '2020', []))
jsalmon_children.append(get_person_base_json('Igor Colin', '2020', []))
jsalmon_children.append(get_person_base_json('Jair Montoya', '2020', []))
jsalmon_children.append(get_person_base_json('Thierry Guillemot', '2020', []))
"""
rwillett_children.append(get_person_base_json('Joseph Salmon', '2012', jsalmon_children, postdoc=1))

laura_children=[]
"""
laura_children.append(get_person_base_json('Dejiao Zhang', '2020', []))
laura_children.append(get_person_base_json('David Hong', '2020', []))
laura_children.append(get_person_base_json('Zhe Du', '2020', []))
laura_children.append(get_person_base_json('Amanda Bower', '2020', []))
laura_children.append(get_person_base_json('Yutong Wang', '2020', []))
laura_children.append(get_person_base_json('Kyle Gilman', '2020', []))
laura_children.append(get_person_base_json('Alex Ritchie', '2020', []))
laura_children.append(get_person_base_json('Ali SOltani-Tehrani', '2020', [], postdoc=1))
laura_children.append(get_person_base_json('Greg Ongie', '2020', []))
laura_children.append(get_person_base_json('John Lipor', '2020', []))
"""
rwillett_children.append(get_person_base_json('Laura Balzano', '2012', laura_children, postdoc=1))


maxim_children=[] #self-research
"""
maxim_children.append(get_person_base_json('Yifeng Chu', '2020', []))
maxim_children.append(get_person_base_json('Joshua Hanson', '2020', []))
maxim_children.append(get_person_base_json('Belinda Tzen', '2020', []))
maxim_children.append(get_person_base_json('Ehsan Shafieepoorfad', '2020', []))
maxim_children.append(get_person_base_json('Jaeho Lee', '2020', []))
maxim_children.append(get_person_base_json('Naci Saldi', '2020', [], postdoc=1))
maxim_children.append(get_person_base_json('Yanina Shkel', '2020', [], postdoc=1))
maxim_children.append(get_person_base_json('Aolin Xu', '2020', []))
maxim_children.append(get_person_base_json('Daphney-Stavroula Zois', '2020', [], postdoc=1))
maxim_children.append(get_person_base_json('Peng Guan', '2020', []))
maxim_children.append(get_person_base_json('Aray Kaliyeva', '2020', []))
maxim_children.append(get_person_base_json('Soomin Lee', '2020', [],postdoc=1))
maxim_children.append(get_person_base_json('Xiaoyu Guang', '2020', []))
"""
rwillett_children.append(get_person_base_json('Maxim Raginsky', '2010', maxim_children, postdoc=1))

roummel_children = [] #self-research
"""
roummel_children.append(get_person_base_json('Omar Deguchy', '2020', []))
roummel_children.append(get_person_base_json('Jacob Rafati', '2020', []))
roummel_children.append(get_person_base_json('Lori Lewis', '2020', []))
roummel_children.append(get_person_base_json('Ashley De Luna', '2020', []))
roummel_children.append(get_person_base_json('Jacqueline Alvarez', '2020', []))
roummel_children.append(get_person_base_json('Alex Ho', '2020', []))
roummel_children.append(get_person_base_json('Hansell Perez', '2020', []))
roummel_children.append(get_person_base_json('Harry Chen', '2020', []))
roummel_children.append(get_person_base_json('Seda Senay', '2020', [], postdoc=1))
roummel_children.append(get_person_base_json('Naveen Somasundream', '2020', [], postdoc=1))
roummel_children.append(get_person_base_json('Johannes Brust', '2020', []))
roummel_children.append(get_person_base_json('Lasith Adhikari', '2020', []))
roummel_children.append(get_person_base_json('Zachary Harmany', '2020', []))
roummel_children.append(get_person_base_json('Daniel Thompson', '2020', []))
roummel_children.append(get_person_base_json('Daniel Swanson', '2020', []))
roummel_children.append(get_person_base_json('Victoria Arias', '2020', []))
roummel_children.append(get_person_base_json('Joanna Valenzuela', '2020', []))
roummel_children.append(get_person_base_json('Aramayis Orkusyan', '2020', []))
roummel_children.append(get_person_base_json('Natalie Azevedo', '2020', []))
roummel_children.append(get_person_base_json('Rubi Almanza', '2020', []))
roummel_children.append(get_person_base_json('David Jones', '2020', []))
roummel_children.append(get_person_base_json('Vibhor Jain', '2020', []))
roummel_children.append(get_person_base_json('Rachel Schlick', '2020', []))
roummel_children.append(get_person_base_json('Brent Edmunds', '2020', []))
roummel_children.append(get_person_base_json('James Hernandez', '2020', []))
"""
rwillett_children.append(get_person_base_json('Roummel Marcia', '2008', roummel_children, postdoc=1))












rwillett_json = get_person_base_json('', '2005', rwillett_children) #started at duke in 2005

with open('rwillett.json', 'w') as outfile:
    json.dump(rwillett_json, outfile)

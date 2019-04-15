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


richb_children = []

# Research Group Alumni - PhD Students
richb_children.append(get_person_base_json('Christopher Metzler', '2018', []))
richb_children.append(get_person_base_json('Ali Mousavi', '2018', []))
richb_children.append(get_person_base_json('AmirAli Aghazadeh', '2017', []))

lan_children= []
lan_children.append(get_person_base_json('Aritra Ghosh', '2020', []))
lan_children.append(get_person_base_json('Brian Zylich', '2020', []))
richb_children.append(get_person_base_json('Mr. Lan', '2015', lan_children))

richb_children.append(get_person_base_json('Andrew Waters', '2014', []))
richb_children.append(get_person_base_json('Eva Dyer', '2014', []))

hedge_children = []
hedge_children.append(get_person_base_json('Mohammadreza Soltani', '2020', []))
hedge_children.append(get_person_base_json('Gauri Jagatap', '2020', []))
hedge_children.append(get_person_base_json('Thanh Nguyen', '2020', []))
hedge_children.append(get_person_base_json('Viraj Shah', '2020', []))
hedge_children.append(get_person_base_json('Ameya Joshi', '2020', []))
hedge_children.append(get_person_base_json('Amitangshu Mukherjee', '2020', []))
hedge_children.append(get_person_base_json('Daniel Cho', '2020', []))
richb_children.append(get_person_base_json('Chinmay Hegde', '2012', hedge_children))

richb_children.append(get_person_base_json('Jason Laska', '2012', []))
richb_children.append(get_person_base_json('Mona Sheikh', '2010', []))

mark_children = []
mark_children.append(get_person_base_json('Hongteng Xu', '2020', []))
mark_children.append(get_person_base_json('Michael Moore', '2020', []))
mark_children.append(get_person_base_json('Andrew Massimino', '2020', []))
mark_children.append(get_person_base_json('Liangbei Xu', '2020', []))
mark_children.append(get_person_base_json('Santhosh Karnik', '2020', []))
mark_children.append(get_person_base_json('Chieh-Feng Cheng', '2020', []))
mark_children.append(get_person_base_json('Matthew O’Shaughnessy', '2020', []))
mark_children.append(get_person_base_json('Niranjan Kannabiran', '2020', []))
mark_children.append(get_person_base_json('Nauman Ahad', '2020', []))
mark_children.append(get_person_base_json('Andrew McRae', '2020', []))
mark_children.append(get_person_base_json('Namrata Nadagouda', '2020', []))

richb_children.append(get_person_base_json('Mark Davenport', '2010', mark_children))


marko_children = []
marko_children.append(get_person_base_json('Shermin Hamzehei', '2020', []))
marko_children.append(get_person_base_json('Siwei Feng', '2019', []))
marko_children.append(get_person_base_json('Dian Mo', '2018', []))
marko_children.append(get_person_base_json('Hamid Dadkhahi', '2016', []))
richb_children.append(get_person_base_json('Marco Duarte', '2009', marko_children))

richb_children.append(get_person_base_json('Shriram Sarvotham', '2008', []))

mike_children = []
mike_children.append(get_person_base_json('Xinshuo Yang', '2020', []))
mike_children.append(get_person_base_json('Shuang Li', '2020', []))
mike_children.append(get_person_base_json('Justin Jayne', '2020', []))
mike_children.append(get_person_base_json('Anna Titova', '2020', []))
mike_children.append(get_person_base_json('Jon Helland', '2020', []))
mike_children.append(get_person_base_json('Dehui Yang', '2020', []))
mike_children.append(get_person_base_json('Zhihui Zhu', '2020', []))
mike_children.append(get_person_base_json('Armin Eftekhari', '2020', []))
mike_children.append(get_person_base_json('Chia Wei Lim', '2020', []))
mike_children.append(get_person_base_json('Jae Young Park', '2020', []))
mike_children.append(get_person_base_json('Alejandro Weinstein', '2020', []))
mike_children.append(get_person_base_json('Borhan Sanandaji', '2020', []))
mike_children.append(get_person_base_json('Michael Coco', '2020', []))
richb_children.append(get_person_base_json('Mike Wakin', '2006', mike_children))


richb_children.append(get_person_base_json('Ray Wagner', '2007', []))
richb_children.append(get_person_base_json('Vinay Ribeiro', '2005', []))
richb_children.append(get_person_base_json('Nadeem Ahmed', '2004', []))

justin_children = []
salman_children = []
# salman_children.append(get_person_base_json('Rakib Hyder', '2020', []))
# salman_children.append(get_person_base_json('Yucheng Zhang', '2020', []))
# salman_children.append(get_person_base_json('Fahimeh Arab', '2020', []))

justin_children.append(get_person_base_json('M Salman Asif', '2020', salman_children))
justin_children.append(get_person_base_json('William Mantzel', '2020', []))
justin_children.append(get_person_base_json('Ali Ahmed', '2020', []))
justin_children.append(get_person_base_json('Chris Turnes', '2020', []))
justin_children.append(get_person_base_json('Aurele Balavoine', '2020', []))
justin_children.append(get_person_base_json('Nishant Zachariah', '2020', []))
justin_children.append(get_person_base_json('Ning Tian', '2020', []))
justin_children.append(get_person_base_json('Kevin Beale', '2020', []))
justin_children.append(get_person_base_json('Shaojie Xu', '2020', []))
justin_children.append(get_person_base_json('Sihan Zeng', '2020', []))
justin_children.append(get_person_base_json('Jihui Jhu', '2020', []))
justin_children.append(get_person_base_json('Alireza Aghasi', '2020', []))
justin_children.append(get_person_base_json('Sohail Bahmani', '2020', []))
justin_children.append(get_person_base_json('Jeff Dugger', '2020', []))
justin_children.append(get_person_base_json('Kiryung Lee', '2020', []))
justin_children.append(get_person_base_json('Thinh Doan', '2020', []))
richb_children.append(get_person_base_json('Justin Romberg', '2003', justin_children))

richb_children.append(get_person_base_json('Ramesh Neelamani', '2003', []))
richb_children.append(get_person_base_json('Timothy Dorney', '2001', []))
richb_children.append(get_person_base_json('Rohit Gaikwad', '2000', []))
richb_children.append(get_person_base_json('Roger Claypoole', '1999', []))
richb_children.append(get_person_base_json('Matthew Crouse', '1999', []))

# Research Group Alumni - Postdocs
richb_children.append(get_person_base_json('Gautam Dasarathy', '2016', [], postdoc=1))
richb_children.append(get_person_base_json('Phillip Grimaldi', '2014', [], postdoc=1))

chi_children = []
chi_children.append(get_person_base_json('Brian Gaines', '2020', []))
chi_children.append(get_person_base_json('Meng Yang', '2020', []))
chi_children.append(get_person_base_json('Xu Han', '2020', []))
chi_children.append(get_person_base_json('Min Zhang', '2020', []))
richb_children.append(get_person_base_json('Eric Chi', '2013', chi_children, postdoc=1))

richb_children.append(get_person_base_json('Ankit Patel', '2013', [], postdoc=1))
richb_children.append(get_person_base_json('Mohammad Golbabaee', '2013', [], postdoc=1))
richb_children.append(get_person_base_json('Thomas Goldstein', '2012', [], postdoc=1))
richb_children.append(get_person_base_json('Divyanshu Vats', '2011', [], postdoc=1))
richb_children.append(get_person_base_json('Jianing Shi', '2011', [], postdoc=1))

studer_children = []
studer_children.append(get_person_base_json('Alexandra Gallyas-Sanhueza', '2020', []))
studer_children.append(get_person_base_json('Seyed Hadi Mirfarshbafan', '2020', []))
studer_children.append(get_person_base_json('Brian Rappaport', '2020', []))
studer_children.append(get_person_base_json('Oscar Castaneda', '2020', []))
studer_children.append(get_person_base_json('Emre Gonultas', '2020', []))
studer_children.append(get_person_base_json('Ramina Ghods', '2020', []))
studer_children.append(get_person_base_json('Michael Pelissier', '2020', []))
studer_children.append(get_person_base_json('Charles Jeon', '2020', []))
studer_children.append(get_person_base_json('Igor Labutov', '2020', []))
richb_children.append(get_person_base_json('Christoph Studer', '2010', studer_children, postdoc=1))

ashwin_children = []
ashwin_children.append(get_person_base_json('Anqi Yang', '2020', []))
ashwin_children.append(get_person_base_json('Michael De', '2020', []))
ashwin_children.append(get_person_base_json('Wei-Yu Chen', '2020', []))
ashwin_children.append(get_person_base_json('Byeongjoo Ahn', '2020', []))
ashwin_children.append(get_person_base_json('Yi Hua', '2020', []))
ashwin_children.append(get_person_base_json('Vishwanath Saragadam', '2020', []))
ashwin_children.append(get_person_base_json('Rick Chang', '2020', []))
ashwin_children.append(get_person_base_json('Harry Hui', '2020', []))
ashwin_children.append(get_person_base_json('Chia-Yin', '2020', []))
ashwin_children.append(get_person_base_json('Jian Wang', '2020', []))
richb_children.append(get_person_base_json('Aswin S', '2009', ashwin_children, postdoc=1))

arian_children = []
arian_children.append(get_person_base_json('Haolei Wang', '2020', []))
arian_children.append(get_person_base_json('Morgane Austern', '2020', []))
arian_children.append(get_person_base_json('Shuaiwen Wang', '2020', []))
arian_children.append(get_person_base_json('Ji Xu', '2020', []))
arian_children.append(get_person_base_json('Milad Bakhshizadeh', '2020', []))
arian_children.append(get_person_base_json('Rishabh Dudeja', '2020', []))
arian_children.append(get_person_base_json('Wenda Zhu', '2020', []))
richb_children.append(get_person_base_json('Arian Maleki', '2010', arian_children, postdoc=1))

jarvis_children = []
jarvis_children.append(get_person_base_json('Akshay Soni', '2020', []))
jarvis_children.append(get_person_base_json('Swayambhoo Jain', '2020', []))
jarvis_children.append(get_person_base_json('Mojtaba Kadkhodaie', '2020', []))
jarvis_children.append(get_person_base_json('Xingguo Li', '2020', []))
jarvis_children.append(get_person_base_json('Di Xiao', '2020', []))
jarvis_children.append(get_person_base_json('Sirisha Rambhatla', '2020', []))
jarvis_children.append(get_person_base_json('Abhinav Sambasivan', '2020', []))
jarvis_children.append(get_person_base_json('Jineng Ren', '2020', []))
jarvis_children.append(get_person_base_json('Akshay Kumar', '2020', []))
jarvis_children.append(get_person_base_json('Gamini Udawat', '2020', []))
richb_children.append(get_person_base_json('Jarvis Haupt', '2009', jarvis_children, postdoc=1))

volkan_children = []
volkan_children.append(get_person_base_json('Tasos Kyrillidis', '2020', []))
volkan_children.append(get_person_base_json('Marwa El Halabi', '2020', []))
volkan_children.append(get_person_base_json('Yen-Huan Li', '2020', []))
volkan_children.append(get_person_base_json('Ilija Bogunovic', '2020', []))
volkan_children.append(get_person_base_json('Jonathan Scarlett', '2020', []))
richb_children.append(get_person_base_json('Volkan Cevher', '2007', [], postdoc=1))

richb_children.append(get_person_base_json('Petros Boufounos', '2008', [], postdoc=1))
richb_children.append(get_person_base_json('Chris Rozell', '2007', [], postdoc=1))
richb_children.append(get_person_base_json('Dror Baron', '2003', [], postdoc=1))
richb_children.append(get_person_base_json('Veronique Delouille', '2003', [], postdoc=1))
richb_children.append(get_person_base_json('Rutger van Spaendonck', '2003', [], postdoc=1))
richb_children.append(get_person_base_json('Xin Wang', '2001', [], postdoc=1))
richb_children.append(get_person_base_json('Maarten Jansen', '2000', [], postdoc=1))
richb_children.append(get_person_base_json('Mark Coates', '1999', [], postdoc=1))
richb_children.append(get_person_base_json('Vidya Venkatachalam', '2000', [], postdoc=1))
richb_children.append(get_person_base_json('Hyeokho Choi', '1998', [], postdoc=1))
richb_children.append(get_person_base_json('Rolf Riedi', '1997', [], postdoc=1))
richb_children.append(get_person_base_json('Ivan Magrin Chagnolleau', '1998', [], postdoc=1))
richb_children.append(get_person_base_json('Jan Odegard', '1997', [], postdoc=1))
richb_children.append(get_person_base_json('Philippe Steeghs', '1997', [], postdoc=1))

nowak_children = []
richb_children.append(get_person_base_json('Robert Nowak', '1995', nowak_children, postdoc=1))
richb_children.append(get_person_base_json('Paulo Goncalves', '1994', [], postdoc=1))


# Current Research Group
richb_children.append(get_person_base_json('Hamid Javadi', '2017', []))
richb_children.append(get_person_base_json('Randall Balestriero', '2017', []))
richb_children.append(get_person_base_json('CJ Barberan', '2015', []))
richb_children.append(get_person_base_json('Daniel LeJeune', '2017', []))
richb_children.append(get_person_base_json('Pavan Kota', '2017', []))
richb_children.append(get_person_base_json('Lorenzo Luzi', '2017', []))
richb_children.append(get_person_base_json('Indu Manickam', '2016', []))
richb_children.append(get_person_base_json('Tan Minh Nguyen', '2015', []))
richb_children.append(get_person_base_json('Shashank Sonkar', '2017', []))
richb_children.append(get_person_base_json('Jasper Tan', '2015', []))
richb_children.append(get_person_base_json('Jack Wang', '2016', []))

richb_json = get_person_base_json('', '1990', richb_children)

with open('richb.json', 'w') as outfile:
    json.dump(richb_json, outfile)

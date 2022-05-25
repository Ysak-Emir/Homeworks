GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bug': {'fails', 'errors', 'stack'}
}

GeekTech.pop('bug')
GeekTech['address'] = 'Ibraimova, 103 Bishkek, 720011'
GeekTech['courses'] = set()
GeekTech['courses'] = 'Android', 'Backend', 'Fronted', 'Fullstack', 'IOS', 'English', 'UX/UI', 'GeekCamp', 'Computer basics'
GeekTech['numbers'] = '507 05 2018', '777 05 2018', '557 05 2018'
GeekTech['instagram'] = '@geektech__kg'



print("Информация GeekTech: ")
for key, value in GeekTech.items():
    print(f"Ключ: {key}")
    print(f"Значение: {value}")



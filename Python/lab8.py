#Найти количество полицейских участков и вывести их в алфавитном порядке (по адресу)
from xml.etree import ElementTree as ET


def get_police_stations(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    police_stations = []

    for node in root.iter('node'):
        tags = node.findall("tag")
        station_name = ""
        for tag in tags:
            if tag.get("k") == "amenity" and tag.get("v") == "police":
                station_name = node.find("tag[@k='name']")
                if station_name is not None:
                    police_stations.append((station_name.get("v"), node.get("id")))

    for way in root.iter('way'):
        tags = way.findall('tag')
        station_name = ""
        for tag in tags:
            if tag.get("k") == "amenity" and tag.get("v") == "police":
                station_name = way.find("tag[@k='name']")
                if station_name is not None:
                    police_stations.append((station_name.get("v"), way.get("id")))

    for relation in root.iter('relation'):
        tags = relation.findall("tag")
        station_name = ""
        for tag in tags:
            if tag.get("k") == "amenity" and tag.get("v") == "police":
                station_name = relation.find("tag[@k='name']")
                if station_name is not None:
                    police_stations.append((station_name.get("v"), relation.get("id")))

    return sorted(police_stations, key=lambda x: x[0])


filename = "lab8/6.osm"
police_stations = get_police_stations(filename)
for station in police_stations:
    print(station[0])
print(f"Всего полицейских участков в первом файле: {len(police_stations)}")
print()

filename = 'lab8/6 - 2.osm'
police_stations = get_police_stations(filename)
for station in police_stations:
    print(station[0])
print(f'Всего полицейских участков во втором файле: {len(police_stations)}')

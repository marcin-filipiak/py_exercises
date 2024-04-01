import xml.etree.ElementTree as ET

# Parsowanie pliku XML
tree = ET.parse('dane.xml')
root = tree.getroot()

# Wyświetlanie zawartości pliku XML
for child in root:
    print(child.tag, child.attrib)


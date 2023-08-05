import xml.etree.ElementTree as ET


def get_value_xpath():
    tree = ET.parse("sma_gentext.xml")
    lst = tree.findall(".//*[@id='42007']/target")
    value = lst[0].text

    with open('value_xpath.txt', 'w', encoding='utf-8') as f:
        f.write(value)


def get_value_iteration():
    tree = ET.parse("sma_gentext.xml")

    found_id = False
    value = ''
    for unit in tree.iter():
        if unit.tag == 'trans-unit' and unit.attrib['id'] == '42007':
            found_id = True
        elif found_id and unit.tag == 'target':
            value = unit.text
            break

    with open('value_iteration.txt', 'w', encoding='utf-8') as f:
        f.write(value)


if __name__ == '__main__':
    get_value_xpath()
    get_value_iteration()


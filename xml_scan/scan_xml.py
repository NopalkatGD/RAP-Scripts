import xml.etree.ElementTree as ET

class ScanXml:
    def __init__(self, file, namespaces={"key":"value"}) -> None:
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()
        self.namespaces = namespaces
    def valuetag(self, xpath):
        try:
            return self.root.find(xpath,self.namespaces).text
        except:
            return None
    def valueattrib(self, xpath, attb):
        try:
            return self.root.find(xpath,self.namespaces).attrib[attb]
        except:
            return None
    def rootattrib(self,attb):
        try:
            return self.root.attrib[attb]
        except:
            return None
    def get_tags_by_tags(self, xpath):
        try:
            lst_tags = []
            for etiqueta in self.root.findall(xpath, self.namespaces):
                lst_tags.append(etiqueta.tag)
            return lst_tags
        except:
            return None
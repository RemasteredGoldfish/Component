class Component:
    processor : str
    voeding : str
    ipnr : str
    type : str = 'unknown'
    name: str = 'unknown'
    netwerk: str = ''

    def __init__(self, type: str, name: str, processor: str, voeding: str, ipnr: str):
        self.processor = processor
        self.voeding = voeding
        self.ipnr = ipnr
        self.type = type
        self.name = name

    def __str__(self):
        connection = ''
        if self.netwerk != '':
            connection = ' connected to ' + self.netwerk
        return 'Component: ' + self.processor + connection

    def connect(self, netwerknaam):
        self.netwerk = netwerknaam

switch1 = Component('switch','netgear','AMD123', '6V','192.168.1.1')
switch1.connect('ICT-academie-2')
print(switch1)
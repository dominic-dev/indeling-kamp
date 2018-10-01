class Persoon:
    def __init__(self, row=None):
        self.naam = ''
        self.dag_2 = []
        self.dag_3 = []
        self.dag_4 = []
        self.dag_5 = []
        self.dag_6 = []
        self.dag_7 = []
        self.dag_8 = []
        self.dag_9 = []
        self.dag_10 = []
        self.dag_11 = []

        self.tag = ''

        if row:
            self.parse(row)

    def parse(self, row):
        self.naam = row[1]
        print(self.naam)
        self.dag_2 = row[2:5]
        self.dag_3 = row[5:8]
        self.dag_4 = row[8:11]
        self.dag_5 = row[11:14]
        self.dag_6 = row[14:17]
        self.dag_7 = row[17:20]
        self.dag_8 = row[23:26]
        self.dag_9 = row[26:29]
        self.dag_10 = row[29:31]
        self.dag_11 = row[31:34]

    def get_voorkeuren(self, dag=0):
        return getattr(self, "dag_" + str(dag))

    def __str__(self):
        return '{} ({})'.format(self.naam, self.tag)


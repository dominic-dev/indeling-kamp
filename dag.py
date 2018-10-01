import os
from xlsxwriter.workbook import Workbook
import csv
from groep import Groep


class Dag:
    MAX_WERKGROEP = 12
    MAX_KABOUTERS = 3
    MAX_KOKEN = 3
    MAX_OPPAS_0_2 = 2
    MAX_OPPAS_2_4 = 2
    MAX_OPPAS_4_6 = 4
    MAX_OPPAS_6 = 3

    WERKGROEP_NAAM = 'werk- groep'
    KABOUTERS_NAAM = 'kabouters'
    KOKEN_NAAM = 'koken'
    OPPAS_0_2_NAAM = 'oppas 0-2'
    OPPAS_2_4_NAAM = 'oppas 2-4'
    OPPAS_4_6_NAAM = 'oppas 4-6'
    OPPAS_6_NAAM = 'oppas 6+'
    NIET_AANWEZIG_NAAM = 'Niet'
    GEEN_VOORKEUR_NAAM = 'Geen'
    OVER_NAAM = 'over'

    DAG_2 = 'dag 2'
    DAG_3 = 'dag 3'
    DAG_4 = 'dag 4'
    DAG_5 = 'dag 5'
    DAG_6 = 'dag 6'
    DAG_7 = 'dag 7'
    DAG_8 = 'dag 8'
    DAG_9 = 'dag 9'
    DAG_10 = 'dag 10'
    DAG_11 = 'dag 11'

    def __init__(self, naam=None):
        self.naam = naam
        self.groepen = {
                Dag.WERKGROEP_NAAM : Groep(Dag.MAX_WERKGROEP),
                Dag.KABOUTERS_NAAM : Groep(Dag.MAX_KABOUTERS),
                Dag.KOKEN_NAAM : Groep(Dag.MAX_KOKEN),
                Dag.OPPAS_0_2_NAAM : Groep(Dag.MAX_OPPAS_0_2),
                Dag.OPPAS_2_4_NAAM : Groep(Dag.MAX_OPPAS_2_4),
                Dag.OPPAS_4_6_NAAM : Groep(Dag.MAX_OPPAS_4_6),
                Dag.OPPAS_6_NAAM : Groep(Dag.MAX_OPPAS_6),
                Dag.OVER_NAAM : Groep(),
        }
        self.aanwezig = 0

    def addTo(self, lid, name):
        if not self.groepen[name]:
            raise ValueError('Deze groep bestaat niet')
        return self.groepen[name].add(lid)

    def write_to_csv(self, path):
        rows = zip(
                ['werkgroep'] + self.groepen[Dag.WERKGROEP_NAAM].leden,
                ['kabouters'] + self.groepen[Dag.KABOUTERS_NAAM].leden,
                ['koken'] + self.groepen[Dag.KOKEN_NAAM].leden,
                ['oppas 0-2'] + self.groepen[Dag.OPPAS_0_2_NAAM].leden,
                ['oppas 2-4'] + self.groepen[Dag.OPPAS_2_4_NAAM].leden,
                ['oppas 4-6'] + self.groepen[Dag.OPPAS_4_6_NAAM].leden,
                ['oppas 6+'] + self.groepen[Dag.OPPAS_6_NAAM].leden,
                ['over'] + self.groepen[Dag.OVER_NAAM].leden
        )

        with open(path, "w") as f:
            writer = csv.writer(f)
            for groepnaam, groep in self.groepen.items():
                writer.writerow([groepnaam] + groep.leden)
            writer.writerow(['Aanwezig: ', self.aanwezig])

    def export_csv_as_xlsx(self, path):
        directory, long_filename = os.path.split(path)
        short_filename, extension = os.path.splitext(long_filename)
        workbook = Workbook(short_filename + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(path, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()

    @staticmethod
    def get_groep_naam(voorkeur):
        voorkeur = voorkeur.lower()

        if Dag.GEEN_VOORKEUR_NAAM.lower() in voorkeur:
            return Dag.GEEN_VOORKEUR_NAAM

        if Dag.NIET_AANWEZIG_NAAM.lower() in voorkeur:
            return Dag.NIET_AANWEZIG_NAAM

        if Dag.WERKGROEP_NAAM.lower() in voorkeur:
            return Dag.WERKGROEP_NAAM

        if Dag.KABOUTERS_NAAM.lower() in voorkeur:
            return Dag.KABOUTERS_NAAM

        if Dag.KOKEN_NAAM.lower() in voorkeur:
            return Dag.WERKGROEP_NAAM

        if Dag.OPPAS_0_2_NAAM.lower() in voorkeur:
            return Dag.OPPAS_0_2_NAAM

        if Dag.OPPAS_2_4_NAAM.lower() in voorkeur:
            return Dag.OPPAS_2_4_NAAM

        if Dag.OPPAS_4_6_NAAM.lower() in voorkeur:
            return Dag.OPPAS_4_6_NAAM

        if Dag.OPPAS_6_NAAM.lower() in voorkeur:
            return Dag.OPPAS_6_NAAM

        if Dag.OVER_NAAM.lower() in voorkeur:
            return Dag.OVER_NAAM
        raise Exception('Geen geldige voorkeur: ' + voorkeur)


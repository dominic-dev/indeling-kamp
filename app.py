import csv
from dag import Dag
from persoon import Persoon

MAX_ATTEMPTS = 3
PATH = 'Indeling Kamp 2018.csv'

class App:
    def __init__(self):
        self.dagen = {
                2: Dag('2'),
                3: Dag('3 '),
                4: Dag('4'),
                5: Dag('5'),
                6: Dag('6'),
                7: Dag('7'),
                8: Dag('8'),
                9: Dag('9'),
                10: Dag('10'),
                11: Dag('11'),
        }
        self.personen = []

    def read_file(self):
        with open(PATH) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                self.personen.append(Persoon(row))


def vulOppassers():
    if dag.addTo(persoon, Dag.OPPAS_0_2_NAAM):
        dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)
        return
    if dag.addTo(persoon, Dag.OPPAS_2_4_NAAM):
        dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)
        return
    if dag.addTo(persoon, Dag.OPPAS_6_NAAM):
        dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)


if __name__ == '__main__':
    app = App()
    app.read_file()

    # Dag
    for dagnummer, dag in app.dagen.items():
        dag.aanwezig = len(app.personen)

        # Personen
        for persoon in app.personen:
            persoon.tag = ''
            attempts = 1

            # Voorkeuren
            for voorkeur in persoon.get_voorkeuren(dagnummer):
                if not voorkeur:
                    continue

                groepnaam = Dag.get_groep_naam(voorkeur)

                if groepnaam == Dag.NIET_AANWEZIG_NAAM:
                    dag.aanwezig -= 1
                    break

                if groepnaam == Dag.GEEN_VOORKEUR_NAAM:
                    print('geen voork')
                    print(persoon)
                    dag.addTo(persoon, Dag.OVER_NAAM)
                    break


                if dag.addTo(persoon, groepnaam):
                    persoon.tag = 'V'
                    break

                if attempts == MAX_ATTEMPTS:
                    dag.addTo(persoon, Dag.OVER_NAAM)
                    break

                attempts += 1

        # Dagen vullen

        # Eerst oppassers aan oppas proberen toe te voegen
        for persoon in dag.groepen[Dag.OVER_NAAM].leden:
            if not 'Oppas' in persoon.get_voorkeuren(dagnummer)[0]:
                persoon.tag = 'X'
                continue
            persoon.tag = '0'
            vulOppassers(dag, persoon)


        # Oppas voor rest
        for persoon in dag.groepen[Dag.OVER_NAAM].leden:
            if dag.addTo(persoon, Dag.OPPAS_0_2_NAAM):
                dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)
                # continue
            if dag.addTo(persoon, Dag.OPPAS_2_4_NAAM):
                dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)
                # continue
            if dag.addTo(persoon, Dag.OPPAS_6_NAAM):
                dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)

        # Dan koken
        for persoon in dag.groepen[Dag.OVER_NAAM].leden:
            if dag.addTo(persoon, Dag.KOKEN_NAAM):
                dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)

        # Dan kabouters
        for persoon in dag.groepen[Dag.OVER_NAAM].leden:
            if dag.addTo(persoon, Dag.KABOUTERS_NAAM):
                dag.groepen[Dag.OVER_NAAM].leden.remove(persoon)

        # Dagen vullen
        for groepnaam, groep in dag.groepen.items():
            if groepnaam in (Dag.OVER_NAAM):
                continue

            while not groep.is_full():
                if not dag.groepen[Dag.OVER_NAAM].leden:
                    break
                groep.add(dag.groepen[Dag.OVER_NAAM].leden.pop())


        path = 'dag {}.csv'.format(dag.naam)
        dag.write_to_csv(path)
        dag.export_csv_as_xlsx(path)


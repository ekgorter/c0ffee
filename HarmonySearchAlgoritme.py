__author__ = 'Elias'

######################################### Libraries #############################################

# Library om csv files te lezen.
import csv

# Library om random getallen te genereren.
import random

######################################### Functies ##############################################

# Functie om in te voeren landen uit csv file op te slaan in tuple.
def invoerlanden_uit_csv(csvBestand):

    # Open het csv bestand.
    f = open(csvBestand)

    # Lees het csv bestand.
    csv_f = csv.reader(f)

    # List om landen in op te slaan.
    invoerlanden = []

    # Voeg de waarden uit de eerste kolom in de csv file toe aan de list.
    for row in csv_f:
        invoerlanden.append(int(row[0]))

    # Zet de list om in een tuple.
    invoerlanden = tuple(invoerlanden)

    # Sluit het bestand.
    f.close()

    # Returnt de tuple met landen.
    return invoerlanden

# Functie om dictionary met connecties per land te maken vanuit csv file.
def connecties_uit_csv(csvBestand, invoerlanden):

    # Opent de csv file.
    f = open(csvBestand)

    # Leest de csv file.
    csv_f = csv.reader(f)

    # Tijdelijke list waarin de buurlanden worden opgeslagen.
    temp = []

    # Laat de eerste kolom (de landen) buiten beschouwing, zodat de buurlanden overblijven.
    for row in csv_f:
        temp.append(row[1:])

    # List waarin de buurlanden per land als tuples worden opgeslagen.
    buurlanden = []

    # Zet de buurlanden lists om in tuples.
    for i in temp:
        temp2 = []
        for j in i:
            temp2.append(int(j))
        temp2 = tuple(temp2)
        buurlanden.append(temp2)

    # Dictionary waarin de buurlanden worden gekoppeld aan de landen.
    connecties = {}

    # Koppelt landen aan buurlanden.
    for i in invoerlanden:
        connecties[i] = buurlanden[i - 1]

    # Sluit csv bestand.
    f.close()

    # Returnt de dictionary met connecties.
    return connecties

# Functie om connectie matrix te maken van kaart of netwerk.
def connectie_matrix(invoerlanden, connecties):

    # De te vullen matrix (2-dimensionale array)
    matrix = []

    # Vult de rijen van de matrix.
    for i in range(len(invoerlanden)):

        # Lijst voor iedere rij van matrix.
        temp = []

        # Vult de kolommen van de matrix.
        for j in range(len(invoerlanden)):

            # Als de huidige rij en kolom aan elkaar grenzen, zet dan een 1 neer.
            if invoerlanden[j] in connecties[i + 1]:

                temp.append(1)

            # Zet anders een 0 neer (als ze niet aan elkaar grenzen).
            else:

                temp.append(0)

        # Voeg deze rij aan de matrix toe.
        matrix.append(temp)

    # Returnt de matrix.
    return matrix

# Functie om random vector te maken.
def random_vector_maken(invoerlanden):

    # De te vullen vector.
    vector = []

    # Vult de vector met een random waarde tussen 1 en 4 (inclusief) voor ieder land.
    for i in range(len(invoerlanden)):

        vector.append(random.randrange(1,5))

    # Returnt de vector
    return vector

# Functie om score toe te kennen aan een vector, hoe lager de score hoe beter.
def vector_score(vector, matrix):

    # Uiteindelijke score.
    score = 0

    # Itereert over helft matrix.
    k = 0

    for i in range(len(matrix)):

        for j in range(k, len(matrix)):

            # Als landen aan elkaar grenzen.
            if matrix[i][j] == 1:

                # Als deze landen dezelfde kleur hebben.
                if vector[i] == vector[j]:

                    # Verhoog de score met 1.
                    score += 1

        # Zorgt ervoor dat over de helft van de matrix wordt geitereerd, zodat alle grenzen slechts 1 keer worden gecheckt.
        k += 1

    # Returnt score
    return score

############################################ Invoerdata #################################################

# Vul hier het te lezen csv bestand in.
csvBestand = '/Users/Elias/Documents/Programmeren/Programmeertheorie/test.csv'

# Alle in te kleuren landen in een tuple uit csv file gehaald.
invoerlanden = invoerlanden_uit_csv(csvBestand)

# Dictionary met voor elk land een tuple met de buurlanden van dat land, uit csv gehaald.
connecties = connecties_uit_csv(csvBestand, invoerlanden)

######################################### Aanroepen functies ############################################

# Maakt connectie matrix uit gegevens csv bestand.
matrix = connectie_matrix(invoerlanden, connecties)

print 'matrix:'
for i in range(len(matrix)):
    print matrix[i]

# Genereert een random ingekleurde vector.
vector = random_vector_maken(invoerlanden)

print 'vector:', vector

# Geeft een score aan een vector, hoe lager hoe beter.
score = vector_score(vector, matrix)

print 'score:', score
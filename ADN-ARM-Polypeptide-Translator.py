# =====================================================
# Traduction ADN -> ARM -> Polypeptide
# =====================================================


# Fonction pour traduire les codons commençant par U
def Traduire_U(codon):

    table_U = {
        "UUU": "Phe",
        "UUC": "Phe",

        "UUA": "Leu",
        "UUG": "Leu",

        "UCU": "Ser",
        "UCC": "Ser",
        "UCA": "Ser",
        "UCG": "Ser",

        "UAU": "Tyr",
        "UAC": "Tyr",

        "UGU": "Cys",
        "UGC": "Cys",

        "UGG": "Trp"
    }

    return table_U[codon]



# Fonction fournie pour les autres codons
def generer(codon):

    table = {

        "CUU":"Leu", "CUC":"Leu", "CUA":"Leu", "CUG":"Leu",

        "AUU":"Ile", "AUC":"Ile", "AUA":"Ile",
        "AUG":"Met",

        "GUU":"Val", "GUC":"Val", "GUA":"Val", "GUG":"Val",

        "CCU":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",

        "ACU":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",

        "GCU":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",

        "AAU":"Asn", "AAC":"Asn",

        "AAA":"Lys", "AAG":"Lys",

        "GAU":"Asp", "GAC":"Asp",

        "GAA":"Glu", "GAG":"Glu",

        "CAU":"His", "CAC":"His",

        "CAA":"Gln", "CAG":"Gln",

        "CGU":"Arg", "CGC":"Arg",
        "CGA":"Arg", "CGG":"Arg",

        "AGU":"Ser", "AGC":"Ser",

        "AGA":"Arg", "AGG":"Arg",

        "GGU":"Gly", "GGC":"Gly",
        "GGA":"Gly", "GGG":"Gly"
    }

    return table[codon]



# =====================================================
# Programme Principal
# =====================================================


# 1) Saisie de N

while True:

    N = int(input("Donner N ([3..40], impair et multiple de 3) : "))

    if 3 <= N <= 40 and N % 2 != 0 and N % 3 == 0:
        break



# 2) Remplissage du tableau ADN

ADN = []

for i in range(N):

    while True:

        lettre = input(
            f"Donner ADN[{i}] (A,C,G,T) : "
        ).upper()


        if lettre in ["A", "C", "G", "T"]:

            ADN.append(lettre)
            break



# 3) Création du tableau ARM

ARM = []

for i in range(N // 3):

    codon = ""

    for j in range(3):

        lettre = ADN[i*3 + j]

        if lettre == "T":
            codon += "U"

        else:
            codon += lettre


    ARM.append(codon)



# 4) Traduction des codons ARM

STOP = ["UAA", "UAG", "UGA"]


print("\nSéquence des polypeptides :")


for codon in ARM:


    # ignorer les codons STOP
    if codon not in STOP:


        # cas spécial : codons commençant par U
        if codon[0] == "U":

            polypeptide = Traduire_U(codon)


        else:

            polypeptide = generer(codon)



        print(polypeptide, end=" ")
from flask import jsonify
from my_input import b_regles, b_faits, b_buts
from collections import defaultdict

LOG, ETAT_BASE, CONTENU, SUCCES = ["", "", "", ""]
LOG = defaultdict(list)
# [
# ([premise],[conclusion])
# ]
regles_initiaux = []
# [premises...]
faits_initiaux = []
# [conclusions ...]
but = []

# [(premis,conclusion)]
deduction = []


"""
On ajoutes toutes regles contenant 



RETOUR TRAITEMENT
    LOG:
    {
        "event_type":"content[old print]"
    }
    ETAT_BASE: final state of base de regle
    CONTENU: final state of base des fait and content
    SUCCES: did we make it ?


"""


def ajouter_regle(regle):
    global deduction, faits_initiaux, regles_initiaux
    global LOG, ETAT_BASE, CONTENU, SUCCES
    s_faits = set(faits_initiaux)
    candidat = []
    for premises, conclusions in regles_initiaux:
        if set(premises).issubset(s_faits) and regle in premises:
            candidat.append((premises, conclusions))
            regles_initiaux.remove((premises, conclusions))
    for i in candidat:
        faits_initiaux.extend(i[1])
    deduction.extend(candidat)


def est_successive():
    global LOG, ETAT_BASE, CONTENU, SUCCES
    return set(but).issubset(set(faits_initiaux))


def b_reg_est_sature():
    s_faits = set(faits_initiaux)
    ret = True
    for pr, ccl in regles_initiaux:
        if set(pr).issubset(s_faits):
            print(f"{' '.join(pr)}: B_Regles n'est pas Sature")
            ret &= False
    return ret


def chainage_avant():
    while (not b_reg_est_sature()) and (not est_successive()):
        print("Base des Faits", faits_initiaux)
        for fait in faits_initiaux:
            # print("fait en cours d'analyse", fait)
            # print("Base des Regles", regles_initiaux)
            ajouter_regle(fait)
            if b_reg_est_sature() or est_successive():
                break
        print("Saturation", b_reg_est_sature())
        print("Succes", est_successive())
        print("Continuité", (not b_reg_est_sature()) and (not est_successive()))
        print("================")


# if __name__ == "__main__":
# change it to function
def make_it_shine____babe():
    global LOG, ETAT_BASE, CONTENU, SUCCES
    regles_initiaux, faits_initiaux, but = b_regles, b_faits, b_buts
    print("Fait", faits_initiaux, "deduction", deduction, "regles", regles_initiaux)
    # ajouter_regle("b")
    chainage_avant()
    if b_reg_est_sature():
        print("Base des règles Saturée!")
    print(
        "Résultat est achevée "
        + ("sans" if not est_successive() else "avec")
        + " Succès"
    )
    return jsonify(LOG=LOG, ETAT_BASE=ETAT_BASE, CONTENU=CONTENU, SUCCES=SUCCES)

from flask import jsonify
from my_input import b_regles, b_faits, b_buts
from data_prep import stringify
from collections import defaultdict
from pprint import pprint

# LOG, ETAT_BASE, CONTENU, SUCCES = ["", "", "", ""]
# LOG = defaultdict(list)
# # [
# # ([premise],[conclusion])
# # ]
# regles_initiaux = []
# # [premises...]
# faits_initiaux = []
# # [conclusions ...]
# but = []

# # [(premis,conclusion)]
# deduction = []


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


def ajouter_regle(regle, deduction, faits_initiaux, regles_initiaux, LOG):
    # global deduction, faits_initiaux, regles_initiaux, LOG, ETAT_BASE, CONTENU, SUCCES
    s_faits = set(faits_initiaux)
    candidat = []
    for premises, conclusions in regles_initiaux:
        if set(premises).issubset(s_faits) and regle in premises:
            candidat.append((premises, conclusions))
            regles_initiaux.remove((premises, conclusions))
    for i in candidat:
        faits_initiaux.extend(i[1])
    deduction.extend(candidat)
    return deduction, faits_initiaux, regles_initiaux, LOG


def est_successive(but, faits_initiaux):
    return set(but).issubset(set(faits_initiaux))


def b_reg_est_sature(faits_initiaux, regles_initiaux, LOG):
    s_faits = set(faits_initiaux)
    ret = True
    for pr, ccl in regles_initiaux:
        if set(pr).issubset(s_faits):
            ret &= False
    LOG.append(f"Detection de B_Regles: {'Saturé!'if ret else 'pas de Saturation!'}")
    return ret, LOG


def chainage_avant(regles_initiaux, faits_initiaux, but, LOG, ETAT_BASE, SUCCES):
    while (not b_reg_est_sature(faits_initiaux, regles_initiaux, LOG)[0]) and (
        not est_successive(but, faits_initiaux)
    ):
        print("Base des Faits", faits_initiaux)
        for fait in faits_initiaux:
            deduction, faits_initiaux, regles_initiaux, LOG = ajouter_regle(
                fait, but, faits_initiaux, regles_initiaux, LOG
            )
            if b_reg_est_sature(faits_initiaux, regles_initiaux, LOG)[
                0
            ] or est_successive(but, faits_initiaux):
                break

        LOG.append("Execution Terminé!\n================")
        ETAT_BASE = (
            "Saturation",
            b_reg_est_sature(faits_initiaux, regles_initiaux, LOG)[0],
        )
        SUCCES = ("Succes", est_successive(but, faits_initiaux))
    return (faits_initiaux, LOG, ETAT_BASE, SUCCES)


# change it to function
def make_it_shine____babe(b_regles, b_faits, b_buts, LOG=[], ETAT_BASE=[], SUCCES=[]):
    regles_initiaux, faits_initiaux, but = b_regles, b_faits, b_buts
    # LOG.append(
    #     "Process avec les parametres: \nFait:\n"
    #     + stringify(faits_initiaux, "\n>")
    #     + "\nBut à atteinder:\n"
    #     + stringify(but, "\n>>")
    #     + "\n Etant donnée les Regles: "
    #     + stringify(regles_initiaux, "\n>>>")
    # )
    LOG.append("Commencing Process")
    # ajouter_regle("b")
    faits_initiaux, LOG, ETAT_BASE, SUCCES = chainage_avant(
        regles_initiaux, faits_initiaux, but, LOG, ETAT_BASE, SUCCES
    )

    # return jsonify(LOG=LOG, ETAT_BASE=ETAT_BASE, SUCCES=SUCCES)
    return (LOG, ETAT_BASE, SUCCES)


if __name__ == "__main__":
    x = make_it_shine____babe(b_regles, b_faits, b_buts)
    pprint(x)

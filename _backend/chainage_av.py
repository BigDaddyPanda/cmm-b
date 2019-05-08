from copy import deepcopy


class ChainageAvantHandler:
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

    """

    def ajouter_regle(self, regle):
        s_faits = set(self.faits_initiaux)
        candidat = []
        for premises, conclusions in self.regles_initiaux:
            if set(premises).issubset(s_faits) and regle in premises:
                candidat.append((premises, conclusions))
                self.regles_initiaux.remove((premises, conclusions))
        for i in candidat:
            self.faits_initiaux.extend(i[1])
        self.deduction.extend(candidat)

    def est_successive(self):
        return set(self.but).issubset(set(self.faits_initiaux))

    def b_reg_est_sature(self):
        s_faits = set(self.faits_initiaux)
        ret = []
        for pr, ccl in self.regles_initiaux:
            ret.append(set(pr).issubset(s_faits))
        return all(ret)

    def chainage_avant(self):
        self.status = "un-successful"
        while not self.b_reg_est_sature():
            for fait in self.faits_initiaux:
                self.ajouter_regle(fait)
                if self.b_reg_est_sature() or self.est_successive():
                    self.status = "successful"
                    break

    def run_it_baaaaaaaaaaaaaabe(self, b_regles, b_faits, b_buts):
        self.regles_initiaux, self.faits_initiaux, self.but = (
            deepcopy(b_regles),
            deepcopy(b_faits),
            deepcopy(b_buts),
        )
        print(
            "Fait",
            self.faits_initiaux,
            "deduction",
            self.deduction,
            "regles",
            self.regles_initiaux,
        )
        self.chainage_avant()
        print(self.est_successive(), self.status)
        print(
            "Fait",
            self.faits_initiaux,
            "deduction",
            self.deduction,
            "regles",
            self.regles_initiaux,
        )

        return self.dfs(b_regles, b_faits, b_buts)

    def dfs(self, b_regles, b_faits, b_buts):
        re = []
        for i in self.deduction:
            if i in b_regles:
                re.append(("given", i))
            elif set(i[0]).issubset(set(b_faits)):
                re.append(("known", i))
            elif i in b_buts:
                re.append(("achieved", i))
            else:
                re.append(("somehow", i))


if __name__ == "__main__":
    from my_input import b_regles, b_faits, b_buts

    myhandler = ChainageAvantHandler()
    myhandler.run_it_baaaaaaaaaaaaaabe(b_regles, b_faits, b_buts)


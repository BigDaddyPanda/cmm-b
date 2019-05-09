from copy import deepcopy


class ChainageAvantHandler:
    # [
    # ([premise],[conclusion])
    # ]
    base_regle = []

    # [premises...]
    base_faits = []

    # [conclusions ...]
    but = []

    # [(premis,conclusion)]
    deduction = []
    status = ""
    saturation_b_f = ""
    saturation_b_r = ""
    """
    On ajoutes toutes regles contenant 

    """

    # def ajouter_regle(self, fait):
    #     s_faits = set(self.base_faits)
    #     candidat = []
    #     for premises, conclusions in self.base_regle:
    #         if set(premises).issubset(s_faits) and fait in premises:
    #             candidat.append((premises, conclusions))
    #             self.base_regle.remove((premises, conclusions))
    #     for i in candidat:
    #         self.base_faits.extend(i[1])
    #     self.deduction.extend(candidat)

    def est_successive(self):
        return set(self.but).issubset(set(self.base_faits))

    def saturation_bf(self):
        s_faits = set(self.base_faits)
        for pr, ccl in self.base_regle:
            if set(pr).issubset(s_faits):
                return False
        return True

    def chainage_avant(self):
        while (not self.saturation_bf()) and (not self.est_successive()):
            for prms, ccls in self.base_regle:
                if set(prms).issubset(set(self.base_faits)):
                    self.base_faits.extend(ccls)
                    print("ch av",type(ccls))
                    self.deduction.append((prms, ccls))
                    self.base_regle.remove((prms, ccls))
        self.status = "Successful" if self.est_successive() else "UnSuccessful"
        self.saturation_b_f = self.saturation_bf()
        self.saturation_b_r = not len(self.base_regle)

    def run_it_baaaaaaaaaaaaaabe(self, b_regles, b_faits, b_buts):
        self.base_regle, self.base_faits, self.but = (
            deepcopy(b_regles),
            deepcopy(b_faits),
            deepcopy(b_buts),
        )
        print(
            "Fait",
            self.base_faits,
            "deduction",
            self.deduction,
            "regles",
            self.base_regle,
        )
        self.chainage_avant()
        print(self.est_successive(), self.status)
        print(
            "Fait",
            self.base_faits,
            "deduction",
            self.deduction,
            "regles",
            self.base_regle,
        )

        # return self.dfs(b_regles, b_faits, b_buts)

    # def dfs(self, b_regles, b_faits, b_buts):
    #     re = []
    #     for i in self.deduction:
    #     return re


if __name__ == "__main__":
    from my_input import b_regles, b_faits, b_buts
    from pprint import pprint

    myhandler = ChainageAvantHandler()
    myhandler.run_it_baaaaaaaaaaaaaabe(b_regles, b_faits, b_buts)
    print(myhandler.deduction,
        myhandler.status,
        myhandler.saturation_b_f,
        myhandler.saturation_b_r
    )


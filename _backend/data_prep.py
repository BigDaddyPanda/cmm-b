
# manual_conclusion_base
# manual_fact_base
# manual_rules_base
# mode_auto_activated
# uploaded_file
# *[Cause(s) (comma/logical-word separated)][,/conclusion expression][Consequence(s) comma/logical-word separated]
# [Tout humain est mortel
# Socrate est humain] => BR
# Socrate => BF
# Mortel => CCL

cause_separator = ["et", "and", ","]

premise_separator = ["et", "and", ","]

premise_conclusion_sep = ["=>", "alors", "so", "donc"]


def prepare_statemen(inp=""):
    premisse, conclusion = "", ""
    for pcs in premise_conclusion_sep:
        if pcs in inp:
            premisse, conclusion = inp.split(pcs)
            break
    for cs in cause_separator:
        if cs in premisse:
            premisse = premisse.split(cs)
            for i in range(len(premisse)):
                while premisse[i][0] == " ":
                    premisse[i] = premisse[i][1:]
                while premisse[i][-1] == " ":
                    premisse[i] = premisse[i][: len(premisse[i]) - 1]
            break

    for ps in premise_separator:
        if ps in premisse:
            conclusion = conclusion.split(ps)
            for i in range(len(conclusion)):
                while conclusion[i][0] == " ":
                    conclusion[i] = conclusion[i][1:]
                while conclusion[i][-1] == " ":
                    conclusion[i] = conclusion[i][: len(conclusion[i]) - 1]
            break
    return (premisse, conclusion)
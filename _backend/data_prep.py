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

conclusion_separator = ["et", "and", ","]

premise_separator = ["et", "and", ","]

premise_conclusion_sep = ["=>", "alors", "so", "donc"]


def prepare_statemen(inp=""):
    premisse, conclusion = "", ""
    for pcs in premise_conclusion_sep:
        if pcs in inp:
            premisse, conclusion = inp.split(pcs)
            break
    for cs in premise_separator:
        if type(premisse) == str:
            if cs in premisse:
                premisse = premisse.split(cs)
        else:
            for i in range(len(premisse)):
                premisse[i] = premisse[i].split(cs)

    for cs in conclusion_separator:
        if type(conclusion) == str:
            if cs in conclusion:
                conclusion = conclusion.split(cs)
        else:
            for i in range(len(conclusion)):
                conclusion[i] = conclusion[i].split(cs)

    if type(premisse) == list:
        for i in range(len(premisse)):
            while premisse[i][0] == " ":
                premisse[i] = premisse[i][1:]
            while premisse[i][-1] == " ":
                premisse[i] = premisse[i][: len(premisse[i]) - 1]
    else:
        while premisse[0] == " ":
            premisse = premisse[1:]
        while premisse[-1] == " ":
            premisse = premisse[: len(premisse) - 1]

    if type(conclusion) == list:
        for i in range(len(conclusion)):
            while conclusion[i][0] == " ":
                conclusion[i] = conclusion[i][1:]
            while conclusion[i][-1] == " ":
                conclusion[i] = conclusion[i][: len(conclusion[i]) - 1]
    else:
        while conclusion[0] == " ":
            conclusion = conclusion[1:]
        while conclusion[-1] == " ":
            conclusion = conclusion[: len(conclusion) - 1]

    premisse = [str(premisse)] if type(premisse) != list else premisse
    conclusion = [str(conclusion)] if type(conclusion) != list else conclusion
    return (premisse, conclusion)


def stringify(stlist, sep=" "):
    return sep.join(list(map(str, stlist)))


def normalizer(
    manual_conclusion_base,
    manual_fact_base,
    manual_rules_base,
    mode_auto_activated,
    uploaded_file,
):
    return "", "", ""


if __name__ == "__main__":
    print("aze, dqs alors ss")
    p, c = prepare_statemen("aze, dqs alors ss")
    print(type(p), type(c))
    print(p, c)


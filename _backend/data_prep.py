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

conclusion_separator = [" et ", " and ", ","]

premise_separator = [" et ", " and ", ","]

premise_conclusion_sep = [" => ", " alors ", " so ", " donc "]


def escape_ws(words, src="x"):
    if words in ["", " ", "\n", "\t"]:
        return ""
    if type(words) == list:
        for i in range(len(words)):
            print(f"{src}escape_ws('{words[i]}')")
            while words[i][0] == " ":
                words[i] = words[i][1:]
            while words[i].lower().startswith("si "):
                words[i]=words[i].lower()[3:]
            while words[i][-1] == " ":
                words[i] = words[i][: len(words[i]) - 1] 
    else:
        while words[0] == " ":
            words = words[1:]
        while words[-1] == " ":
            words = words[: len(words) - 1]
    return words


def continuos_sep(iterated, sep):
    for cs in sep:
        print("iterated",iterated,type(iterated))
        if type(iterated) == str:
            if cs in iterated:
                iterated = iterated.split(cs)
        else:
            for i in range(len(iterated)):
                print("iterated > i >",i,iterated[i])
                xx=iterated[i].split(cs)
                iterated[i:i+len(xx)] = xx
    return iterated


def prepare_statement(inp=""):
    premisse, conclusion = "", ""
    for pcs in premise_conclusion_sep:
        if pcs in inp:
            premisse, conclusion = inp.split(pcs)
            break

    premisse = continuos_sep(premisse, premise_separator)
    conclusion = continuos_sep(conclusion, conclusion_separator)

    premisse = escape_ws(premisse, "v")
    conclusion = escape_ws(conclusion, "e")

    premisse = [str(premisse).lower()] if type(premisse) != list else [i.lower() for i in premisse]
    conclusion = [str(conclusion).lower()] if type(conclusion) != list else [i.lower() for i in conclusion]

    return (premisse, conclusion)


def stringify(stlist, sep=" "):
    return sep.join(list(map(str, stlist))).lower()


def escape_nl(st):
    return st.replace("\n", "").lower()


def normalizer(
    manual_conclusion_base, manual_fact_base, manual_rules_base, uploaded_file
):
    uploaded_file = list(map(escape_nl, uploaded_file))
    uploaded_file = list(map(prepare_statement, uploaded_file))

    manual_conclusion_base = manual_conclusion_base.split("\n")
    # print(manual_conclusion_base)
    manual_conclusion_base = list(map(escape_ws, manual_conclusion_base))
    # print("manual_conclusion_base",manual_conclusion_base)

    manual_fact_base = manual_fact_base.split("\n")
    # manual_fact_base = list(map(escape_nl, manual_fact_base))
    manual_fact_base = list(map(escape_ws, manual_fact_base))
    manual_fact_base = [i for i in manual_fact_base if i != ""]

    manual_rules_base = manual_rules_base.split("\n")
    manual_rules_base = [i for i in manual_rules_base if i != ""]
    # manual_rules_base = list(map(escape_ws, manual_rules_base))
    manual_rules_base = list(map(prepare_statement, manual_rules_base))

    manual_rules_base.extend(uploaded_file)

    # print("Conclusion to Achieve")
    # print(manual_conclusion_base)
    # print("Facts to start With")
    # print(manual_fact_base)
    # print("Given Rules")
    # print(manual_rules_base)
    return manual_conclusion_base, manual_fact_base, manual_rules_base
    # b_regles
    # b_faits
    # b_buts


if __name__ == "__main__":
    print("aze, dqs alors ss")
    p, c = prepare_statement("aze, dqs alors ss")
    print(type(p), type(c))
    print(p, c)


def prefers(W, w, m0, m1):
    return W[w].index(m0) < W[w].index(m1)


def extended_stable_matche(W, M):
    men_last_propose = {}
    w_partners = {}

    free_mens = list(M.keys())
    for man in free_mens:
        men_last_propose[man] = -1

    while len(free_mens) > 0:
        man = free_mens[0]
        i = men_last_propose[man]
        while i < len(M[man]) - 1:
            i += 1
            woman = M[man][i]
            woman_partner = w_partners.get(woman, None)
            if woman_partner is None:
                w_partners[woman] = man
                free_mens.remove(man)
                break
            elif prefers(W, woman, man, woman_partner):
                free_mens.append(woman_partner)
                free_mens.remove(man)
                w_partners[woman] = man
                break
        if i == len(M[man]) - 1:
            free_mens.remove(man)
        men_last_propose[man] = i
    return w_partners


M = {
    "bob": ["lea", "sue"],
    "jim": ["lea", "sue", "ann"],
    "tom": ["sue", "lea", "ann"],
}

W = {
    "ann": ["jim", "tom"],
    "lea": ["tom", "bob", "jim"],
    "sue": ["jim", "tom", "bob"],
}

print(extended_stable_matche(W, M))
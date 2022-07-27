from random import randint


def choose_elements(lst: list, k: int) -> list:
    """Ответ на вопрос 1"""
    n = len(lst)
    chosen = set()
    if k <= n // 2:
        # собираем индексы, которые войдут в итоговый список:
        while len(chosen) < k:
            chosen.add(randint(0, n - 1))

        output_list = [lst[i] for i in chosen]
    else:
        # собираем индексы, которые не войдут в итоговый список:
        while len(chosen) < n - k:
            chosen.add(randint(0, n - 1))

        output_list = [lst[i] for i in range(n) if i not in chosen]

        # перемешиваем полученный список:
        for i in range(k - 1):
            j = randint(i + 1, k - 1)
            output_list[i], output_list[j] = output_list[j], output_list[i]
    return output_list


def choose_elements_prob(lst: list, prob: list, k: int) -> list:
    """Ответ на вопрос 2"""
    n = len(lst)
    chosen = set()
    if k <= n // 2:
        # собираем индексы, которые войдут в итоговый список:
        while len(chosen) < k:
            ind = randint(0, n - 1)
            if prob[ind] >= randint(1, 10) / 10:
                chosen.add(ind)

        output_list = [lst[i] for i in chosen]
    else:
        # собираем индексы, которые не войдут в итоговый список:
        while len(chosen) < n - k:
            ind = randint(0, n - 1)
            if prob[ind] <= randint(1, 10) / 10:
                chosen.add(ind)

        output_list = [lst[i] for i in range(n) if i not in chosen]

        # перемешиваем полученный список:
        for i in range(k - 1):
            j = randint(i + 1, k - 1)
            output_list[i], output_list[j] = output_list[j], output_list[i]
    return output_list

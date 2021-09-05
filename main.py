from random import randint


def choose_elements(lst, k):
    """Ответ на вопрос 1. Сложность алгоритма O(k). Случай k —> N проблем не вызывает."""
    input_list = lst[:]  # создаем копию, чтобы не портить исходный список
    output_list = []
    n = len(input_list) - 1
    for i in range(k):
        output_list.append(input_list.pop(randint(0, n - i)))
    return output_list


def choose_elements_prob(lst, prob, k):
    """Ответ на вопрос 2. Сложность алгоритма O(k). Случай k —> N проблем не вызывает."""
    input_list = lst[:]  # создаем копию, чтобы не портить исходный список
    prob_list = prob[:]  # создаем копию, чтобы не портить исходный список
    output_list = []
    n = len(input_list) - 1
    while k > 0:
        index = randint(0, n)
        if randint(0, 10) <= 10 * prob_list[index]:  # применяем выроятность из списка prob к выбранному индексу
            output_list.append(input_list.pop(index))
            prob_list.pop(index)
            k -= 1
            n -= 1
    return output_list


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    prob = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    print(choose_elements_prob(input_list, prob, 9))

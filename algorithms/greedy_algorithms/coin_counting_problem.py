def basic_small_cange(denom, total_amount):
    sorted_denominations = sorted(denom, reverse=True)

    series = []
    for j in range(len(sorted_denominations)):
        term = sorted_denominations[j:]

        number_of_denoms = []
        combination = []
        local_total = total_amount

        for i in term:
            div = local_total // i
            local_total = local_total % i
            if div > 0:
                combination.append((i, div))

        series.append(combination)

    return series


print(basic_small_cange([1, 3, 5, 8], 14))

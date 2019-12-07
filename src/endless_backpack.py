def sort_by_price(item):
    return -(item[0] / float(item[1]))


def fill_backpack(items, backpack_volume):
    total_price = 0
    current_weight = 0
    items.sort(key=sort_by_price)

    for item in items:
        if item[1] + current_weight <= backpack_volume:
            total_price += item[0]
            current_weight += item[1]
        else:
            remaining_volume = backpack_volume - current_weight
            price_for_single = item[0] / float(item[1])
            total_price += remaining_volume * price_for_single
            current_weight += remaining_volume

    return total_price


def main():
    number_of_items, backpack_volume = map(int, input().split())
    if backpack_volume == 0:
        print("{0:.3f}".format(0))
        return
    items = []
    for i in range(number_of_items):
        price, volume = map(int, input().split())
        items.append((price, volume))

    full_backpack_price = fill_backpack(items, backpack_volume)
    print("{0:.3f}".format(full_backpack_price))


# Examples
# 3 60
# 60 20
# 100 50
# 120 30
if __name__ == "__main__":
    main()

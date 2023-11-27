len_a = int(input())
a = [int(i) for i in input().split()]

def counting_sort(cards):
    count = [0] * 10
    for card in cards:
        count[card] += 1
    sorted_cards = []
    for digit in range(9, -1, -1): 
        sorted_cards.extend([digit] * count[digit])

    return sorted_cards

print(int(''.join([str(num) for num in counting_sort(a)])))
def solution(phone_book):
    sorted(phone_book)
    flag = False
    for x in phone_book:
        for y in phone_book[phone_book.index(x):]:
            if phone_book.index(x) == phone_book.index(y):
                continue
            for n in range(len(x)):
                if x[n] != y[n]:
                    flag = True
                    break
    if flag:
        return True
    return False

if solution(["119", "97674223", "1195524421"]):
    print(True)
else:
    print(False)
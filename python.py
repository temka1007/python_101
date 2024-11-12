def find_it(seq):
    unique = set(seq)
    tracker: dict = {}
    for item in list(unique):
        tracker[item] = len([x for x in seq if x == item])
    print(tracker)
    for key, value in tracker.items():
        if value%2 == 1:
            return key

test = [20,1,1,2,2,3,3,5,5,4,20,4,5]

print(find_it(test))
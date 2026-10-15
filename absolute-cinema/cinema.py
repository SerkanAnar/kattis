n, q = map(int, input().strip().split())
unavailable = set()
for _ in range(q):
    request = input().strip().split()
    request = [int(x) for x in request]
    if len(request) == 2: # seat availability
        if request[1] not in unavailable:
            unavailable.add(request[1])
            print("Ledig")
        else:
            print("Upptagen")
    else: # seat move
        if request[2] not in unavailable:
            unavailable.remove(request[1])
            unavailable.add(request[2])
            print("Ledig")
        else:
            print("Upptagen")


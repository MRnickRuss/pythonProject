votes = {}
for a in range(int(input())):
    ppl, num = input().split()
    votes[ppl] = votes.get(ppl, 0) + int(num)
for ppl, num in sorted(votes.items()):
    print(ppl, num)
import sys


def find_cycle(srt, before, edge, node):
    visited[srt] = True
    node.append(srt)
    for nxt in tree[srt]:
        if nxt != before:
            edge.append([srt, nxt])
            if visited[nxt]:
                return True
            find_cycle(nxt, srt, edge, node)

    if len(node) != len(edge)+1:
        return True
    return False


for cases in range(1, int(2e9)):
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    tree = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    cnt = 0
    for i in range(1, n + 1):
        if not find_cycle(i, 0, [], []):
            cnt += 1

    print(f"Case {cases}:", end=" ")
    if cnt == 0:
        print("No trees.")
    else:
        print("There is one tree.") if cnt == 1 else print(f"A forest of {cnt} trees.")

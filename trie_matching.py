# python3
import sys
NA=-1
class Node:
    def __init__(self):
        self.next=[NA]*4
        self.fail=0
        self.output=[]
def solve(text,n,patterns):
    def c_idx(c):return{'A':0,'C':1,'G':2,'T':3}[c]
    nodes=[Node()]
    for i,p in enumerate(patterns):
        cur=0
        for ch in p:
            c= c_idx(ch)
            if nodes[cur].next[c]==NA:
                nodes[cur].next[c]=len(nodes)
                nodes.append(Node())
            cur=nodes[cur].next[c]
        nodes[cur].output.append(i)
    from collections import deque
    q=deque()
    for c in range(4):
        nxt=nodes[0].next[c]
        if nxt!=NA:
            nodes[nxt].fail=0
            q.append(nxt)
        else:
            nodes[0].next[c]=0
    while q:
        r=q.popleft()
        for c in range(4):
            nxt=nodes[r].next[c]
            if nxt!=NA:
                nodes[nxt].fail=nodes[nodes[r].fail].next[c]
                nodes[nxt].output+=nodes[nodes[nxt].fail].output
                q.append(nxt)
            else:
                nodes[r].next[c]=nodes[nodes[r].fail].next[c]
    result=[]
    state=0
    for i,ch in enumerate(text):
        c=c_idx(ch)
        state=nodes[state].next[c]
        for pi in nodes[state].output:
            result.append(i-len(patterns[pi])+1)
    return sorted(result)
text=sys.stdin.readline().strip()
n=int(sys.stdin.readline())
patterns=[sys.stdin.readline().strip() for _ in range(n)]
ans=solve(text,n,patterns)
sys.stdout.write(' '.join(map(str,ans))+'\n')
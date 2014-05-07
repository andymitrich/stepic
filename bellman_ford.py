from decimal import Decimal

class Graph(object):
    def __init__(self, count):
        self.count = count
        self.e = {}
        self.has_cycle = False

        for v in range(1, self.count + 1):
            self.e[v] = {}

    def add_edge(self, u, v, w):
        self.e[u][v] = w

    def bf(self):
        self.dist = {}
        self.prev = {}

        for i in range(1, self.count + 1):
            self.dist[i] = Decimal('Infinity')
            self.prev[i] = None

        self.dist[1] = 0

        for i in range(1, self.count + 1):
            for u in range(1, self.count + 1):
                for v in self.e[u]:
                    result = self.relax(u, v)
                    # print(str(u)+":"+str(v))
                    
                    # print("Cycle " + str(i))
                    # print(result)
                    if i == self.count and result:
                        self.has_cycle = True


    def relax(self, u, v):
        if self.dist[v] > self.dist[u] + self.e[u][v]:
            self.dist[v] = self.dist[u] + self.e[u][v]
            self.prev[v] = u
            return True
        return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)

    for i in range(0, m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.bf()
    print(g.has_cycle)

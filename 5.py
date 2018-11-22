class Dijkstra(object):
    def __init__(self, graph):
        self.open_list = []
        self.close_list = []
        self.previous = []
        self.graph = graph
        self.actual_node = None
        self.distance = 0

        self.step = 0
        self.once = True

    def get_path(self, start_node, end_node, debugging=False):
        self.actual_node = {start_node: self.distance}
        self.open_list.append(self.actual_node)
        self.previous.append({start_node: start_node})
        self.debug(debugging)

        while list(self.actual_node.keys())[0] != end_node:
            self.close_list.append(list(self.actual_node.keys())[0])
            self.open_list.pop(self.open_list.index(self.actual_node))
            for node in self.graph:
                if node['Node'] in list(self.actual_node.keys()):
                    for element in node:
                        if element != 'Node':
                            if element not in self.close_list:
                                if any(element in d for d in
                                       self.open_list):
                                    for e in self.open_list:
                                        if list(e.keys())[0] == element:
                                            if node.get(element) + self.distance < list(e.values())[0]:
                                                e[list(e.keys())[0]] = node.get(element) + self.distance
                                                for p in self.previous:
                                                    if list(p.keys())[0] == element:
                                                        p[list(e.keys())[0]] = list(self.actual_node.keys())[0]
                                else:
                                    self.open_list.append({element: node.get(element) + self.distance})
                                    self.previous.append({element: list(self.actual_node.keys())[0]})

            values = []
            for element in self.open_list:
                for node in element:
                    values.append(element.get(node))
            self.actual_node = self.open_list[(values.index(min(values)))]
            self.distance = list(self.actual_node.values())[0]
            self.debug(debugging)

        a = end_node
        string = str(end_node)
        while a != start_node:
            for element in self.previous:
                for node in element:
                    if node == a:
                        a = element.get(node)
                        string = str(a) + " -> " + string
        print("\nThe shortest way between " + str(start_node) + " and " + str(end_node) + " is:")
        print(string)

    def debug(self, debugging=True):
        if debugging:
            if self.once:
                self.once = False
                print("Step | Node | Distance")
            node = list(self.actual_node.keys())[0]
            value = list(self.actual_node.values())[0]
            print("%4d" % self.step + " | %4s" % node + " | %8s" % value + " | Open: " + str(
                self.open_list) + " | Close: " + str(self.close_list))
            self.step += 1

graph = []
A = {}


A.setdefault('Node', []).append('A')

A.setdefault('B', []).append(2)

A.setdefault('C', []).append(3)

print("A = ", A)



B = {}

B.setdefault('Node', []).append('B')

B.setdefault('A', []).append(2)

B.setdefault('C', []).append(4)

B.setdefault('D', []).append(5)

print("B = ", B)


C = {}

C.setdefault('Node', []).append('C')

C.setdefault('A', []).append(3)

C.setdefault('B', []).append(4)

C.setdefault('D', []).append(4)

C.setdefault('E', []).append(2)

print("C = ", C)

D = {}

D.setdefault('Node', []).append('D')

D.setdefault('B', []).append(5)

D.setdefault('C', []).append(4)

D.setdefault('E', []).append(3)

D.setdefault('F', []).append(2)

print("D = ", D)

E = {}

E.setdefault('Node', []).append('E')

E.setdefault('C', []).append(2)

E.setdefault('D', []).append(3)

E.setdefault('F', []).append(4)

print("E = ", E)

F = {}

F.setdefault('Node', []).append('F')

F.setdefault('D', []).append(2)

F.setdefault('E', []).append(4)

print("F = ", F)

graph.append(A)
graph.append(B)
graph.append(C)
graph.append(D)
graph.append(E)
graph.append(F)



source = str(input("Masukkan Node Awal : "))
dest = str(input("Masukkan Node Tujuan : "))
d = Dijkstra(graph)
d.get_path(source, dest, True)

'''
A = {'Node': 'A', 'C': 1, 'D': 2}
B = {'Node': 'B', 'C': 2, 'F': 3}
C = {'Node': 'C', 'A': 1, 'B': 2, 'D': 1, 'E': 3}
D = {'Node': 'D', 'A': 2, 'C': 1, 'G': 1}
E = {'Node': 'E', 'C': 3, 'F': 2}
F = {'Node': 'F', 'B': 3, 'E': 2, 'G': 1}
G = {'Node': 'G', 'D': 1, 'F': 1}
'''

#graph.append(G)

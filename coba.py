import pprint
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

letter = ["A","B","C","D","E","F","G","H","I","J","K", "L","M","N","O","P","Q","R","S","T","U", "V","W","X","Y","Z"]

a = int(input("Enter number of vertices: "))
for i in range(a):
    
    print("Masukkan jumlah tetangga ", letter[i])
    n = int(input("Jumlah tetangga = "))          #n is the number of items you want to enter
    var ={}
    d ={}
    d['Node'] = letter[i]                     
    for i in range(n+1):
                
        text = input().split()     #split the input text based on space & store in the list 'text'
        d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
        var[i] = d
        
             
      
    graph.append(var[i])

newlist=[]                       #make an empty list
for x in graph:                    # loop to hv a dict in list  
    s={}
                             # make an empty dict to store new dict data 
    for k in x.keys():            # to get keys in the dict of the list 
        
        if k != 'Node':    
            s[k]=int(x[k])
        else:
            s[k]=x[k]        # change the values from string to int by int func
         
    newlist.append(s)             # to add the new dict with integer to the list

print(newlist)

  



source = str(input("Masukkan Node Awal : "))
dest = str(input("Masukkan Node Tujuan : "))
d = Dijkstra(newlist)
d.get_path(source, dest, True)
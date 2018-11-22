import pprint
import time
start_time = time.time()

class Dijkstra(object):
    def __init__(self, graph):                  #Fungsi untuk menentukan atau membuat suatu graph dictionary dalam list
        self.open_list = []
        self.close_list = []
        self.previous = []
        self.graph = graph
        self.actual_node = None
        self.distance = 0

        self.step = 0
        self.once = True
    
    def get_path(self, start_node, end_node, debugging=False):          #Fungsi untuk mencari jarak terpendek dari suatu node dalam graph 
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
            #Untuk menampilkan elemen node ke dalam list values
            values = []
            for element in self.open_list:
                for node in element:
                    values.append(element.get(node))
            self.actual_node = self.open_list[(values.index(min(values)))]
            self.distance = list(self.actual_node.values())[0]
            self.debug(debugging)
        #Untuk mencari jarak dari setiap node yang menuju ke variable a(end_node) dengan syarat menemukan jarak terpendek dari suatu node 
        a = end_node
        string = str(end_node)
        while a != start_node:
            for element in self.previous:
                for node in element:
                    if node == a:
                        a = element.get(node)
                        string = str(a) + " -> " + string
        print("\n                         Jarak Terpendek Antara " + str(start_node) + " Dan " + str(end_node) + " Adalah:")
        print("                                            "+string)
    
    def debug(self, debugging=True):                #Fungsi untuk menampilkan jarak terpendek(shortest path)
        if debugging:
            if self.once:
                self.once = False
                print("\n\n\n                    Langkah | Node |   Jarak  |")
            node = list(self.actual_node.keys())[0]
            value = list(self.actual_node.values())[0]
            print("                       %4d" % self.step + " | %4s" % node + " | %8s" % value + " | Open: " + str(
                self.open_list) + " | Close: " + str(self.close_list))
            self.step += 1

#main

graph = []
letter = ["A","B","C","D","E","F","G","H","I","J","K", "L","M","N","O","P","Q","R","S","T","U", "V","W","X","Y","Z"]
print("========================================================================================================")
print("                                 PROGRAM ALGORITMA DIJKSTRA")
print("========================================================================================================")
print("\n")

a = int(input("                                   Masukkan Jumlah Node: "))
#Perulangan yang dilakukan sebanyak jumlah node(a) 
for i in range(a):
    n = int(input("\n                                 Jumlah Tetangga Node " +letter[i]+ " = "))       #n Adalah Jumlah Tetangga Suatu Node
    print("\n")
    print("                         Masukkan Nama Node Tetangga " +letter[i]+ " (spasi) Bobot    ") 
    var ={}
    d ={}
    d['Node'] = letter[i]
                   
    for i in range(n):
        print("                                      Tetangga ke "+str(i+1)+" = ")
        text = input("                                             ").split()    
        d[text[0]] = text[1]
        var[i] = d

    graph.append(var[i])

#Untuk mengubah string Angka Menjadi Integer
newlist=[]                       
for x in graph:                      
    s={}
                           
    for k in x.keys():            
        
        if k != 'Node':    
            s[k]=int(x[k])
        else:
            s[k]=x[k]       
         
    newlist.append(s)            

print("\n                         "+str(newlist))

#Untuk mencari jarak terpendek dari source menuju dest
source = str(input("                                  Masukkan Node Awal : "))
dest = str(input("                                 Masukkan Node Tujuan : "))
d = Dijkstra(newlist)
d.get_path(source, dest, True)

print("                       Waktu Eksekusi : %s second" % (time.time() - start_time))
print("\n\n")  
print("                                 Muhammad Fajar Al Hanief(1302160191)")
print("                                        Putri Enita(1302162016)")
print("                                         Iyon Priyono(1302160036)")
print("                                       Reyhan Al Kadri(1302164071)")
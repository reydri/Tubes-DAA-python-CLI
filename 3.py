import pprint
import sys



def dijkstra(graph,src,dest,totalnode,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """    
    # a few sanity checks
    neighbor=[]
    letter =["a","b","c","d","e","f","g","h","i","k", "l","m","n","o","p","q","r","s","t","u", "v","w","x","y","z"]
    for i in range(1,v):
        if(graph[src][letter[i]] != 0):
            neighbor[i] = letter[i]
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]= 0
        # visit the neighbors
        for i in range(1,v) :
            if neighbor[i] not in visited:
                new_distance = distances[src] + graph[src][neighbor[i]]
                if new_distance < distances.get(neighbor[i],float('inf')):
                    distances[neighbor[i]] = new_distance
                    predecessors[neighbor[i]] = src


        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)


#graph = {'A' : {'C':1},'B':{'A': 1, 'C':2}}
'''
def jarak_terpendek(graph, source, dest):
    result = []
    result.append(source)

    while dest not in result:
        current_node = result[-1]

        local_max = min(graph[current_node].values())
        for node, weight in graph[current_node].items():
            if weight == local_max:
                result.append(node)


    print(result)

    '''
if __name__ == '__main__':

    graph = {}
    values = {} 
    v = int(input("Enter number of vertices: ")) 
    print("Enter vertices(keys) : ") 
    for i in range(v): 
        graph.setdefault(input()) 
    edges = {} 
    for x in graph: 
        edges.setdefault(x) 
    for i in graph: 
        graph[i] = edges.copy()
    print("Enter weights: ") 
    for i in graph:  
        for j in graph[i]:
            print(i, "ke", j)
            var = input() 
            graph[i][j] = var 
    
    pprint.pprint(graph)
    #print(graph['A']['B'])
    source = str(input("Masukkan Node Awal : "))
    dest = str(input("Masukkan Node Akhir : "))
    print(graph[source])


print(dijkstra(graph, source, dest,v))
##minimum spanning tree kruskal's Algorithm Mrigank's implementation

graph_edges = {'a' : 1, "b" : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7 , 'h' : 8, 'i' : 9 , 'j' : 10, 'k' : 11,
               'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18}

graph_vertex = {'a' : ('A', 'E'), 'b' : ('D', "G"), 'c' : ('C','E') , 'd' : ('A', 'B'), 'e' : ("B", "E"), 'f' : ("E", "F"),
                'g' : ('C', 'F'), 'h' : ("C", "D"), "i" : ('H', 'E'), 'j' : ('F', 'H'), "k" : ('H', 'I') , 'l': ('B', 'C'),
                'm' : ("G", "H"), 'n' : ('C', "G"), 'o' : ('G', 'I') , 'p': ('I', 'J'), 'q' : ('H', 'J'), 'r' : ('F', 'G')}

clusters = []
min_spanning_tree = []
class priority_queue:
    def __init__(self):
        self.__pq = []
    def enqueue(self, a):
        self.__pq.extend(a)
        self.__pq.sort(key = lambda x : x[1])
        return self.__pq
    def dequeue(self):
        if len(self.__pq) == 0:
            return
        c = self.__pq.pop(0)
        return c
    def length(self):
        return len(self.__pq)


def kruskal(edges, vertices, clusters):
    prior = priority_queue()
    prior.enqueue(edges.items())
    while prior.length() != 0:
        found_1 = -1
        found_2 = -1
        c = prior.dequeue()
        d = -1
        for i in clusters:
            d += 1

            if vertices[c[0]][0] in i:
                found_1 = d
            if vertices[c[0]][1] in i:
                found_2 = d
            
        if found_1 == -1 and found_2 == -1:
            #creating new clusters if none of the vertices belong to any clusters
            clusters.append([])
            
            min_spanning_tree.append(c[0])
            clusters[-1].append(vertices[c[0]][0])
            clusters[-1].append(vertices[c[0]][1])
            continue
        if found_1 == found_2:
            continue
        if found_1 > found_2 and found_2 > -1:
            clusters[found_2].extend(clusters[found_1])
            min_spanning_tree.append(c[0])
            del clusters[found_1]
            continue
        if found_2 > found_1 and found_1 > -1:
            clusters[found_1].extend(clusters[found_2])
            min_spanning_tree.append(c[0])
            del clusters[found_2]
            continue
        if found_1 > -1 and found_2 == -1:
            
            clusters[found_1].append(vertices[c[0]][1])
            min_spanning_tree.append(c[0])
            continue
        if found_2 > -1 and found_1 == -1:
            clusters[found_2].append(vertices[c[0]][0])
            min_spanning_tree.append(c[0])
            continue
    return min_spanning_tree
c = kruskal(graph_edges, graph_vertex,clusters)
print("The edges of the min spanning tree are ", c)

            
                
                
            
            
            
            
            
            
            
                
                
                
            
                
                
                
                
            
        
    
    

    
    
    






        
        

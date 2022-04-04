#mriganka saikia Dijkstra's Algorithm implementation
from math import inf
class pqueue:
    def __init__(self):
        self.queue = []
    def push(self, a):
        self.queue.append(a)
        self.queue.sort(key = lambda x : x[1])
    def notempty(self):
        if len(self.queue) == 0:
            return False
        else:
            return True
    def dequeue(self):
        return self.queue.pop(0)
        


# Dijkstra's Algorithm
graph = {'A' : [('D',1),("B", 2)], "B" : [("E", 10), ('D',3)], 'C' : [("F", 5),
        ('A', 4)], "D" : [('C',2), ('E', 2), ('F', 8),('G',4)],
         "E" : [('G',6)], "F" : 0, "G" : [('F', 1)]
         }
cost = {x : inf for x in ["A", "B", "C", "D", "E","F","G", "H"]}
prev = {x : 0 for x in ['A', 'B', 'C', 'D', 'F', 'F', 'G', 'H']}
visited = []

def dijkstra(A, B, graph, visited):
    queue = pqueue()
    cost[A] = 0
    queue.push((A, 0))
    while queue.notempty():
        holder = queue.dequeue()
        if holder[0] == B:
            path = "" + B + '-'
            c = prev[B]
            while c != A:
                path += c
                path += '-'
                c = prev[c]
            path += A
            path = path[::-1]
            return "The shortest path is  " + path + "," + " the min cost is " + str(cost[B])
            
            
        visited.append(holder[0])
        if graph[holder[0]] != 0:
            for i in graph[holder[0]]:
                if i[0] in visited:
                    continue
                costf = cost[holder[0]] + i[1]
                if costf < cost[i[0]]:
                    cost[i[0]] = costf
                    prev[i[0]] = holder[0]
                    queue.push((i[0], costf))

print(dijkstra('A','F', graph, visited))
                    
                    
                
                
                
            
            
        
        
        
    














    
    

         


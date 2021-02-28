import os
import sys
import time

class Graph () :
    def __init__ (self) :
        self.adjList = dict()
        self.inDegree = dict()
    def addEdge (self, start, end) :
        self.addNode(start)
        self.addNode(end)
        self.adjList[start].append(end)
        self.addInDegree(end)
    def addNode (self, node) :
        if node not in self.adjList:
            self.adjList[node] = []
            self.inDegree[node] = 0
    def addInDegree(self, node):
        if node not in self.inDegree:
            self.inDegree[node] = 0
        self.inDegree[node] += 1
    def printGraph(self):
        for key in self.adjList.keys():
            print(key + ": ")
            print(self.adjList[key])
    def printInDegree(self):
        for key in self.inDegree.keys():
            print(key + ": ")
            print(self.inDegree[key])

    def topologicalSort(self) :
        adjList = self.adjList.copy()
        inDegree = self.inDegree.copy()

        self.topologicalSortUtils(adjList, inDegree, 1)
        
    def topologicalSortUtils (self, adjList : dict, inDegree : dict, depth : int):
        toDelete = []
        for course in inDegree.keys():
            if inDegree[course] == 0:
                toDelete.append(course)
        if len(toDelete) > 0:
            print("Semester {} : ".format(depth), end=" ")
            for course in toDelete:
                print(course, end=" ")
                neighbourList = adjList[course]
                del inDegree[course]
                del adjList[course]

                for neighbour in neighbourList:
                    inDegree[neighbour] -= 1
            print()
            self.topologicalSortUtils(adjList, inDegree, depth + 1)

    def constructGraphFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                line = line[:len(line) - 1]
                courseList = line.split(",")
                self.addNode(courseList[0].strip())
                for course in courseList[1:]:
                    self.addEdge(course.strip(), courseList[0].strip())
                
        




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python topological.py FILE_NAME")
    else:
        testFilePath = os.path.join(os.getcwd(), "../test", sys.argv[1] + ".txt")
        if os.path.exists(testFilePath) :
            start_time = time.time()
            graph = Graph()
            graph.constructGraphFromFile(testFilePath)
            graph.topologicalSort()
            print("---------%s seconds ---------" % (time.time() - start_time))
            
        else:
            print("Not a valid test file")



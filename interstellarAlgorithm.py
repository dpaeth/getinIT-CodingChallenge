import json
import networkx as nx

data = json.load(open('generatedGraph.json'))
G = nx.Graph()
i = 0

#Weise Nodes zu und finde Start und Ziel
for nodes in data['nodes']:
    if nodes['label'] == 'Erde':
        start = i
    elif nodes['label'] == 'b3-r7-r4nd7':
        target = i
    G.add_node(i)
    i += 1

#Weise die Edges dem Graphen zu
for edges in data['edges']:
    G.add_edge(edges['source'], edges['target'], cost=edges['cost'])

#Gebe den kürzesten Weg mithilfe des Dijkstra-Algorithmus aus
fastest = nx.bidirectional_dijkstra(G, start, target, weight='cost')
print('Optimale Abfolge der Nodes:\t', fastest[1])
print('Gesamtentfernung:\t\t\t', fastest[0])





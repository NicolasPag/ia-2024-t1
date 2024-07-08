"""Implementação do algoritmo de Dijkstra para o menor caminho em grafos."""

from heapq import heapify, heappush, heappop

#from util import reverse_path


def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Dijkstra."""

    stackNodes= []
    processedNodes = []

    heappush(stackNodes, (0, start))

    tempNodes = {}
    tempNodes[start] = {
        'predecessor' : None,
        'currWeight' : 0,
        'allPredec' : [None]
    }

    while stackNodes:

        _, node = heappop(stackNodes)

        if node in processedNodes:
            continue

        processedNodes.append(node)

        if node == goal:

            path = [goal]
            currPath = goal

            while path[-1] != start:
                currPath = tempNodes[currPath]['predecessor']
                path.append(currPath)

            path.reverse()

            break

        visitedNode = tempNodes[node]

        for neighborNode, neighborWeight in graph[node][1].items():

            if (
                neighborNode not in tempNodes or 
                node not in tempNodes[neighborNode]['allPredec']
            ):
                newWeight = visitedNode['currWeight'] + neighborWeight
                newPredec = node

                if neighborNode not in tempNodes:

                    heappush(stackNodes, (newWeight, neighborNode))
                    tempNodes[neighborNode] = {
                        'predecessor' : newPredec,
                        'currWeight' : newWeight,
                        'allPredec' : [newPredec]
                    }

                elif newWeight < tempNodes[neighborNode]['currWeight']:

                    heappush(stackNodes, (newWeight, neighborNode))
                    newAllPredec = tempNodes[neighborNode]['allPredec']
                    newAllPredec.append(newPredec)

                    tempNodes[neighborNode] = {
                        'predecessor' : newPredec,
                        'currWeight' : newWeight,
                        'allPredec' : newAllPredec
                    }

                else:
                    tempNodes[neighborNode]['allPredec'].append(newPredec)

    return (len(processedNodes), tempNodes[node]['currWeight'], path)
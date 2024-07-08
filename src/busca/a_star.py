"""Implementação do algoritmo A*."""
from queue import PriorityQueue
from util import haversine

def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando A*."""

    frontier = PriorityQueue()
    frontier.put((0, start))

    cameFrom = {}
    cameFrom[start] = None

    constSoFar = {}
    constSoFar[start] = 0

    countNodes = 0

    while not frontier.empty():
        _, current = frontier.get()
        countNodes += 1

        if current == goal:
            predecessor = cameFrom[current]
            path = [current]

            while predecessor is not None:
                path.append(predecessor)
                predecessor = cameFrom[predecessor]

            path.reverse()

            break

        for nextNode, nextNodeCost in graph[current][1].items():
            newCost = float(constSoFar[current]) + nextNodeCost

            if (
                nextNode not in constSoFar or
                newCost < constSoFar[nextNode]
            ):
                constSoFar[nextNode] = newCost
                priority = newCost + haversine(
                    graph[goal][0][0],
                    graph[goal][0][1],
                    graph[nextNode][0][0],
                    graph[nextNode][0][1]
                )

                frontier.put((priority, nextNode))
                cameFrom[nextNode] = current

    return (countNodes, constSoFar[goal], path)
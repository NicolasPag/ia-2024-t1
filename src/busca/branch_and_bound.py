"""Implementação do algoritmo 'branch and bound'."""


def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando Branch and Bound."""

    stack = [(start, None)]
    visitedNodes = {}
    bestPath = None
    bestCost = float('inf')
    countNodes = 0

    while stack:

        currNode, predecessor = stack.pop(0)

        if goal == currNode:
            path = [currNode]
            totalCost = 0

            while predecessor is not None:
                path.append(predecessor)
                totalCost += graph[predecessor][1][currNode]
                currNode = predecessor
                predecessor = visitedNodes.get(currNode)

            path.reverse()

            if totalCost < bestCost:
                bestCost = totalCost
                bestPath = path

            continue

        if currNode not in visitedNodes:

            countNodes += 1
            visitedNodes[currNode] = predecessor

            for neighbor, cost in graph[currNode][1].items():
                if neighbor not in visitedNodes and cost < bestCost:
                    stack.append((neighbor, currNode))

    if bestPath is not None:
        return (countNodes, bestCost, bestPath)
    
    return None
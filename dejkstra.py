def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

graph = {'start':{'a':6, 'b':2}, 'a':{'fin':1}, 'b':{'a':3, 'fin':5}, 'fin':{}}
costs = {'a':6, 'b':2, 'fin':float('inf')}
parents = {'a':'start', 'b':'start', 'fin':None}
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(parents)
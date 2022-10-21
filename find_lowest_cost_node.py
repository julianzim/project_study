def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node

costs = {'a': 10, 'b': 5, 'c': 13}
node = find_lowest_cost_node(costs)
print(node)
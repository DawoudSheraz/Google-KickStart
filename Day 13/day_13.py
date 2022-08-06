
TEST_DATA = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""


class Graph:

    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.possible_distances = []

    def create_connection(self, node_1, node_2, cost):
        if node_1 not in self.nodes:
            self.nodes.append(node_1)
            self.graph[node_1] = []
        if node_2 not in self.nodes:
            self.nodes.append(node_2)
            self.graph[node_2] = []
        self.graph[node_1].append((node_2, cost))

    def parse_graph(self, current_node, visited, distance, start_node):

        if current_node not in visited:
            visited.append(current_node)
        elif current_node in visited:
            return

        if set(visited) == set(self.nodes):
            # When on the last node, find the path distance from Last -> First node in both directions
            end_to_start = [node for node in self.graph[current_node] if node[0] == start_node][0]
            start_to_end= [node for node in self.graph[start_node] if node[0] == current_node][0]
            updated_distance = distance + end_to_start[1] + start_to_end[1]
            self.possible_distances.append(updated_distance)
            return

        for connected_node in self.graph[current_node]:
            current_visited = visited.copy()
            reverse_node = [node for node in self.graph[connected_node[0]] if node[0] == current_node][0]
            updated_distance = distance + connected_node[1] + reverse_node[1]
            self.parse_graph(connected_node[0], current_visited, updated_distance, start_node)

        return

    def start_parse(self):
        for node in self.nodes:
            self.parse_graph(node, [], 0, node)

    def build_graph(self, data_str):
        for connection in data_str.splitlines():
            connection = connection.split(' ')
            cost = int(connection[3]) * (1 if connection[2] == 'gain' else -1)
            self.create_connection(connection[0], connection[-1][:-1], cost)

    def self_inclusion(self):
        for node in self.nodes:
            self.create_connection(node, 'self', 0)
            self.create_connection('self', node, 0)


def solve(data, part=1):
    graph = Graph()
    graph.build_graph(data)
    if part == 2:
        graph.self_inclusion()
    graph.start_parse()
    return max(graph.possible_distances)


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(solve(data)))
    print("Part 2: {}".format(solve(data, part=2)))

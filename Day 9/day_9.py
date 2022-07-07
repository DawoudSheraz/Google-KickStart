
TEST_DATA = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


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
        self.graph[node_2].append((node_1, cost))

    def parse_graph(self, current_node, visited, distance):
        if current_node not in visited:
            visited.append(current_node)
        elif current_node in visited:
            return

        if set(visited) == set(self.nodes):
            self.possible_distances.append(distance)
            return

        for connected_node in self.graph[current_node]:
            current_visited = visited.copy()
            self.parse_graph(connected_node[0], current_visited, distance + connected_node[1])
        return

    def start_parse(self):
        for node in self.nodes:
            self.parse_graph(node, [], 0)

    def build_graph(self, data_str):
        for connection in data_str.splitlines():
            connection = connection.split(' ')
            self.create_connection(connection[0], connection[2], int(connection[-1]))


def solve(data):
    graph = Graph()
    graph.build_graph(data)
    graph.start_parse()
    return min(graph.possible_distances), max(graph.possible_distances)


with open('input.in') as f:
    data = f.read()
    print("Mix: {}, Max: {}".format(*solve(data)))

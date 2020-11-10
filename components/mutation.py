import random
class Mutation:
    def mutation(self, number_of_disconnections, G):
        # 1. Select Edges to be removed
        edges_to_remove = int(len(list(self.multicast_tree.edges()))*number_of_disconnections)
        edges_removed = 0
        while edges_removed < edges_to_remove:
            edges = list(self.multicast_tree.edges())
            random_edge_to_remove = random.choice(edges)
            self.multicast_tree.remove_edge(random_edge_to_remove)
            edges_removed += 1
        self.multicast_tree.reconnect(G)
        self.multicast_tree.prune()
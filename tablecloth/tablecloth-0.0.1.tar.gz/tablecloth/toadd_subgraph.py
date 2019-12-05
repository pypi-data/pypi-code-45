    def subgraph(self, keys: typing.Iterable) -> T:
        """Create a subgraph from the specified keys.

        The subgraph will use the specified keys to build
        a subgraph, only conserving edges if vertices on
        both ends are among the specified set of keys.
        
        Args:
        - keys: an iterable with node IDs.
        Returns:
        - An instance of the same class as a subgraph.
        """
        res = type(self)()
        for k in keys:
            if k not in self._nodes:
                raise ValueError('No node {}'.format(k))
            res._nodes.add(k)
            for k_b in self.nodes_from(k):
                if k_b in keys:
                    res.add_edge(k, k_b)
            for k_a in self.nodes_to(k):
                if k_a in keys:
                    res.add_edge(k_a, k)
        return res

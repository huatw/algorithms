start_node = None
graph = collections.defaultdict(list)


def build_graph(node, parent, k):
    if not node:
        return

    if node.val == k:
        start_node = node

    if parent:
        graph[node].append(parent)
        graph[parent].append(node)

    build_graph(node.left, node, k)
    build_graph(node.right, node, k)


def find_closest_lead(root, k):
    build_graph(root, None, k)

    q = Queue.deque([start_node])
    seen = set()

    while q:
        node = q.popleft()
        seen.add(node)
        if not node.left and not node.right:
            return node.val
        for next_node in graph[node]:
            if next_node not in seen:
                q.append(node)

    return 0



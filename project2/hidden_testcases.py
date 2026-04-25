from graph_algorithms import bfs, dfs, dijkstra, kosaraju, tarjan, required_edges, a_star
#AI-made hidden test cases

# =========================
# BFS TESTS
# =========================
def test_bfs():
    graph = {
        "A": {"B": 1, "C": 1},
        "B": {"D": 1},
        "C": {"E": 1},
        "D": {},
        "E": {}
    }

    assert bfs(graph, "A", "E") == 1
    assert bfs(graph, "A", "Z") == 0
    assert bfs(graph, "D") == ["D"]


# =========================
# DFS TESTS
# =========================
def test_dfs():
    graph = {
        "A": {"B": 1},
        "B": {"C": 1},
        "C": {"D": 1},
        "D": {"A": 1}
    }

    path = dfs(graph, "A")
    assert set(path) == {"A", "B", "C", "D"}

    assert dfs(graph, "A", search_node="C") == 1
    assert dfs(graph, "A", search_node="Z") == 0


# =========================
# DIJKSTRA TESTS
# =========================
def test_dijkstra():
    graph = {
        "A": {"B": 1, "C": 10},
        "B": {"D": 1},
        "C": {"D": 1},
        "D": {}
    }

    path, dist, hops = dijkstra(graph, "A", "D")

    assert path == ["A", "B", "D"]
    assert dist == 2
    assert hops == 2

    assert dijkstra(graph, "A", "Z") == 0


# =========================
# KOSARAJU TESTS
# =========================
def test_kosaraju():
    graph = {
        "A": {"B": 1},
        "B": {"C": 1},
        "C": {"A": 1},
        "D": {}
    }

    scc = kosaraju(graph)
    flat = [set(c) for c in scc]

    assert {"A", "B", "C"} in flat
    assert {"D"} in flat


# =========================
# TARJAN TESTS
# =========================
def test_tarjan():
    graph = {
        "A": {"B": 1},
        "B": {"C": 1},
        "C": {"A": 1},
        "D": {"E": 1},
        "E": {"D": 1},
        "F": {}
    }

    scc = tarjan(graph)
    flat = [set(c) for c in scc]

    assert {"A", "B", "C"} in flat
    assert {"D", "E"} in flat
    assert {"F"} in flat


# =========================
# REQUIRED EDGES TESTS
# =========================
def test_required_edges():
    graph = {
        "A": {"B": 1},
        "B": {"C": 1},
        "C": {}
    }

    edges = required_edges(graph)

    assert ("A", "B") in edges
    assert ("B", "C") in edges


# =========================
# A* TESTS
# =========================
def test_astar():
    graph = {
        "A": {"B": 1, "C": 5},
        "B": {"D": 1},
        "C": {"D": 1},
        "D": {}
    }

    path = a_star(graph, "A", "D")
    assert path == ["A", "B", "D"]


def test_astar_unreachable():
    graph = {
        "A": {"B": 1},
        "B": {},
        "C": {}
    }

    assert a_star(graph, "A", "C") is None

import random
import time
from graph_algorithms import bfs, dfs, dijkstra, kosaraju, tarjan, required_edges, a_star


def build_sparse_graph(n=2000):
    graph = {}
    nodes = [f"N{i}" for i in range(n)]

    for i in range(n):
        graph[nodes[i]] = {}

    # sparse chain + random edges
    for i in range(n - 1):
        graph[nodes[i]][nodes[i + 1]] = 1

    for _ in range(n * 2):
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            graph[u][v] = 1

    return graph


def test_bfs_large():
    graph = build_sparse_graph(2000)
    start = "N0"

    t0 = time.time()
    res = bfs(graph, start)
    t1 = time.time()

    assert isinstance(res, list)
    assert t1 - t0 < 2.0   # hidden-style timing constraint


def test_dfs_large():
    graph = build_sparse_graph(2000)

    t0 = time.time()
    res = dfs(graph, "N0")
    t1 = time.time()

    assert isinstance(res, list)
    assert len(res) > 0
    assert t1 - t0 < 2.0


def test_dijkstra_large():
    graph = build_sparse_graph(2000)

    t0 = time.time()
    res = dijkstra(graph, "N0", "N1999")
    t1 = time.time()

    assert res != 0
    assert isinstance(res[0], list)
    assert t1 - t0 < 3.0


def test_kosaraju_large():
    # big SCC cycle
    n = 1000
    graph = {}

    nodes = [f"N{i}" for i in range(n)]

    for i in range(n):
        graph[nodes[i]] = {}

    for i in range(n):
        graph[nodes[i]][nodes[(i + 1) % n]] = 1  # full cycle

    t0 = time.time()
    scc = kosaraju(graph)
    t1 = time.time()

    assert any(len(c) == n for c in scc)
    assert t1 - t0 < 3.0


def test_tarjan_large():
    n = 1000
    graph = {}

    nodes = [f"N{i}" for i in range(n)]

    for i in range(n):
        graph[nodes[i]] = {}

    for i in range(n):
        graph[nodes[i]][nodes[(i + 1) % n]] = 1

    t0 = time.time()
    scc = tarjan(graph)
    t1 = time.time()

    assert any(len(c) == n for c in scc)
    assert t1 - t0 < 3.0


def test_required_edges_large():
    graph = build_sparse_graph(300)

    t0 = time.time()
    edges = required_edges(graph)
    t1 = time.time()

    assert isinstance(edges, list)
    assert t1 - t0 < 5.0


def test_astar_large():
    graph = build_sparse_graph(1000)

    t0 = time.time()
    path = a_star(graph, "N0", "N999")
    t1 = time.time()

    assert path is None or isinstance(path, list)
    assert t1 - t0 < 3.0


# =========================
# RUNNER (like hidden grader)
# =========================
if __name__ == "__main__":
    tests = [
        test_bfs,
        test_dfs,
        test_dijkstra,
        test_kosaraju,
        test_tarjan,
        test_required_edges,
        test_astar,
        test_astar_unreachable,
        test_bfs_large,
        test_dfs_large,
        test_dijkstra_large,
        test_kosaraju_large,
        test_tarjan_large,
        test_required_edges_large,
        test_astar_large
    ]

    passed = 0
    failed = 0

    for t in tests:
        try:
            t()
            print(f"{t.__name__}: PASS")
            passed += 1
        except AssertionError as e:
            print(f"{t.__name__}: FAIL")
            print("  ", e)
            failed += 1

    print("\n===================")
    print("TOTAL PASSED:", passed)
    print("TOTAL FAILED:", failed)
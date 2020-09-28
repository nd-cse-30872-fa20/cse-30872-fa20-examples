// graph.cpp

#include "graph.h"

#include <queue>
#include <tuple>

// Function Definitions

bool	read_graph(Graph &graph, std::istream &stream) {
    size_t vertices, edges;

    if (!(stream >> vertices >> edges) || !vertices || !edges) {
	return false;
    }

    graph.clear();

    int source, target;
    for (size_t e = 0; e < edges; e++) {
    	if (!(stream >> source >> target)) {
    	    return false;
	}
    	graph[source].insert(target);
    	graph[target].insert(source);
    }

    return true;
}

bool	is_bicolorable(Graph &graph) {
    std::queue<std::tuple<int, int>> frontier;
    std::unordered_map<int, int>     visited;

    frontier.push(std::make_tuple(0, 0));

    while (!frontier.empty()) {
    	int vertex, color;

	std::tie(vertex, color) = frontier.front(); frontier.pop();

    	if (visited.count(vertex)) {
    	    if (visited[vertex] != color) {
    	    	return false;
	    }
	    	
	    continue;
	}

	visited[vertex] = color;

	for (auto neighbor : graph[vertex]) {
	    frontier.push(std::make_tuple(neighbor, (color + 1) % 2));
	}
    }

    return true;
}

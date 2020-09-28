// main.cpp

#include "graph.h"

#include <iostream>

// Main Execution

int main(int argc, char *argv[]) {
    Graph g;

    while (read_graph(g, std::cin)) {
	std::cout << (is_bicolorable(g) ? "BICOLORABLE" : "NOT BICOLORABLE") << std::endl;
    }

    return 0;
}

// graph.h

#pragma once

#include <iostream>
#include <unordered_map>
#include <unordered_set>

// Type Definitions

typedef std::unordered_map<int, std::unordered_set<int>> Graph;

// Function Prototypes

bool	read_graph(Graph &graph, std::istream &stream);
bool	is_bicolorable(Graph &graph);

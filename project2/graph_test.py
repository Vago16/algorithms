#test to make sure graph is being built correctly
from graph_creation import TitleDictionary, MovieNetwork

td = TitleDictionary("imdb_network.csv")

print("title_dict size:", len(td.title_dict))
print("profession_dict size:", len(td.profession_dict))

# Build graph
mn = MovieNetwork(td.title_dict, td.profession_dict)
graph = mn.create_graph()

print("graph nodes:", len(graph))
print("sample node:", list(graph.items())[:1])
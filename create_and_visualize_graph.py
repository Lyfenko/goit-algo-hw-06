import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim


def get_street_name(lat, lon):
    geolocator = Nominatim(user_agent="my_app")

    try:
        location = geolocator.reverse((lat, lon), language="uk")
        return location.raw.get("address", {}).get("road", "Ім'я вулиці відсутнє")
    except Exception as e:
        print(f"Помилка отримання імені вулиці: {e}")
        return "Помилка отримання імені вулиці"


def add_edge_weights(G):
    G.edges.data('weight', default=G.edges.data('length'))


def create_and_visualize_graph(place_query):
    G = ox.graph_from_place(place_query, network_type="all")
    add_edge_weights(G)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(12, 12))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightcoral", label="Вершини")
    nx.draw_networkx_edges(G, pos, edge_color="gray", width=1, alpha=0.7, label="Ребра")
    nx.draw_networkx_labels(G, pos, font_size=8, font_color="black", font_weight="bold")

    plt.text(
        0.5,
        1.1,
        place_query,
        ha="center",
        va="center",
        transform=plt.gca().transAxes,
        fontsize=14,
        bbox=dict(facecolor="white", edgecolor="white", boxstyle="round,pad=0.3"),
    )

    print("Основні характеристики графа:")
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print("Ступінь вершин:", dict(G.degree()))

    print("\nІмена вулиць:")
    for node, data in G.nodes(data=True):
        lat, lon = data["y"], data["x"]
        street_name = get_street_name(lat, lon)
        print(f"Вершина {node}: {street_name}")

        for key, value in data.items():
            if key not in ["x", "y"]:
                print(f"  {key}: {value}")

    plt.legend()
    plt.show()

    return G


if __name__ == "__main__":
    place_query = "Мала Березянка, Київська область, Україна"
    create_and_visualize_graph(place_query)

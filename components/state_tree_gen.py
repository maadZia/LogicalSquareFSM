import pyqtgraph as pg


def draw_tree(graph_widget, edges, node_names=None):
    graph_widget.clear()
    node_names = node_names or {}

    children_map = {}
    levels = {}
    for parent, child in edges:
        parent = str(parent)
        child = str(child)
        if parent not in children_map:
            children_map[parent] = []
        children_map[parent].append(child)

    def assign_levels(node, current_level=0):
        levels[node] = current_level
        for child in children_map.get(node, []):
            assign_levels(child, current_level + 1)

    all_nodes = set(str(parent) for parent, _ in edges) | set(str(child) for _, child in edges)
    child_nodes = set(str(child) for _, child in edges)
    root_nodes = all_nodes - child_nodes
    root = list(root_nodes)[0] if root_nodes else None

    if root is None:
        raise ValueError("Nie znaleziono korzenia drzewa!")

    assign_levels(root)
    positions = {}

    def calculate_positions(node, x_offset=0, y_offset=0, horizontal_gap=100):
        """
        Rekurencyjnie oblicza pozycje węzłów, rozmieszczając dzieci w poziomie.
        """
        children = children_map.get(node, [])
        if not children:
            positions[node] = (x_offset, y_offset)
            return x_offset

        subtree_widths = []
        for child in children:
            width = calculate_positions(child, x_offset, y_offset - 100, horizontal_gap)
            subtree_widths.append(width)
            x_offset = width + horizontal_gap

        node_x = (subtree_widths[0] + subtree_widths[-1]) / 2
        positions[node] = (node_x, y_offset)
        return node_x

    calculate_positions(root, x_offset=0, y_offset=0)

    for parent, child in edges:
        parent = str(parent)
        child = str(child)
        x1, y1 = positions[parent]
        x2, y2 = positions[child]
        graph_widget.plot([x1, x2], [y1, y2], pen=pg.mkPen('black', width=3))

    # Obliczenie maksymalnej liczby poziomów w drzewie
    max_level = max(levels.values())

    # Skalowanie rozmiaru węzłów globalnie na podstawie maksymalnej liczby poziomów
    base_size = 50
    min_size = 20
    size_scale = max(base_size - (max_level * 5), min_size) / base_size

    # Rysowanie węzłów
    for node, (x, y) in positions.items():
        # Dynamicznie skalowany rozmiar węzła
        node_size = base_size * size_scale

        graph_widget.plot(
            [x], [y], pen=None, symbol='o', symbolSize=node_size, symbolBrush='lightgreen'
        )
        text = pg.TextItem(str(node), anchor=(0.5, 0.5), color='black')
        text.setPos(x, y)
        graph_widget.addItem(text)

        state_name = node_names.get(node, None)
        if state_name:
            name_text = pg.TextItem(state_name, anchor=(0.5, 0), color='darkgreen')
            name_text.setPos(x, y-0.5)
            graph_widget.addItem(name_text)


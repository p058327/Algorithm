from tqdm import tqdm
import cv2
import matplotlib.pyplot as plt

from dijkstra_algorithm import dijkstra


# file = 'mazes/maze.png'
# file = 'mazes/maze5.jpg'
# file = 'mazes/162a11.png'
file = 'mazes/58cc0d.png'

img = cv2.imread(file)  # read an image from a file using
cv2.circle(img, (400, 50), 3, (255, 0, 0), -1)  # add a circle at (42, 330)
cv2.circle(img, (390, 350), 3, (0, 0, 255), -1)  # add a circle at (25,5)
plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image
img = cv2.imread(file)
plt.show()
img = img[:, :, 0]


class GraphNode:
    def __init__(self, position: tuple, neighborhoods):
        """Initializes a graph node with position and neighborhoods."""
        self.position = position
        self.neighborhoods = neighborhoods
        self.previous = None
        self.distance = float('inf')

    def __lt__(self, other):
        return self.distance < other.distance


def get_neighborhoods(point):
    """Returns neighboring points and distances for a given point."""
    x, y = point
    width, height = img.shape
    neighborhoods = {}
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 < i < (width - 1) and 0 < j < (height - 1) and (i, j) != point and img[(i, j)] > 200:
                distance = get_distance(point, (i, j))
                neighborhoods[(i, j)] = distance
    return neighborhoods


def get_distance(point_1, point_2):
    """Calculates Euclidean distance between two points."""
    distance = (((point_1[0] - point_2[0]) ** 2) + ((point_1[1] - point_2[1]) ** 2)) ** 0.5
    return distance


def get_graph():
    """Creates a graph of nodes with positions and neighborhoods."""
    all_nodes = {}
    width, height = img.shape
    for i in tqdm(range(width + 1), "made graph"):
        for j in range(height + 1):
            point = i, j
            neighborhoods = get_neighborhoods(point)
            all_nodes[(i, j)] = GraphNode((i, j), neighborhoods)
    return all_nodes


def get_path(start, end):
    """Finds shortest path using Dijkstra's algorithm."""
    path_maze = []
    graph = get_graph()
    step = dijkstra(start, end, graph)
    if step is not end:
        NotImplementedError("can't selotion this maze")
    while step.previous is not None:
        # the step.previous is None only in the first step
        path_maze.append(step.position)
        step = step.previous
    return path_maze


def drawPath(image, short_path, thickness=1):
    """path is a list of (x,y) tuples"""
    x0, y0 = path[0]
    for vertex in short_path[1:]:
        x1, y1 = vertex
        cv2.line(image, (y0, x0), (y1, x1), (255, 0, 0), thickness)
        x0, y0 = vertex


path = get_path((50, 400), (350, 390))
img = cv2.imread(file)
drawPath(img, path)
plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image on the screen
plt.show()

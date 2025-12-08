import numpy as np
import warnings
warnings.filterwarnings("error")

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    # boxes = {}
    # for l in lines:
    #     l = l.strip('\n')
    #     pos = eval(l)
    #     boxes[pos] = {'circuit': None, 'distances': {}}
    boxes = [eval(l.strip('\n')) for l in lines]

    return boxes

class Lights:
    def __init__(self):
        self.circuits = []

    def add_circuit(self, c):
        self.circuits.append(c)

    def update_distances(self):
        for i, c1 in enumerate(self.circuits):
            for c2 in self.circuits[i+1:]:

                d = c1.get_distance(c2)
                c1.distances[c2] = d
                c2.distances[c1] = d

    def connect_closest(self):
        smallest = np.inf
        smallest_cxn = None
        for c in self.circuits:
            smallest_key = min(c.distances, key=c.distances.get)
            if c.distances[smallest_key] < smallest:
                smallest_cxn = (c, smallest_key)
                smallest = c.distances[smallest_key]
        
        self.merge_circuits(smallest_cxn[0], smallest_cxn[1])
        print(f"Connected {smallest_cxn[0].boxes}")

    def merge_circuits(self, c1, c2):
        self.circuits.remove(c2)
        c1.boxes += c2.boxes
        c1.distances.pop(c2)
        for c in c1.distances:
            if c == c2:
                continue
            c1.distances[c] = min(c1.distances[c], c2.distances[c])
        
        for c in self.circuits:
            if c == c1:
                continue
            c.distances.pop(c2)
            c.distances[c1] = c1.distances[c]


class Circuit:
    def __init__(self, lights):
        self.lights = lights
        self.boxes = []
        self.distances = {}

    def size(self):
        return len(self.boxes)
    
    def add_box(self, pos):
        # Add box
        self.boxes.append(pos)

        # Update distances
        for c in self.lights.circuits:
            if c == self:
                continue

            smallest = np.inf
            for ob in c.boxes:
                d = np.sqrt((pos[0]-ob[0])**2 + (pos[1]-ob[1])**2 + (pos[2]-ob[2])**2)
                smallest = min(smallest, d)
            if c not in self.distances or smallest < self.distances[c]:
                self.distances[c] = smallest
                c.distances[self] = smallest

    def get_distance(self, circuit):
        smallest = np.inf
        for b in self.boxes:
            for ob in circuit.boxes:
                d = np.sqrt(np.sum([(b[i]-ob[i])**2 for i in range(3)]))
                smallest = min(smallest, d)
        return smallest
    
class Box:
    def __init__(self, pos, circuit, lights):
        self.lights = lights
        self.circuit = circuit
        self.pos = pos
        self.distances = {}
        self.connections = []

    def get_distance(self, b):
        # print(b.pos)
        return np.sqrt(np.sum([(b.pos[i] - self.pos[i])**2 for i in range(3)], dtype=np.int64))
    
    def connect(self, b):
        self.distances.pop(b)
        b.distances.pop(self)
        c = b.circuit
        if c != self.circuit:
            self.lights.circuits.remove(c)
            self.circuit.boxes += c.boxes
        self.connections.append(b)
        b.connections.append(self)
        for bc in c.boxes:
            bc.circuit = self.circuit

class SimpleCircuit:
    def __init__(self, lights):
        self.lights = lights
        self.boxes = []
    
    def add_box(self, box):
        self.boxes.append(box)

    def size(self):
        return len(self.boxes)

class SimpleLights:
    def __init__(self):
        self.boxes = []
        self.circuits = []

    def add_circuit(self, c):
        self.circuits.append(c)

    def add_box(self, b):
        self.boxes.append(b)

    def update_distances(self):
        for i, b1 in enumerate(self.boxes):
            for b2 in self.boxes[i+1:]:
                d = b1.get_distance(b2)
                b1.distances[b2] = d
                b2.distances[b1] = d

    def connect_closest(self):
        smallest = np.inf
        smallest_cxn = None
        for i, b1 in enumerate(self.boxes):
            for b2 in self.boxes[i+1:]:
                if b2 not in b1.distances:
                    continue
                if b1.distances[b2] < smallest:
                    smallest = b1.distances[b2]
                    smallest_cxn = (b1, b2)
        
        print(smallest_cxn[0].pos, '-', smallest_cxn[1].pos)
        smallest_cxn[0].connect(smallest_cxn[1])
    
    def connect_closest_circuit(self):
        smallest = np.inf
        smallest_cxn = None
        for i, c1 in enumerate(self.circuits):
            for c2 in self.circuits[i+1:]:
                for b1 in c1.boxes:
                    for b2 in c2.boxes:
                        if b1.distances[b2] < smallest:
                            smallest_cxn = (b1, b2)
                            smallest = b1.distances[b2]
        smallest_cxn[0].connect(smallest_cxn[1])
        print(smallest, smallest_cxn[0].pos, '-', smallest_cxn[1].pos)


    

boxes = parse_input('day8/input.txt')

l = SimpleLights()

for b in boxes:
    c = SimpleCircuit(lights=l)
    l.add_circuit(c)
    box = Box(b, c, l)
    c.add_box(box)
    l.add_box(box)

l.update_distances()

n = 10

# Part 1
for i in range(n):
    print(i)
    l.connect_closest()

circuits = sorted(l.circuits, key=lambda x: x.size(), reverse=True)
print(np.prod([c.size() for c in circuits[:3]]))

#Part 2
i=0
while len(l.circuits) > 1:
    print(i)
    l.connect_closest_circuit()
    i += 1
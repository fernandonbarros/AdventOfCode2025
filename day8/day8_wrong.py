import numpy as np

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
                print(f"Smallest - {b} to {ob}")
        return smallest

boxes = parse_input('day8/test.txt')

l = Lights()

for b in boxes:
    c = Circuit(lights=l)
    c.add_box(b)
    l.add_circuit(c)

l.update_distances()

i=0
while len(l.circuits) > 1:
    print(i)
    l.connect_closest()
    i+= 1
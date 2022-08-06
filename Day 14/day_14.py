import math

TEST_INPUT = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


class Reindeer:

    def __init__(self, speed, flight_time, rest_time):
        self.speed = speed
        self.flight_time = flight_time
        self.rest_time = rest_time
        self.distance_covered = 0

    def find_distance_covered(self, max_seconds):
        """
        * Use flight + rest time as a slice of time
        * Find out distance covered by counting number of time slices
        * The seconds remaining from number of time slices are then used to find the covered distance that
           is not calculated in the time slice

        Example: flight 1 sec, rest 5 sec, time slice = 6sec
        max seconds 13 sec
        2 time slices or 12 seconds have passed leaving only one second
        the remaining one second is flight time
        """
        distance_covered = 0
        total_seconds = self.flight_time + self.rest_time
        covered_seconds = int(max_seconds / total_seconds)
        remaining_seconds = max_seconds % total_seconds
        while remaining_seconds > 0:
            flight_time = min(remaining_seconds, self.flight_time)
            distance_covered += self.speed * flight_time
            remaining_seconds -= total_seconds
        return (self.speed * self.flight_time * covered_seconds) + distance_covered


def get_reindeers(data):
    reindeers = []
    for data_item in data.splitlines():
        data_list = data_item.split(' ')
        reindeer = Reindeer(int(data_list[3]), int(data_list[6]), int(data_list[-2]))
        reindeers.append(reindeer)
    return reindeers


def part_1(data, seconds):
    reindeers = get_reindeers(data)
    distances = []
    for reindeer in reindeers:
        distances.append(reindeer.find_distance_covered(seconds))
    return max(distances)


def part_2(data, seconds):
    reindeers = get_reindeers(data)
    points = [0] * len(reindeers)
    distances = []
    count = 1
    while count <= seconds:
        # Brute force, get distance on every second and find the occurrences of max distance on every second
        for reindeer in reindeers:
            distances.append(reindeer.find_distance_covered(count))
        max_distance = max(distances)
        max_indices = [idx for idx, distance in enumerate(distances) if distance == max_distance]
        for idx in max_indices:
            points[idx] += 1
        distances = []
        count += 1
    return max(points)


with open('input.in') as f:
    data = f.read()
    print("Part 1: {}".format(part_1(data, 2503)))
    print("Part 2: {}".format(part_2(data, 2503)))

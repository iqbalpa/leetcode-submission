class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        jarak_clockwise = 0
        jarak_counter = 0
        if start > destination:
            start, destination = destination, start
        for i in range(len(distance)):
            if i >= start and i < destination:
                jarak_clockwise += distance[i]
            else:
                jarak_counter += distance[i]
        return min(jarak_clockwise, jarak_counter)
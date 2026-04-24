class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0

        # Pair position and speed, then sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        fleets = 0
        prev_time = 0.0  # time of the last (front-most) fleet

        for pos, spd in cars:
            time = (target - pos) / spd  # time for this car to reach target

            # If this car takes longer, it cannot catch up to the fleet ahead -> new fleet
            if time > prev_time:
                fleets += 1
                prev_time = time
            # else: it joins the fleet ahead, so we ignore it

        return fleets
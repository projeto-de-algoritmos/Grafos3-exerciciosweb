class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        if total_tank >= 0:
            return start_station
        else:
            return -1

# Create an instance of the Solution class
solution = Solution()

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(gas, cost))  # Output: 3
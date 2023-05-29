def interval_partitioning(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    resources = [[sorted_intervals[0]]]

    for interval in sorted_intervals[1:]:
        earliest_end_time = float('inf')
        chosen_resource = None

        for resource in resources:
            last_interval_end_time = resource[-1][1]
            if interval[0] >= last_interval_end_time and last_interval_end_time < earliest_end_time:
                earliest_end_time = last_interval_end_time
                chosen_resource = resource

        if chosen_resource is None:
            resources.append([interval])
        else:
            chosen_resource.append(interval)

    return resources

intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
result = interval_partitioning(intervals)
for i, resource in enumerate(result):
    print(f"Recurso {i+1}: {resource}")
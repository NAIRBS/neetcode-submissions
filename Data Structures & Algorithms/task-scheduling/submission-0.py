class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        f_max = max(task_count.values()) # Freq of most frequent task
        n_max = list(task_count.values()).count(f_max) # How many tasks have max_freq
        ans = (f_max - 1) * (n + 1) + n_max
        return max(ans, len(tasks)) # When no idle time needed, return len(tasks)
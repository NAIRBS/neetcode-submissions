class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The core question is trying to find a cycle in the prerequisites, which renders invalid
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # Step 2: Track visit states
        # 0 = unvisited, 1 = visiting (in current path), 2 = visited (safe)
        visit_state = {}

        def dfs(course):
            # If visited and safe, return True
            if course in visit_state:
                return visit_state[course] == 2
            visit_state[course] = 1 # Mark as currently visiting
            for pre in pre_map[course]:
                if visit_state.get(pre) == 1: # If a prerequisite is currently being visited, we found a cycle!
                    return False
                if not dfs(pre): # Recursively check the prerequisite's prerequisites
                    return False
            visit_state[course] = 2 # Mark as fully visited and safe
            return True
        for c in range(numCourses): # Step 3: Run DFS for every course (handles disconnected components)
            if not dfs(c):
                return False
        return True
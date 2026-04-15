from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build adjacency list & in_degree array
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            # Example: [a, b] means b -> a
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        # 2. Initialize queue with courses having in_degree == 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 3. Process courses in the queue
        processed_count = 0
        while queue:
            curr = queue.popleft()
            processed_count += 1  # We can take this course
            
            # Reduce the in-degree of the courses that depend on 'curr'
            for next_course in adj_list[curr]:
                in_degree[next_course] -= 1
                # If no more prerequisites, add to queue
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # 4. Check if we processed all courses
        return processed_count == numCourses

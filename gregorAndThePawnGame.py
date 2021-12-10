class GFG:
    def __init__(self,graph,n):
        self.graph = graph
        self.ppl = n
        self.jobs = n
 
    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):
 
        # Try every job one by one
        for v in self.graph[u]:
 
            # If applicant u is interested
            # in job v and v is not seen
            if not seen[v]:
                 
                # Mark v as visited
                seen[v] = True
 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False
 
    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs
         
        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
             
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
             
            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result
 
for _ in range(int(input())):
    bpGraph = {}
    n = int(input())
    enemies = input()
    gregor = input()
    for x in range(n):
        bpGraph[x] = []
    if gregor[0] == '1':
        if enemies[0] == '0':
            bpGraph[0].append(0)
        if enemies[1] == '1':
            bpGraph[0].append(1)

    for x in range(1, n-1):
        if gregor[x] == '1':
            if enemies[x-1] == '1':
                bpGraph[x].append(x-1)
            if enemies[x] == '0':
                bpGraph[x].append(x)
            if enemies[x+1] == '1':
                bpGraph[x].append(x+1)
               
    if gregor[n-1] == '1':
        if enemies[n-1] == '0':
            bpGraph[n-1].append(n-1)
        if enemies[n-2] == '1':
            bpGraph[n-1].append(n-2)
 
    g = GFG(bpGraph, n)
    print(g.maxBPM())
#print ("Maximum number of applicants that can get job is %d " % g.maxBPM())
 
# This code is contributed by Neelam Yadav
        
            
            
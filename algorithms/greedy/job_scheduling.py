# Job scheduling algorithms manage how tasks, processes, or jobs are assigned to system
# resources or processors to optimize performance, fairness, or profit

# Exaplanation

# We are given a set of jobs,

# Each with:
# A unique ID (job name) 
# A deadline (latest time by which it must be completed)
# A profit (reward for completing it)

# We assume each job takes 1 unit of time

# The aim is to select and order jobs such that:

# No job is scheduled after its deadline.
# The total profit is maximum

# We will use a greedy algorithm approach

# Sort all jobs in descending order of profit
# Create an empty timeline (slots) for available time units.
# For each job (in sorted order):
# If a slot before its deadline is free -> schedule it there.
# Otherwise , skip the job


class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs: list[Job]):
    
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    schedule = [-1] * (max_deadline + 1)

    total_profit = 0
    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if schedule[t] == -1:
                schedule[t] = job.job_id
                total_profit += job.profit
                break
    result = [job_id for job_id in schedule if job_id != -1]
    return result, total_profit


# Example Usage

jobs = [
    Job("A", 2, 100),
    Job("B", 1, 19),
    Job("C", 2, 27),
    Job("D", 1, 25),
    Job("E", 3, 15),
]

scheduled_jobs, total_profit = job_scheduling(jobs)

print(f"Scheduled jobs : {scheduled_jobs}")
print(f"Total profit : {total_profit}")

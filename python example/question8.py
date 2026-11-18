import queue

task_queue = queue.Queue()

def worker():
    while not task_queue.empty():
        task = task_queue.get()
        print("Processing:", task)
        task_queue.task_done()

task_queue.put("Send Email")
task_queue.put("Generate Report")
task_queue.put("Send Notification")

worker()
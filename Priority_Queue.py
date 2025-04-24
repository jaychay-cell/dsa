def create_queue(size: int) -> dict:
    return {
        "data": [None] * size,  # list of elements
        "front": -1,  # index of the first element in the queue
        "rear": -1,  # index of the last element in the queue
        "n": 0,  # number of elements in the queue
        "size": size,  # size of the queue
    }

# Check if the queue is full
def is_full(queue: dict) -> bool:
    if queue["n"] == queue["size"]:
        return True
    return False


# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    if queue["n"] == 0:
        return True
    return False

# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    if not(is_full(queue)):
        if queue["n"] == 0:
            queue["front"] = 0
        queue["rear"] = (queue["rear"] + 1) % queue["size"]
        queue["data"][queue["rear"]] = item
        queue["n"] += 1


# Remove and return the element from the front of the queue
def dequeue(queue: dict):
    if not(is_empty(queue)):
        item = queue['data'][queue["front"]]
        queue["data"][queue["front"]] = None
        queue["front"] = (queue["front"] + 1) % queue["size"]
        queue["n"] -= 1
    if queue["n"]==0:
        queue["front"]=-1
        queue["rear"]=-1
    return item

# Return the element at the front of the queue without removing it
def peek(queue: dict):
    if not(is_empty(queue)):
        return queue["data"][queue["front"]]
    


# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    tuple = (item, priority)
    if not(is_full(priority_queue)):
        if is_empty(priority_queue):
            enqueue(priority_queue,tuple)
        else:
            minimum = min(peek_priority(priority_queue)[1],priority)
            if priority == minimum:            
                enqueue(priority_queue,tuple)
            else:
                insert = False
                count = 0
                while priority_queue["n"]!=count:
                    if peek_priority(priority_queue)[1]<= priority:
                        front = dequeue(priority_queue)
                        enqueue(priority_queue,front)
                        count+=1
                    else:
                        break
                if count == priority_queue["n"]:
                    enqueue(priority_queue,tuple)
                else:
                    enqueue(priority_queue,tuple)
                    insert = True 
            while peek_priority(priority_queue)[1] != minimum:
                front = dequeue(priority_queue)
                enqueue(priority_queue,front)

# Remove and return the element with the minimum priority from the priority queue
def dequeue_priority(priority_queue: dict):
    return dequeue(priority_queue)


# Return the element with the minimum priority from the priority queue without removing it
def peek_priority(priority_queue: dict):
    return peek(priority_queue)


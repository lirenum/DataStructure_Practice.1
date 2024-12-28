q = LWPriorityQueue()

test_in = []
#normal order, duplicate priorities/people
test_in.append([{'complete_time': 45, 'customer': 'AJ', 'priority': 4, 'task': 'belt'},
 {'complete_time': 45, 'customer': 'Stu', 'priority': 9, 'task': 'belt'},
 {'complete_time': 60, 'customer': 'Alex', 'priority': 12, 'task': 'wallet'},
 {'complete_time': 45, 'customer': 'Alex', 'priority': 12, 'task': 'belt'}])
#reverse order, duplicate priorities/people
test_in.append([ {'complete_time': 45, 'customer': 'Alex', 'priority': 12, 'task': 'belt'},
 {'complete_time': 60, 'customer': 'Alex', 'priority': 12, 'task': 'wallet'},
 {'complete_time': 45, 'customer': 'Stu', 'priority': 9, 'task': 'belt'},       {'complete_time': 45, 'customer': 'AJ', 'priority': 4, 'task': 'belt'}
])
#empty queue
test_in.append([])
#single item
test_in.append([{'complete_time': 45, 'customer': 'Stu', 'priority': 9, 'task': 'belt'}])
#two items, same priority
test_in.append([{'complete_time': 45, 'customer': 'Stu', 'priority': 9, 'task': 'belt'},
 {'complete_time': 45, 'customer': 'Steve', 'priority': 9, 'task': 'wallet'}])

test_out = []
test_out.append([{'complete_time': 45, 'customer': 'AJ', 'priority': 0, 'task': 'belt'},
 {'complete_time': 45, 'customer': 'Stu', 'priority': 1, 'task': 'belt'},
 {'complete_time': 60, 'customer': 'Alex', 'priority': 2, 'task': 'wallet'},
 {'complete_time': 45, 'customer': 'Alex', 'priority': 2, 'task': 'belt'}])
test_out.append([{'complete_time': 45, 'customer': 'Alex', 'priority': 2, 'task': 'belt'},
 {'complete_time': 60, 'customer': 'Alex', 'priority': 2, 'task': 'wallet'},
 {'complete_time': 45, 'customer': 'Stu', 'priority': 1, 'task': 'belt'},
 {'complete_time': 45, 'customer': 'AJ', 'priority': 0, 'task': 'belt'}])
test_out.append([])
test_out.append([{'complete_time': 45, 'customer': 'Stu', 'priority': 0, 'task': 'belt'}])
test_out.append([{'complete_time': 45, 'customer': 'Stu', 'priority': 0, 'task': 'belt'},
 {'complete_time': 45, 'customer': 'Steve', 'priority': 0, 'task': 'wallet'}])
for i in range(len(test_in)):
    print('Test',i+1,end=": ")
    q.items = test_in[i]
    q.compact()
    if (q.items == test_out[i]):
        print("Passed")
    else:
        print("Failed")
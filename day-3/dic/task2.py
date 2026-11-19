student=[{"name":"Riya","marks":88},
         {"name":"aman","marks":95},
         {"name":"tanu","marks":77},
        {"name":"sara","marks":98}
         ]
highest=student[0]
for i in student:
    if i['marks']>highest['marks']:
        highest=i
        print("highest student:",highest)
    
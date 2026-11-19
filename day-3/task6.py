no=[20,30,40,50,60,70]
large=no[0]
second=None
for n in no:
    if n>large:
        second=large
        large=n
    elif second  is None or n>second:
        second=n
        print("Maximum value:",large)
        print("second maximum value:",second)  
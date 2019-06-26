def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([34, 76, 98, 54, 35])
drop_first_last([34, 76, 98, 54, 35, 34, 54,24]) 
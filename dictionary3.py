#to sort (ascending and descending) a dictionary by value.
#to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
import operator
data={
    "one":1,
    "four":4,
    "three":3,
    "two":2
}
asc_data=dict(sorted(data.items(),key=operator.itemgetter(1)))
desc_data=dict(sorted(data.items(),key=operator.itemgetter(1),reverse=True))
print(data)
print(asc_data)
print(desc_data)

import matplotlib.pyplot as plt
from collections import Counter

data = [5, 7, 9, 5, 6, 8, 9, 7, 5]


mean = sum(data) / len(data)


sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]



data_counts = Counter(data)
mode = max(data_counts, key=data_counts.get)




plt.hist(data, bins=5, color='blue', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

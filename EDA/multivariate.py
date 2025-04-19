import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [40000, 50000, 60000, 80000, 100000],
    'Experience': [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)


correlation_matrix = df.corr()


sns.pairplot(df)
plt.show()


sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()


print("Dataset:")
print(df)
print("\nCorrelation Matrix:")
print(correlation_matrix)

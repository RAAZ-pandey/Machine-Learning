import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]  
y = [2, 4, 5, 4, 5]  


mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)





plt.scatter(x, y, color='blue', label='Data points')
plt.title('Scatter Plot of X vs Y')
plt.xlabel('X (Independent Variable)')
plt.ylabel('Y (Dependent Variable)')
plt.legend()
plt.show()


print("Mean of X:", mean_x)
print("Mean of Y:", mean_y)


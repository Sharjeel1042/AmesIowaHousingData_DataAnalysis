from main import df_cleaned
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,3))
sns.kdeplot(data=df_cleaned,x='saleprice')

plt.xlabel("Sale Price")

plt.savefig('KDE_SalePrice.png')
plt.show()
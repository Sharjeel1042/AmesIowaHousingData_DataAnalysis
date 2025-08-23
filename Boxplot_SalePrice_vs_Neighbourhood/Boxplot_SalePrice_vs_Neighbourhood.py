from main import df_cleaned
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(8,4))
sns.boxplot(data=df_cleaned,x='saleprice',y='neighborhood')
plt.ylabel('Neighbourhood')
plt.xlabel('Sale Price')
plt.savefig('Boxplot_SalePrice_vs_Neighbourhood.png')
plt.show()
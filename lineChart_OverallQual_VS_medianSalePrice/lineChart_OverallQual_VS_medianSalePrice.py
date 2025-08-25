from main import df_cleaned
import pandas as pd
import matplotlib.pyplot as plt

grp=df_cleaned.groupby('overall qual')['saleprice'].median()

plt.figure(figsize=(10,5))
plt.plot(grp.index,grp.values,color='purple',marker='x',markeredgecolor='black',markersize=7,markeredgewidth=2.5)
plt.title('Overall Quality vs Median Sale Price')
plt.xlabel('Overall Quality',fontdict={'size':12})
plt.ylabel('Median Sale Price',fontdict={'size':12})
plt.savefig('lineChart_OverallQual_VS_medianSalePrice.png')
plt.show()
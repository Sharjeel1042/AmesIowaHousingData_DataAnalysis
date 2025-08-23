from main import df_cleaned
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_cleaned['log_saleprice']=np.log(df_cleaned['saleprice'])
plt.subplot(1,2,1)
sns.histplot(data=df_cleaned,x='saleprice',kde=True,bins=25)

plt.subplot(1,2,2)
sns.histplot(data=df_cleaned,x='log_saleprice',kde=True,bins=25)
plt.savefig('SalePrice_Histogram_VS_KDE.png')
plt.show()
from main import df_cleaned
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

plt.figure(figsize=(14,7))
#result=stats.linregress(df_cleaned['gr liv area'],df_cleaned['saleprice'])
#plt.scatter(df_cleaned['gr liv area'],df_cleaned['saleprice'])
#plt.plot(df_cleaned['gr liv area'],result.slope*df_cleaned['gr liv area']+result.intercept)
sns.regplot(data=df_cleaned,x='gr liv area',y='saleprice')
plt.savefig('Reg_GrLiveArea_VS_SalePrice')
plt.show()
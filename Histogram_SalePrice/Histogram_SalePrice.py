from main import df_cleaned
import matplotlib.pyplot as plt
import seaborn as sns



plt.figure(figsize=(12,3),dpi=100)
ax=sns.histplot(data=df_cleaned,x='saleprice',bins=40)
for patch in ax.patches:
    height=patch.get_height()
    ax.text(
        patch.get_x()+patch.get_width()/2,
        height,
        int(height),
        ha='center',
        va='bottom'
    )

plt.savefig('Histogram_SalePrice.png')
plt.show()

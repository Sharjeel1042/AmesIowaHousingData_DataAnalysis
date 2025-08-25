from main import df_cleaned
import matplotlib.pyplot as plt
import pandas as pd


grp=df_cleaned.groupby('neighborhood')['saleprice'].mean()
plt.figure(figsize=(15,5))
bars=plt.bar(grp.index,grp.values,color='purple')
plt.xticks(fontsize=6)
plt.title('Average Sale Price vs Neighborhood',fontdict={'family':'DejaVu Sans'})
plt.xlabel('Neighborhood',fontdict={'family':'Georgia','size':15})
plt.ylabel('Average Sale Price/$',fontdict={'family':'Georgia','size':15})

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height():.0f}',
        ha='center',
        va='bottom',
        fontsize=7

    )
plt.savefig('barChart_Neighborhood_VS_salePrice')
plt.show()

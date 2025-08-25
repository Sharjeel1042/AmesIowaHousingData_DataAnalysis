from main import df_cleaned
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(18,6))
ax=sns.countplot(data=df_cleaned,x='neighborhood',hue='neighborhood',palette='viridis')
plt.xticks(fontsize=6)
plt.title('Neighborhood House Count')
plt.ylabel('Count')
plt.xlabel('Neighborhood')
for patch in ax.patches:
    height=patch.get_height()
    ax.text(
        patch.get_x()+patch.get_width()/2,
        height,
        int(height),
        ha='center',
        va='bottom'
    )
plt.savefig('CountPlot_Neighborhood.png')
plt.show()
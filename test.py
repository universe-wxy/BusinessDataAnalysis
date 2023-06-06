import matplotlib.pyplot as plt
import pandas as pd

# 创建数据
data = {
    'Treatment': ['T1', 'T2', 'T3', 'T4'],
    'Group1': [0.25, 0.30, 0.28, 0.32],
    'Group2': [0.40, 0.35, 0.38, 0.42],
    'Group3': [0.60, 0.55, 0.58, 0.62]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 绘制表格图形
fig, ax = plt.subplots()
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colWidths=[0.15] * len(df.columns))

# 设置表格样式
table = ax.tables[0]
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 1.2)

# 显示图形
plt.show()

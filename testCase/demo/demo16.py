from matplotlib import pyplot as plt
import numpy as np
# 3D绘图必须的模块
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
n_girds = 51        # x-y平面的隔点数
nf = 2              # 低频成分的个数
c = n_girds/2       # 中心位置

# 生成隔点
x = np.linspace(0, 1, n_girds)
y = np.linspace(0, 1, n_girds)

# x, y是长度为n_girds的array
# meshgrid会把x, y组成n_girds*n_girds的array，X, Y对应的位置就是每个格点的位置
X, Y = np.meshgrid(x, y)

# 生成一个0值的傅里叶增
spectrum = np.zeros((n_girds, n_girds), dtype=np.complex)

# 生成一段噪音,长度是n*
noise = [np.complex(x, y) for x,y in np.random.uniform(-1, 1, ((2*nf+1)**2/2, 2))]

# 傅里叶级数的每一项和其共轭关于中心对称
noisy_block = np.concatenate((noise, [0j], np.conjugate(noise[::-1])))

# 将生成的频谱作为低频部分
spectrum[c-nf:c+nf+1, c-nf:c+nf+1] = noisy_block.reshape((2*nf+1, 2*nf+1))

# 进行反傅里叶变换
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))

# 创建图表
fig = plt.figure('3D surface & write')

# 第一个子图, suface图
ax = fig.add_subplot(1, 2, 1, projection='3d')

# alpha定义透明度, cmap是color map
# rstride和cstride是两个方向上的采样, 约小越精细, lw是线宽
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)

# 第二个子图，网线图
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)

# plt.show()
plt.savefig('F:\\3d-1.png')

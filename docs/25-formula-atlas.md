# LaTeX 公式图鉴

> 本页把高频关系从宽表格中抽出，统一使用可渲染的 LaTeX 展示。公式不是“看到外形就套”，每组都附有适用条件和检查项。

!!! note "符号约定"
    连续系统默认采用单边拉氏变换和零初始条件推导传递函数；负反馈默认特征方程为 $1+G(s)H(s)=0$。时间指标、相角和稳定裕度如采用不同教材定义，应先在题面旁写明。

## C1 反馈结构

### F-C1-01 误差信号

\[
e(t)=r(t)-b(t)
\]

### F-C1-02 负反馈闭环传递函数

\[
\Phi(s)=\frac{C(s)}{R(s)}=\frac{G(s)}{1+G(s)H(s)}
\]

### F-C1-03 灵敏度与互补灵敏度

\[
S(s)=\frac{1}{1+L(s)},\qquad T(s)=\frac{L(s)}{1+L(s)},\qquad S(s)+T(s)=1
\]

其中 $L(s)=G(s)H(s)$。该组关系用于统一解释参考跟踪、模型扰动与测量噪声通道。

## C2 动态数学模型

### F-C2-01 平动机械系统

\[
M\ddot x(t)+D\dot x(t)+kx(t)=f(t)
\]

### F-C2-02 转动机械系统

\[
J\ddot\theta(t)+D\dot\theta(t)+k\theta(t)=T(t)
\]

### F-C2-03 线性化的一阶泰勒式

\[
\Delta y\approx\sum_{i=1}^{n}
\left.\frac{\partial f}{\partial x_i}\right|_{0}\Delta x_i
\]

只在选定工作点邻域内有效；工作点应先满足静态平衡。

### F-C2-04 导数的单边拉氏变换

\[
\mathcal L\{\dot x(t)\}=sX(s)-x(0^-)
\]

\[
\mathcal L\{\ddot x(t)\}=s^2X(s)-sx(0^-)-\dot x(0^-)
\]

### F-C2-05 延迟定理

\[
f(t-a)u(t-a)\ \xleftrightarrow{\mathcal L}\ e^{-as}F(s)
\]

### F-C2-06 周期函数的拉氏变换

\[
F(s)=\frac{\displaystyle\int_0^T f(t)e^{-st}\,dt}{1-e^{-sT}}
\]

### F-C2-07 卷积

\[
(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau
\]

\[
\mathcal L\{f*g\}=F(s)G(s)
\]

### F-C2-08 传递函数定义

\[
G(s)=\left.\frac{Y(s)}{U(s)}\right|_{\text{零初始条件}}
\]

### F-C2-09 一阶惯性环节

\[
G(s)=\frac{K}{Ts+1}
\]

### F-C2-10 标准二阶振荡环节

\[
G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}
\]

### F-C2-11 梅逊公式

\[
P=\frac{1}{\Delta}\sum_{k=1}^{m}P_k\Delta_k
\]

\[
\Delta=1-\sum_iL_i+\sum_{i<j}L_iL_j-\sum_{i<j<k}L_iL_jL_k+\cdots
\]

只有互不接触回路的乘积才能进入高阶项。

### F-C2-12 状态空间模型

\[
\dot x=Ax+Bu,\qquad y=Cx+Du
\]

### F-C2-13 状态空间到传递函数

\[
G(s)=C(sI-A)^{-1}B+D
\]

### F-C2-14 多自由度机械系统

\[
\bigl(Ms^2+Ds+K\bigr)X(s)=F(s)
\]

## C3 时域瞬态响应

### F-C3-01 一阶单位阶跃响应

\[
y(t)=K\left(1-e^{-t/T}\right)u(t)
\]

### F-C3-02 一阶系统关键时刻

\[
y(T)=0.632K,\qquad t_s\approx3T\ (5\%),\qquad t_s\approx4T\ (2\%)
\]

### F-C3-03 欠阻尼二阶单位阶跃响应

\[
y(t)=1-\frac{e^{-\zeta\omega_nt}}{\sqrt{1-\zeta^2}}
\sin\!\left(\omega_dt+\arccos\zeta\right)
\]

\[
\omega_d=\omega_n\sqrt{1-\zeta^2}
\]

### F-C3-04 最大超调量

\[
M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}
\]

若写成百分数，应再乘 $100\%$。

### F-C3-05 峰值时间

\[
t_p=\frac{\pi}{\omega_n\sqrt{1-\zeta^2}}
\]

### F-C3-06 上升时间（教材 0—100% 首次到达定义）

\[
t_r=\frac{\pi-\arccos\zeta}{\omega_n\sqrt{1-\zeta^2}}
\]

### F-C3-07 调整时间近似

\[
t_s\approx\frac{3}{\zeta\omega_n}\quad(5\%)
\]

\[
t_s\approx\frac{4}{\zeta\omega_n}\quad(2\%)
\]

### F-C3-08 初值与终值定理

\[
x(0^+)=\lim_{s\to\infty}sX(s)
\]

\[
x(\infty)=\lim_{s\to0}sX(s)
\]

终值定理要求 $sX(s)$ 的全部极点位于左半平面，允许原点处至多有按定理消去后的情形。

### F-C3-09 高阶模态展开

\[
y(t)=y(\infty)+\sum_i r_i e^{p_it}
\]

极点 $p_i$ 决定模态，留数 $r_i$ 决定该模态在指定输入输出通道中的权重。

## C4 频率特性

### F-C4-01 频率响应

\[
G(j\omega)=U(\omega)+jV(\omega)=A(\omega)e^{j\varphi(\omega)}
\]

### F-C4-02 模与相角

\[
A(\omega)=\sqrt{U^2+V^2},\qquad
\varphi(\omega)=\operatorname{atan2}(V,U)
\]

### F-C4-03 正弦稳态输出

\[
u(t)=A_u\cos(\omega t+\phi_u)
\]

\[
y_{ss}(t)=A_u|G(j\omega)|
\cos\!\left[\omega t+\phi_u+\angle G(j\omega)\right]
\]

### F-C4-04 分贝

\[
L(\omega)=20\log_{10}|G(j\omega)|
\]

### F-C4-05 一阶零点和极点的 Bode 贡献

\[
1+j\omega T:
\quad 20\log_{10}\sqrt{1+(\omega T)^2},\quad
+\arctan(\omega T)
\]

\[
\frac{1}{1+j\omega T}:
\quad -20\log_{10}\sqrt{1+(\omega T)^2},\quad
-\arctan(\omega T)
\]

### F-C4-06 二阶环节的幅相

\[
\left|\frac{1}{1-(\omega/\omega_n)^2+j2\zeta(\omega/\omega_n)}\right|
=\frac{1}{\sqrt{[1-(\omega/\omega_n)^2]^2+[2\zeta\omega/\omega_n]^2}}
\]

### F-C4-07 二阶闭环谐振峰

\[
M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}},
\qquad 0<\zeta<\frac{1}{\sqrt2}
\]

### F-C4-08 谐振频率

\[
\omega_r=\omega_n\sqrt{1-2\zeta^2}
\]

### F-C4-09 闭环带宽方程

\[
|\Phi(j\omega_b)|=\frac{|\Phi(0)|}{\sqrt2}
\]

### F-C4-10 单位脉冲响应与频率特性

\[
G(j\omega)=\int_0^\infty g(t)e^{-j\omega t}\,dt
\]

## C5 稳定性

### F-C5-01 闭环特征方程

\[
1+G(s)H(s)=0
\]

### F-C5-02 三阶 Routh 简化条件

对

\[
s^3+a_2s^2+a_1s+a_0=0
\]

渐近稳定要求

\[
a_2>0,\quad a_1>0,\quad a_0>0,\quad a_2a_1>a_0
\]

### F-C5-03 极点区域平移

若要求全部极点满足 $\Re(s)<-\alpha$，令

\[
s=z-\alpha
\]

再对关于 $z$ 的多项式做 Routh 判定。

### F-C5-04 Nyquist 判据

采用本项目约定的轮廓方向时

\[
Z=P-N
\]

其中 $P$ 为开环右半平面极点数，$N$ 为对 $-1+j0$ 的净顺时针环绕数，$Z$ 为闭环右半平面极点数。使用其他方向约定时必须同步改变符号。

### F-C5-05 相角裕度

\[
\gamma=180^\circ+\angle L(j\omega_c),
\qquad |L(j\omega_c)|=1
\]

### F-C5-06 增益裕度

\[
K_g=\frac{1}{|L(j\omega_g)|},
\qquad \angle L(j\omega_g)=-180^\circ
\]

### F-C5-07 纯延迟的频率特性

\[
e^{-\tau s}\big|_{s=j\omega}=e^{-j\omega\tau},
\qquad |e^{-j\omega\tau}|=1,
\qquad \angle=-\omega\tau
\]

## C6 误差分析

### F-C6-01 误差传递函数

单位负反馈时

\[
\Phi_e(s)=\frac{E(s)}{R(s)}=\frac{1}{1+G(s)H(s)}
\]

### F-C6-02 位置、速度、加速度误差系数

\[
K_p=\lim_{s\to0}G(s)H(s)
\]

\[
K_v=\lim_{s\to0}sG(s)H(s)
\]

\[
K_a=\lim_{s\to0}s^2G(s)H(s)
\]

### F-C6-03 典型输入稳态误差

\[
e_{ss,\text{step}}=\frac{A}{1+K_p}
\]

\[
e_{ss,\text{ramp}}=\frac{v}{K_v}
\]

\[
e_{ss,\text{parabolic}}=\frac{a}{K_a}
\]

以上均要求闭环稳定，并按输入的标准定义解释 $A,v,a$。

### F-C6-04 动态误差系数

\[
\Phi_e(s)=C_0+C_1s+C_2s^2+\cdots
\]

\[
e(t)\approx C_0r(t)+C_1\dot r(t)+C_2\ddot r(t)+\cdots
\]

## C7 综合与校正

### F-C7-01 一阶超前校正器

\[
G_c(s)=K_c\frac{Ts+1}{\alpha Ts+1},
\qquad 0<\alpha<1
\]

### F-C7-02 最大超前角

\[
\sin\phi_m=\frac{1-\alpha}{1+\alpha}
\]

### F-C7-03 最大超前角对应频率

\[
\omega_m=\frac{1}{T\sqrt\alpha}
\]

### F-C7-04 一阶滞后校正器

\[
G_c(s)=K_c\frac{Ts+1}{\beta Ts+1},
\qquad \beta>1
\]

### F-C7-05 PID 控制器

\[
G_c(s)=K_P+\frac{K_I}{s}+K_Ds
\]

### F-C7-06 设计闭环检查集合

\[
\{\text{极点},\ M_p,\ t_s,\ e_{ss},\ \omega_c,\ \gamma,\ K_g,\ u_{\max}\}
\]

任何校正结果至少应覆盖稳定性、时域、稳态误差和频域四类指标。

## C8 根轨迹

### F-C8-01 根轨迹方程

\[
1+KG_0(s)H(s)=0
\]

### F-C8-02 相角条件

\[
\sum_i\angle(s-z_i)-\sum_j\angle(s-p_j)=(2k+1)180^\circ
\]

### F-C8-03 幅值条件

\[
K=\frac{\prod_j|s-p_j|}{\prod_i|s-z_i|}
\]

### F-C8-04 渐近线重心

\[
\sigma_a=\frac{\sum_jp_j-\sum_i z_i}{n-m}
\]

### F-C8-05 渐近线角度

\[
\theta_q=\frac{(2q+1)180^\circ}{n-m},
\qquad q=0,1,\ldots,n-m-1
\]

### F-C8-06 分离/会合点

\[
\frac{dK(s)}{ds}=0
\]

候选点还必须满足实轴根轨迹段、相角条件和正增益条件。

### F-C8-07 等阻尼线

\[
\zeta=-\frac{\Re(s)}{|s|}
\]

## C9 非线性问题

### F-C9-01 描述函数

对输入 $x(t)=A\sin\omega t$，输出基波写成

\[
y_1(t)=a_1\cos\omega t+b_1\sin\omega t
\]

则

\[
N(A)=\frac{b_1+ja_1}{A}
\]

符号应与教材采用的正弦/余弦约定保持一致。

### F-C9-02 极限环近似条件

\[
G(j\omega)N(A)=-1
\]

等价于寻找 $G(j\omega)$ 与 $-1/N(A)$ 的交点。

### F-C9-03 相轨迹微分方程

若

\[
\dot x_1=f_1(x_1,x_2),\qquad
\dot x_2=f_2(x_1,x_2)
\]

则在 $f_1\ne0$ 区域

\[
\frac{dx_2}{dx_1}=\frac{f_2(x_1,x_2)}{f_1(x_1,x_2)}
\]

### F-C9-04 Lyapunov 条件

\[
V(x)>0\quad(x\ne0),\qquad
\dot V(x)=\nabla V^\mathsf T f(x)<0
\]

可推出原点渐近稳定。若仅有 $\dot V\le0$，还需额外条件。

## C10 计算机控制系统

### F-C10-01 采样角频率与周期

\[
\omega_s=\frac{2\pi}{T}
\]

### F-C10-02 零阶保持器

\[
G_h(s)=\frac{1-e^{-sT}}{s}
\]

其相位在低于奈奎斯特频率的常用近似为

\[
\angle G_h(j\omega)\approx-\frac{\omega T}{2}
\]

### F-C10-03 Z 变换

\[
X(z)=\sum_{k=0}^{\infty}x(kT)z^{-k}
\]

### F-C10-04 离散初值与终值定理

\[
x(0)=\lim_{z\to\infty}X(z)
\]

\[
x(\infty)=\lim_{z\to1}(z-1)X(z)
\]

终值定理需检查 $(z-1)X(z)$ 的极点。

### F-C10-05 ZOH 等效脉冲传递函数

\[
G(z)=(1-z^{-1})\mathcal Z\left\{\frac{G_p(s)}{s}\right\}
\]

### F-C10-06 离散状态空间

\[
x_{k+1}=Ax_k+Bu_k,\qquad y_k=Cx_k+Du_k
\]

### F-C10-07 离散状态空间到脉冲传递函数

\[
G(z)=C(zI-A)^{-1}B+D
\]

### F-C10-08 连续极点到离散极点

\[
z=e^{sT}
\]

\[
\Re(s)<0\Longleftrightarrow |z|<1
\]

### F-C10-09 双线性变换

\[
s=\frac{2}{T}\frac{z-1}{z+1}
\]

双线性变换把左半平面一一映到单位圆内，但会产生频率畸变。

## 使用建议

1. 先在本页看**显示公式**，再回到[规则与公式卡](14-formula-cards.md)检查触发条件和失效边界。
2. 每道习题的关键公式已经放入[逐题解析](exercises/index.md)，不要孤立背诵。
3. 网站若仍显示原始美元符号，先强制刷新；项目已通过 MathJax 加载和 Arithmatex 转换渲染公式。

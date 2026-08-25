# 习题反哺补充库

> 这页不是答案汇总，而是把 193 道题中反复出现、正文节点尚未充分展开的结论重新抽象为可迁移知识。每条均链接到对应逐题解析。

## C1 概论

### S-C1-01 闭环判据不是“装了传感器”

输出信息必须返回比较环节，并实际改变后续控制作用，才形成闭环。见 [1-1](exercises/01-introduction.md#ex-c1-01) 与 [1-4](exercises/01-introduction.md#ex-c1-04)。

### S-C1-02 设备名称与功能角色不是一一对应

同一电机可能被划入执行元件，也可能被并入被控对象；分类取决于所选系统边界。见 [1-3](exercises/01-introduction.md#ex-c1-03)。

### S-C1-03 反馈的收益与代价必须成对回答

反馈通常改善低频精度和抗扰，却可能增加结构复杂性、噪声通道和失稳风险。见 [1-2](exercises/01-introduction.md#ex-c1-02)。

## C2 动态数学模型

### S-C2-01 分段信号优先写成阶跃、斜坡的叠加

折线信号可按“初始斜率 + 每次斜率变化 × 延迟斜坡”表示，矩形窗可写成开启阶跃减关闭阶跃。见 [2-4](exercises/02-dynamic-models.md#ex-c2-04)、[2-22](exercises/02-dynamic-models.md#ex-c2-22)。

### S-C2-02 传递函数不承载初始条件

\[
G(s)=\left.\frac{Y(s)}{U(s)}\right|_{x(0^-)=0}
\]

非零初值应作为响应计算中的附加项处理。见 [2-3](exercises/02-dynamic-models.md#ex-c2-03)。

### S-C2-03 多自由度系统的统一表示

\[
\bigl(Ms^2+Ds+K\bigr)X(s)=F(s)
\]

所有输入输出传递函数共享动态刚度矩阵行列式作为分母。见 [2-18](exercises/02-dynamic-models.md#ex-c2-18)、[2-19](exercises/02-dynamic-models.md#ex-c2-19)、[2-21](exercises/02-dynamic-models.md#ex-c2-21)。

### S-C2-04 同一闭环的不同通道共享特征分母

参考、扰动、噪声和内部节点通道分子不同，但内部闭环动态由共同特征方程决定。见 [2-7](exercises/02-dynamic-models.md#ex-c2-07)、[2-15](exercises/02-dynamic-models.md#ex-c2-15)。

### S-C2-05 理想运放模型有隐含工作条件

“虚短、虚断”要求运放处于负反馈线性工作区；输出饱和后该模型失效。见 [2-11](exercises/02-dynamic-models.md#ex-c2-11)。

## C3 时域瞬态响应

### S-C3-01 切换系统要继承状态，不是重新零初始

一阶系统继承当前输出；二阶系统通常同时继承位移和速度。见 [3-3](exercises/03-time-response.md#ex-c3-03)、[3-4](exercises/03-time-response.md#ex-c3-04)、[3-13](exercises/03-time-response.md#ex-c3-13)。

### S-C3-02 极点决定模态，零点决定留数

相同闭环极点并不保证相同峰值、初始斜率和波形。见 [3-10](exercises/03-time-response.md#ex-c3-10)、[3-22](exercises/03-time-response.md#ex-c3-22)。

### S-C3-03 指标公式必须先按阻尼类型分区

\[
M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}
\]

只适用于 $0<\zeta<1$。临界、过阻尼和无阻尼情形应分别处理。见 [3-7](exercises/03-time-response.md#ex-c3-07)、[3-8](exercises/03-time-response.md#ex-c3-08)。

### S-C3-04 调整时间必须注明误差带

\[
t_s\approx\frac{3}{\zeta\omega_n}\quad(5\%),
\qquad
 t_s\approx\frac{4}{\zeta\omega_n}\quad(2\%)
\]

见 [3-9](exercises/03-time-response.md#ex-c3-09)、[3-17](exercises/03-time-response.md#ex-c3-17)。

### S-C3-05 主导极点还需检查零点和留数

“最靠近虚轴”只是候选条件；近邻零点和很小留数都可能破坏简单二阶近似。见 [3-24](exercises/03-time-response.md#ex-c3-24)。

## C4 频率特性

### S-C4-01 0 dB 表示幅值比 1

\[
20\log_{10}1=0\ \mathrm{dB}
\]

它不表示输出为零。见 [4-1](exercises/04-frequency-response.md#ex-c4-01)。

### S-C4-02 最小相位假设决定能否由幅值反推模型

仅凭 Bode 幅值图通常不能区分左、右半平面零点，也不能识别纯延迟；题目明确最小相位后才可唯一按斜率反推。见 [4-6](exercises/04-frequency-response.md#ex-c4-06)、[4-21](exercises/04-frequency-response.md#ex-c4-21)。

### S-C4-03 Nyquist 手绘的四个锚点

先确定低频起点、高频终点、坐标轴交点和频率方向，再连接曲线。见 [4-9](exercises/04-frequency-response.md#ex-c4-09)、[4-15](exercises/04-frequency-response.md#ex-c4-15)。

### S-C4-04 闭环带宽不等于开环交叉频率

开环交叉频率与闭环带宽常相关，但严格带宽由

\[
|\Phi(j\omega_b)|=\frac{|\Phi(0)|}{\sqrt2}
\]

定义。见 [4-14](exercises/04-frequency-response.md#ex-c4-14)。

### S-C4-05 时间延迟与单频相位差

\[
\varphi=-\omega t_0
\]

该换算只对指定单一频率成立。见 [2-20](exercises/02-dynamic-models.md#ex-c2-20)。

## C5 稳定性

### S-C5-01 “系数全正”只是高阶稳定的必要条件

三阶及更高阶还需 Routh/Hurwitz 条件。见 [5-4](exercises/05-stability.md#ex-c5-04)、[5-17](exercises/05-stability.md#ex-c5-17)。

### S-C5-02 Routh 首列变号数就是右半平面根数

这使 Routh 不仅能判稳定，还能定量给出不稳定根数。见 [5-2](exercises/05-stability.md#ex-c5-02)、[5-5](exercises/05-stability.md#ex-c5-05)。

### S-C5-03 指定稳定区域可通过变量平移

要求 $\Re(s)<-\alpha$ 时令

\[
s=z-\alpha
\]

再判断 $z$ 多项式的左半平面稳定性。见 [5-11](exercises/05-stability.md#ex-c5-11)、[5-12](exercises/05-stability.md#ex-c5-12)。

### S-C5-04 纯延迟只改相位，不改幅值

\[
e^{-j\omega\tau}:\quad |\cdot|=1,\qquad \angle=-\omega\tau
\]

见 [5-3](exercises/05-stability.md#ex-c5-03)。

### S-C5-05 小时间常数能否忽略取决于闭环时间尺度

参数“数值小”不是充分条件，应比较它与带宽、主导时间常数和环路增益的组合。见 [5-26](exercises/05-stability.md#ex-c5-26)。

## C6 误差分析

### S-C6-01 稳态误差计算前必须先判闭环稳定

不稳定系统没有题目所称的有限稳态误差，终值定理也失效。见 [6-10](exercises/06-error-analysis.md#ex-c6-10)。

### S-C6-02 系统型别由开环原点极点数决定

不是由闭环极点数，也不是由输入次数决定。见 [6-1](exercises/06-error-analysis.md#ex-c6-01)。

### S-C6-03 扰动误差必须按注入点单独推导

令参考输入为零，从扰动源到误差信号建立传递函数，不能照搬参考输入的误差系数。见 [6-4](exercises/06-error-analysis.md#ex-c6-04)、[6-14](exercises/06-error-analysis.md#ex-c6-14)。

### S-C6-04 测速反馈不增加系统型别

它常改善阻尼，却可能增大位置跟踪斜坡误差。见 [6-8](exercises/06-error-analysis.md#ex-c6-08)、[6-15](exercises/06-error-analysis.md#ex-c6-15)。

### S-C6-05 动态误差系数是低频渐近式

它适用于缓变输入，不是对任意高速信号都精确成立。见 [6-2](exercises/06-error-analysis.md#ex-c6-02)、[6-5](exercises/06-error-analysis.md#ex-c6-05)。

## C7 综合与校正

### S-C7-01 校正后必须重新寻找交叉频率

串联网络改变幅值，因而“在原交叉频率补多少相位”只是一阶估计。见 [7-1](exercises/07-design-compensation.md#ex-c7-01)、[7-3](exercises/07-design-compensation.md#ex-c7-03)。

### S-C7-02 滞后与超前的分工

- 滞后：提高低频相对增益，主要改善稳态精度；
- 超前：在中频提供正相位，主要提高稳定裕度和速度。

见 [7-6](exercises/07-design-compensation.md#ex-c7-06)、[7-12](exercises/07-design-compensation.md#ex-c7-12)。

### S-C7-03 超前峰值频率应靠近新交叉频率

\[
\omega_m=\frac{1}{T\sqrt\alpha}
\]

见 [7-11](exercises/07-design-compensation.md#ex-c7-11)、[7-15](exercises/07-design-compensation.md#ex-c7-15)。

### S-C7-04 高频极点“很远”也应估算相位损失

至少计算它在交叉频率处的 $-\arctan(\omega_cT)$。见 [7-9](exercises/07-design-compensation.md#ex-c7-09)。

### S-C7-05 极点配置不是设计终点

PID 通过系数比较满足特征根要求后，还要检查闭环零点、控制量、噪声和鲁棒性。见 [7-20](exercises/07-design-compensation.md#ex-c7-20)。

## C8 根轨迹

### S-C8-01 分离点候选要经过三次筛选

\[
\frac{dK}{ds}=0
\]

只生成候选；还需位于实轴根轨迹段、满足相角条件且对应 $K>0$。见 [8-3](exercises/08-root-locus.md#ex-c8-03)。

### S-C8-02 参数根轨迹先分离参数

把特征式写成

\[
A(s)+\lambda B(s)=0
\]

才能把 $\lambda$ 当作根轨迹增益。见 [8-7](exercises/08-root-locus.md#ex-c8-07)、[8-8](exercises/08-root-locus.md#ex-c8-08)。

### S-C8-03 等阻尼线只确定几何交点

增益必须继续由幅值条件求：

\[
K=\frac{\prod|s-p_i|}{\prod|s-z_i|}
\]

见 [8-6](exercises/08-root-locus.md#ex-c8-06)、[8-10](exercises/08-root-locus.md#ex-c8-10)。

### S-C8-04 高阶系统需复核非主导极点

等阻尼线选出的共轭极点只有在其他极点足够远、零点影响较小时才可主导二阶近似。见 [8-10](exercises/08-root-locus.md#ex-c8-10)。

## C9 非线性问题

### S-C9-01 描述函数是基波近似

它忽略高次谐波，因此交点是可能极限环的近似条件，不是严格存在性证明。见 [9-1](exercises/09-nonlinear.md#ex-c9-01)、[9-7](exercises/09-nonlinear.md#ex-c9-07)。

### S-C9-02 滞环描述函数一般为复数

滞环含记忆效应，会产生正交基波分量。见 [9-14](exercises/09-nonlinear.md#ex-c9-14)。

### S-C9-03 分段相轨迹跨区时状态连续

积分常数需由边界状态传递，不能每进一个区就重新任意选取。见 [9-3](exercises/09-nonlinear.md#ex-c9-03)、[9-16](exercises/09-nonlinear.md#ex-c9-16)。

### S-C9-04 自治系统相轨迹不能相交

在解唯一条件下，不同轨迹除平衡点外不能相交；交叉通常意味着手绘方向或方程错误。见 [9-11](exercises/09-nonlinear.md#ex-c9-11)。

### S-C9-05 线性化只给局部分类

远离平衡点的吸引域、极限环和分界轨迹仍需非线性方法。见 [9-10](exercises/09-nonlinear.md#ex-c9-10)、[9-17](exercises/09-nonlinear.md#ex-c9-17)。

## C10 计算机控制系统

### S-C10-01 零阶保持器近似引入半采样周期延迟

\[
\angle G_h(j\omega)\approx-\frac{\omega T}{2}
\]

见 [10-2](exercises/10-digital-control.md#ex-c10-02)。

### S-C10-02 Z 变换代数式必须配收敛域

同一有理式可对应右边、左边或双边序列。见 [10-6](exercises/10-digital-control.md#ex-c10-06)、[10-9](exercises/10-digital-control.md#ex-c10-09)。

### S-C10-03 连续模型不能直接把 $s$ 换成 $z$

采样序列、零阶保持器和离散化方法都会改变模型。见 [10-8](exercises/10-digital-control.md#ex-c10-08)、[10-13](exercises/10-digital-control.md#ex-c10-13)。

### S-C10-04 采样器位置改变脉冲传递函数结构

一般而言

\[
\mathcal Z\{G_1(s)G_2(s)\}\ne G_1(z)G_2(z)
\]

见 [10-12](exercises/10-digital-control.md#ex-c10-12)。

### S-C10-05 连续稳定域与离散稳定域

\[
z=e^{sT},\qquad \Re(s)<0\Longleftrightarrow |z|<1
\]

见 [10-15](exercises/10-digital-control.md#ex-c10-15)、[10-16](exercises/10-digital-control.md#ex-c10-16)。

### S-C10-06 采样周期本身是设计参数

改变 $T$ 会同时改变离散对象、保持器相位和闭环极点；连续对象稳定不能保证任意采样周期下的离散闭环稳定。见 [10-17](exercises/10-digital-control.md#ex-c10-17)。

返回：[逐题解析总览](exercises/index.md) · [LaTeX 公式图鉴](25-formula-atlas.md)

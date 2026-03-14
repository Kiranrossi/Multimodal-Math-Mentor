# 3D Geometry (Comprehensive - JEE Scope)

## Direction Cosines & Direction Ratios
- If a line makes angles $\alpha, \beta, \gamma$ with the positive $x, y, z$-axes:
  - **Direction Cosines (DCs)**: $l = \cos\alpha,\ m = \cos\beta,\ n = \cos\gamma$
  - $l^2 + m^2 + n^2 = 1$
- **Direction Ratios (DRs)**: Any three numbers $a, b, c$ proportional to $l, m, n$
  - $l = \dfrac{a}{\sqrt{a^2+b^2+c^2}}$, similarly for $m$, $n$

## Distance Formula
- Between $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$:
  $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$

## Section Formula
- Internal division in ratio $m:n$:
  $\left(\dfrac{mx_2+nx_1}{m+n},\ \dfrac{my_2+ny_1}{m+n},\ \dfrac{mz_2+nz_1}{m+n}\right)$

## Equation of a Line
- **Vector Form**: $\vec{r} = \vec{a} + \lambda\vec{b}$
- **Cartesian Form**: $\dfrac{x - x_1}{a} = \dfrac{y - y_1}{b} = \dfrac{z - z_1}{c}$
  - where $(x_1, y_1, z_1)$ is a point on the line and $(a, b, c)$ are DRs.
- **Two-Point Form**: $\dfrac{x-x_1}{x_2-x_1} = \dfrac{y-y_1}{y_2-y_1} = \dfrac{z-z_1}{z_2-z_1}$

### Angle Between Two Lines
- $\cos\theta = |l_1 l_2 + m_1 m_2 + n_1 n_2|$
- $\cos\theta = \dfrac{|a_1 a_2 + b_1 b_2 + c_1 c_2|}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$
- **Parallel**: $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$
- **Perpendicular**: $a_1 a_2 + b_1 b_2 + c_1 c_2 = 0$

### Skew Lines
- **Shortest Distance**:
  $d = \dfrac{|(\vec{a_2} - \vec{a_1}) \cdot (\vec{b_1} \times \vec{b_2})|}{|\vec{b_1} \times \vec{b_2}|}$

## Equation of a Plane
- **General Form**: $ax + by + cz + d = 0$ (normal vector $(a, b, c)$)
- **Normal Form**: $lx + my + nz = p$ (where $l, m, n$ are DCs of normal, $p > 0$)
- **Intercept Form**: $\dfrac{x}{a} + \dfrac{y}{b} + \dfrac{z}{c} = 1$
- **Vector Form**: $\vec{r} \cdot \hat{n} = d$
- **Three-Point Form**: $\begin{vmatrix} x-x_1 & y-y_1 & z-z_1 \\ x_2-x_1 & y_2-y_1 & z_2-z_1 \\ x_3-x_1 & y_3-y_1 & z_3-z_1 \end{vmatrix} = 0$

### Angle Between Two Planes
- $\cos\theta = \dfrac{|a_1 a_2 + b_1 b_2 + c_1 c_2|}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$
- **Parallel planes**: $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$
- **Perpendicular planes**: $a_1 a_2 + b_1 b_2 + c_1 c_2 = 0$

### Distance from Point to Plane
- Point $(x_1, y_1, z_1)$ to plane $ax + by + cz + d = 0$:
  $\text{Distance} = \dfrac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2 + b^2 + c^2}}$

## Angle Between Line and Plane
- Line with DRs $(a, b, c)$, plane $Ax + By + Cz + D = 0$:
  $\sin\theta = \dfrac{|Aa + Bb + Cc|}{\sqrt{A^2+B^2+C^2}\sqrt{a^2+b^2+c^2}}$
- **Line parallel to plane**: $Aa + Bb + Cc = 0$
- **Line perpendicular to plane**: $\dfrac{A}{a} = \dfrac{B}{b} = \dfrac{C}{c}$

## Family of Planes
- Planes through intersection of $P_1 = 0$ and $P_2 = 0$: $P_1 + \lambda P_2 = 0$

## Sphere
- **Standard Form** (center at origin): $x^2 + y^2 + z^2 = r^2$
- **General Form**: $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$
  - Center: $(-u, -v, -w)$, Radius: $\sqrt{u^2 + v^2 + w^2 - d}$

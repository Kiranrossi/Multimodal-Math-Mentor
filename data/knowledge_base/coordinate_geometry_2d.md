# Coordinate Geometry 2D (Comprehensive - JEE Scope)

## Basic Concepts
- **Distance Formula**: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
- **Section Formula (Internal)**: $\left(\dfrac{mx_2 + nx_1}{m+n},\ \dfrac{my_2 + ny_1}{m+n}\right)$
- **Section Formula (External)**: $\left(\dfrac{mx_2 - nx_1}{m-n},\ \dfrac{my_2 - ny_1}{m-n}\right)$
- **Midpoint**: $\left(\dfrac{x_1+x_2}{2},\ \dfrac{y_1+y_2}{2}\right)$
- **Centroid of Triangle**: $\left(\dfrac{x_1+x_2+x_3}{3},\ \dfrac{y_1+y_2+y_3}{3}\right)$
- **Area of Triangle**: $\dfrac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$

## Straight Lines
- **Slope**: $m = \tan\theta = \dfrac{y_2 - y_1}{x_2 - x_1}$
- **Slope-Intercept Form**: $y = mx + c$
- **Point-Slope Form**: $y - y_1 = m(x - x_1)$
- **Two-Point Form**: $\dfrac{y - y_1}{y_2 - y_1} = \dfrac{x - x_1}{x_2 - x_1}$
- **Intercept Form**: $\dfrac{x}{a} + \dfrac{y}{b} = 1$
- **Normal Form**: $x\cos\alpha + y\sin\alpha = p$
- **General Form**: $ax + by + c = 0$

### Distance and Angle
- **Distance from point to line**: $d = \dfrac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}}$
- **Angle between two lines**: $\tan\theta = \left|\dfrac{m_1 - m_2}{1 + m_1 m_2}\right|$
- **Parallel lines**: $m_1 = m_2$
- **Perpendicular lines**: $m_1 m_2 = -1$
- **Distance between parallel lines** $ax + by + c_1 = 0$ and $ax + by + c_2 = 0$: $d = \dfrac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}$

### Family of Lines
- Lines through intersection of $L_1 = 0$ and $L_2 = 0$: $L_1 + \lambda L_2 = 0$

## Circle
- **Standard Form** (center at origin): $x^2 + y^2 = r^2$
- **Center-Radius Form**: $(x-h)^2 + (y-k)^2 = r^2$
- **General Form**: $x^2 + y^2 + 2gx + 2fy + c = 0$
  - Center: $(-g, -f)$, Radius: $\sqrt{g^2 + f^2 - c}$
- **Diameter Form** (endpoints $(x_1,y_1)$ and $(x_2,y_2)$): $(x-x_1)(x-x_2) + (y-y_1)(y-y_2) = 0$

### Tangent to Circle $x^2 + y^2 = r^2$
- At point $(x_1, y_1)$: $xx_1 + yy_1 = r^2$
- With slope $m$: $y = mx \pm r\sqrt{1+m^2}$
- Length of tangent from external point $(x_1,y_1)$: $\sqrt{x_1^2 + y_1^2 - r^2}$

## Parabola
Standard form $y^2 = 4ax$ (opens right, $a > 0$):
- **Focus**: $(a, 0)$
- **Directrix**: $x = -a$
- **Vertex**: $(0, 0)$
- **Axis**: $y = 0$
- **Latus Rectum**: $x = a$, length $= 4a$
- **Parametric**: $(at^2, 2at)$
- **Tangent at $(x_1, y_1)$**: $yy_1 = 2a(x + x_1)$
- **Tangent with slope $m$**: $y = mx + \dfrac{a}{m}$

## Ellipse
Standard form $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ($a > b > 0$):
- **Foci**: $(\pm ae, 0)$ where eccentricity $e = \sqrt{1 - b^2/a^2}$
- **Directrices**: $x = \pm a/e$
- **Vertices**: $(\pm a, 0)$, $(0, \pm b)$
- **Latus Rectum** length: $\dfrac{2b^2}{a}$
- **Relation**: $b^2 = a^2(1 - e^2)$
- **Parametric**: $(a\cos\theta, b\sin\theta)$
- **Tangent at $(x_1, y_1)$**: $\dfrac{xx_1}{a^2} + \dfrac{yy_1}{b^2} = 1$
- **Tangent with slope $m$**: $y = mx \pm \sqrt{a^2m^2 + b^2}$

## Hyperbola
Standard form $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$:
- **Foci**: $(\pm ae, 0)$ where $e = \sqrt{1 + b^2/a^2} > 1$
- **Directrices**: $x = \pm a/e$
- **Vertices**: $(\pm a, 0)$
- **Asymptotes**: $y = \pm \dfrac{b}{a}x$
- **Relation**: $b^2 = a^2(e^2 - 1)$
- **Parametric**: $(a\sec\theta, b\tan\theta)$
- **Tangent at $(x_1, y_1)$**: $\dfrac{xx_1}{a^2} - \dfrac{yy_1}{b^2} = 1$
- **Rectangular Hyperbola** $xy = c^2$: Parametric $(ct, c/t)$

## General Second-Degree Curve
$ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$
- **Pair of straight lines** if $\Delta = \begin{vmatrix} a & h & g \\ h & b & f \\ g & f & c \end{vmatrix} = 0$
- **Circle** if $a = b$, $h = 0$
- **Parabola** if $\Delta \ne 0$ and $ab - h^2 = 0$
- **Ellipse** if $\Delta \ne 0$ and $ab - h^2 > 0$
- **Hyperbola** if $\Delta \ne 0$ and $ab - h^2 < 0$

# Linear Algebra & Vectors (Comprehensive - JEE Scope)

## Matrices
- **Types**: Row, Column, Square, Diagonal, Scalar, Identity.
- **Operations**:
  - **Addition**: $A+B$
  - **Multiplication**: $AB$ (Associative but NOT Commutative)
  - **Transpose**: $(AB)^T = B^T A^T$
- **Inverse**: $A^{-1} = \frac{1}{|A|} \text{adj}(A)$
  - Only exists if $|A| \ne 0$ (Non-singular).

## Determinants
- **Properties**:
  - $|A| = |A^T|$
  - $|AB| = |A||B|$
  - Row/Column operations ($R_1 \to R_1 + kR_2$) do not change $|A|$.
- **Area of Triangle**: $\frac{1}{2} |x_1(y_2-y_3) + ...|$

## System of Linear Equations (Cramer's Rule / Matrix Method)
$AX = B$
- **Consistent Unique**: $|A| \ne 0$
- **Inconsistent (No solution)**: $|A| = 0$ and $(\text{adj } A)B \ne 0$
- **Infinite Solutions**: $|A| = 0$ and $(\text{adj } A)B = 0$

## Vectors
- **Unit Vector**: $\hat{a} = \frac{\vec{a}}{|\vec{a}|}$
- **Section Formula**: $\vec{r} = \frac{m\vec{b} + n\vec{a}}{m+n}$
- **Dot Product**: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos \theta$
  - $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$
- **Cross Product**: $\vec{a} \times \vec{b} = |\vec{a}||\vec{b}|\sin \theta \hat{n}$
  - $\vec{a} \parallel \vec{b} \iff \vec{a} \times \vec{b} = 0$
- **Scalar Triple Product**: $[\vec{a} \vec{b} \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c})$
  - Represents volume of parallelepiped.
  - Coplanar if $[\vec{a} \vec{b} \vec{c}] = 0$.

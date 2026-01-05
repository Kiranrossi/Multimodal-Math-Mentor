# Calculus (Comprehensive - JEE Scope)

## Limits
- **Standard Limits**:
  - $\lim_{x \to 0} \frac{\sin x}{x} = 1$
  - $\lim_{x \to 0} \frac{e^x - 1}{x} = 1$
  - $\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$
- **L'Hospital's Rule**: If form is $0/0$ or $\infty/\infty$, then $\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$

## Differentiation
- **Chain Rule**: $\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$
- **Product Rule**: $(uv)' = u'v + uv'$
- **Quotient Rule**: $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$
- **Standard Derivatives**:
  - $\frac{d}{dx} \sin x = \cos x$
  - $\frac{d}{dx} \ln x = \frac{1}{x}$

## Integration
- **Integration by Parts**: $\int u v \, dx = u \int v \, dx - \int (u' \int v \, dx) \, dx$
- **Standard Integrals**:
  - $\int x^n \, dx = \frac{x^{n+1}}{n+1}$
  - $\int \frac{1}{x^2 + a^2} \, dx = \frac{1}{a} \tan^{-1}(\frac{x}{a})$
  - $\int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \sin^{-1}(\frac{x}{a})$

## Definite Integrals
- **Newton-Leibniz Formula**: $\int_a^b f(x) \, dx = F(b) - F(a)$
- **Properties**: $\int_a^b f(x) \, dx = \int_a^b f(a+b-x) \, dx$

## Differential Equations
- **Variable Separable**: $f(y) dy = g(x) dx$
- **Linear D.E.**: $\frac{dy}{dx} + Py = Q$
  - Integrating Factor (IF) = $e^{\int P \, dx}$
  - Solution: $y \cdot \text{IF} = \int (Q \cdot \text{IF}) \, dx + C$

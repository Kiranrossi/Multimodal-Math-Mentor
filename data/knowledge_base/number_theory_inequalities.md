# Number Theory & Inequalities (Comprehensive - JEE Scope)

## Number Systems
- **Natural Numbers** $\mathbb{N}$: $\{1, 2, 3, \ldots\}$
- **Whole Numbers** $\mathbb{W}$: $\{0, 1, 2, \ldots\}$
- **Integers** $\mathbb{Z}$: $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$
- **Rationals** $\mathbb{Q}$: $\{p/q : p, q \in \mathbb{Z},\ q \ne 0\}$
- **Irrationals**: Non-terminating, non-repeating decimals (e.g., $\sqrt{2}, \pi$)
- **Real Numbers** $\mathbb{R}$: $\mathbb{Q} \cup$ Irrationals

## Divisibility
- $a \mid b$ means $b = ka$ for some integer $k$.
- **Division Algorithm**: $a = bq + r$, where $0 \le r < b$
- **GCD / HCF**: Greatest Common Divisor of $a$ and $b$: $\gcd(a, b)$
- **LCM**: Least Common Multiple: $\text{lcm}(a, b)$
- **Key Relation**: $\gcd(a, b) \times \text{lcm}(a, b) = a \times b$

## Prime Numbers
- A prime has exactly two divisors: 1 and itself.
- **Fundamental Theorem of Arithmetic**: Every integer $> 1$ has a unique prime factorization.
- If $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, then:
  - Number of divisors: $(a_1 + 1)(a_2 + 1) \cdots (a_k + 1)$
  - Sum of divisors: $\dfrac{p_1^{a_1+1}-1}{p_1-1} \cdot \dfrac{p_2^{a_2+1}-1}{p_2-1} \cdots$

## Modular Arithmetic
- $a \equiv b \pmod{m}$ means $m \mid (a - b)$
- **Properties**:
  - $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$
  - $(a \cdot b) \bmod m = ((a \bmod m) \cdot (b \bmod m)) \bmod m$
- **Fermat's Little Theorem**: If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$
- **Euler's Theorem**: $a^{\phi(n)} \equiv 1 \pmod{n}$ when $\gcd(a, n) = 1$
  - $\phi(n)$ = Euler's totient function = count of integers in $[1, n]$ coprime to $n$

## Important Inequalities

### AM-GM Inequality
For non-negative reals $a_1, a_2, \ldots, a_n$:
$$\frac{a_1 + a_2 + \cdots + a_n}{n} \ge (a_1 a_2 \cdots a_n)^{1/n}$$
Equality holds iff $a_1 = a_2 = \cdots = a_n$.

### AM-HM Inequality
$$\frac{a + b}{2} \ge \frac{2ab}{a+b} \quad (a, b > 0)$$
i.e., $\text{AM} \ge \text{GM} \ge \text{HM}$

### Cauchy-Schwarz Inequality
$$(a_1^2 + a_2^2 + \cdots + a_n^2)(b_1^2 + b_2^2 + \cdots + b_n^2) \ge (a_1 b_1 + a_2 b_2 + \cdots + a_n b_n)^2$$

### Triangle Inequality
- $|a + b| \le |a| + |b|$
- $|a - b| \ge ||a| - |b||$

### Useful Inequalities
- For $x > 0$: $x + \dfrac{1}{x} \ge 2$
- For $a, b > 0$: $\dfrac{a}{b} + \dfrac{b}{a} \ge 2$
- $e^x \ge 1 + x$ for all $x \in \mathbb{R}$
- $\ln x \le x - 1$ for $x > 0$

## Absolute Value Properties
- $|x| = \max(x, -x)$
- $|x| < a \iff -a < x < a$
- $|x| > a \iff x > a$ or $x < -a$
- $|xy| = |x||y|$
- $\left|\dfrac{x}{y}\right| = \dfrac{|x|}{|y|}$

## Intervals and Modulus Equations
- $|x - a| < r \iff a - r < x < a + r$ (open interval around $a$)
- $|x - a| \le r \iff a - r \le x \le a + r$ (closed interval around $a$)

## Logarithm Properties
- $\log_a(mn) = \log_a m + \log_a n$
- $\log_a\left(\dfrac{m}{n}\right) = \log_a m - \log_a n$
- $\log_a(m^n) = n \log_a m$
- **Change of Base**: $\log_a b = \dfrac{\log_c b}{\log_c a}$
- $\log_a b = \dfrac{1}{\log_b a}$
- $a^{\log_a x} = x$
- $\log_a 1 = 0$, $\log_a a = 1$
- For $a > 1$: $\log_a x$ is increasing; for $0 < a < 1$: decreasing.
- $\log_a x > \log_a y \iff x > y$ (if $a > 1$) or $x < y$ (if $0 < a < 1$)

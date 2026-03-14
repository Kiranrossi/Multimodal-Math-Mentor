# Sets, Relations & Functions (Comprehensive - JEE Scope)

## Sets
- **Union**: $A \cup B = \{x : x \in A \text{ or } x \in B\}$
- **Intersection**: $A \cap B = \{x : x \in A \text{ and } x \in B\}$
- **Complement**: $A' = \{x : x \notin A\}$
- **Difference**: $A - B = \{x : x \in A \text{ and } x \notin B\}$

### Properties
- $A \cup A' = U$, $A \cap A' = \emptyset$
- **De Morgan's Laws**:
  - $(A \cup B)' = A' \cap B'$
  - $(A \cap B)' = A' \cup B'$
- $n(A \cup B) = n(A) + n(B) - n(A \cap B)$
- $n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(A \cap C) + n(A \cap B \cap C)$

### Power Set
- Power set of $A$: $P(A)$ = set of all subsets of $A$
- If $|A| = n$, then $|P(A)| = 2^n$

## Relations
- A relation $R$ from set $A$ to $B$ is a subset of $A \times B$.
- **Domain** of $R$: set of all first elements.
- **Range** of $R$: set of all second elements.

### Types of Relations (on a set $A$)
- **Reflexive**: $(a, a) \in R\ \forall\ a \in A$
- **Symmetric**: $(a, b) \in R \Rightarrow (b, a) \in R$
- **Transitive**: $(a,b) \in R$ and $(b,c) \in R \Rightarrow (a,c) \in R$
- **Equivalence Relation**: Reflexive + Symmetric + Transitive
- **Equivalence Class** of $a$: $[a] = \{x \in A : (a, x) \in R\}$

## Functions
A function $f: A \to B$ assigns exactly one element of $B$ to each element of $A$.
- **Domain**: Set $A$
- **Codomain**: Set $B$
- **Range**: $\{f(x) : x \in A\} \subseteq B$

### Types of Functions
- **One-One (Injective)**: $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$
- **Onto (Surjective)**: Range = Codomain, i.e., every $b \in B$ has a preimage.
- **Bijective**: Both one-one and onto.
  - For bijection between finite sets: $|A| = |B|$

### Composition of Functions
- $(g \circ f)(x) = g(f(x))$
- $g \circ f$ is defined if Range of $f \subseteq$ Domain of $g$
- **Not commutative**: $f \circ g \ne g \circ f$ in general
- **Associative**: $(h \circ g) \circ f = h \circ (g \circ f)$

### Inverse Function
- Inverse $f^{-1}$ exists $\iff$ $f$ is bijective.
- $(f^{-1} \circ f)(x) = x$ and $(f \circ f^{-1})(y) = y$

## Important Standard Functions & Their Graphs
- **Identity**: $f(x) = x$, Domain $= \mathbb{R}$, Range $= \mathbb{R}$
- **Constant**: $f(x) = c$
- **Modulus**: $f(x) = |x|$, Range $= [0, \infty)$
- **Signum**: $f(x) = \begin{cases} 1 & x > 0 \\ 0 & x = 0 \\ -1 & x < 0 \end{cases}$
- **Greatest Integer (Floor)**: $f(x) = \lfloor x \rfloor$, $\lfloor x \rfloor = n$ if $n \le x < n+1$
- **Fractional Part**: $f(x) = \{x\} = x - \lfloor x \rfloor$, Range $= [0, 1)$

## Even and Odd Functions
- **Even**: $f(-x) = f(x)$ (symmetric about $y$-axis)
- **Odd**: $f(-x) = -f(x)$ (symmetric about origin)
- Every function = even part + odd part:
  $f(x) = \dfrac{f(x)+f(-x)}{2} + \dfrac{f(x)-f(-x)}{2}$

## Periodic Functions
- $f(x + T) = f(x)$ for all $x$, smallest such $T > 0$ is the period.
- $\sin x$, $\cos x$: period $2\pi$
- $\tan x$, $\cot x$: period $\pi$
- $|\sin x|$, $|\cos x|$: period $\pi$

## Transformation of Graphs
- $y = f(x) + c$: shift up by $c$
- $y = f(x+c)$: shift left by $c$
- $y = cf(x)$: stretch vertically by factor $c$
- $y = f(cx)$: compress horizontally by factor $c$
- $y = -f(x)$: reflect in $x$-axis
- $y = f(-x)$: reflect in $y$-axis
- $y = |f(x)|$: reflect portions below $x$-axis upward

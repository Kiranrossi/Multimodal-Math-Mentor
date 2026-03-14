# Mathematical Reasoning & Induction (Comprehensive - JEE Scope)

## Mathematical Logic

### Statements and Connectives
- A **statement** is a sentence that is either true (T) or false (F), not both.
- **Negation** ($\sim p$): "not $p$" — flips truth value.
- **Conjunction** ($p \wedge q$): "$p$ and $q$" — true only if both are true.
- **Disjunction** ($p \vee q$): "$p$ or $q$" — false only if both are false.
- **Implication** ($p \Rightarrow q$): "if $p$ then $q$" — false only when $p$ is T and $q$ is F.
- **Biconditional** ($p \Leftrightarrow q$): "$p$ if and only if $q$" — true when $p$ and $q$ have the same truth value.

### Truth Table Summary
| $p$ | $q$ | $\sim p$ | $p \wedge q$ | $p \vee q$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ |
|---|---|---|---|---|---|---|
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

### Important Logical Equivalences
- **Contrapositive**: $p \Rightarrow q \equiv \sim q \Rightarrow \sim p$
- **Converse**: $q \Rightarrow p$ (not equivalent to original)
- **Inverse**: $\sim p \Rightarrow \sim q$
- **De Morgan's Laws**:
  - $\sim(p \wedge q) \equiv \sim p \vee \sim q$
  - $\sim(p \vee q) \equiv \sim p \wedge \sim q$
- **Tautology**: Always true (e.g., $p \vee \sim p$)
- **Contradiction (Fallacy)**: Always false (e.g., $p \wedge \sim p$)

### Quantifiers
- **Universal**: $\forall$ (for all)
- **Existential**: $\exists$ (there exists)
- Negation of $\forall x, P(x)$: $\exists x$ such that $\sim P(x)$
- Negation of $\exists x, P(x)$: $\forall x$, $\sim P(x)$

## Mathematical Induction
Used to prove statements $P(n)$ true for all natural numbers $n \ge n_0$.

### Steps
1. **Base Case**: Verify $P(n_0)$ is true (usually $n_0 = 1$).
2. **Inductive Hypothesis**: Assume $P(k)$ is true for some $k \ge n_0$.
3. **Inductive Step**: Prove $P(k+1)$ is true using the hypothesis.
4. **Conclusion**: By induction, $P(n)$ is true for all $n \ge n_0$.

### Standard Results Proved by Induction
- $\displaystyle\sum_{r=1}^n r = \dfrac{n(n+1)}{2}$
- $\displaystyle\sum_{r=1}^n r^2 = \dfrac{n(n+1)(2n+1)}{6}$
- $\displaystyle\sum_{r=1}^n r^3 = \left[\dfrac{n(n+1)}{2}\right]^2$
- $\displaystyle\sum_{r=1}^n r(r+1) = \dfrac{n(n+1)(n+2)}{3}$
- $1 + 3 + 5 + \cdots + (2n-1) = n^2$

## Well-Ordering Principle
Every non-empty subset of $\mathbb{N}$ has a least element. (Equivalent to Mathematical Induction.)

## Proof Techniques
- **Direct Proof**: Assume $p$, derive $q$ directly.
- **Proof by Contradiction**: Assume $\sim q$, derive a contradiction.
- **Proof by Contrapositive**: Prove $\sim q \Rightarrow \sim p$ instead of $p \Rightarrow q$.
- **Proof by Cases**: Divide the domain into exhaustive cases and prove each.
- **Counterexample**: A single example showing a universal statement is false.

# Probability (Comprehensive - JEE Scope)

## Axiomatic Probability
- **Sample Space ($S$)**: Set of all possible outcomes.
- **Event ($E$)**: Subset of $S$.
- **Probability**: $P(E) = \frac{n(E)}{n(S)}$

## Theorems
- **Addition Theorem**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Independent Events**: $P(A \cap B) = P(A) \cdot P(B)$
- **Conditional Probability**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

## Total Probability & Bayes' Theorem
If $E_1, E_2, ... E_n$ are mutually exclusive and exhaustive:
- **Total Probability**: $P(A) = \sum P(E_i) P(A|E_i)$
- **Bayes' Theorem** (Reverse Probability):
  $$P(E_k|A) = \frac{P(E_k) P(A|E_k)}{\sum P(E_i) P(A|E_i)}$$

## Probability Distributions
### Binomial Distribution
For $n$ independent Bernoulli trials with probability of success $p$:
- $P(X = r) = ^nC_r p^r q^{n-r}$ where $q = 1-p$
- **Mean**: $np$
- **Variance**: $npq$
- **Standard Deviation**: $\sqrt{npq}$

### Random Variables
- **Mean (Expectation)** $E[X] = \sum x_i p_i$
- **Variance**: $Var(X) = E[X^2] - (E[X])^2$

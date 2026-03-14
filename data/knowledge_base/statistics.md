# Statistics (Comprehensive - JEE Scope)

## Measures of Central Tendency

### Mean
- **Arithmetic Mean (ungrouped)**: $\bar{x} = \dfrac{\sum x_i}{n}$
- **Arithmetic Mean (grouped/frequency)**: $\bar{x} = \dfrac{\sum f_i x_i}{\sum f_i}$
- **Step Deviation Method**: $\bar{x} = A + \left(\dfrac{\sum f_i u_i}{\sum f_i}\right) \times h$ where $u_i = \dfrac{x_i - A}{h}$

### Median
- **Ungrouped**: Middle value when sorted. If $n$ is even, average of two middle values.
- **Grouped**:
  $M = l + \dfrac{\dfrac{n}{2} - cf}{f} \times h$
  - $l$ = lower boundary of median class
  - $cf$ = cumulative frequency before median class
  - $f$ = frequency of median class
  - $h$ = class width

### Mode
- **Ungrouped**: Most frequently occurring value.
- **Grouped**:
  $\text{Mode} = l + \dfrac{f_1 - f_0}{2f_1 - f_0 - f_2} \times h$
  - $l$ = lower boundary of modal class
  - $f_1$ = frequency of modal class
  - $f_0$ = frequency of class before modal class
  - $f_2$ = frequency of class after modal class

### Empirical Relation
$\text{Mode} \approx 3\,\text{Median} - 2\,\text{Mean}$

## Measures of Dispersion

### Range
$\text{Range} = \text{Maximum value} - \text{Minimum value}$

### Mean Deviation
- **Mean Deviation about Mean**: $\text{M.D.}(\bar{x}) = \dfrac{\sum |x_i - \bar{x}|}{n}$
- **Mean Deviation about Median**: $\text{M.D.}(M) = \dfrac{\sum |x_i - M|}{n}$
- For grouped data: use $f_i$ in numerator and $\sum f_i$ in denominator.

### Variance and Standard Deviation
- **Variance** (ungrouped): $\sigma^2 = \dfrac{\sum (x_i - \bar{x})^2}{n} = \dfrac{\sum x_i^2}{n} - \bar{x}^2$
- **Variance** (grouped): $\sigma^2 = \dfrac{\sum f_i (x_i - \bar{x})^2}{\sum f_i}$
- **Standard Deviation**: $\sigma = \sqrt{\sigma^2}$
- **Shortcut Formula**: $\sigma^2 = \dfrac{\sum f_i x_i^2}{\sum f_i} - \left(\dfrac{\sum f_i x_i}{\sum f_i}\right)^2$

### Coefficient of Variation (CV)
$CV = \dfrac{\sigma}{\bar{x}} \times 100\%$
- Used to compare variability of two distributions.
- Lower CV → more consistent.

## Properties of Mean and Variance
- If each value is increased by $k$: Mean increases by $k$, Variance unchanged.
- If each value is multiplied by $k$: Mean multiplied by $k$, Variance multiplied by $k^2$, SD multiplied by $|k|$.

## Correlation (Basic)
- **Karl Pearson's Coefficient of Correlation**:
  $r = \dfrac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n\sigma_x \sigma_y}$
- $-1 \le r \le 1$
- $r = 1$: perfect positive correlation
- $r = -1$: perfect negative correlation
- $r = 0$: no linear correlation

## Quartiles & Percentiles
- **Lower Quartile** $Q_1$: 25th percentile
- **Upper Quartile** $Q_3$: 75th percentile
- **Interquartile Range (IQR)**: $Q_3 - Q_1$
- **Semi-Interquartile Range**: $\dfrac{Q_3 - Q_1}{2}$

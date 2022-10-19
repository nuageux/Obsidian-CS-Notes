#Theoretical #Math 
# Time and Space Complexity

## Time Complexity

-   How fast is my _**algorithm**_?
    -   We want to describe this in the **number of operations** with respect to the **input size** _n_.

## Notations of Complexity

-   Big-_O_ describes the **upper** bound
    -   $f(n)$ is $O(g(n))$ if there exists some constant $A$ such that $Ag(n) ≥ f(n)$ when $n → infinity$.
    -   a.k.a. “$f(n)$ is upper-bounded by $g(n)$”.
    -   Describes the worst-case, which is all we care about, really.
-   Big-_Ω_ describes the **lower** bound
-   Big-_θ_ describes the **tight** bound

## Finding Big-O Time Complexity

1.  Determine $f(n)$: The number of operations vs. $n$.
    
2.  Drop all the lower terms of $n$.
    
3.  Drop the constant coefficients.
    

-   **Important**! If the inner loop depends on the outer loop for its time complexity, then it’s safe to say you can’t just multiply them together!

## Common Big-O Time Complexities

-   $O(1)$ → “Constant” time
-   $O(log n)$ → “Logarithmic” time
    -   Doubling the input size only increases algorithm operations by 1.
    -   We don’t list a base for the logarithm, since we can always convert to base 2 through the logarithm convert base formula (with a constant).
-   $O(n)$ → “Linear” time
-   $O(n log n)$
    -   Ex: Merge sort
-   $O($$n^2$$)$ → “Quadratic” time
-   $O(n^3)$ → “Cubic” time
-   $O(n^c)$ for any constant $c$ → “Polynomial” time
    -   “Good” time complexity
-   “Bad” time complexities:
    -   $O(K^n)$ for some constant $K$ → “Exponential” time
    -   $O(n!)$ → “Factorial” time

## Space Complexity

-   How much space an algorithm takes with respect to $_n_$.
-   Sometimes, we have to take in the details of the specific language, but when summarizing to the level of big-_O_ notation, it becomes language agnostic again.
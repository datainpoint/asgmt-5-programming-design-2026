# asgmt-5-programming-design-2025

> Assignment 5: Programming Design 2025.

## 01. Define a class `SquareSqrtArgs` which instantiates objects with two methods `square_args()` and `sqrt_args()` that take flexible integers and returns their squared and square-root values in a `list`.

```python
class SquareSqrtArgs:
    """
    >>> square_sqrt_args = SquareSqrtArgs()
    >>> square_sqrt_args.square_args(2)
    [4]
    >>> square_sqrt_args.sqrt_args(4)
    [2.0]
    >>> square_sqrt_args.square_args(1, 2)
    [1, 4]
    >>> square_sqrt_args.sqrt_args(1, 4)
    [1.0, 2.0]
    >>> square_sqrt_args.square_args(0, 1, 2)
    [0, 1, 4]
    >>> square_sqrt_args.sqrt_args(0, 1, 4)
    [0.0, 1.0, 2.0]
    >>> square_sqrt_args.square_args(3, 4, 5)
    [9, 16, 25]
    >>> square_sqrt_args.sqrt_args(9, 16, 25)
    [3.0, 4.0, 5.0]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `ReverseKwargs` which instantiates objects that take flexible `**kwargs` with two methods `fetch_key_value()` and `reverse_key_value()`.

```python
class ReverseKwargs:
    """
    >>> reverse_kwargs = ReverseKwargs(one=1, two=2, three=3)
    >>> reverse_kwargs.fetch_key_value()
    {'key': ('one', 'two', 'three'), 'value': (1, 2, 3)}
    >>> reverse_kwargs.reverse_key_value()
    {1: 'one', 2: 'two', 3: 'three'}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class `CommonDivisors` which instantiates objects with 2 attributes `x_divisors` and `y_divisors`, and 1 method `get_common_divisors()`.

```python
class CommonDivisors:
    """
    >>> cd = CommonDivisors(3, 6)
    >>> cd.x_divisors
    {1, 3}
    >>> cd.y_divisors
    {1, 2, 3, 6}
    >>> cd.get_common_divisors()
    {1, 3}
    >>> cd = CommonDivisors(4, 8)
    >>> cd.x_divisors
    {1, 2, 4}
    >>> cd.y_divisors
    {1, 2, 4, 8}
    >>> cd.get_common_divisors()
    {1, 2, 4}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `PrimeJudger` which instantiates objects with 2 methods `get_divisors()`, `is_prime()`.

```python
class PrimeJudger:
    """
    >>> pj = PrimeJudger(1)
    >>> pj.get_divisors()
    {1}
    >>> pj.is_prime()
    False
    >>> pj = PrimeJudger(2)
    >>> pj.get_divisors()
    {1, 2}
    >>> pj.is_prime()
    True
    >>> pj = PrimeJudger(4)
    >>> pj.get_divisors()
    {1, 2, 4}
    >>> pj.is_prime()
    False
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `import_countries_json` which imports the `countries.json` as a `list` in working directory.

```python
def import_countries_json() -> list:
    """
    >>> countries_json = import_countries_json()
    >>> type(countries_json)
    list
    >>> len(countries_json)
    249
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `lookup_country_iso_codes` which returns the 2-digit and 3-digit ISO country code given the name of country, based on `countries.json` in working directory.

```python
def lookup_country_iso_codes(country: str) -> tuple:
    """
    >>> lookup_country_iso_codes("Taiwan")
    ('TW', 'TWN')
    >>> lookup_country_iso_codes("Japan")
    ('JP', 'JPN')
    >>> lookup_country_iso_codes("Lithuania")
    ('LT', 'LTU')
    >>> lookup_country_iso_codes("Slovenia")
    ('SI', 'SVN')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a class named `ArrayGetAttrs` which instantiates objects with 4 methods `get_ndim()`, `get_shape()`, `get_size()`, and `get_dtype()`.

```python
class ArrayGetAttrs:
    """
    >>> arr = np.array([5, 5, 6, 6])
    >>> aga = ArrayGetAttrs(arr)
    >>> aga.get_ndim()
    1
    >>> aga.get_shape()
    (4,)
    >>> aga.get_size()
    4
    >>> aga.get_dtype()
    dtype('int64')
    >>> arr = np.array([[5, 5],
                        [6, 6]])
    >>> aga = ArrayGetAttrs(arr)
    >>> aga.get_ndim()
    2
    >>> aga.get_shape()
    (2, 2)
    >>> aga.get_size()
    4
    >>> aga.get_dtype()
    dtype('int64')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `add_intercepts()` which horizontally combines a `(m, 1)` array of ones to a given array.

```python
def add_intercepts(arr: np.ndarray) -> np.ndarray:
    """
    >>> A = np.array([5, 5, 6, 6]).reshape(-1, 1)
    >>> add_intercepts(A)
    array([[1, 5],
           [1, 5],
           [1, 6],
           [1, 6]])
    >>> B = np.arange(10, dtype=int).reshape(5, 2)
    >>> add_intercepts(B)
    array([[1, 0, 1],
           [1, 2, 3],
           [1, 4, 5],
           [1, 6, 7],
           [1, 8, 9]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `create_square_matrix()` which generates a square matrix with elements equal to the multiplication of row number and column number.

```python
def create_square_matrix(n: int) -> np.ndarray:
    """
    >>> create_square_matrix(3)
    array([[1, 2, 3],
           [2, 4, 6],
           [3, 6, 9]])
    >>> create_square_matrix(4)
    array([[ 1,  2,  3,  4],
           [ 2,  4,  6,  8],
           [ 3,  6,  9, 12],
           [ 4,  8, 12, 16]])
    >>> create_square_matrix(5)
    array([[ 1,  2,  3,  4,  5],
           [ 2,  4,  6,  8, 10],
           [ 3,  6,  9, 12, 15],
           [ 4,  8, 12, 16, 20],
           [ 5, 10, 15, 20, 25]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `create_diagonal_split_matrix()` which generates a diagonal matrix given `n` as the order, `fill_int` as the elements outside the main diagonal and zeros as the main diagonal.

```python
def create_diagonal_split_matrix(n: int, fill_int: int) -> np.ndarray:
    """
    >>> create_diagonal_split_matrix(2, 5566)
    array([[   0, 5566],
           [5566,    0]])
    >>> create_diagonal_split_matrix(3, 55)
    array([[ 0, 55, 55],
           [55,  0, 55],
           [55, 55,  0]])
    >>> create_diagonal_split_matrix(4, 66)
    array([[ 0, 66, 66, 66],
           [66,  0, 66, 66],
           [66, 66,  0, 66],
           [66, 66, 66,  0]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```
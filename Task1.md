

### **1. What will X be after the following statements complete?**
```python
x = 10
y = 20
x = y
y = 40
x = x + y
x = x - y
```
#### **Explanation:**
- `x = 10`
- `y = 20`
- `x = y` → Now `x = 20`
- `y = 40`
- `x = x + y` → `x = 20 + 40 = 60`
- `x = x - y` → `x = 60 - 40 = 20`

**Final value of `x`:** `20`

---

### **2. What will k be after the following statements complete?**
```python
w = 10
k = 17
for k in range(10, k):
    k = w
```
#### **Explanation:**
- `w = 10`
- `k = 17`
- The loop runs for `k in range(10, 17)`, meaning `k` takes values from `10` to `16`. However, the statement inside the loop (`k = w`) does not modify the loop variable itself.
- Once the loop is complete, `k` remains **17** (as the loop does not affect it after completion).

**Final value of `k`:** `17`

---

### **3. What will a and b be after the following statements complete?**
```python
a = b = 6
for i in range(b):
    a += 3
    b -= 1
```
#### **Explanation:**
- `a = 6`
- `b = 6`
- The loop runs **b times** (`range(6)` means it iterates 6 times), and in each iteration:
  - `a` increases by `3`
  - `b` decreases by `1`
  
| Iteration | `a` | `b` |
|-----------|-----|-----|
| 0         | 9   | 5   |
| 1         | 12  | 4   |
| 2         | 15  | 3   |
| 3         | 18  | 2   |
| 4         | 21  | 1   |
| 5         | 24  | 0   |

**Final values:**
- `a = 24`
- `b = 0`

---

### **4. What will x be after the following statement?**
```python
x = (2+3)**(5-2*2)
```
#### **Explanation:**
- `2 + 3 = 5`
- `5 - 2 * 2 = 5 - 4 = 1`
- `5 ** 1 = 5`

**Final value of `x`:** `5`

---

### **Task 4: Sine Loops (8 marks)**
You need to generate a sine wave plot in Python. You can use `matplotlib` for this:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)  # Generate x values from -π to π
y = np.sin(x)  # Compute the sine of x

plt.plot(x, y)
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Sine Wave")
plt.show()
```

---

### **Task 6: Sine Wave Plus (4 marks)**
To extend the sine wave by adding values to the axes:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-180, 180, 100)  # Convert degrees to radians
y = np.sin(np.radians(x))  # Compute sine values

plt.plot(x, y)
plt.xticks([-180, -90, 0, 90, 180])  # Label x-axis with degrees
plt.yticks([-1, -0.5, 0, 0.5, 1])  # Label y-axis
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Extended Sine Wave")
plt.show()
```

---
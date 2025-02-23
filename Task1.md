

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
import turtle
import math

# Set up the turtle screen
turtle.setup(800, 400)
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
fred = turtle.Turtle()
fred.speed(0)  # Fastest speed
fred.penup()

# Move to the starting position
fred.goto(-360, 0)
fred.pendown()

# Draw the sine wave
for angle in range(-360, 361, 5):  # Step by 5 for smooth curve
    y = math.sin(math.radians(angle)) * 100  # Scale for visibility
    fred.goto(angle, y)

# Draw x-axis
fred.penup()
fred.goto(-360, 0)
fred.pendown()
fred.goto(360, 0)

# Draw y-axis
fred.penup()
fred.goto(0, -120)
fred.pendown()
fred.goto(0, 120)

# Hide the turtle
fred.hideturtle()

# Keep the window open
screen.mainloop()

```

---

### **Task 6: Sine Wave Plus (4 marks)**
To extend the sine wave by adding values to the axes:
```python
import turtle
import math

# Set up the turtle screen
turtle.setup(800, 400)
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
fred = turtle.Turtle()
fred.speed(0)  # Fastest speed
fred.penup()

# Move to the starting position
fred.goto(-360, 0)
fred.pendown()

# Draw the sine wave
for angle in range(-360, 361, 5):  # Step by 5 for smoother curve
    y = math.sin(math.radians(angle)) * 100  # Scale for visibility
    fred.goto(angle, y)

# Draw x-axis
fred.penup()
fred.goto(-360, 0)
fred.pendown()
fred.goto(360, 0)

# Label the x-axis
x_labels = [-360, -270, -180, -90, 0, 90, 180, 270, 360]
for x in x_labels:
    fred.penup()
    fred.goto(x, -15)  # Move slightly below the axis
    fred.write(str(x), align="center", font=("Arial", 10, "normal"))

# Draw y-axis
fred.penup()
fred.goto(0, -120)
fred.pendown()
fred.goto(0, 120)

# Label the y-axis
y_labels = [-100, -50, 0, 50, 100]  # Equivalent to -1 to 1
for y in y_labels:
    fred.penup()
    fred.goto(10, y)  # Move slightly right of the axis
    fred.write(str(y / 100), align="left", font=("Arial", 10, "normal"))  # Convert back to -1 to 1 scale

# Hide the turtle
fred.hideturtle()

# Keep the window open
screen.mainloop()

```

---
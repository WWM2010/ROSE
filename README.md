# 🌸 Rose Curve Flower Plot

This project demonstrates how to generate and visualize a **rose curve** (also known as a rhodonea curve) using Python, NumPy, and Matplotlib. Rose curves are mathematical curves that create beautiful flower-like patterns depending on the parameter `k`.

---

## 📖 How It Works

1. **Angle Range**  
   - We define `theta` as a set of angles from `0` to `2π`.  (example of using my 1bac sm lessons "Calcule tigonometrique ")
   - This gives us the domain for plotting the curve.

2. **Rose Curve Function**  
   - The rose curve equation in polar coordinates is:  
     \[
     r = \sin(k \cdot \theta)
     \]
   - The parameter `k` controls the number of petals:
     - If `k` is **odd**, the curve has `k` petals.
     - If `k` is **even**, the curve has `2k` petals.

3. **Convert Polar to Cartesian**  
   - Using the equations:
     \[
     x = r \cdot \cos(\theta), \quad y = r \cdot \sin(\theta)
     \]
   - This allows us to plot the curve in standard Cartesian coordinates.

4. **Plotting**  
   - The curve is plotted in magenta with equal axis scaling.
   - The figure is titled according to the number of petals.

---

## 🖼️ Example Output

For `k = 5`, the plot generates a flower with **5 petals**:

```python
k = 5
```
5.**Installation**
```python
pip install numpy matplotlib
```
6.**This is an example with k = 20:**



<img width="593" height="671" alt="image" src="https://github.com/user-attachments/assets/7d82f89f-2c11-4ac1-a943-ffe1452b7e07" />



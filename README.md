# optimization-demonstration
A showcase of my passion for mathematical optimization and real-world business applications by using computer science and mathematics tools to solve complex logistics and supply chain concerns.

# 🧠 Optimization Project: Maximize Production with Limited Shared Materials

## 📌 Use Case

A factory produces 10 different products (A–J), each requiring a unique mix of 6 raw materials. Two materials — **Material 3** and **Material 5** — are shared across all products and are in **limited supply**. This creates a bottleneck, requiring an optimized production plan that maximizes total output without exceeding material constraints.

---

## 🎯 Objective

- Maximize the total number of product units manufactured
- Respect inventory limits for shared materials

---

## 📥 Inputs

- 10 products: A to J
- Material usage per product (6 types of raw materials)
- Limited quantities of Material 3 (50 units) and Material 5 (40 units)

---

## 📤 Output

- Optimal quantity of each product to produce
- Total number of units manufactured
- Summary in table format (DataFrame)

---

## 🛠️ Technologies Used

- Python 3
- PuLP (`pip install pulp`)
- pandas (`pip install pandas`)

---

## 💻 How It Works

1. Define each product’s usage of materials
2. Create decision variables for each product
3. Add constraints for limited materials
4. Set the objective to maximize total units produced
5. Solve using PuLP’s linear programming solver

---

## 📊 Sample Output

```
🧮 Optimization Status: Optimal

📊 Optimal Production Plan:

✅ Produce 10 units of Product F
✅ Produce 4 units of Product D
✅ Produce 4 units of Product G
✅ Produce 3 units of Product H
✅ Produce 2 units of Product B

🔢 Total Units Produced: 23
```

---

## 🔍 Notes

- This version uses integer programming — results are realistic for manufacturing
- Material constraints drive prioritization of efficient products
- Easily extendable with profit, cost, or labor constraints

---

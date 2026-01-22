let allExpenses = [];

function formatAmount(x) {
  return Number(x).toFixed(2);
}

function getTodayDate() {
  const d = new Date();
  const yyyy = d.getFullYear();
  const mm = String(d.getMonth() + 1).padStart(2, "0");
  const dd = String(d.getDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
}

function renderTable(expenses) {
  const tbody = document.getElementById("expenseTableBody");
  tbody.innerHTML = "";

  expenses.forEach((exp, index) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${index + 1}</td>
      <td>${exp.date}</td>
      <td>${exp.category}</td>
      <td>₹${formatAmount(exp.amount)}</td>
      <td>${exp.note || ""}</td>
      <td>
        <button class="delete-btn" onclick="deleteExpense(${exp.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(row);
  });

  document.getElementById("totalEntries").innerText = expenses.length;
}

async function loadExpenses() {
  const res = await fetch("/expenses");
  const data = await res.json();

  allExpenses = data;
  renderTable(allExpenses);

  let total = 0;
  let todayTotal = 0;
  const today = getTodayDate();

  allExpenses.forEach(exp => {
    total += Number(exp.amount);
    if (exp.date === today) todayTotal += Number(exp.amount);
  });

  document.getElementById("totalSpent").innerText = formatAmount(total);
  document.getElementById("todaySpent").innerText = formatAmount(todayTotal);
}

document.getElementById("expenseForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const amount = parseFloat(document.getElementById("amount").value);
  const category = document.getElementById("category").value;
  const date = document.getElementById("date").value;
  const note = document.getElementById("note").value;

  await fetch("/expenses", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount, category, date, note })
  });

  document.getElementById("expenseForm").reset();
  document.getElementById("date").value = getTodayDate();

  loadExpenses();
});

document.getElementById("searchInput").addEventListener("input", (e) => {
  const q = e.target.value.toLowerCase().trim();

  const filtered = allExpenses.filter(exp =>
    exp.category.toLowerCase().includes(q) ||
    (exp.note || "").toLowerCase().includes(q) ||
    exp.date.toLowerCase().includes(q)
  );

  renderTable(filtered);
});

async function deleteExpense(id) {
  const confirmDelete = confirm("Delete this expense?");
  if (!confirmDelete) return;

  await fetch(`/expenses/${id}`, { method: "DELETE" });
  loadExpenses();
}

/* Auto set today's date */
document.getElementById("date").value = getTodayDate();
loadExpenses();

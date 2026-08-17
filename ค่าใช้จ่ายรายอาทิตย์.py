<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weekly Budget Planner</title>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: Arial, "Noto Sans Thai", sans-serif;
    }

    body {
      background: #f4f7fb;
      color: #1f2937;
      min-height: 100vh;
    }

    header {
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      color: white;
      padding: 28px 20px 70px;
      text-align: center;
    }

    header h1 {
      font-size: 28px;
      margin-bottom: 8px;
    }

    header p {
      opacity: .9;
    }

    .container {
      width: min(1000px, 94%);
      margin: -45px auto 40px;
    }

    .card {
      background: white;
      border-radius: 20px;
      padding: 22px;
      box-shadow: 0 10px 30px rgba(0,0,0,.08);
      margin-bottom: 20px;
    }

    .balance {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 15px;
    }

    .stat {
      padding: 20px;
      border-radius: 16px;
      background: #f8fafc;
    }

    .stat span {
      display: block;
      color: #64748b;
      font-size: 14px;
      margin-bottom: 8px;
    }

    .stat strong {
      font-size: 25px;
    }

    .income strong {
      color: #16a34a;
    }

    .expense strong {
      color: #ef4444;
    }

    .remaining strong {
      color: #2563eb;
    }

    h2 {
      margin-bottom: 18px;
      font-size: 21px;
    }

    .input-group {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 15px;
    }

    label {
      display: block;
      font-size: 14px;
      font-weight: bold;
      margin-bottom: 7px;
    }

    input, select {
      width: 100%;
      padding: 13px;
      border: 1px solid #dbe1ea;
      border-radius: 12px;
      font-size: 16px;
      outline: none;
    }

    input:focus, select:focus {
      border-color: #2563eb;
    }

    button {
      border: none;
      border-radius: 12px;
      padding: 13px 20px;
      cursor: pointer;
      font-size: 15px;
      font-weight: bold;
      transition: .2s;
    }

    button:hover {
      transform: translateY(-1px);
      opacity: .9;
    }

    .primary {
      background: #2563eb;
      color: white;
    }

    .danger {
      background: #fee2e2;
      color: #dc2626;
      padding: 8px 12px;
    }

    .budget-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 15px;
    }

    .budget-item {
      background: #f8fafc;
      border-radius: 15px;
      padding: 16px;
    }

    .budget-top {
      display: flex;
      justify-content: space-between;
      margin-bottom: 10px;
    }

    .budget-name {
      font-weight: bold;
    }

    .budget-money {
      color: #64748b;
      font-size: 14px;
    }

    .progress {
      height: 9px;
      background: #e5e7eb;
      border-radius: 20px;
      overflow: hidden;
    }

    .progress-bar {
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #7c3aed);
      border-radius: 20px;
      transition: .3s;
    }

    .progress-bar.over {
      background: #ef4444;
    }

    .transaction {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px 0;
      border-bottom: 1px solid #edf0f4;
    }

    .transaction:last-child {
      border-bottom: none;
    }

    .transaction-info {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .icon {
      width: 42px;
      height: 42px;
      display: grid;
      place-items: center;
      border-radius: 12px;
      background: #eff6ff;
      font-size: 20px;
    }

    .transaction-info small {
      color: #64748b;
      display: block;
      margin-top: 4px;
    }

    .amount {
      color: #ef4444;
      font-weight: bold;
      margin-right: 10px;
    }

    .empty {
      text-align: center;
      color: #94a3b8;
      padding: 30px;
    }

    .auto-budget {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
      margin-top: 15px;
    }

    .auto-budget button {
      background: #eef2ff;
      color: #4338ca;
    }

    .category-row {
      margin-bottom: 15px;
    }

    .category-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 7px;
    }

    .summary {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    .summary-box {
      padding: 20px;
      background: #f8fafc;
      border-radius: 15px;
    }

    .summary-box h3 {
      margin-bottom: 10px;
    }

    .summary-box p {
      color: #64748b;
    }

    @media (max-width: 700px) {
      header h1 {
        font-size: 23px;
      }

      .balance {
        grid-template-columns: 1fr;
      }

      .input-group,
      .budget-grid,
      .summary {
        grid-template-columns: 1fr;
      }

      .auto-budget {
        grid-template-columns: repeat(2, 1fr);
      }

      .transaction {
        gap: 10px;
      }
    }
  </style>
</head>

<body>

<header>
  <h1>💰 Weekly Budget</h1>
  <p>แอปจัดสรรค่าใช้จ่ายรายอาทิตย์</p>
</header>

<div class="container">

  <!-- สรุปเงิน -->
  <div class="card">
    <div class="balance">

      <div class="stat income">
        <span>💵 เงินทั้งหมด</span>
        <strong id="totalIncome">฿0</strong>
      </div>

      <div class="stat expense">
        <span>💸 ใช้ไปแล้ว</span>
        <strong id="totalExpense">฿0</strong>
      </div>

      <div class="stat remaining">
        <span>💰 เงินคงเหลือ</span>
        <strong id="remaining">฿0</strong>
      </div>

    </div>
  </div>

  <!-- ตั้งงบ -->
  <div class="card">
    <h2>💵 ตั้งเงินสำหรับสัปดาห์นี้</h2>

    <div class="input-group">

      <div>
        <label>จำนวนเงินทั้งหมด</label>
        <input
          type="number"
          id="incomeInput"
          placeholder="เช่น 5000"
          min="0"
        >
      </div>

      <div style="display:flex;align-items:end;">
        <button class="primary" onclick="setIncome()">
          บันทึกเงิน
        </button>
      </div>

    </div>

    <div class="auto-budget">
      <button onclick="autoBudget(50)">สมดุล 50/20/10</button>
      <button onclick="autoBudget(40)">ประหยัด</button>
      <button onclick="autoBudget(70)">เน้นใช้ชีวิต</button>
      <button onclick="clearData()">ล้างข้อมูล</button>
    </div>
  </div>

  <!-- เพิ่มรายจ่าย -->
  <div class="card">
    <h2>➕ เพิ่มรายจ่าย</h2>

    <div class="input-group">

      <div>
        <label>รายการ</label>
        <input
          type="text"
          id="expenseName"
          placeholder="เช่น ข้าวกลางวัน"
        >
      </div>

      <div>
        <label>จำนวนเงิน</label>
        <input
          type="number"
          id="expenseAmount"
          placeholder="เช่น 60"
          min="0"
        >
      </div>

      <div>
        <label>หมวดหมู่</label>
        <select id="expenseCategory">
          <option value="อาหาร">🍜 อาหาร</option>
          <option value="เดินทาง">🚗 เดินทาง</option>
          <option value="ช้อปปิ้ง">🛍️ ช้อปปิ้ง</option>
          <option value="บิล">📱 บิล / ค่าใช้จ่าย</option>
          <option value="ความบันเทิง">🎮 ความบันเทิง</option>
          <option value="อื่นๆ">📦 อื่นๆ</option>
        </select>
      </div>

      <div style="display:flex;align-items:end;">
        <button class="primary" onclick="addExpense()">
          เพิ่มรายการ
        </button>
      </div>

    </div>
  </div>

  <!-- งบประมาณ -->
  <div class="card">
    <h2>📊 การจัดสรรงบประมาณ</h2>

    <div id="budgetList"></div>
  </div>

  <!-- รายการ -->
  <div class="card">
    <h2>🧾 รายการค่าใช้จ่าย</h2>

    <div id="transactionList">
      <div class="empty">
        ยังไม่มีรายการค่าใช้จ่าย
      </div>
    </div>
  </div>

  <!-- สรุป -->
  <div class="card">
    <h2>📈 สรุปประจำสัปดาห์</h2>

    <div class="summary">

      <div class="summary-box">
        <h3>เหลือใช้ต่อวัน</h3>
        <p id="dailyBudget">฿0</p>
      </div>

      <div class="summary-box">
        <h3>ค่าใช้จ่ายเฉลี่ยต่อวัน</h3>
        <p id="dailyExpense">฿0</p>
      </div>

    </div>
  </div>

</div>

<script>
  let data = JSON.parse(
    localStorage.getItem("weeklyBudget")
  ) || {
    income: 0,
    expenses: [],
    budgets: {
      "อาหาร": 0,
      "เดินทาง": 0,
      "ช้อปปิ้ง": 0,
      "บิล": 0,
      "ความบันเทิง": 0,
      "อื่นๆ": 0
    }
  };

  const icons = {
    "อาหาร": "🍜",
    "เดินทาง": "🚗",
    "ช้อปปิ้ง": "🛍️",
    "บิล": "📱",
    "ความบันเทิง": "🎮",
    "อื่นๆ": "📦"
  };

  function saveData() {
    localStorage.setItem(
      "weeklyBudget",
      JSON.stringify(data)
    );
  }

  function money(number) {
    return new Intl.NumberFormat("th-TH", {
      style: "currency",
      currency: "THB",
      maximumFractionDigits: 0
    }).format(number || 0);
  }

  function setIncome() {
    const amount = Number(
      document.getElementById("incomeInput").value
    );

    if (amount <= 0) {
      alert("กรุณาใส่จำนวนเงิน");
      return;
    }

    data.income = amount;

    saveData();
    render();

    document.getElementById("incomeInput").value = "";
  }

  function addExpense() {
    const name =
      document.getElementById("expenseName").value.trim();

    const amount =
      Number(document.getElementById("expenseAmount").value);

    const category =
      document.getElementById("expenseCategory").value;

    if (!name || amount <= 0) {
      alert("กรุณากรอกข้อมูลให้ครบ");
      return;
    }

    data.expenses.push({
      id: Date.now(),
      name,
      amount,
      category,
      date: new Date().toLocaleDateString("th-TH")
    });

    saveData();
    render();

    document.getElementById("expenseName").value = "";
    document.getElementById("expenseAmount").value = "";
  }

  function deleteExpense(id) {
    data.expenses = data.expenses.filter(
      expense => expense.id !== id
    );

    saveData();
    render();
  }

  function autoBudget(type) {

    if (data.income <= 0) {
      alert("กรุณาตั้งเงินทั้งหมดก่อน");
      return;
    }

    let percentages;

    if (type === 40) {
      percentages = {
        "อาหาร": .30,
        "เดินทาง": .10,
        "ช้อปปิ้ง": .05,
        "บิล": .20,
        "ความบันเทิง": .05,
        "อื่นๆ": .30
      };
    }

    else if (type === 70) {
      percentages = {
        "อาหาร": .35,
        "เดินทาง": .15,
        "ช้อปปิ้ง": .15,
        "บิล": .15,
        "ความบันเทิง": .15,
        "อื่นๆ": .05
      };
    }

    else {
      percentages = {
        "อาหาร": .30,
        "เดินทาง": .15,
        "ช้อปปิ้ง": .10,
        "บิล": .15,
        "ความบันเทิง": .10,
        "อื่นๆ": .20
      };
    }

    for (const category in percentages) {
      data.budgets[category] =
        data.income * percentages[category];
    }

    saveData();
    render();
  }

  function getCategoryExpense(category) {
    return data.expenses
      .filter(item => item.category === category)
      .reduce((sum, item) => sum + item.amount, 0);
  }

  function renderBudget() {

    const container =
      document.getElementById("budgetList");

    container.innerHTML = "";

    for (const category in data.budgets) {

      const budget = data.budgets[category];
      const spent = getCategoryExpense(category);

      let percent = budget > 0
        ? (spent / budget) * 100
        : 0;

      const displayPercent =
        Math.min(percent, 100);

      const over =
        spent > budget && budget > 0;

      container.innerHTML += `
        <div class="category-row">

          <div class="category-header">

            <span>
              ${icons[category]} ${category}
            </span>

            <span>
              ${money(spent)} / ${money(budget)}
            </span>

          </div>

          <div class="progress">

            <div
              class="progress-bar ${over ? "over" : ""}"
              style="width:${displayPercent}%"
            ></div>

          </div>

          ${
            over
              ? `<small style="color:#ef4444;">
                   ⚠️ ใช้เกินงบ ${money(spent - budget)}
                 </small>`
              : ""
          }

        </div>
      `;
    }
  }

  function renderTransactions() {

    const container =
      document.getElementById("transactionList");

    if (data.expenses.length === 0) {

      container.innerHTML = `
        <div class="empty">
          ยังไม่มีรายการค่าใช้จ่าย
        </div>
      `;

      return;
    }

    const sorted =
      [...data.expenses].reverse();

    container.innerHTML = "";

    sorted.forEach(item => {

      container.innerHTML += `
        <div class="transaction">

          <div class="transaction-info">

            <div class="icon">
              ${icons[item.category]}
            </div>

            <div>
              <strong>${escapeHTML(item.name)}</strong>

              <small>
                ${item.category} • ${item.date}
              </small>
            </div>

          </div>

          <div>
            <span class="amount">
              -${money(item.amount)}
            </span>

            <button
              class="danger"
              onclick="deleteExpense(${item.id})"
            >
              ลบ
            </button>
          </div>

        </div>
      `;
    });
  }

  function render() {

    const totalExpense =
      data.expenses.reduce(
        (sum, item) => sum + item.amount,
        0
      );

    const remaining =
      data.income - totalExpense;

    document.getElementById("totalIncome")
      .textContent = money(data.income);

    document.getElementById("totalExpense")
      .textContent = money(totalExpense);

    document.getElementById("remaining")
      .textContent = money(remaining);

    const dailyBudget =
      Math.max(remaining / 7, 0);

    const dailyExpense =
      totalExpense / 7;

    document.getElementById("dailyBudget")
      .textContent = money(dailyBudget);

    document.getElementById("dailyExpense")
      .textContent = money(dailyExpense);

    renderBudget();
    renderTransactions();
  }

  function clearData() {

    const confirmDelete =
      confirm("ต้องการล้างข้อมูลทั้งหมดหรือไม่?");

    if (!confirmDelete) return;

    localStorage.removeItem("weeklyBudget");

    data = {
      income: 0,
      expenses: [],
      budgets: {
        "อาหาร": 0,
        "เดินทาง": 0,
        "ช้อปปิ้ง": 0,
        "บิล": 0,
        "ความบันเทิง": 0,
        "อื่นๆ": 0
      }
    };

    render();
  }

  function escapeHTML(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  render();
</script>

</body>
</html>
frappe.pages["expense-dashboard"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "Expense Dashboard",
    single_column: true,
  });

  // Inject Bootstrap
  let style = document.createElement("link");
  style.rel = "stylesheet";
  style.href =
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css";
  document.head.appendChild(style);

  // Add Dashboard Layout
  // Add Dashboard Layout
  $(wrapper).append(`
    <div class="container mt-4">
        <div class="card p-4 shadow-lg" style="background: #f5e3c3; border-radius: 15px; max-height: 80vh; overflow-y: auto;">
            <div class="row text-center">
                <div class="col-md-4">
                    <div class="card shadow-sm p-3 mb-3 bg-light">
                        <h5>Total Expenses</h5>
                        <h2 id="total-expense" class="text-primary">₹0</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card shadow-sm p-3 mb-3 bg-light">
                        <h5>Top Category</h5>
                        <h2 id="top-category" class="text-success">-</h2>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card shadow-sm p-3 mb-3 bg-light">
                        <h5>Total Transactions</h5>
                        <h2 id="total-transactions" class="text-danger">0</h2>
                    </div>
                </div>
            </div>

            <div class="table-responsive mt-4">
                <table class="table table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th>User ID</th>
                            <th>Amount (₹)</th>
                            <th>Category</th>
                            <th>Date</th>
                            <th>Payment Mode</th>
                        </tr>
                    </thead>
                    <tbody id="expense-table">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
`);

  load_expense_dashboard();
};

function load_expense_dashboard() {
  frappe.call({
    method: "frappe.client.get_list",
    args: {
      doctype: "Expense",
      fields: ["user_id", "amount", "category", "date", "payment_mode"],
    },
    callback: function (response) {
      if (response.message) {
        render_expense_dashboard(response.message);
      } else {
        $("#expense-table").html(
          '<tr><td colspan="5" class="text-center">No expenses found.</td></tr>'
        );
      }
    },
  });
}

function render_expense_dashboard(expenses) {
  let total_expense = 0;
  let category_summary = {};
  let table_content = "";

  expenses.forEach((exp) => {
    total_expense += parseFloat(exp.amount);
    category_summary[exp.category] =
      (category_summary[exp.category] || 0) + parseFloat(exp.amount);

    table_content += `
            <tr>
                <td>${exp.user_id}</td>
                <td>₹${exp.amount}</td>
                <td>${exp.category}</td>
                <td>${new Date(exp.date).toLocaleDateString()}</td>
                <td>${exp.payment_mode}</td>
            </tr>
        `;
  });

  let topCategory = getTopCategory(category_summary);

  $("#total-expense").text(`₹${total_expense.toFixed(2)}`);
  $("#top-category").text(topCategory || "-");
  $("#total-transactions").text(expenses.length);
  $("#expense-table").html(table_content);
}

function getTopCategory(category_summary) {
  if (Object.keys(category_summary).length === 0) return "-";
  return Object.keys(category_summary).reduce((a, b) =>
    category_summary[a] > category_summary[b] ? a : b
  );
}

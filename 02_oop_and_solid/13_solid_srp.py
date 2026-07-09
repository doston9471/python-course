# =============================================================
# LESSON 13: SOLID — S = SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# =============================================================


# --- Step 1: The VIOLATION (a "God object") -----------------
class BadInvoice:
    def __init__(self, items):
        self._items = items

    def total(self):
        return sum(price for _, price in self._items)

    def to_text(self):
        lines = [f"  {name}: ${price}" for name, price in self._items]
        return f"INVOICE\n" + "\n".join(lines) + f"\n  TOTAL: ${self.total()}"

    def save_to_file(self, path):
        return f"saved to {path}"

    def email_to(self, address):
        return f"pretend-emailing invoice to {address}"


print("--- BadInvoice (violates SRP) ---")
bad = BadInvoice([("Pen", 2), ("Notebook", 5)])
print(bad.to_text())
print(f"Total: {bad.total()}")

print("-" * 50)


# --- Step 2: The FIX — one responsibility per class ---------
class Invoice:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(price for _, price in self.items)


class InvoiceFormatter:
    def __init__(self, invoice):
        self._invoice = invoice

    def to_text(self):
        lines = [f"  {name}: ${price}" for name, price in self._invoice.items]
        return f"INVOICE\n" + "\n".join(lines) + f"\n  TOTAL: ${self._invoice.total()}"


class FileRepository:
    def save(self, content, path):
        return f"saved {len(content)} bytes to {path}"


class EmailNotifier:
    def send_to(self, address, body):
        return f"emailed {len(body.splitlines())}-line invoice to {address}"


print("--- SRP-compliant versions ---")
invoice = Invoice([("Pen", 2), ("Notebook", 5)])
text = InvoiceFormatter(invoice).to_text()
print(text)
print(FileRepository().save(text, "/tmp/invoice.txt"))
print(EmailNotifier().send_to("client@example.com", text))

print("-" * 50)


class HtmlInvoiceFormatter:
    def __init__(self, invoice):
        self._invoice = invoice

    def to_html(self):
        rows = "".join(f"<li>{n}: ${p}</li>" for n, p in self._invoice.items)
        return f"<h1>Invoice</h1><ul>{rows}</ul><p>Total: ${self._invoice.total()}</p>"


print("New HTML formatter, zero changes elsewhere:")
print(HtmlInvoiceFormatter(invoice).to_html())

print("-" * 50)


print("""SRP RECAP
---------
One class = one responsibility = one reason to change.""")

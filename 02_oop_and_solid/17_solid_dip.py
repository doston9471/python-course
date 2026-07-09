# =============================================================
# LESSON 17: SOLID — D = DEPENDENCY INVERSION PRINCIPLE (DIP)
# =============================================================


# --- Step 1: The VIOLATION ----------------------------------
class MySQLDatabase:
    def save(self, record):
        return f"MySQL: saved {record}"


class SmtpMailer:
    def send_mail(self, to, msg):
        return f"SMTP: '{msg}' -> {to}"


class OrderServiceBad:
    def __init__(self):
        self._db = MySQLDatabase()
        self._mailer = SmtpMailer()

    def place(self, order, email):
        return [self._db.save(order), self._mailer.send_mail(email, f"Order placed: {order}")]


print("--- OrderServiceBad (violates DIP) ---")
print(OrderServiceBad().place("Widget", "a@x.com"))

print("-" * 50)


# --- Step 2: The FIX — depend on abstractions, inject details
class OrderService:
    def __init__(self, repository, notifier):
        self._repository = repository
        self._notifier = notifier

    def place(self, order, email):
        saved = self._repository.save(order)
        sent = self._notifier.notify(email, f"Order placed: {order}")
        return [saved, sent]


class PostgresRepository:
    def save(self, record):
        return f"Postgres: saved {record}"


class S3Repository:
    def save(self, record):
        return f"S3: stored {record}"


class EmailNotifier:
    def notify(self, to, msg):
        return f"Email: '{msg}' -> {to}"


class SmsNotifier:
    def notify(self, to, msg):
        return f"SMS: '{msg}' -> {to}"


print("--- OrderService (DIP-compliant) ---")
svc = OrderService(PostgresRepository(), EmailNotifier())
print(svc.place("Widget", "a@x.com"))

svc2 = OrderService(S3Repository(), SmsNotifier())
print(svc2.place("Gadget", "555-1234"))

print("-" * 50)


class FakeRepository:
    def __init__(self):
        self.saved = []

    def save(self, record):
        self.saved.append(record)
        return "fake-saved"


class FakeNotifier:
    def __init__(self):
        self.messages = []

    def notify(self, to, msg):
        self.messages.append([to, msg])
        return "fake-sent"


fake_repo = FakeRepository()
fake_note = FakeNotifier()
OrderService(fake_repo, fake_note).place("TestItem", "t@x.com")

print(f"Test: repo recorded {fake_repo.saved}")
print(f"Test: notifier recorded {fake_note.messages}")

print("-" * 50)


print("""DIP RECAP
---------
High-level policy depends on abstractions; inject concrete details.""")

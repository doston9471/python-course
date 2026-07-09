# =============================================================
# LESSON 18: SOLID CAPSTONE — A NOTIFICATION / ORDER PIPELINE
# =============================================================

from abc import ABC, abstractmethod


class Order:
    def __init__(self, id, customer, email, amount):
        self.id, self.customer, self.email, self.amount = id, customer, email, amount

    def __str__(self):
        return f"Order #{self.id} ({self.customer}, ${self.amount:.2f})"


class OrderValidator:
    def validate(self, order):
        if order.amount <= 0:
            raise ValueError("amount must be positive")
        if not order.email:
            raise ValueError("email required")
        return True


class PaymentMethod(ABC):
    @abstractmethod
    def charge(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, last4):
        self.last4 = last4

    def charge(self, amount):
        return f"charged ${amount:.2f} to card ****{self.last4}"


class PayPal(PaymentMethod):
    def __init__(self, account):
        self.account = account

    def charge(self, amount):
        return f"charged ${amount:.2f} via PayPal ({self.account})"


class StoreCredit(PaymentMethod):
    def charge(self, amount):
        return f"deducted ${amount:.2f} from store credit"


class Channel(ABC):
    @abstractmethod
    def deliver(self, to, message):
        pass


class Repository(ABC):
    @abstractmethod
    def save(self, order):
        pass


class EmailChannel(Channel):
    def deliver(self, to, message):
        return f"  [email] to {to}: {message}"


class SmsChannel(Channel):
    def deliver(self, to, message):
        return f"  [sms]   to {to}: {message}"


class PushChannel(Channel):
    def deliver(self, to, message):
        return f"  [push]  to {to}: {message}"


class InMemoryRepository(Repository):
    def __init__(self):
        self.orders = []

    def save(self, order):
        self.orders.append(order)
        return f"  saved {order}"


class OrderProcessor:
    def __init__(self, validator, repository, channels):
        self._validator = validator
        self._repository = repository
        self._channels = channels

    def process(self, order, payment):
        log = []
        self._validator.validate(order)
        log.append(f"  payment: {payment.charge(order.amount)}")
        log.append(self._repository.save(order))
        for ch in self._channels:
            log.append(ch.deliver(order.email, f"Your {order} is confirmed"))
        return f"Processed {order}\n" + "\n".join(log)


repo = InMemoryRepository()
processor = OrderProcessor(
    OrderValidator(),
    repo,
    [EmailChannel(), SmsChannel()],
)

o1 = Order(1, "Alice", "alice@x.com", 49.99)
o2 = Order(2, "Bob", "bob@x.com", 12.00)

print(processor.process(o1, CreditCard("4242")))
print("-" * 50)
print(processor.process(o2, PayPal("bob@pp")))
print("-" * 50)

push_processor = OrderProcessor(
    OrderValidator(),
    repo,
    [EmailChannel(), PushChannel()],
)
o3 = Order(3, "Carol", "carol@x.com", 5.00)
print(push_processor.process(o3, StoreCredit()))
print("-" * 50)

try:
    bad = Order(4, "Dave", "", -1)
    processor.process(bad, CreditCard("0000"))
except ValueError as e:
    print(f"Rejected bad order: {e}")
print("-" * 50)


class FakeChannel(Channel):
    def __init__(self):
        self.sent = []

    def deliver(self, to, message):
        self.sent.append([to, message])
        return "ok"


fake = FakeChannel()
OrderProcessor(
    OrderValidator(),
    InMemoryRepository(),
    [fake],
).process(Order(99, "Test", "t@x.com", 1.0), StoreCredit())

print(f"Test: FakeChannel recorded {len(fake.sent)} message(s): {fake.sent}")
print(f"Repo now holds {len(repo.orders)} real orders.")

print("-" * 50)

print("""SOLID CAPSTONE — what you just saw
----------------------------------
[S] SRP  [O] OCP  [L] LSP  [I] ISP  [D] DIP
Together: small, focused, swappable, testable objects. 🎓""")

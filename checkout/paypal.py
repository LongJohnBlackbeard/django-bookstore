import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Aazg1gY6lYwWnScngQ0OFX6REqxjGR0CMC59f5cL1-Td5jgYddQBrYPy1agazAZl6mykJHJ45WzZL3qk"
        self.client_secret = "EKJrZCxR8NDyW4-HD-y9rl3GpyMHCHwVxQHrivbK8Vtb2kPjYYYKTtlUS043zSEJAYJFrXCMff89pdlJ"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)

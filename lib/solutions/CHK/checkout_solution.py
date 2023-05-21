

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from challenges.checkoutCalculator import CheckoutCalculator
    calculator = CheckoutCalculator()
    return calculator.computeCost(skus)



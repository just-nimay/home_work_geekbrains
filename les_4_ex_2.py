import sys
import utils


input_ = sys.argv[1]
data, value = utils.currency_rates(input_)
print(value, data)

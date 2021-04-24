# Working with locale in Python


## Example
```(python3)
import locale


# Current locale
locale.getlocale()  # ('en_US', 'UTF-8')

# Set up locale to 'ru_RU.UTF-8'
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

# Current locale
locale.getlocale()  # ('ru_RU', 'UTF-8')

# Format digit to locale format
locale.format_string("%d", 9531479, grouping=True, monetary=True)  # 9 531 479

# Currency symbol  for current locale
locale.localeconv()["currency_symbol"]  # ₽

# Format digits and floats to locale format
locale.format_string("%.2f", 1234567.30, grouping=True)  # 1 234 567,30
locale.format_string("%d", 9531479, grouping=True)  # 9 531 479

# Reset locale
locale.resetlocale(locale.LC_ALL)

# Current locale
locale.getlocale()  # ('en_US', 'UTF-8')
```

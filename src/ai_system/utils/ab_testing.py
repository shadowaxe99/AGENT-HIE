```python
import numpy as np
from scipy import stats

class ABTesting:
    def __init__(self, group_a, group_b):
        self.group_a = group_a
        self.group_b = group_b

    def perform_ttest(self):
        t_stat, p_val = stats.ttest_ind(self.group_a, self.group_b)
        return t_stat, p_val

    def calculate_conversion_rate(self, group):
        conversions = sum(group)
        total_users = len(group)
        return conversions / total_users

    def report_results(self):
        t_stat, p_val = self.perform_ttest()
        conversion_rate_a = self.calculate_conversion_rate(self.group_a)
        conversion_rate_b = self.calculate_conversion_rate(self.group_b)

        print(f"Conversion rate for Group A: {conversion_rate_a}")
        print(f"Conversion rate for Group B: {conversion_rate_b}")
        print(f"T-statistic: {t_stat}")
        print(f"P-value: {p_val}")

        if p_val < 0.05:
            print("There is a significant difference between the two groups.")
        else:
            print("There is no significant difference between the two groups.")
```

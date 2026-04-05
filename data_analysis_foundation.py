class DataAnalyzer:
    """
    A simple OOP structure for basic data analysis operations.
    Created by Fikret.
    """

    def __init__(self, dataset_name, values):
        self.dataset_name = dataset_name
        self.values = values

    def calculate_mean(self):
        if not self.values:
            return 0
        return sum(self.values) / len(self.values)

    def display_summary(self):
        mean_value = self.calculate_mean()
        print(f"\n--- Summary for: {self.dataset_name} ---")
        print(f"Total elements: {len(self.values)}")
        print(f"Arithmetic Mean: {mean_value:.2f}")
        print("Status: Successfully Processed")
        print("-" * 30)


# Testing the Class with sample data
math_scores = DataAnalyzer("Algebra Finals", [86, 91, 78, 90, 88])
math_scores.display_summary()

# Another instance for practice
trading_pnl = DataAnalyzer("ICT Strategy Trades", [150, -50, 200, 120, -30])
trading_pnl.display_summary()

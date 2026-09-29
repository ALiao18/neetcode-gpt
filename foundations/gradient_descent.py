class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        x = init

        def df_dx(x):
            return 2*x

        for i in range(iterations):
            x = x - learning_rate * df_dx(x)
        
        print(x)
        return round(x, 5)

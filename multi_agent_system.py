import os
import yfinance as yf
import matplotlib.pyplot as plt
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class Researcher:
    def __init__(self):
        self.data = None

    def fetch_data(self, ticker, start_date, end_date):
        self.data = yf.download(ticker, start=start_date, end=end_date)
        return self.data

class Coder:
    def __init__(self):
        self.plot = None

    def plot_data(self, data):
        self.plot = data['Close'].plot(title='SCHG Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.show()

class Supervisor:
    def __init__(self):
        self.researcher = Researcher()
        self.coder = Coder()

    def execute_task(self, task_description):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": task_description}
            ]
        )
        print(response['choices'][0]['message']['content'])

    def run(self):
        # Step 1: Researcher fetches data
        data = self.researcher.fetch_data('SCHG', '2019-01-01', '2024-05-01')
        
        # Step 2: Supervisor coordinates the task
        self.execute_task("Find the historical prices of SCHG for the last 5 years from Yahoo Finance.")
        
        # Step 3: Coder plots the data
        self.coder.plot_data(data)

# Run the supervisor to manage the workflow
if __name__ == "__main__":
    supervisor = Supervisor()
    supervisor.run()

import pandas as pd
import matplotlib.pyplot as plt


# Function to read data, filter by date, and plot trading volume
def plot_trading_volume(file_path, start_date, end_date):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter the DataFrame for the specified date range
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df_filtered = df[mask]

    # Sort the filtered DataFrame by date
    df_filtered = df_filtered.sort_values(by='Date')

    # Plot the trading volume
    plt.figure(figsize=(12, 6))
    plt.bar(df_filtered['Date'], df_filtered['Volume'], color='green')
    plt.xlabel('Date')
    plt.ylabel('Trading Volume')
    plt.title('Trading Volume of Alphabet Inc. (GOOGL) Stock')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Example usage
file_path = r'D:\HITECH NAVTTC\TASK QUESTIONS\dataset_task3_alphabet_stock_data.csv'
start_date = '04-01-2020'  # Replace with your start date
end_date = '04-09-2020'  # Replace with your end date

plot_trading_volume(file_path, start_date, end_date)

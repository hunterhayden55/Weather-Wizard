import pandas as pd
import matplotlib.pyplot as plt

# Read the file
file_path = "SacTemps.txt"

# Modified reading approach to handle both formats
df = pd.read_csv(file_path, skiprows=3, sep='\s+', header=None, 
                 usecols=[0, 1, 2, 3],  # Only read the first 4 columns
                 names=['Date', 'Temp High (°F)', 'Temp Low (°F)', 'Precip (in)'])

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index for the DataFrame
df.set_index('Date', inplace=True)

# Remove any rows where temperature values are invalid (e.g., less than -100 or greater than 150)
df = df[
    (df['Temp High (°F)'].between(-100, 150)) & 
    (df['Temp Low (°F)'].between(-100, 150))
]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Temp High (°F)'], label="High Temp", alpha=0.7)
plt.plot(df.index, df['Temp Low (°F)'], label="Low Temp", alpha=0.7)
plt.legend()
plt.title("Temperature Trends in Sacramento")
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.show()

# Step 7: Optional - Plot Precipitation, if desired
#plt.figure(figsize=(12, 6))
#plt.plot(df.index, df['Precip (in)'], label="Precipitation (in)", color='blue')
#plt.legend()
#plt.title("Precipitation in Sacramento")
#plt.xlabel("Date")
#plt.ylabel("Precipitation (inches)")
#plt.savefig("Precipitation_Sacramento.png")  # Save the plot as an image file
#plt.show()


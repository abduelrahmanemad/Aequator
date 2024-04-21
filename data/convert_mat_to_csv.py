import scipy.io
import pandas as pd

# Load the MATLAB .mat file
mat_data = scipy.io.loadmat(r"C:\Faculty Materials\3rd year\DSP\Equalizer\data\MLII\3 AFL\202m (0).mat")  # Replace 'your_file.mat' with the path to your .mat file

# Extract the data from the loaded mat file
data = mat_data['val']  # Replace 'your_variable' with the variable name in the .mat file

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)
print(df)
# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)  # Replace 'output.csv' with the desired output file name

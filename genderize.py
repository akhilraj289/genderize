import pandas as pd
import nltk

# Download NLTK resources (uncomment and run once if not downloaded)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Load the feedback data from CSV into a pandas DataFrame
file_path = 'home/paper_plane/genderize.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Define the keywords and corresponding categories
keyword_categories = {
    'good': 'Positive',
    'excellent': 'Positive',
    'bad': 'Negative',
    'terrible': 'Negative'
}

# Function to categorize feedback based on keywords
def categorize_feedback(feedback):
    for word, category in keyword_categories.items():
        if word in feedback.lower():
            return category
    return 'Neutral'

# Apply the categorize_feedback function to the feedback column
df['Category'] = df['intention'].apply(categorize_feedback)

# Save the updated DataFrame with categories to a new CSV file
output_file_path = 'home/paper_plane/file.csv'  # Replace with the desired output file path
df.to_csv(output_file_path, index=False)

print("Categorization completed. Output file saved.")

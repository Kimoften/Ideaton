from openai import OpenAI
import csv

client = OpenAI()

# Retrieve embedding for the given text
response = client.embeddings.create(
    input="embedding for the given text",
    model="text-embedding-3-small"
)

# Extract the embedding data
embedding = response.data[0].embedding

# Specify the CSV file name
filename = 'PDB.csv'

# Open the CSV file in append mode
with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    # Write the embedding data to the CSV file
    writer.writerow(embedding)

print("Embedding data added to", filename)

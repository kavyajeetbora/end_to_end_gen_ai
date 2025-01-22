import ollama
import os


model = 'llama3.2:3b'

input_file = ".//data/grocery_list.txt"
output_file = ".//data/categorized_grocery_list.txt"

if os.path.exists(input_file):
    with open(input_file, "r") as file_handler:
        items = file_handler.read().strip()

# Prepare the prompt for the model
prompt = f"""
You are an assistant that categorizes and sorts grocery items.

Here is a list of grocery items:

{items}

Please:

1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
2. Sort the items alphabetically within each category.
3. Present the categorized list in a clear and organized manner, using bullet points or numbering.

"""

try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")

    with open(output_file, "w") as txt_file:
        txt_file.write(generated_text.strip())

    print(f"Output written to {output_file}")  

except Exception as e:
    print("There was some problem in generating the response")
    print("Error: ", e)
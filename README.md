ASCII Art Reconstruction using Run-Length Decoding (Python)

📌 Project Overview

This project reconstructs a large ASCII art image from pre-analyzed data using pure Python loops and conditions.

The ASCII art is stored in a compressed format where each row is represented as a list of tuples:

(count, character)

This technique is known as Run-Length Encoding (RLE). The program performs the reverse process, decoding, to rebuild the original ASCII image.

🧠What is Run-Length Decoding?

Instead of storing characters repeatedly like this:

#####%%%%%***

We store them as:

[(5, '#'), (5, '%'), (3, '*')]

This saves space and makes large ASCII images easier to analyze and rebuild.

📂 Project Structure
ascii-art-reconstruction/
│
├── ascii.py   # Main Python file
├── README.md                 # Project documentation

🧾 Data Format Explanation

Each row of the ASCII art is stored as:

[(count1, symbol1), (count2, symbol2), ...]

Example:
[(35,'#'), (3,'%'), (3,'#')]

This means:

Print # 35 times

Then % 3 times

Then # 3 times

⚙️ How the Program Works

The program follows three simple loops:

🔁 Loop 1 – Row Loop

Iterates through each row of compressed data.

🔁 Loop 2 – Group Loop

Iterates through each (count, symbol) tuple in the row.

🔁 Loop 3 – Character Loop

Repeats the symbol count times and appends it to the output line.

After processing all groups, the complete row is printed.

▶️ How to Run the Program
1️⃣ Make sure Python is installed

Check using:

python --version

2️⃣ Run the script
python ascii_reconstruction.py

3️⃣ Output

The terminal will print the fully reconstructed ASCII art, line by line.

🧩 Key Function Used
def reconstruct_ascii_art():

This function:

Reads compressed ASCII data

Decodes each row using loops

Prints the final ASCII image

✅ Features

- Uses only loops and conditions
- No external libraries
- Beginner-friendly logic
- Handles large ASCII images
- Demonstrates real image compression logic

🎯 Learning Outcomes

By studying this project, you will learn:

Run-Length Encoding and Decoding

Nested loops in Python

String reconstruction

ASCII image processing

How compression works internally


🚀 Possible Enhancements

Save reconstructed art to a .txt file

Add re-encoding (compression) feature

Visualize character density

Animate ASCII reconstruction

Add color support (ANSI codes)

👤 Author

Author

Modit Kumar Vishwakarma

Learning Python, logic building, and ASCII image processing.






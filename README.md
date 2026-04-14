🧹 Easy Menu-Driven Python Tool

A simple and beginner-friendly Python tool to clean and process text files.
No command-line knowledge is required — just run the script and choose options from a menu.

🚀 Features
Remove extra spaces (multiple → single)
Remove special characters (~!@#$%^&*())
Remove empty lines
Remove duplicate lines
Search only – count how many times a word appears (without modifying the file)
Search & Replace – replace full words (case-insensitive)
Word count – total number of words in the file
ALL option – perform all cleaning + search/replace in one step

👨‍💻 Who Is This For?

Anyone working with messy text files (logs, notes, data exports)
Beginners learning Python
Freelancers offering file-cleaning or automation services

⚙️ Requirements

Windows / Mac / Linux
Python 3.6 or higher
📥 Installation & Usage

1️⃣ Save the Script

Save your Python file as:

text_processor.py

2️⃣ Run the Script

Windows:

python text_processor.py

Mac/Linux:

python3 text_processor.py

3️⃣ Menu Interface
==================================================
📁 TEXT FILE PROCESSOR MENU
==================================================

1. Remove extra spaces
2. Remove special characters (~!@#$%^&*())
3. Remove empty lines
4. Remove duplicate lines
5. Search only (count word occurrences)
6. Search & Replace (full word)
7. Word count only
8. ALL (cleaning + search & replace)
9. Exit

==================================================

📌 User Input

The program will ask for:

Input file name (e.g., myfile.txt)
Output file name (e.g., cleaned.txt)
Search word (for options 5, 6, 8)
Replace word (for options 6, 8)

🧪 Example

Input (myfile.txt)
Hello I, how are you?
maintain your health.

~!@#$%^&*() special chars
I I I I
🔍 Option 5 (Search Only)

Search word: I

Output:

Word 'I' appears 5 times
⚡ Option 8 (ALL)

Search: I
Replace: You

Output (cleaned.txt):

Hello You, how are you?

special chars

You You You You

📊 Output Summary Example

✅ Output saved to: cleaned.txt

📊 Summary:
- Removed extra spaces
- Removed special characters
- Removed 1 empty line
- Removed 0 duplicate lines
- Replaced 'I' with 'You'
💼 Custom Work / Freelancing

If you need advanced features, I can help with:

Bulk file processing

CSV / Excel support

Convert script to .exe (no Python installation needed)

Custom automation tools


📧 Email: ghulamali31@gmail.com

👤 Author: Ghulam Ali

GitHub: ghulamali-786

📜 License

MIT License — free to use, modify, and distribute.

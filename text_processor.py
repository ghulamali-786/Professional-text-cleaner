#!/usr/bin/env python3
"""
Multi-Function Text File Processor
Customer can choose specific operations or run all.
Now includes: Search word count only (without replacement)
"""

import os
import re

# ---------- Helper Functions ----------
def remove_extra_spaces(text):
    return " ".join(text.split())

def remove_special_chars(text):
    return re.sub(r'[~!@#$%^&*()]', '', text)

def remove_empty_lines(lines):
    return [line for line in lines if line.strip() != ""]

def remove_duplicate_lines(lines):
    seen = set()
    unique = []
    for line in lines:
        if line not in seen:
            seen.add(line)
            unique.append(line)
    return unique

def word_count(text):
    return len(text.split())

def search_only_count(lines, search_word):
    """Count occurrences of search word (full word, case-insensitive) without modifying"""
    pattern = r'\b' + re.escape(search_word) + r'\b'
    total = 0
    for line in lines:
        total += len(re.findall(pattern, line, flags=re.IGNORECASE))
    return total

def search_replace_in_text(text, search, replace):
    pattern = r'\b' + re.escape(search) + r'\b'
    return re.sub(pattern, replace, text, flags=re.IGNORECASE)

# ---------- Main Processing ----------
def process_file(input_file, output_file, operations, search=None, replace=None, just_search=False):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    processed_lines = lines.copy()
    stats = {}

    # If just_search mode: count and return without writing
    if just_search and search:
        count = search_only_count(processed_lines, search)
        print(f"\n🔍 Word '{search}' appears {count} times in '{input_file}'")
        return

    # Apply operations
    for op in operations:
        if op == 'spaces':
            processed_lines = [remove_extra_spaces(line) for line in processed_lines]
            stats['spaces'] = "Removed extra spaces"
        elif op == 'special':
            processed_lines = [remove_special_chars(line) for line in processed_lines]
            stats['special'] = "Removed special chars"
        elif op == 'empty':
            before = len(processed_lines)
            processed_lines = remove_empty_lines(processed_lines)
            stats['empty'] = f"Removed {before - len(processed_lines)} empty lines"
        elif op == 'duplicate':
            before = len(processed_lines)
            processed_lines = remove_duplicate_lines(processed_lines)
            stats['duplicate'] = f"Removed {before - len(processed_lines)} duplicate lines"
        elif op == 'searchreplace' and search and replace:
            processed_lines = [search_replace_in_text(line, search, replace) for line in processed_lines]
            count = search_only_count(processed_lines, search)  # count after replacement? Actually count original? We'll count after replace for info
            stats['searchreplace'] = f"Replaced '{search}' with '{replace}'"
        elif op == 'wordcount':
            full_text = "".join(processed_lines)
            wc = word_count(full_text)
            stats['wordcount'] = f"Total words: {wc}"

    # Write output
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print(f"\n✅ Output saved to: {output_file}")
        print("\n📊 Summary:")
        for key, value in stats.items():
            print(f"   - {value}")
    except Exception as e:
        print(f"Error writing: {e}")

def show_menu():
    print("\n" + "="*50)
    print("📁 TEXT FILE PROCESSOR MENU")
    print("="*50)
    print("1. Remove extra spaces")
    print("2. Remove special characters (~!@#$%^&*())")
    print("3. Remove empty lines")
    print("4. Remove duplicate lines")
    print("5. SEARCH only – count word occurrences (no replace)")
    print("6. SEARCH & REPLACE (full word)")
    print("7. Word count only (total words, no change)")
    print("8. ALL – run all cleaning + search & replace")
    print("0. Exit")
    print("="*50)

def main():
    print("\n🔧 Welcome to Text File Processor")
    input_file = input("Input file name: ").strip()
    if not os.path.exists(input_file):
        print("File not found.")
        return

    output_file = input("Output file name (for save): ").strip()
    if not output_file:
        output_file = "processed_" + input_file

    while True:
        show_menu()
        choice = input("Choose (0-8): ").strip()

        if choice == '0':
            print("Goodbye!")
            break

        # Search only (just count)
        if choice == '5':
            search_word = input("Enter word to search: ").strip()
            if not search_word:
                print("Word cannot be empty.")
                continue
            process_file(input_file, output_file, [], search=search_word, just_search=True)
            input("Press Enter...")
            continue

        # Search & Replace
        if choice == '6':
            search = input("Search word: ").strip()
            replace = input("Replace with: ").strip()
            if not search:
                continue
            process_file(input_file, output_file, ['searchreplace'], search=search, replace=replace)
            input("Press Enter...")
            continue

        # Word count only (no file change)
        if choice == '7':
            try:
                with open(input_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                wc = word_count(content)
                print(f"\n📊 Total words in '{input_file}': {wc}")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
            continue

        # All operations (including search & replace)
        if choice == '8':
            search = input("Word to search (for replace): ").strip()
            replace = input("Replace with: ").strip()
            if not search:
                print("Skipping search/replace.")
                ops = ['spaces', 'special', 'empty', 'duplicate']
            else:
                ops = ['spaces', 'special', 'empty', 'duplicate', 'searchreplace']
            process_file(input_file, output_file, ops, search=search, replace=replace)
            input("Press Enter...")
            continue

        # Single operations 1-4
        if choice in ['1','2','3','4']:
            op_map = {'1':'spaces', '2':'special', '3':'empty', '4':'duplicate'}
            process_file(input_file, output_file, [op_map[choice]])
            input("Press Enter...")
            continue

        print("Invalid choice.")

if __name__ == "__main__":
    main()
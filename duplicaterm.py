def process_file(filename):
    """
    Reads a text file with lists of filenames with extensions, determines unique filenames per row (ignoring extensions),
    and returns a list of processed lines.
    """
    processed_lines = []
    with open(filename, 'r') as f:
        for line in f:
            filenames = [name.split('.')[0] for name in line.strip().split('|')]
            unique_filenames = [filename for filename in filenames if filenames.count(filename) == 1]
            processed_lines.append('|'.join(unique_filenames))
    return processed_lines



filename = 'file.txt'  # Replace with the correct filename or path
print("Processing file:", filename)
processed_lines = process_file(filename)
print("Processed lines:")
for line in processed_lines:
    print(line)


import re

def extract_domains_from_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    domains = []
    for line in lines:
        # Menggunakan regex untuk mengambil domain
        match = re.search(r'(?<=://)([^/]+)', line)
        if match:
            domains.append(match.group(1))

    # Menyimpan hasil domain ke output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for domain in domains:
            file.write(domain + '\n')

if __name__ == "__main__":
    input_file = 'result.txt'  # File input yang berisi URL
    output_file = 'domains.txt'  # File output untuk menyimpan domain
    extract_domains_from_file(input_file, output_file)
    print(f"Domains have been saved to {output_file}")

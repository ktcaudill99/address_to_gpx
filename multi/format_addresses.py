def format_address(address):
    # This function will format the address as per your requirements.
    # Currently, it just strips extra spaces and returns the address.
    # You can add more formatting rules if needed.
    return address.strip()

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        addresses = f.readlines()

    formatted_addresses = [format_address(addr) for addr in addresses]

    with open(output_file, 'w') as f:
        for addr in formatted_addresses:
            f.write(addr + '\n')

if __name__ == "__main__":
    # Change these file names as per your setup
    input_filename = "addresses.txt"
    output_filename = "formatted_addresses.txt"
    main(input_filename, output_filename)

def decode_message(encoded_message):
    # A helper function to recursively find all possible decodings
    def helper(s, path, result):
        # If the string is empty, we have found a valid decoding
        if not s:
            result.append(''.join(path))
            return
        
        # Try to decode one digit
        if s[0] != '0':  # Skip if it starts with '0' because '0' has no mapping
            helper(s[1:], path + [chr(int(s[0]) + 64)], result)
        
        # Try to decode two digits (ensure it is a valid number between 10 and 26)
        if len(s) > 1 and '10' <= s[:2] <= '26':
            helper(s[2:], path + [chr(int(s[:2]) + 64)], result)

    result = []
    helper(encoded_message, [], result)
    return result


# Main program
if __name__ == "__main__":
    encoded_message = input("Enter the encoded message: ")
    
    # Decode the message
    decoded_messages = decode_message(encoded_message)
    
    # Display the possible decoded messages
    print("Possible decoded messages:")
    for message in decoded_messages:
        print(message)

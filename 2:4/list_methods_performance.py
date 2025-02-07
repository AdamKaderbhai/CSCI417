def find_duplicates_in_list(input_list):
    duplicates = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] == input_list[j] and input_list[i] not in duplicates:
                duplicates.append(input_list[i])
    return duplicates

# Example usage
input_list = [1, 2, 3, 4, 5, 1, 2, 6]
duplicates_list = find_duplicates_in_list(input_list)
print("Duplicates in list:", duplicates_list)
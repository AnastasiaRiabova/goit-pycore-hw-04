def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []

            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Error processing line: {line.strip()} (skipped)")

            return cats

    except FileNotFoundError:
        print(f"File at path '{path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


cats_path = "./cats_file.txt"
cats_info = get_cats_info(cats_path)
print(cats_info)

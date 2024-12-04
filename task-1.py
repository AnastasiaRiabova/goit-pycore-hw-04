def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Error processing line: {line.strip()} (skipped)")

            if count == 0:
                return 0, 0

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"File at path '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0


salary_path = "./salary_file.txt"
counted_total, counted_average = total_salary(salary_path)
print(f"Total salary: {counted_total}, Average salary: {counted_average}")

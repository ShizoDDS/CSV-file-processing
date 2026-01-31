import csv 




CSV_FILE = 'info.csv'
CSV_INFO_FILE = 'info_cleanned.csv'
TXT_FILE = 'report.txt'




def main():
    header, seen_rows, ages = read_csv()
    if seen_rows:
        write_csv(header, seen_rows)
        write_txt(ages)




def read_csv():
    ages = []
    seen_rows = set()
    header = None


    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            lines = csv.reader(file)
            header = next(lines, None)

            for line in lines:
                if len(line) >= 2:
                    try: 
                        row = tuple(line)
                        age = int(line[1])

                        if row not in seen_rows:
                            seen_rows.add(row)
                            ages.append(age)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Error: The file '{CSV_FILE}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{CSV_FILE}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return header, seen_rows, ages




def write_csv(header, seen_rows):
    try:
        with open(CSV_INFO_FILE, 'w', encoding='utf-8', newline='') as file:
            write = csv.writer(file)

            if header:
                write.writerow(header)
            else:
                write.writerow(["Имя", "Возраст", "Город"])

            for row in sorted(seen_rows, key=lambda x: int(x[1])):
                write.writerow(row)
    except FileNotFoundError:
        print(f"Error: The file '{CSV_INFO_FILE}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{CSV_INFO_FILE}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def write_txt(ages):
    try:
        with open(TXT_FILE, 'w', encoding='utf-8') as file:
                if not ages:
                    file.write('There is no data for calculating the average age')
                    return
                
                average_age = sum(ages) / len(ages)
                file.write(f"Средний возраст: {average_age:.2f}")
    except FileNotFoundError:
        print(f"Error: The file '{TXT_FILE}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{TXT_FILE}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




if __name__ == "__main__":
    main()
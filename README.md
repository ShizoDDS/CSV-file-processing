# CSV-file-processing

## 📌 Description

This project is a Python script for cleaning and processing CSV files with user data.

The script:

* Removes duplicate rows
* Sorts records by age
* Calculates the average age
* Saves cleaned data to a new CSV file
* Writes the average age to a TXT report

This project demonstrates basic data processing and file handling in Python.

---

## 📂 Project Structure

```
.
├── info.csv              # Input CSV file
├── info_cleanned.csv     # Cleaned and sorted CSV output
├── report.txt            # TXT report with average age
├── main.py               # Main script
└── README.md             # Documentation
```

---

## 🧾 Input Data Format (`info.csv`)

The input CSV file should contain at least the following columns:

```
Name,Age,City
John,25,London
Anna,30,Berlin
```

* The second column must contain numeric age values
* Rows with invalid age values are ignored
* Duplicate rows are automatically removed

---

## ⚙️ What the Script Does

1. Reads data from `info.csv`
2. Removes duplicate rows
3. Sorts records by age
4. Calculates the average age
5. Saves cleaned data to `info_cleanned.csv`
6. Writes the average age to `report.txt`

---

## 📄 Output Examples

### `report.txt`

```
Средний возраст: 27.50
```

### `info_cleanned.csv`

```
Name,Age,City
John,25,London
Anna,30,Berlin
```

---

## ▶️ How to Run

1. Make sure Python 3.8+ is installed
2. Place `info.csv` in the project directory
3. Run the script:

```bash
python main.py
```

---

## 🛠 Technologies Used

* Python 3
* csv module

---

## 🎯 Purpose

This project demonstrates:

* CSV file processing
* Data cleaning and validation
* Sorting and aggregation
* Writing reports

It is suitable as a junior-level portfolio project for freelance platforms.

---

## 👤 Author

Junior Python Developer

---

## 📬 Contact

If you need a custom CSV data processing script, feel free to contact me.

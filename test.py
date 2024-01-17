import re

filePath = "output_pdf.txt"
with open(filePath, 'r', encoding='utf-8') as file:
    textContent = file.read()

    insured_party_pattern = r"السكن: (.+)"
    matchedInsured_party = re.findall(insured_party_pattern, textContent)
    insured_party = []
    if matchedInsured_party:
        # Convert to a set to remove duplicates and then back to a list
        insured_party = list(set(matchedInsured_party))

    date_pattern = r"(\d{4}/\d{2}/\d{2})"
    dates = re.findall(date_pattern, textContent)

print("السكن:", insured_party)
print("التواريخ:", dates)

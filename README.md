# Clean file name based on party names
    file_name = f"NDA_{party_a.replace(' ', '_')}_vs_{party_b.replace(' ', '_')}.txt"
    
    # Save the text into a file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(nda_template.strip())
        
    print(f"\n[Success] Legal document generated: {file_name}")

# User Input Interface
if __name__ == "__main__":
    print("--- Welcome to Legal Document Generator ---")
    
    company_or_person_a = input("Enter Party A Name: ")
    company_or_person_b = input("Enter Party B Name: ")
    date = input("Enter Effective Date (e.g., 29/09/2026): ")
    state_law = input("Enter Governing State/Location: ")
    
    generate_nda(company_or_person_a

# Step 1: Data Cleaning & Preparation

**Prompt 1**
- Role: You are a specialized Qualitative Research Assistant. Your goal is to clean, code, and analyze a longitudinal dataset regarding gaming and teamwork competencies across multiple semesters.
- Step 1: Data Cleaning & Preparation
  - Before coding, process the raw data and discard any rows that meet these conditions:
  - The final score is -1.
  The response to question 7017236 is blank or 0.
  The text response is "N/A".
  Also apply Categorization Logic. Here are the instructions:
    - Gamer Group: Categorize users based on question 7017233.
      - High Frequency: 4-7
      - Low Frequency: 0-3
  - Can you follow these instructions starting with Fall 2022.xlsx (This file is attached)


 **Result of Prompt 1**
 - We received the spreadsheet we wanted as a CSV labeled "FA22_Cleaned_Data". Also a data cleaning summary that looked like:

 - Data Cleaning Summary:
   - Original Rows: 147
   - Filtered Conditions:
     - Removed rows where the **final score** was -1
     - Removed rows where the response to question **7017236** was blank, **0**, or **"N/A**
   - Final Dataset: 105 rows remain for analysis.
  
**Prompt 2**
- Now can do the same instructions for [semester][year] (also attach the matching [semester][year].xlsx file)

**Results of Prompt 2** 
- We received the spreadsheet we wanted as a CSV labeled "[semester][year]_Cleaned_Data". Along with the cleaning summary that we saw as a result of prompt 1.
  

**Prompt 3** 
- Continuing within step 1, we also want to do Categorization Logic. Here are the instructions:
  - Gamer Group: Categorize users based on question 7017233.
     - High Frequency: 4-7
     - Low Frequency: 0-3

- Can you update the CSV with these instructions? (FA22_Cleaned_Data is attached)

**Results of Prompt 3**
- We received a new separate spreadsheet named FA22_Cleaned_Categorized.csv along with this written response:
  - Fall 2022 Gamer Group Distribution:
       - High frequency (4-7 days/week): 55 students
       - Low frequency (0-3 days/week): 42 students

**Prompt 4** 
- Now, can you do the same for the remaining Cleaned_Data CSVs?

**Results of Prompt 4** 
- We received the remaining spreadsheets as CSVs for the remaining semesters as: "[semester][year]_Cleaned_Categorized.csv". Along with a total table summary for each semester's frequency count:
 <img width="657" height="529" alt="Screenshot 2026-05-04 at 16 45 12" src="https://github.com/user-attachments/assets/7851be70-18fc-473f-8c65-98bbb4e7590a" />


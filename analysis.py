import pandas as pd

# CareerConnect student data
data = {
    "Student": [
        "Aarav Sharma",
        "Priya Das",
        "Rohan Singh",
        "Ananya Patel",
        "Rahul Kumar",
        "Neha Singh",
        "Aditya Das",
        "Simran Patel"
    ],

    "Branch": [
        "CSE", "ECE", "CSE", "EEE",
        "ME", "CSE", "ECE", "CSE"
    ],

    "CGPA": [
        8.4, 7.8, 6.9, 8.1,
        7.4, 8.7, 7.1, 6.8
    ],

    "Placement_Status": [
        "Selected",
        "Selected",
        "Rejected",
        "Under Review",
        "Selected",
        "Selected",
        "Under Review",
        "Rejected"
    ]
}

df = pd.DataFrame(data)

print("CareerConnect Student Data")
print("--------------------------")

print(df)

print("\nAverage CGPA:")
print(round(df["CGPA"].mean(), 2))

print("\nStudents by Branch:")
print(df["Branch"].value_counts())

print("\nPlacement Status:")
print(df["Placement_Status"].value_counts())

import matplotlib.pyplot as plt

# Branch-wise student count
branch_count = df["Branch"].value_counts()

plt.figure(figsize=(8, 5))
branch_count.plot(kind="bar")

plt.title("Students by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Placement status analysis
status_count = df["Placement_Status"].value_counts()

plt.figure(figsize=(8, 5))
status_count.plot(kind="bar")

plt.title("Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# CGPA distribution
plt.figure(figsize=(8, 5))

plt.hist(df["CGPA"], bins=5, edgecolor="black")

plt.title("CGPA Distribution")
plt.xlabel("CGPA")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("cgpa_distribution.png")
plt.close()

# Placement package analysis

placement_data = {
    "Student": [
        "Aarav Sharma",
        "Priya Das",
        "Neha Singh",
        "Ananya Patel",
        "Rahul Kumar",
        "Simran Patel",
        "Aditya Das",
        "Rohan Singh"
    ],

    "Company": [
        "Deloitte",
        "TCS",
        "Infosys",
        "Accenture",
        "Wipro",
        "Oracle",
        "Capgemini",
        "Deloitte"
    ],

    "Package": [
        8.0,
        5.5,
        6.0,
        6.5,
        5.2,
        12.0,
        6.2,
        8.0
    ],

    "Status": [
        "Placed",
        "Placed",
        "Placed",
        "Placed",
        "Placed",
        "Placed",
        "Under Review",
        "Not Placed"
    ]
}

placement_df = pd.DataFrame(placement_data)

print("\nPlacement Data")
print(placement_df)

print("\nAverage Package:")
print(
    round(
        placement_df[
            placement_df["Status"] == "Placed"
        ]["Package"].mean(),
        2
    ),
    "LPA"
)
# Company-wise package analysis

placed_df = placement_df[
    placement_df["Status"] == "Placed"
]

company_package = (
    placed_df.groupby("Company")["Package"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

company_package.plot(kind="bar")

plt.title("Average Package by Company")
plt.xlabel("Company")
plt.ylabel("Average Package (LPA)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("company_package.png")
plt.close()

# Export data for Power BI

df.to_csv("students.csv", index=False)

placement_df.to_csv("placements.csv", index=False)

print("\nCSV files created successfully!")
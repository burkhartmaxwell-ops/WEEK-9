import io 
import matplotlib.pyplot as plt 
import pandas as pd

# exercise 1 load and explore data

# create sample csv content for execution
csv_data = """name,age,major,gpa,credits
Alice,20,Computer Science,3.8,45
Bob,22,Mathematics,3.5,60
Charlie,21,Computer Science,3.9,52
Diana,19,Pnysics,3.7,38
Eve,23,Mathematics,3.6,68"""

# load csv into dataframe

df = pd.read_csv(io.StringIO(csv_data))
print("Sample CSV data loaded Successfully.\n")

print("1. First 3 rows:")
print(df.head(3), "\n")

print(f"2. Shape of DataFrame (rows, columns): {df.shape}\n")

print("3. Info output:")
df.info()
print("\n")

print("4. Describe statistics:")
print(df.describe(), "\n")

print("5. Column names:")
print(list(df.columns), "\n")

# Exercise 2: filter and sort

print("--- Exercise 2: Filter and Sort ---")

print("1. Students with GPA > 3.6:")
print(df[df["gpa"] > 3.6], "\n")

print("2. Computer Science majors only:")
print(df[df["major"] == "Computer Science"], "\n")

print("3. Students with credits >= 50:")
print(df[df["credits"] >= 50], "\n")

print("4. Sorted by GPA (descending):")
print(df.sort_values(by="gpa", ascending=False), "\n")

print("5. Sorted by Age (ascending), then GPA (ascending):")
print(df.sort_values(by=["age", "gpa"]), "\n")

# Exercise 3: Grouping and Aggregation

print("--- Exercise 3: Grouping and Aggregation ---")

print("1. Group by major, calculate average GPA:")
print(df.groupby("major")["gpa"].mean(), "\n")

print("2. Group by major, count students:")
print(df.groupby("major")["name"].count(), "\n")

print("3. Group by major, get max credits:")
print(df.groupby("major")["credits"].max(), "\n")

overall_avg_gpa = df["gpa"].mean()
print(f"4. Overall average GPA: {overall_avg_gpa:.2f}\n")

highest_gpa_row = df.loc[df["gpa"].idxmax()]
print("5. Student with the highest GPA")
print(f"Name: {highest_gpa_row['name']} | GPA: {highest_gpa_row['gpa']} Major: {highest_gpa_row['major']}\n")

# Exercise 4: Data Cleaning

print("--- Exercise 4 Data Cleaning ---")

# create messy data sample 

messy_csv_data = """name,score,grade
Alice,85,B
Bob,,A
Charlie,92,A
Diana,78,
Eve,88,B
Alice,85,B"""

messy_df = pd.read_csv(io.StringIO(messy_csv_data))
print("Original Messy Dataframe:")
print(messy_df, "\n")

print("1. Checking for missing values:")
print(messy_df.isnull().sum(), "\n")

# fill missing scores with the column mean

score_mean = messy_df["score"].mean()
messy_df["score"] = messy_df["score"].fillna(score_mean)
print(f"2. Filled missing scores with mean ({score_mean:.1f}):")
print(messy_df, "\n")

# drop rows where 'grade' is missing

messy_df = messy_df.dropna(subset=["grade"])
print("3. Dropped rows with missing grades:")
print(messy_df, "\n")

# remove duplicate rows

cleaned_df = messy_df.drop_duplicates()
print("4. Removed duplicate rows (Final Cleaned DataFrame):")
print(cleaned_df, "\n")


# Exercise 5: Create visualizations

fig, ax = plt.subplots(figsize=(7, 4))
counts = df["major"].value_counts()
counts.plot(
    kind="bar",
    ax=ax,
    color=["steelblue", "coral", "mediumseagreen"],
    edgecolor="black",
)
ax.set_title("Students per Major")
ax.set_xlabel("Major")
ax.set_ylabel("Number of Students")
ax.tick_params(axis="x", rotation=30)
plt.tight_layout()
plt.savefig("chart1_bar.png", dpi=120)
plt.close()
print("Saved: chart1_bar.png")

# chart 2: line plot

fig, ax = plt.subplots(figsize=(7, 4))
sorted_df = df.sort_values("gpa").reset_index(drop=True)
ax.plot(
    sorted_df["name"],
    sorted_df["gpa"],
    marker="o",
    color="darkorange",
    linewidth=2,
)
ax.set_title("GPA Trend (Sorted by GPA)")
ax.set_xlabel("Student")
ax.set_ylabel("GPA")
ax.set_ylim(3.0, 4.0)
plt.tight_layout()
plt.savefig("chart2_line.png", dpi=120)
plt.close()
print("Saved: chart2_line.png")

# chart 3 histogram

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(df["gpa"], bins=5, color="mediumpurple", edgecolor="black")
ax.set_title("Distribution of GPAs")
ax.set_xlabel("GPA")
ax.set_ylabel("Frequemcy")
plt.tight_layout()
plt.savefig("chart3_histogram.png", dpi=120)
plt.close()
print("Saved: chart3_histogram.png")

print("\nAll exercises complete!")



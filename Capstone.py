import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 20)

df = pd.read_csv("Capstone.csv")
# print(df)

# Question 1: Which country in West Africa recorded the highest number of attacks?

west_africa = ["Nigeria", "Ghana", "Zimbabwa", "Benin", "Togo",
               "Chad", "Mali", "Burkina Faso", "Liberia", "Gambia"]
west_africa_df = df[df["Country"].isin(west_africa)]
country_attacks = west_africa_df["Country"].value_counts().reset_index()
country_attacks.columns = ["Country", "Number of Attacks"]
print(country_attacks)

plt.bar(country_attacks["Country"], country_attacks["Number of Attacks"],
        color="blue")
plt.title("Number of Attacks by Country in West Africa")
plt.xlabel("Country")
plt.ylabel("Number of Attacks")
plt.xticks(rotation=20)


# Question 2: What bare the top 5 cities with the most reported crime incidents?

city_attacks = df["City"].value_counts().head(5).reset_index()
city_attacks.columns = ["City", "Number of Incidents"]
print(city_attacks)

plt.bar(city_attacks["City"], city_attacks["Number of Incidents"],
        color="orange")
plt.title("Top 5 Cities with the most Reported Crime Incidents")
plt.xlabel("City")
plt.ylabel("Number of Incidents")
plt.xticks(rotation=20)



# Question 3: How has the number of attacks changed over the years?
yearly_attacks = df["Year"].value_counts().sort_index().reset_index()
yearly_attacks.columns = ["Year", "Number of Attacks"]
# print(yearly_attacks)

# plt.plot(yearly_attacks["Year"], yearly_attacks["Number of Attacks"],
#          color="teal")
# plt.figure(figsize=(14,6))
# plt.title("Number of Attacks over the Years")
# plt.xlabel("Year")
# plt.ylabel("Number of Attacks")
# plt.xticks(yearly_attacks["Year"], rotation=45, ha="right")
# plt.tight_layout()


# Question 4: Are there particular months or seasons when attacks are more frequent?
monthly_attacks = df.groupby("Month").size().reset_index(name="Number of Attacks")
month_order = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
monthly_attacks["Month"] = pd.Categorical(monthly_attacks["Month"],
                categories=month_order, ordered=True)
monthly_attacks = monthly_attacks.sort_values("Month")
print(monthly_attacks)


plt.figure(figsize=(10,6))
plt.plot(monthly_attacks["Month"],
        monthly_attacks["Number of Attacks"], color="orange")
plt.title("Number of Attacks per Month")
plt.xlabel("Month")
plt.ylabel("Number of Attacks")
plt.xticks(rotation=30)
plt.tight_layout()


# Question 5: Which Perpetrator group was responsible for the most fatalities?
fatalities_by_group = df.groupby("Perpetrator_group")["fatalities"].sum().reset_index()
fatalities_by_group = fatalities_by_group.sort_values("fatalities", ascending=False)
# print(fatalities_by_group.head(10))


top_groups = fatalities_by_group.head(10)

plt.figure(figsize=(14,8))
plt.barh(top_groups["Perpetrator_group"], top_groups["fatalities"], color="crimson")
plt.title("Top 10 perpetrator Groups by fatalities")
plt.xlabel("Number of fatalities")
plt.ylabel("perpetrator Group")
plt.xticks(rotation=30)



# What is the total fatality for each country?
fatalities_by_country = df.groupby("Country")["fatalities"].sum().reset_index()
fatalities_by_country = fatalities_by_country.sort_values("fatalities",
        ascending=False)
print(fatalities_by_country.head(10))

top_countries = fatalities_by_country.head(10)
plt.figure(figsize=(10,6))
plt.bar(top_countries["Country"], top_countries["fatalities"], color="teal")
plt.title("Top 10 Countries by Total Fatalities")
plt.xlabel("Number of Fatalities")
plt.ylabel("Country")






plt.show()
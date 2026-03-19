import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data of gurugram real Estate.csv')
print(df.head())
print(df.columns.tolist())

# Data Cleaning
print(df.info())
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
print(df.columns.to_list())
df = df.drop_duplicates()
#Numerical Columns Cleaning
df['price'] = df['price'].astype(str).str.replace(",","").astype(float)
df['area'] = df['area'].astype(str).str.replace(",","").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",","").astype(float)
print(df['rate_per_sqft'])

#Categorial Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera' : True,'not approved by rera' : False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()
df = df.drop_duplicates()
print(df)


# Question 1 : What is the costliest flat in the dataset ?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"Costliest Flat Details :\nPrice : {costliest_flat['price']}\nStatus : {costliest_flat['status']}\nArea : {costliest_flat['area']} sqft\nRate per sqft : {costliest_flat['rate_per_sqft']}\nProperty Type : {costliest_flat['property_type']}\nLocality : {costliest_flat['locality']}\nBuilder Name : {costliest_flat['builder_name']}\nRERA Approval : {costliest_flat['rera_approval']}\nBHK Count : {costliest_flat['bhk_count']}\nSociety : {costliest_flat['socity']}\nCompany Name : {costliest_flat['company_name']}\nFlat Type : {costliest_flat['flat_type']}")

# Question 2 : Which locality has the highest average price ?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}")

print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(10))

# Question 3 : Which locality has the highest rate per square foot?
highest_rate_per_square_foot = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_per_square_foot}")

# Question 4 : Do ready to move properties cost more than under construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price : 
    print("Ready to move properties cost more on average than under construction properties")
else:
    print("Under - construction properties cost more on average than ready-to-move properties")

# Question 5 : Do RERA approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print("RERA approved properties command a price premium on average")
else:    
    print("RERA approved properties do not command a price premium on average")

# Question 6 : How does area impact price?
sns.scatterplot(x='area',y='price',data=df)
plt.title('Area vs Price')
plt.show()

# Question 7 : How does the number of BHKs impact price based on per square foot?
most_expensive_bhk_count = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The number of BHKs that is the most expensive on average is {most_expensive_bhk_count}")

# Question 8 : Which property type is the costliest ?
most_expensive_property_type = df.groupby('property_type')['price'].mean().idxmax()
print(f"The costliest property type on average is {most_expensive_property_type}")

# Question 9 : Do certain builders price higher ?
print(df.groupby("company_name")['price'].mean().sort_values(ascending=False).head(10))  



# Question 10 : Are larger homes more expensive on a per square foot basis ? 
sns.scatterplot(x='area',y='rate_per_sqft',data=df)
plt.title('Area vs Rate per Square Foot')
plt.show()  
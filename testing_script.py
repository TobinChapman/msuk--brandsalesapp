#testing script for brand sales app from field and binet

import pandas as pd

category_df = pd.DataFrame({
    'category': ['FMCG Non Food', 'FMCG Food and Drink', 'Retail', 'FMCG ALL', 'Durables All', 'Durable Non Automotive', 'Financial Service', 'Other services all', 'Other services Telco/ISP', 'Other services Travel/QSR/MEDIA'],
    'value': [65, 56, 64, 60, 58, 69, 80, 51, 58, 48]
})

purchase_df = pd.DataFrame({
    'category': ['Offline', 'Online', 'Serial', 'Subscrip'],
    'value': [-7, 12, -5, 12]
})

pricing_df = pd.DataFrame({
    'category': ['Value/Mainstream', 'Premium'],
    'value':[-5,0]
})

innovation_df = pd.DataFrame({
    'category': ['None', 'Any', 'New Variant', 'New Sub Brand', 'Entry to new Category'],
    'value': [-1,10,0,16,22]
})

lifestage_df = pd.DataFrame({
    'category': ['New Category', 'Est Category', 'Declining Category', 'Stagnant or low growth', 'Medium or high growth'],
    'value': [3,0,-4,-2,11]
})

size_df = pd.DataFrame({
    'category': ['Launches in first 1 to 2 years', 'Launches after first year', 'Small Brand', 'Medium Brand', 'Large Brand', 'Leading Brand'],
    'value': [-27,-5,13,-6,14,10]
})

category_val = "FMCG Non Food"
purchase = "Offline"
pricing = "Premium"
innovation = "None"
lifestage = "New Category"
size = "Small Brand"

start_df = pd.concat([category_df[category_df['category'] == category_val], 
                      purchase_df[purchase_df['category'] == purchase],
                      pricing_df[pricing_df['category'] == pricing],
                      innovation_df[innovation_df['category'] == innovation],
                      lifestage_df[lifestage_df['category'] == lifestage],
                      size_df[size_df['category'] == size]], 
                     ignore_index=True)

print(start_df)

final_df = start_df.sum().reset_index

print(final_df)

test_df = purchase_df[purchase_df['category'] == purchase]

final_df = pd.concat([start_df, test_df])

if starting_balance == "FMCG Non Food":
    print("FMCG Non Food")
else:
    print("Something else")

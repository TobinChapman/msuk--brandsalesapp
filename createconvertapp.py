import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="BrandPerformanceCalc", page_icon=":crystal_ball:", initial_sidebar_state="expanded")

    st.image('MS_Logo.png', width=80)
    st.title("Brand and Performance Calculator")

    result_area = st.empty()

    st.write("Input some details about your business:")

    category_val = st.selectbox('Category:', ('FMCG Non Food', 'FMCG Food and Drink', 'Retail', 'FMCG ALL', 'Durables All', 'Durable Non Automotive', 'Financial Service', 'Other services all', 'Other services Telco/ISP', 'Other services Travel/QSR/MEDIA'))

    purchase = st.selectbox('How is it purchased:', ('Offline', 'Online', 'Serial', 'Subscrip'))

    pricing = st.selectbox('Pricing:', ('Value/Mainstream', 'Premium'))

    innovation = st.selectbox('Level of innovation:', ('None', 'Any', 'New Variant', 'New Sub Brand', 'Entry to new Category'))

    lifestage = st.selectbox('Category lifestage:', ('New Category', 'Est Category', 'Declining Category', 'Stagnant or low growth', 'Medium or high growth'))

    size = st.selectbox('Size:', ('Launches in first 1 to 2 years', 'Launches after first year', 'Small Brand', 'Medium Brand', 'Large Brand', 'Leading Brand'))

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

    start_df = pd.concat([category_df[category_df['category'] == category_val], 
                      purchase_df[purchase_df['category'] == purchase],
                      pricing_df[pricing_df['category'] == pricing],
                      innovation_df[innovation_df['category'] == innovation],
                      lifestage_df[lifestage_df['category'] == lifestage],
                      size_df[size_df['category'] == size]], 
                     ignore_index=True)

    final_df = pd.DataFrame(start_df.sum()).reset_index()

    create = final_df.iloc[1,1]
    convert = 100-create

    result_area.write("<b1 style='text-align: center; font-size: {}px;'>Your recommended split is <i><b>{}% Brand</b></i> and <i><b>{}% Performance</b></i></b1>".format(26, create, convert), unsafe_allow_html=True)

    st.write("This tool is designed to be a rough starting point for planning media. It is based off research from the IPA. Please contact Marketing Science if you have any questions or would like more info on how we can help media planning.") 

if __name__ == '__main__':
    main()

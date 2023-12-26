import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog")

# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put data into dataframe 
df = pandas.DataFrame(my_catalog)

# temp write the dataframe to the page to see what we're working with 
# streamlit.write(df)

# put first col into a list
color_list = df[0].values.tolist()
print(color_list)

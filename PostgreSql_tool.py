import psycopg2
import numpy
import pandas as pd
print("start to use psycopg2")

conn = psycopg2.connect(
    host = "140.110.5.72",
    database = "baa87699-e895-43bd-80c2-81e3810d75fc",
    user = "44352c6e-5d46-4e2b-a27c-565ecf11e0ec",
    password = "oileco7orrp49cadqg371hom3f",
)
# obj = pd.read_csv("18d1.csv")
obj = pd.read_csv("VD.csv")
print("Open database successfully")

cur = conn.cursor()

# create a new table && set all parameters
# cur.execute("""CREATE TABLE economic.VD2
#     (
#         date timestamp without time zone NOT NULL,
#         vd1_origin  double precision,
#         vd1_predict double precision,
#         vd1_mask   double precision,

#         vd2_origin  double precision,
#         vd2_mask   double precision,

#         vd3_origin  double precision,
#         vd3_predict double precision,
#         vd3_mask   double precision,

#         vd4_origin  double precision,
#         vd4_predict double precision,
#         vd4_mask   double precision,

#         vd5_origin  double precision,
#         vd5_predict double precision,
#         vd5_mask   double precision,

#         vd6_origin  double precision,
#         vd6_predict double precision,
#         vd6_mask   double precision,

#         PRIMARY KEY (date));""")
# cur.execute("""CREATE TABLE economic.VD2
#     (
#         date timestamp without time zone NOT NULL,
#         vd1_density  double precision,
#         vd1_flow double precision,
#         vd1_speed double precision,
#         vd2_density double precision,
#         vd2_flow double precision,
#         vd2_speed double precision,

#         PRIMARY KEY (date));""")
print ("Table created successfully")

# insert data to the dataset
# cur.execute("""
#     INSERT INTO economic.VDtest(date,vd1_density,vd1_flow,vd1_speed,vd2_density,vd2_flow,vd2_speed,week)
#     VALUES('2015-01-01 00:10',1.2,27.0,54.92666666666667,0.46666666666666673,8.0,53.5,4.0);
# """)

# string replace example str.replace( origin char, replace char, times )

for i in range(0,len(obj)):
    # print(obj.loc[i]['date'])
    l2 = obj.loc[i]['date'].replace("-"," ")
    l2 = l2.replace("-"," ")
    l2 = l2.replace("/","-",2)
    #print(l2)
    query = "INSERT INTO economic.VD2(date,vd1_density,vd1_flow,vd1_speed,vd2_density,vd2_flow,vd2_speed)VALUES("
    query = query + "'"+str(l2) + "'," + str(obj.loc[i]['vd1_density']) + "," + str(obj.loc[i]['vd1_flow']) + "," + str(obj.loc[i]['vd1_speed']) + ","
    query = query + str(obj.loc[i]['vd2_density']) + "," + str(obj.loc[i]['vd2_flow']) + "," + str(obj.loc[i]['vd2_speed']) +");"
    # query = "INSERT INTO economic.VD18test(date,vd1_origin,vd1_predict,vd1_mask,vd2_origin,vd2_mask,vd3_origin,vd3_predict,vd3_mask,vd4_origin,vd4_predict,vd4_mask,vd5_origin,vd5_predict,vd5_mask,vd6_origin,vd6_predict,vd6_mask)VALUES("
    # query = query + "'"+str(obj.loc[i]['idx']) + "'," + str(obj.loc[i]['vd1_origin']) + "," + str(obj.loc[i]['vd1_predict']) + "," + str(obj.loc[i]['vd1_mask']) + ","
    # query = query + str(obj.loc[i]['vd2_origin']) + "," + str(obj.loc[i]['vd2_mask']) + ","
    # query = query + str(obj.loc[i]['vd3_origin']) + "," + str(obj.loc[i]['vd3_predict']) + "," + str(obj.loc[i]['vd3_mask']) + ","
    # query = query + str(obj.loc[i]['vd4_origin']) + "," + str(obj.loc[i]['vd4_predict']) + "," + str(obj.loc[i]['vd4_mask']) + ","
    # query = query + str(obj.loc[i]['vd5_origin']) + "," + str(obj.loc[i]['vd5_predict']) + "," + str(obj.loc[i]['vd5_mask']) + ","
    # query = query + str(obj.loc[i]['vd6_origin']) + "," + str(obj.loc[i]['vd6_predict']) + "," + str(obj.loc[i]['vd6_mask']) +");"

    cur.execute(query)
    conn.commit()

print("Records created successfully")
conn.close()

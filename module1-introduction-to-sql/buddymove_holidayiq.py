import sqlite3
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

df = pd.read_csv('/Users/sparatan117/Downloads/lambda/unit3/mysqul/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

df['User_Id'] = df['User Id']
df2 = df.drop('User Id', axis=1)



def write_df_to_sql_df(df, name_of_sql):
    df.to_sql(name_of_sql, con=engine)

def creat_table(curs):
    conn.execute("""CREATE TABLE user_review (
        Sports integer,
        Religious interger,
        Nature interger,
        Theatre interger,
        Shopping interger, 
        Picnic interger,
        User_id varchar(225)
    )
    """)

def insert(review, conn, curs):
    with conn:
        curs.execute("""
        INSERT INTO user_review VALUES(:Sports, :Religious, :Nature, :Theatre,
        :Shopping, :Picnic, :User_id)""",
        {'Sports': review.Sports, 'Religious': review.Religious, 'Nature':review.Nature,
        'Theatre': review.Theatre, 'Shopping': review.Shopping, 'Picnic': review.Picnic,
        'User_id': review.User_id})

def insert2(df, conn, curs):
    for index, row in df.iterrows():
        insert(row, conn, curs)





if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    write_df_to_sql_df(df2, 'buddymove_holidayiq.sqlite3')
    creat_table(curs)
    insert2(df2, conn, curs)
    curs.close()
import psycopg2

"""
Execute sql selects:
    This code was done quick and dirty just to get it to a working stage, and would be cleaned if we had more time.
    The connection data should not be stored like this but this was the quickest way of doing it for now.
    Would rather use the heroku variable to get the information but just to make it work on both heroku and local this 
    became the solution.
    
    This one is made to execute a select and then return the value from the query.
"""


def execute_sql_select(sql, params):
    pred = None
    try:
        connection = psycopg2.connect(
            user="abjaykmgqyrfmn",
            password="fe036509d198e4b10c24c1a50c576867af01b19afa3ff2f0a1f9edfba6eda8d8",
            host="ec2-34-254-24-116.eu-west-1.compute.amazonaws.com",
            port="5432",
            database="d405qjg06557ab"
        )
        cursor = connection.cursor()
        cursor.execute(sql, params)
        pred = cursor.fetchall()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close

    return pred


"""
Execute sql query:
    Same thing here as stated above. This would be cleaned and stored in a proper manner.
    
    Here we use the sql string and parameters from the user to insert data to the database. 
    This one should be able to update and delete data as well, as another implementation in the update route. 
"""


def execute_sql_query(sql, params):
    try:
        connection = psycopg2.connect(
            user="abjaykmgqyrfmn",
            password="fe036509d198e4b10c24c1a50c576867af01b19afa3ff2f0a1f9edfba6eda8d8",
            host="ec2-34-254-24-116.eu-west-1.compute.amazonaws.com",
            port="5432",
            database="d405qjg06557ab"
        )
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        print("Query error ", error)
    finally:
        if (connection):
            cursor.close()
            connection.close
    return

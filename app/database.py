import psycopg2


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


def execute_sql_insert(sql, params):
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
        print(count, "Record inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Insert error ", error)
    finally:
        if (connection):
            cursor.close()
            connection.close
    return
